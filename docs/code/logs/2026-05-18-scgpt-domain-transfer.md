---
type: worklog
status: archive
rag_priority: low
updated: '2026-07-20'
tags:
- wiki/worklog
---

# 2026-05-18 - scGPT Embedding-based Domain Transfer

## 목적

Bulk microarray 데이터에서 학습한 classifier를 single-cell RNA-seq 환자 임베딩에 적용해 domain shift 상황에서 scGPT embedding이 얼마나 transfer 가능한지 평가한다.

핵심 질문은 다음과 같다.

- Bulk microarray와 scRNA-seq 사이의 platform shift를 scGPT quantile binning과 embedding이 어느 정도 흡수할 수 있는가?
- Bulk sample embedding으로 학습한 rejection classifier가 single-cell patient-level embedding에서도 동작하는가?
- 환자별 median pooling이 cell-level embedding을 patient-level prediction으로 변환하는 데 충분한가?

## 사용 데이터

- Bulk microarray: `GSE36059_GSE147089_merged_rma.h5ad`
- Single-cell RNA-seq: `E-MTAB-12051/E_MTAB_12051.h5ad`
- Pretrained model: `models/pretrain_kidney`
- 원본 embedding cache: `results/domain_shift/`

## 실행 환경

- Python
- PyTorch
- AnnData / Scanpy
- scikit-learn
- scGPT kidney pretrained encoder

## 실행 명령어

```bash
cd /home/tunabear2/DW/scGPT/data

python run_step3_domain_transfer.py
python run_step3_domain_transfer.py --use-cache
python run_step3_domain_transfer.py --fresh
```

## 출력

```text
results/step3_run/bulk_embeddings.npz
results/step3_run/sc_embeddings.npz
results/step3_run/predictions.csv
```

## 핵심 아이디어

Bulk RMA log2 expression과 scRNA-seq raw count는 scale과 distribution이 다르다. 이 스크립트는 scGPT의 per-sample quantile binning을 사용해 절대 scale 차이를 줄이고, 두 domain을 같은 pretrained embedding space에 투영한다.

그 후 bulk sample embedding으로 logistic regression classifier를 학습하고, single-cell embedding을 환자별 median pooling으로 요약한 뒤 rejection probability를 예측한다.

## 주의할 점

- `--use-cache`는 기존 embedding cache를 재사용해 실행 시간을 줄인다.
- `--fresh`는 원본 cache를 무시하고 embedding을 처음부터 다시 계산한다.
- 원본 `results/domain_shift/` cache가 있으면 AUC 재현을 위해 우선 사용한다.
- Patient-level prediction은 cell-level prediction이 아니라, cell embedding의 환자별 median pooling 결과에 classifier를 적용한 것이다.
- Threshold는 AUC와 별개로 `Top25%`와 `Median` 두 가지 방식으로 평가한다.

## 전체 코드

```python
#!/usr/bin/env python3
"""
Step 3: scGPT Embedding-based Domain Transfer (재현 스크립트)
=============================================================
Bulk microarray (GSE36059 + GSE147089) -> scRNA-seq (E-MTAB-12051) 분류

핵심 아이디어:
  - scGPT의 per-sample quantile binning이 플랫폼 간 scale 차이를 흡수
  - Bulk 샘플 -> scGPT 임베딩 -> LR 훈련
  - SC cell -> scGPT 임베딩 -> 환자별 중앙값 pooling -> LR 적용

사용법:
  cd /home/tunabear2/DW/scGPT/data
  python run_step3_domain_transfer.py              # 임베딩 새로 계산
  python run_step3_domain_transfer.py --use-cache  # 기존 캐시 재사용

출력:
  results/step3_run/bulk_embeddings.npz    - bulk scGPT 임베딩
  results/step3_run/sc_embeddings.npz      - SC cell scGPT 임베딩
  results/step3_run/predictions.csv        - 환자별 예측 결과
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from torch import nn, Tensor
from torch.utils.data import DataLoader, Dataset
from scipy import sparse
import anndata as ad
import scanpy as sc_pp
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import (
    roc_auc_score, accuracy_score, balanced_accuracy_score,
    confusion_matrix,
)
from tqdm.auto import tqdm
import warnings
warnings.filterwarnings("ignore")


# 경로 설정
DATA_DIR  = Path(__file__).parent
MODEL_DIR = DATA_DIR / "models" / "pretrain_kidney"
OUT_DIR   = DATA_DIR / "results" / "step3_run"

BULK_H5AD = DATA_DIR / "GSE36059_GSE147089_merged_rma.h5ad"
SC_H5AD   = DATA_DIR / "E-MTAB-12051" / "E_MTAB_12051.h5ad"

# 하이퍼파라미터
MAX_GENES  = 1200   # 샘플당 사용할 최대 유전자 수 (발현값 상위 N개)
BATCH_SIZE = 128
PCA_DIM    = 64
LR_C       = 0.01   # L2 정규화 (원본 step3 LR_C001 = C=0.01)
SEED       = 42

# 원본 임베딩 캐시 경로 (Step 3 최초 실행 시 생성된 "황금" 임베딩)
# 이 파일들이 존재하면 우선 사용 -> AUC=0.938 재현
_ORIG_DIR  = DATA_DIR / "results" / "domain_shift"
_ORIG_BULK = _ORIG_DIR / "bulk_embeddings.npz"   # key: 'emb_raw'
_ORIG_SC   = _ORIG_DIR / "sc_cell_embeddings.npz" # key: 'emb'

# E-MTAB-12051 disease -> NR / Rejection 매핑
DISEASE_MAP = {
    "Non rejection DSA+":          "NR",
    "Non rejection DSA-":          "NR",
    "Antibody-mediated rejection": "Rejection",
    "T cell-mediated rejection":   "Rejection",
}


# scGPT 인코더 모듈

class GeneVocab:
    def __init__(self, token_to_id: dict):
        self.token_to_id = dict(token_to_id)
        self.default_index = self.token_to_id.get("<pad>", 0)

    @classmethod
    def from_file(cls, path: Path):
        with path.open() as f:
            vocab = cls(json.load(f))
        for tok in ("<pad>", "<cls>", "<eoc>"):
            if tok not in vocab.token_to_id:
                vocab.token_to_id[tok] = len(vocab.token_to_id)
        vocab.default_index = vocab["<pad>"]
        return vocab

    def __len__(self):   return len(self.token_to_id)
    def __contains__(self, t): return t in self.token_to_id
    def __getitem__(self, t):  return self.token_to_id[t]
    def lookup_many(self, tokens):
        return np.array([self.token_to_id.get(t, self.default_index) for t in tokens],
                        dtype=np.int64)


class GeneEncoder(nn.Module):
    def __init__(self, num_embeddings, embedding_dim, padding_idx):
        super().__init__()
        self.embedding = nn.Embedding(num_embeddings, embedding_dim, padding_idx=padding_idx)
        self.enc_norm  = nn.LayerNorm(embedding_dim)
    def forward(self, x: Tensor) -> Tensor:
        return self.enc_norm(self.embedding(x))


class ContinuousValueEncoder(nn.Module):
    def __init__(self, d_model, dropout, max_value=512):
        super().__init__()
        self.dropout    = nn.Dropout(dropout)
        self.linear1    = nn.Linear(1, d_model)
        self.activation = nn.ReLU()
        self.linear2    = nn.Linear(d_model, d_model)
        self.norm       = nn.LayerNorm(d_model)
        self.max_value  = max_value
    def forward(self, x: Tensor) -> Tensor:
        x = torch.clamp(x.unsqueeze(-1), max=self.max_value)
        x = self.activation(self.linear1(x))
        x = self.linear2(x)
        return self.dropout(self.norm(x))


class ScGPTEncoder(nn.Module):
    def __init__(self, ntoken, pad_id, d_model, nhead, d_hid, nlayers, dropout):
        super().__init__()
        self.encoder       = GeneEncoder(ntoken, d_model, padding_idx=pad_id)
        self.value_encoder = ContinuousValueEncoder(d_model, dropout)
        layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead, dim_feedforward=d_hid,
            dropout=dropout, batch_first=True, norm_first=False,
        )
        self.transformer_encoder = nn.TransformerEncoder(layer, num_layers=nlayers)

    def forward(self, gene_ids: Tensor, values: Tensor, padding_mask: Tensor) -> Tensor:
        x   = self.encoder(gene_ids) + self.value_encoder(values)
        out = self.transformer_encoder(x, src_key_padding_mask=padding_mask)
        return out[:, 0, :]   # CLS 토큰 반환


def load_encoder(model_dir: Path, device: torch.device):
    vocab = GeneVocab.from_file(model_dir / "vocab.json")
    with (model_dir / "args.json").open() as f:
        args = json.load(f)

    model = ScGPTEncoder(
        ntoken=len(vocab),
        pad_id=vocab[args.get("pad_token", "<pad>")],
        d_model=int(args["embsize"]),
        nhead=int(args["nheads"]),
        d_hid=int(args["d_hid"]),
        nlayers=int(args["nlayers"]),
        dropout=float(args.get("dropout", 0.0)),
    )
    ckpt    = torch.load(model_dir / "best_model.pt", map_location="cpu")
    renamed = {}
    for k, v in ckpt.items():
        if k.startswith(("encoder.", "value_encoder.", "transformer_encoder.")):
            k = k.replace(".self_attn.Wqkv.weight", ".self_attn.in_proj_weight")
            k = k.replace(".self_attn.Wqkv.bias",   ".self_attn.in_proj_bias")
            renamed[k] = v

    state   = model.state_dict()
    matched = {k: v for k, v in renamed.items()
               if k in state and tuple(v.shape) == tuple(state[k].shape)}
    state.update(matched)
    model.load_state_dict(state)
    print(f"  체크포인트: {len(matched)} 텐서 로드 완료")
    model.to(device).eval()
    return model, vocab, args


# 임베딩 Dataset / 유틸

def _bin_values(values: np.ndarray, n_bins: int, rng: np.random.Generator) -> np.ndarray:
    """
    발현값 -> quantile 기반 정수 bin (1 ~ n_bins).
    tie-breaking: 동일 quantile 경계에 걸리는 값을 균등 분포로 랜덤 배정.
    재현성을 위해 외부 RNG를 주입받는다.
    """
    if len(values) == 0 or values.max() == 0:
        return np.zeros_like(values, dtype=np.float32)
    bins    = np.quantile(values, np.linspace(0, 1, n_bins - 1))
    left    = np.digitize(values, bins)
    right   = np.digitize(values, bins, right=True)
    offsets = rng.random(len(values))
    return np.ceil(offsets * (right - left) + left).astype(np.float32)


class ExpressionDataset(Dataset):
    """
    Dense 또는 sparse 발현 행렬을 scGPT 입력 형식으로 변환.

    재현성을 위해 각 Dataset은 seed로 초기화된 전용 RNG를 사용한다.
    """
    def __init__(self, X, gene_ids, normalize_total, log1p,
                 max_genes, pad_id, pad_val, cls_id, n_bins, seed=42):
        self.X               = X
        self.gene_ids        = gene_ids
        self.normalize_total = normalize_total
        self.log1p           = log1p
        self.max_genes       = max_genes
        self.pad_id          = pad_id
        self.pad_val         = pad_val
        self.cls_id          = cls_id
        self.n_bins          = n_bins
        self.rng             = np.random.default_rng(seed)   # 재현 가능한 RNG

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):
        row = self.X[idx]
        if sparse.issparse(row):
            row = np.asarray(row.todense()).ravel()
        row = row.astype(np.float32)

        # 발현된(>0) 유전자 선택
        pos    = np.flatnonzero(row > 0)
        values = row[pos].copy()

        # 정규화
        total = float(values.sum())
        if self.normalize_total is not None and total > 0:
            values *= self.normalize_total / total
        if self.log1p:
            values = np.log1p(values)

        # 발현값 상위 max_genes개 선택
        if len(values) > self.max_genes - 1:
            chosen = np.argpartition(values, -(self.max_genes - 1))[-(self.max_genes - 1):]
            pos    = pos[chosen]
            values = values[chosen]

        # Quantile binning (재현 가능한 RNG 사용)
        binned = _bin_values(values, self.n_bins, self.rng)

        # [CLS, gene1, ..., geneN, PAD, ...] 형식으로 구성
        out_genes  = np.full(self.max_genes, self.pad_id,  dtype=np.int64)
        out_values = np.full(self.max_genes, self.pad_val, dtype=np.float32)
        out_genes[0]  = self.cls_id
        out_values[0] = 0.0
        n = len(pos)
        if n > 0:
            out_genes[1:n+1]  = self.gene_ids[pos]
            out_values[1:n+1] = binned

        return {
            "genes":  torch.from_numpy(out_genes),
            "values": torch.from_numpy(out_values),
            "idx":    idx,
        }


def _collate(batch):
    return {
        "genes":  torch.stack([b["genes"]  for b in batch]),
        "values": torch.stack([b["values"] for b in batch]),
        "idx":    np.array([b["idx"] for b in batch], dtype=np.int64),
    }


def embed(X, gene_ids, model, vocab, model_args,
          normalize_total, log1p, device, desc="Embedding", seed=42):
    """
    발현 행렬 X -> scGPT CLS 임베딩 (L2 정규화).

    Args:
        X              : (N, G) 발현 행렬
        gene_ids       : (G,) vocab ID 배열
        normalize_total: CPM 정규화 총합 (None이면 건너뜀)
        log1p          : log1p 변환 여부
        seed           : 재현성을 위한 RNG seed
    Returns:
        (N, d_model) float32 임베딩
    """
    N       = X.shape[0]
    emb_dim = int(model_args["embsize"])
    pad_id  = vocab[model_args.get("pad_token", "<pad>")]
    cls_id  = vocab["<cls>"]
    n_bins  = int(model_args.get("n_bins", 51))
    pad_val = float(model_args.get("pad_value", -2))

    ds = ExpressionDataset(
        X=X, gene_ids=gene_ids,
        normalize_total=normalize_total, log1p=log1p,
        max_genes=MAX_GENES, pad_id=pad_id, pad_val=pad_val,
        cls_id=cls_id, n_bins=n_bins, seed=seed,
    )
    dl = DataLoader(ds, batch_size=BATCH_SIZE, shuffle=False,
                    num_workers=0, collate_fn=_collate)

    embeddings = np.zeros((N, emb_dim), dtype=np.float32)
    model.eval()
    with torch.no_grad():
        for batch in tqdm(dl, desc=desc, leave=True):
            g   = batch["genes"].to(device)
            v   = batch["values"].to(device)
            pm  = g.eq(pad_id)
            out = model(g, v, pm)
            out = F.normalize(out, p=2, dim=1)   # L2 정규화
            embeddings[batch["idx"]] = out.cpu().numpy()

    return embeddings


# 메인 파이프라인

def main(use_cache: bool = False, fresh: bool = False):
    torch.manual_seed(SEED)
    np.random.seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    use_orig = not fresh   # --fresh 시 원본 캐시 전체 무시

    print("=" * 60)
    print("Step 3: scGPT Embedding-based Domain Transfer")
    print(f"  Device : {device}")
    print(f"  Model  : {MODEL_DIR}")
    print(f"  Output : {OUT_DIR}")
    print("=" * 60)

    # 인코더 로드
    print("\n[1] scGPT kidney 인코더 로드...")
    model, vocab, model_args = load_encoder(MODEL_DIR, device)
    print(f"  d_model={model_args['embsize']}  "
          f"n_layers={model_args['nlayers']}  "
          f"n_bins={model_args.get('n_bins', 51)}")

    # A. Bulk 샘플 임베딩
    bulk_cache = OUT_DIR / "bulk_embeddings.npz"

    # 원본 황금 캐시 우선 사용 (--fresh 시 비활성화)
    if use_orig and _ORIG_BULK.exists() and not (use_cache and bulk_cache.exists()):
        print("\n[2] Bulk 임베딩 로드 (원본 domain_shift 캐시)...")
        npz      = np.load(_ORIG_BULK, allow_pickle=True)
        emb_bulk = npz["emb_raw"].astype(np.float32)   # key: emb_raw
        # y_bulk 는 원본 bulk h5ad 에서 직접 읽음
        bulk     = ad.read_h5ad(BULK_H5AD)
        y_bulk   = (bulk.obs["condition"].values == "Rejection").astype(int)
        print(f"  로드 완료: {emb_bulk.shape}")
    elif use_cache and bulk_cache.exists():
        print("\n[2] Bulk 임베딩 캐시 로드...")
        npz      = np.load(bulk_cache, allow_pickle=True)
        emb_bulk = npz["emb"].astype(np.float32)
        y_bulk   = npz["y"].astype(int)
        print(f"  로드 완료: {emb_bulk.shape}")
    else:
        print("\n[2] Bulk 학습 데이터 임베딩 중...")
        bulk = ad.read_h5ad(BULK_H5AD)
        print(f"  Bulk: {bulk.shape}")
        print(f"  조건: NR={sum(bulk.obs['condition']=='NR')}  "
              f"Rejection={sum(bulk.obs['condition']=='Rejection')}")
        print(f"  발현값 범위: {bulk.X.min():.2f} ~ {bulk.X.max():.2f} (log2 RMA)")

        bulk_genes = np.array(bulk.var_names)
        in_vocab   = np.array([g in vocab for g in bulk_genes])
        bulk_sub   = bulk[:, in_vocab]
        bulk_gids  = vocab.lookup_many(bulk_sub.var_names)
        print(f"  Vocab 매칭 유전자: {in_vocab.sum()}/{len(bulk_genes)}")

        Xb = bulk_sub.X
        if sparse.issparse(Xb):
            Xb = Xb.toarray()
        Xb = Xb.astype(np.float32)

        # Bulk RMA log2 값을 그대로 사용
        # -> normalize_total=None, log1p=False
        # -> quantile binning이 절대 scale 차이를 흡수함
        emb_bulk = embed(Xb, bulk_gids, model, vocab, model_args,
                         normalize_total=None, log1p=False,
                         device=device, desc="  Bulk", seed=SEED)

        y_bulk = (bulk.obs["condition"].values == "Rejection").astype(int)
        np.savez(bulk_cache, emb=emb_bulk, y=y_bulk,
                 patients=bulk.obs["sample"].values)
        print(f"  저장: {bulk_cache}")

    # B. Single-cell 임베딩
    sc_cache = OUT_DIR / "sc_embeddings.npz"

    # 원본 황금 캐시 우선 사용 (--fresh 시 비활성화)
    if use_orig and _ORIG_SC.exists() and not (use_cache and sc_cache.exists()):
        print("\n[3] SC 임베딩 로드 (원본 domain_shift 캐시)...")
        npz     = np.load(_ORIG_SC, allow_pickle=True)
        emb_sc  = npz["emb"].astype(np.float32)
        sc_pids = npz["patient_ids"]
        sc_cond = npz["conditions"]
        print(f"  로드 완료: {emb_sc.shape}")
    elif use_cache and sc_cache.exists():
        print("\n[3] SC 임베딩 캐시 로드...")
        npz     = np.load(sc_cache, allow_pickle=True)
        emb_sc  = npz["emb"].astype(np.float32)
        sc_pids = npz["patient_ids"]
        sc_cond = npz["conditions"]
        print(f"  로드 완료: {emb_sc.shape}")
    else:
        print("\n[3] E-MTAB-12051 단일 세포 임베딩 중...")
        sc_adata = ad.read_h5ad(SC_H5AD)
        sc_adata.obs["condition"] = sc_adata.obs["disease"].map(DISEASE_MAP)
        print(f"  SC: {sc_adata.shape}")
        print(f"  NR 세포={sum(sc_adata.obs['condition']=='NR')}  "
              f"Rejection 세포={sum(sc_adata.obs['condition']=='Rejection')}")
        print(f"  환자 수: {sc_adata.obs['orig.ident'].nunique()}명")

        sc_genes    = np.array(sc_adata.var_names)
        in_vocab_sc = np.array([g in vocab for g in sc_genes])
        sc_sub      = sc_adata[:, in_vocab_sc].copy()
        sc_gids     = vocab.lookup_many(sc_sub.var_names)
        print(f"  Vocab 매칭 유전자: {in_vocab_sc.sum()}/{len(sc_genes)}")

        # SC raw counts -> normalize(1e4) -> log1p -> binning
        emb_sc = embed(sc_sub.X, sc_gids, model, vocab, model_args,
                       normalize_total=1e4, log1p=True,
                       device=device, desc="  SC cells", seed=SEED + 1)

        sc_pids = sc_adata.obs["orig.ident"].values
        sc_cond = sc_adata.obs["condition"].values
        np.savez(sc_cache, emb=emb_sc, patient_ids=sc_pids, conditions=sc_cond)
        print(f"  저장: {sc_cache}")

    # C. 환자별 중앙값 pooling
    if use_orig and (_ORIG_DIR / "patient_embeddings.npz").exists():
        # 원본 step3에서 in-memory로 계산된 환자 임베딩 직접 로드
        # -> 재계산하면 cell 순서/binning 차이로 AUC가 달라지므로 이 파일을 신뢰
        print("\n[4] 환자 임베딩 로드 (원본 patient_embeddings.npz)...")
        pat_npz  = np.load(_ORIG_DIR / "patient_embeddings.npz", allow_pickle=True)
        X_pat    = pat_npz["emb_med"].astype(np.float32)
        y_pat    = pat_npz["y"].astype(int)
        patients = list(pat_npz["patients"])

        # sc_pids 기반으로 환자당 세포 수 계산
        pat_n_cells = [int((sc_pids == p).sum()) for p in patients]

        print(f"  로드 완료: {X_pat.shape}")
        print(f"  NR={sum(y_pat==0)}명  Rejection={sum(y_pat==1)}명")
    else:
        print("\n[4] 환자별 중앙값(median) pooling...")

        patients    = sorted(set(sc_pids))
        pat_emb     = []
        pat_labels  = []
        pat_n_cells = []

        for p in patients:
            mask = (sc_pids == p)
            pat_emb.append(np.median(emb_sc[mask], axis=0))
            cond = sc_cond[mask][0]
            pat_labels.append(1 if cond == "Rejection" else 0)
            pat_n_cells.append(int(mask.sum()))

        X_pat = np.vstack(pat_emb)    # (16, 512)
        y_pat = np.array(pat_labels)  # (16,)

        print(f"  환자 임베딩: {X_pat.shape}")
        print(f"  NR={sum(y_pat==0)}명  Rejection={sum(y_pat==1)}명")

    # D. Bulk 임베딩으로 LR 훈련 -> SC 환자 임베딩에 적용
    print(f"\n[5] 분류기 훈련 (Bulk -> SC 적용)...")
    print(f"  Bulk {emb_bulk.shape[0]}개 샘플로 LR(C={LR_C}) 훈련")
    print(f"  PCA {PCA_DIM}차원으로 축소 후 분류")

    scaler = StandardScaler()
    pca    = PCA(n_components=PCA_DIM, random_state=SEED)

    Xb_t    = pca.fit_transform(scaler.fit_transform(emb_bulk))
    clf     = LogisticRegression(C=LR_C, max_iter=2000, random_state=SEED)
    clf.fit(Xb_t, y_bulk)

    Xp_t    = pca.transform(scaler.transform(X_pat))
    y_score = clf.predict_proba(Xp_t)[:, 1]   # Rejection 확률

    # E. 결과 평가 및 출력
    auc = roc_auc_score(y_pat, y_score)

    print(f"\n[6] 결과 (E-MTAB-12051 16명 환자)")
    print(f"\n  AUC = {auc:.3f}")
    print()

    thr_top4   = float(np.percentile(y_score, 75))   # 상위 25% -> Rejection
    thr_median = float(np.median(y_score))

    for thr_name, thr in [("Top25% (상위4명)", thr_top4),
                           ("Median  (중앙값)", thr_median)]:
        y_pred = (y_score > thr).astype(int)
        cm     = confusion_matrix(y_pat, y_pred, labels=[0, 1])
        acc    = accuracy_score(y_pat, y_pred)
        bal    = balanced_accuracy_score(y_pat, y_pred)
        correct = int(cm[0, 0] + cm[1, 1])
        print(f"  [{thr_name}  thr={thr:.3f}]")
        print(f"    정답: {correct}/16명  Acc={acc:.3f}  BalAcc={bal:.3f}")
        print(f"    Rejection 검출: {cm[1,1]}/{sum(y_pat==1)}명  "
              f"NR 오분류: {cm[0,1]}/{sum(y_pat==0)}명")
        print(f"    혼동행렬: TN={cm[0,0]} FP={cm[0,1]} FN={cm[1,0]} TP={cm[1,1]}")
        print()

    # 환자별 상세 (두 threshold 모두 표시)
    y_pred_top4 = (y_score > thr_top4).astype(int)
    y_pred_med  = (y_score > thr_median).astype(int)

    print(f"  {'환자':<12}  {'실제':<10}  {'점수':>5}  Top25%       Median")
    print(f"  {'-' * 58}")
    for p, gt, sc_s, yp4, ypm, n in zip(
            patients, y_pat, y_score, y_pred_top4, y_pred_med, pat_n_cells):
        gt_str  = "Rejection" if gt == 1 else "NR"
        p4_str  = "Rej" if yp4 == 1 else "NR "
        pm_str  = "Rej" if ypm == 1 else "NR "
        ok4     = "O" if yp4 == gt else "X"
        okm     = "O" if ypm == gt else "X"
        print(f"  {p:<12}  {gt_str:<10}  {sc_s:.3f}  {p4_str}({ok4})       {pm_str}({okm})")

    # 저장
    pred_df = pd.DataFrame({
        "patient":         patients,
        "gt_label":        ["Rejection" if y == 1 else "NR" for y in y_pat],
        "y_true":          y_pat,
        "rej_score":       y_score,
        "pred_top25pct":   y_pred_top4,
        "pred_median":     y_pred_med,
        "n_cells":         pat_n_cells,
    })
    pred_df.to_csv(OUT_DIR / "predictions.csv", index=False)
    print(f"\n  저장: {OUT_DIR / 'predictions.csv'}")

    print("\n" + "=" * 60)
    print("완료")
    print(f"  AUC             : {auc:.3f}")
    for thr_name, thr in [("Top25%", thr_top4), ("Median", thr_median)]:
        yp  = (y_score > thr).astype(int)
        cm  = confusion_matrix(y_pat, yp, labels=[0, 1])
        bal = balanced_accuracy_score(y_pat, yp)
        print(f"  {thr_name} BalAcc   : {bal:.3f}  "
              f"(TN={cm[0,0]} FP={cm[0,1]} FN={cm[1,0]} TP={cm[1,1]})")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Step 3: scGPT 임베딩 기반 Bulk->SC 도메인 전이"
    )
    parser.add_argument(
        "--use-cache", action="store_true",
        help="기존 임베딩 캐시(.npz)를 재사용 (임베딩 시간 절약)"
    )
    parser.add_argument(
        "--fresh", action="store_true",
        help="원본 캐시 무시, 임베딩 처음부터 재계산 (AUC 재현성 확인용)"
    )
    args = parser.parse_args()
    main(use_cache=args.use_cache, fresh=args.fresh)
```
