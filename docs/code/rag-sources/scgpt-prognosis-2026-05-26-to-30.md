---
type: worklog-chunk
status: archive
rag_priority: medium
updated: '2026-07-20'
date_range: 2026-05-26..2026-05-30
source: code/logs/2026-06-16-scgpt-prognosis-worklog.md
topics:
- single-cell
- kidney-transplant
- prognosis
models:
- scGPT
tags:
- wiki/worklog-chunk
---

# scGPT prognosis worklog — 2026-05-26~30

> [!note] 검색용 분할본
> 원본은 [2026-06-16 scGPT prognosis worklog](../logs/2026-06-16-scgpt-prognosis-worklog.md)입니다. 결론이 충돌하면 최신 `reports/` 문서를 우선합니다.

## 완료: prognosis_sc_to_microarray_v2.py — encoder 학습 가능 확장 (2026-05-30)

### 목표
v1(`prognosis_sc_to_microarray.py`)은 scGPT encoder를 완전 동결(adapter+head만 학습)했음.
그러나 **학습 데이터가 scRNA-seq**로 인코더 사전학습(pretrain_kidney)과 동일 도메인이므로,
encoder를 함께 학습시키는 게 타당. full-tuning / last-n tuning / freeze 세 모드를 비교 실험하기 위해
`data/scripts/prognosis_sc_to_microarray_v2.py` 신규 작성(v1 복사 후 수정).

### 신규 인자 (train 서브커맨드)
| 인자 | 기본값 | 역할 |
|------|--------|------|
| `--encoder-mode {freeze, last_n, full}` | `freeze` | freeze=v1 동작(encoder 동결), last_n=마지막 N개 transformer layer만 unfreeze, full=encoder 전체 unfreeze |
| `--unfreeze-last-n` | 2 | last_n 모드에서 unfreeze할 마지막 layer 수 |
| `--encoder-lr` | 1e-5 | 학습 가능한 encoder 파라미터 전용 LR(별도 옵티마이저 그룹). adapter/head는 `--lr`(1e-4). freeze 모드에선 무시 |

### 구현 핵심
- `configure_encoder_trainable(model, mode, n)`: make_model이 동결해 둔 encoder를 모드에 따라 재설정. last_n은 `encoder.transformer_encoder.layers[-n:]`만 unfreeze. adapter+head는 항상 학습. trainable 파라미터 수 출력. `train_encoder`(bool) 반환.
- `make_optimizer`: encoder 파라미터를 별도 그룹(encoder_lr)으로, head/adapter는 lr. encoder 동결 시 단일 그룹으로 축퇴. `id(p)` 집합으로 encoder/그 외 분리.
- **체크포인트 저장/복원 (가장 중요)**: `get_state`에 `train_encoder=True`일 때만 `"encoder"` 키 추가 저장. `load_state`는 `"encoder"` 키 존재 시 자동 복원. → `evaluate`는 코드 수정 없이 fine-tuned encoder를 그대로 사용. **이 처리가 없으면 evaluate에서 make_model이 사전학습 encoder를 재로드해 학습된 encoder가 통째로 버려지는 치명적 버그 발생.**
- fold 학습 루프 / 최종 모델 학습 루프 모두에 configure 호출 + encoder_lr 전달 + get_state에 train_encoder 전달.
- `config.json`에 `encoder_mode`/`unfreeze_last_n`/`encoder_lr` 기록(재현·문서화).
- CosineAnnealingLR은 파라미터 그룹별 base_lr 기준으로 스케줄(encoder 그룹은 encoder_lr에서 코사인 감쇠).

### 세 모드 비교 실행 (evaluate는 v1과 동일, run-dir만 각각 지정)
```bash
# freeze (baseline)
... train --encoder-mode freeze --output-base results/prog_v2_freeze --fp16
# last-2 layers
... train --encoder-mode last_n --unfreeze-last-n 2 --encoder-lr 1e-5 --output-base results/prog_v2_last2 --fp16
# full fine-tune
... train --encoder-mode full --encoder-lr 1e-5 --output-base results/prog_v2_full --fp16
```
비교 지표: 각 run의 `cv_metrics.json`(OOF AUROC) + microarray `*.metrics.json`.

### 주의
- `full`은 transformer 전체 backprop이라 메모리 큼 → OOM 시 `--batch-size`↓ 또는 `--fp16`, 그래도 안 되면 `last_n`(1~2)부터.
- 환자 16명 규모라 `full`은 overfit 위험 → 보통 freeze<last_n<full 순으로 어디서 꺾이는지 관찰 권장.

### 검증
- `py_compile` 통과, `train --help`로 신규 플래그 노출 확인. 실제 학습은 미실행(사용자가 하이퍼파라미터 정해 실행 예정).

---

## 완료: prognosis_sc_to_microarray.py — scRNA-seq 학습 → microarray 평가 (2026-05-29)

### 목표
방향 전환: 기존(microarray 학습 → scRNA-seq 예측)의 **역방향**.
scRNA-seq(E-MTAB-12051)로 **학습**, 외부 microarray(GSE36059+GSE147089 merged RMA)로 **단 1회 평가**.
환자 단위 예후(NR vs Rejection) 예측. Backbone = frozen scGPT encoder(pretrain_kidney).

### 신규 스크립트: `data/scripts/prognosis_sc_to_microarray.py`
- 서브커맨드 `train`(scRNA-seq) / `evaluate`(microarray 1회).
- `prognosis_microarray_adapter.py`의 인코더/토크나이저/binning/metric 빌딩블록 재사용.

### `--train-mode` 3종
| 모드 | 학습 단위 | 관련 인자 |
|------|-----------|-----------|
| `pseudobulk_augment` (메인) | 환자별 K개 셀 샘플링→집계, M회 반복 | `--pseudobulk-cells K` `--pseudobulk-repeats M` `--pseudobulk-method {sum,mean,median}` |
| `cell_level` | 개별 셀(환자 라벨), 검증 시 환자 집계 | `--cell-agg {mean,median,p60,p75,p90}` (기본 p60) |
| `patient_pseudobulk` | 환자당 1 pseudobulk(베이스라인) | `--no-adapter` 허용 |

### Leakage 차단 (설계로 강제)
1. **환자 단위 그룹 CV** — `StratifiedGroupKFold(groups=patient)`. 같은 환자의 셀/pseudobulk가 train·val에 동시 등장 불가. CV는 threshold·epoch 선택용일 뿐 최종 평가 아님.
2. **샘플 자기완결 전처리** — scRNA-seq: `normalize_total(1e4)+log1p` (셀/pseudobulk별) → per-sample quantile binning. 데이터셋·샘플 간 통계 공유 없음 → microarray가 학습 입력에 영향 불가.
3. **결정 threshold는 train OOF 환자 점수(Youden)에서 고정** → 테스트에서 튜닝 안 함.
4. **유전자 풀은 학습 데이터에서만 도출**(train ∩ vocab = 20,783) 후 저장. 평가 시 `풀 ∩ microarray 유전자`(17,704)로 제한 — 테스트 플랫폼이 학습 유전자 선택에 관여 안 함.
5. **microarray .h5ad는 `evaluate`에서 정확히 1회만 read.** gene 선택/정규화/threshold/모델·epoch 선택에 일절 사용 안 함.

### 검증 집계 규칙
- pseudobulk_augment / patient_pseudobulk: 환자별 augmented 예측 **mean prob**로 집계 후 환자 단위 metric.
- cell_level: 셀 prob → `--cell-agg`(기본 p60)로 환자 점수. microarray는 sample-level=환자 단위 1회 예측.

### 산출물 (run_dir)
`config.json`(아키텍처·threshold·label_map·val_agg), `training_genes.json`, `oof_predictions.csv`,
`cv_metrics.json`, `fold_*/best_state.pt`, `final_model.pt`. 평가 시 fold+final 앙상블.
`evaluate` 출력: 예측 CSV + `.metrics.json`(AUROC/AUPRC/BalAcc/F1/Acc/Brier) + ROC PNG.

### 검증
- 데이터: train 53,630 cells×28,794 genes(raw counts, 16 patients, Rejection 4/NR 12), test 627×21,463(RMA log2).
- train→evaluate 스모크 테스트 통과(3 epoch, 의미 없는 수치). 유전자 교집합·threshold 재사용·앙상블 동작 확인.
- 실제 학습은 미실행(사용자가 하이퍼파라미터 정해 실행 예정).

---

## 완료: 데이터 분포 비교 시각화 & 전처리 (2026-05-28)

### 목표
scRNA-seq와 microarray 데이터 간 분포 차이를 시각적으로 확인하고,
scgpt_training_data.h5ad의 전처리 방식 개선(min-max 스케일링) 탐색

### 작업 내역

**1. E_MTAB_12051_log2cpm.h5ad 생성**
- 입력: `E_MTAB_12051.h5ad` (53,630 cells, raw counts)
- 전처리: `normalize_total(target_sum=1e6)` → `log1p(base=2)`
- 결과 범위: 0.0 ~ 19.88, 출력: `E-MTAB-12051/E_MTAB_12051_log2cpm.h5ad`

**2. Gene mean scatter plot (scRNA-seq vs microarray)**
- 방법: 공통 유전자(17,736개) 기준 gene별 평균 발현값 → scatter (x=microarray, y=scRNA-seq)
- 비교 조합 및 결과:

| microarray | scRNA-seq | Pearson r | Spearman rho |
|---|---|---|---|
| GSE36059_GSE147089_merged_rma | log2cpm (53k cells) | 0.562 | 0.739 |
| GSE36059_GSE147089_merged_rma | pseudobulk_preprocessed | 0.746 | 0.738 |
| scgpt_training_data (zeroing) | pseudobulk_preprocessed | 0.702 | 0.736 |
| scgpt_training_data_minmax | pseudobulk_preprocessed | 0.740 | 0.737 |

**3. scgpt_training_data.h5ad 전처리 분석**
- RMA ≤5인 gene을 0으로 zeroing → 5~15 구간에만 non-zero 값 존재 (bimodal)
- zero 비율: 24.07%

**4. scgpt_training_data_minmax.h5ad 생성**
- 방법: 샘플별 non-zero 값에 min-max 스케일링 적용
  - `[min_nz, max_nz] → [0, max_nz]` (선형 변환, zero 비율 유지)
- 결과: non-zero 값이 0~max 사이로 고르게 분포, Pearson r 0.702 → 0.740으로 개선
- 출력: `data/scgpt_training_data_minmax.h5ad`

### 출력 파일
- `data/E-MTAB-12051/E_MTAB_12051_log2cpm.h5ad`
- `data/scgpt_training_data_minmax.h5ad`
- `data/scatter_pseudobulk_vs_rma_v3.png` — RMA 원본 vs pseudobulk
- `data/scatter_pseudobulk_vs_zeroed_v3.png` — zeroing vs pseudobulk
- `data/scatter_pseudobulk_vs_minmax_v3.png` — min-max scaled vs pseudobulk

---

## 완료: prognosis_microarray_adapter.py 작성 (2026-05-27)

### 목표
microarray 데이터(scgpt_training_data.h5ad)를 scGPT frozen encoder로 임베딩한 후
도메인 어댑터 MLP를 거쳐 prognosis head(BCE + Cox)로 예후 예측

### 파이프라인 구조

```
microarray sample
  → preprocessing / binning  (RMA log2 → per-sample quantile bins)
  → Frozen scGPT encoder (pretrain_kidney, 12L-512d)
  → CLS embedding (512-dim)
  → MicroarrayToSCAdapter MLP
      LN(512) → Linear(512→256) → GELU → Dropout → Linear(256→512) → +x (residual)
      fc2 zero-init → 학습 초기 identity 유지
  → L2-norm
  → PrognosisHead
      LN(512) → Linear(512→256) → GELU → Dropout
        ├─ binary_out: Linear(256→1) → BCE loss
        └─ cox_out:    Linear(256→1) → Cox partial-likelihood loss
```

### 손실 함수

| 손실 | 수식 | 활성화 조건 |
|------|------|------------|
| BCE | `-Σ y·log(σ(h)) + (1-y)·log(1-σ(h))` | 항상 |
| Cox | `-Σ_i [h_i - log Σ_{j:t_j≥t_i} exp(h_j)] / n_events` | `--time-col` 지정 시 |
| Combined | `L_bce + cox_weight * L_cox` | — |

- Breslow approximation (tied times 처리)
- `--time-col`이 없으면 Cox 항 자동 비활성화

### 모델 파라미터 규모

| 구분 | 파라미터 수 |
|------|------------|
| Frozen encoder | ~50,278,400 |
| Adapter MLP | 263,680 |
| Prognosis head | 133,122 |
| **학습 대상 합계** | **396,802 (0.78%)** |

### Commands

| 커맨드 | 역할 |
|--------|------|
| `finetune` | bulk microarray 5-fold CV + final model 학습 |
| `predict-bulk` | bulk / pseudobulk h5ad → 환자별 risk CSV |
| `predict-cell` | single-cell h5ad → 세포별 risk → p{q} 집계 → CSV + plot |

### 실행 예시

```bash
# Step 1: Training (bulk microarray, time 없으면 BCE만)
python3 scripts/prognosis_microarray_adapter.py finetune \
    --adata scgpt_training_data.h5ad \
    --model-dir models/pretrain_kidney \
    --label-col condition --positive-label Rejection \
    --output-base results/prognosis_adapter

# Step 2: predict-cell (권장 — p60 집계)
python3 scripts/prognosis_microarray_adapter.py predict-cell \
    --adata E-MTAB-12051/E_MTAB_12051.h5ad \
    --normalize \
    --model-dir models/pretrain_kidney \
    --checkpoint-dir results/prognosis_adapter/run_YYYYMMDD-HHMMSS \
    --patient-col orig.ident \
    --label-col condition --positive-label Rejection \
    --time-col sampling_time_point \
    --quantile 60 --plot \
    --output results/prognosis_adapter/predict_cell_p60.csv
```

### 데이터 특성

| 구분 | 파일 | 특성 |
|------|------|------|
| 학습 | scgpt_training_data.h5ad | 627 samples, 21,463 genes, condition only, time 없음 → BCE only |
| 테스트 | E_MTAB_12051.h5ad | 53,630 cells, 16 patients, sampling_time_point 포함 → Cox 가능 |

### 설계 포인트

1. **Adapter zero-init**: fc2 weight/bias를 0으로 초기화 → 학습 초기 adapter = identity. 인코더 임베딩 공간 보존 후 점진적 도메인 이동
2. **Cox loss with event indicator = Rejection label**: 이식 후 거부반응이 발생하면 event=1, NR은 censored(event=0)로 처리
3. **predict-cell**: 세포별 risk → patient p60 집계 (WORKLOG AUC=1.000 방법 계승)
4. **Ensemble**: fold 1~5 best + final_model 평균

### 출력 파일
- `data/scripts/prognosis_microarray_adapter.py`

---

## 완료: rejection_finetune_end2end_v5.py 작성 (2026-05-27)

### 목표
WORKLOG 실험 결론을 반영하여 v4 대비 세 가지 핵심 변경 + 신규 predict-cell 커맨드 추가

### v4 → v5 변경사항

| 항목 | v4 | v5 |
|------|----|----|
| `--finetune-mode` 기본값 | `full` | **`none`** (frozen encoder) |
| DomainAdapter 기본값 | `use_adapter=True` | **`use_adapter=False`** |
| 예측 커맨드 | `predict-ft` (pseudobulk만) | `predict-ft` + **`predict-cell`** (단일세포 추가) |

### 신규: predict-cell 커맨드

단일세포 h5ad → 세포별 rejection 확률 → 환자별 p{q} 집계 파이프라인.
WORKLOG 벤치마크에서 AUC=1.000을 달성한 p60 방법을 finetune-head 기반으로 구현.

**핵심 구현: `embed_cells_batched()`**
- sparse/dense 행렬 자동 처리 (CSR 지원)
- 배치 단위로 sparse→dense 변환 → OOM 방지
- 앙상블(fold×N + final) × n_subsets 평균

**환자 집계:**
```python
patient_score = np.percentile(cell_probs[patient_mask], quantile)  # default q=60
```
- n_cells < max_seq_len: 모든 nonzero gene 사용, n_subsets 간 동일 → n_subsets=1 충분
- n_cells ≥ max_seq_len: 랜덤 서브셋 → n_subsets=3(기본값) 평균

**평가 기능:**
- 레이블 있을 경우: AUC, BalAcc, CM 자동 계산
- `--bootstrap 200`: 500 cells/환자 서브샘플링 200회 → AUC 분포 보고
- `--plot`: ROC + 환자 점수 막대 + 세포 violin 플롯 저장

### 실행 예시

```bash
# Step 1: Training (frozen encoder)
python3 scripts/rejection_finetune_end2end_v5.py finetune \
    --adata scgpt_training_data.h5ad \
    --model-dir models/pretrain_kidney \
    --label-col condition --positive-label Rejection \
    --output-base results/rejection_end2end_v5

# Step 2: predict-cell (권장 — 단일세포 p60)
python3 scripts/rejection_finetune_end2end_v5.py predict-cell \
    --adata E-MTAB-12051/E_MTAB_12051.h5ad \
    --normalize \
    --model-dir models/pretrain_kidney \
    --checkpoint-dir results/rejection_end2end_v5/run_YYYYMMDD-HHMMSS \
    --patient-col orig.ident \
    --label-col condition --positive-label Rejection \
    --quantile 60 --bootstrap 200 --plot \
    --output results/rejection_end2end_v5/predict_cell_p60.csv
```

### 설계 근거 (WORKLOG 결론 요약)

1. **Frozen encoder 필수**: full fine-tuning → specificity=0 (domain collapse)
2. **단일세포 > pseudobulk**: 거부반응은 특정 세포 서브집단이 고활성 → pseudobulk 평균화 시 신호 희석
3. **DomainAdapter 불필요**: CV AUROC는 개선되나 test BalAcc 동일 (v2 none == v1 none)

### 출력 파일
- `data/scripts/rejection_finetune_end2end_v5.py`

---

## 완료: v3 finetune 실행 + E-MTAB-12051 예측 (2026-05-27)

### 설정
- finetune-mode: `none` (encoder 완전 동결, adapter+head 265k params만 학습)
- max_seq_len: **8000** (nonzero gene 중앙값 14,514 대비 ~55% 커버)
- gene filter: `common_train_test_genes.json` (train∩test 공통 17,736 → vocab 매칭 17,704개)
- --gene-filter 옵션 신규 추가 (스크립트 수정)
- model: pretrain_kidney

### CV 결과 (5-fold stratified)

| Fold | AUROC | AUPRC | bal_acc | best_epoch |
|------|-------|-------|---------|------------|
| 1 | 0.7772 | 0.5796 | 0.6556 | 36 |
| 2 | 0.8225 | 0.6479 | 0.6833 | 41 |
| 3 | 0.8063 | 0.6348 | 0.6643 | 16 |
| 4 | 0.7460 | 0.5841 | 0.6421 | 18 |
| 5 | 0.7466 | 0.5198 | 0.6323 | 31 |
| **OOF (thr=0.5)** | **0.769** | 0.558 | 0.656 | — |
| **OOF (thr=0.234)** | — | — | **0.720** | — |

- Per-fold AUROC: 0.780 ± 0.031
- 최적 threshold: 0.234 (Youden)
- 최종 모델 학습 에폭: 28

### E-MTAB-12051 예측 결과 (16 샘플, threshold=0.234)

| sample_id | ensemble | std | 예측 |
|-----------|----------|-----|------|
| EXT217 | 0.045 | 0.011 | NR |
| EXT230 | 0.610 | 0.081 | Rejection |
| EXT238 | 0.176 | 0.040 | NR |
| EXT240 | 0.346 | 0.067 | Rejection |
| EXT241 | **0.944** | 0.021 | Rejection |
| NEPH006 | 0.346 | 0.037 | Rejection |
| NEPH009 | 0.618 | 0.092 | Rejection |
| NEPH010 | 0.039 | 0.009 | NR |
| NEPH011 | 0.053 | 0.010 | NR |
| NEPH012 | 0.065 | 0.013 | NR |
| NEPH014 | 0.134 | 0.024 | NR |
| NEPH015 | 0.296 | 0.051 | Rejection |
| NEPH016 | 0.103 | 0.019 | NR |
| NEPH017 | **0.864** | 0.057 | Rejection |
| NEPH018 | **0.832** | 0.066 | Rejection |
| NEPH019 | 0.299 | 0.042 | Rejection |

- 결과: `results/rejection_end2end_v3/run_20260526-145015/predictions_emtab12051.csv`
- 앙상블: fold 1~5 + final_model (6개 모델), n_subsets=20

---

## 완료: rejection_finetune_end2end_v3.py 작성 (2026-05-26)

### 목표
v2 대비 두 가지 핵심 변경 적용:
1. `include_zero_gene=False` — 샘플별 nonzero 유전자만 인코더에 입력 (scGPT 표준 동작)
2. raw count test 데이터(E_MTAB_12051_pseudobulk.h5ad)에 scGPT 정규화 지원

### 학습/테스트 데이터 분리

| 구분 | 파일 | 상태 | 처리 |
|------|------|------|------|
| Training | `scgpt_training_data.h5ad` | 전처리 완료 (RMA zeroed) | 정규화 없음, nonzero 필터만 |
| Test | `E_MTAB_12051_pseudobulk.h5ad` | raw counts | `--normalize` 플래그 → normalize_total(1e4)+log1p |

### v2 → v3 변경사항 요약

| 항목 | v2 | v3 |
|------|----|----|
| 토크나이즈 | 전체 유전자 랜덤 샘플링 (zero 포함) | `include_zero_gene=False`: 샘플별 nonzero 유전자만 |
| `sample_gene_columns()` | 존재 (고정 col_idx 지원) | 제거 |
| `make_token_batch()` | 벡터화된 고정 col_idx 방식 | `make_token_batch_nonzero()` (샘플별 nonzero 루프) |
| `fixed_col_idx` | `--fixed-genes-file` 파라미터 지원 | 제거 |
| 정규화 함수 | 없음 | `normalize_scgpt(X, target_sum=1e4)` 추가 |
| `--normalize` 플래그 | 없음 | `finetune` / `predict-ft` 양쪽에 추가 |
| Step 2 템플릿 | v2 파일명 | v3 파일명 + `--normalize` 포함 |

### 핵심 구현: `make_token_batch_nonzero()`

```python
for i, row in enumerate(row_idx):
    x_row = X[row]
    nonzero_cols = np.where(x_row > 0)[0]   # include_zero_gene=False
    n_select = min(max_seq_len - 1, len(nonzero_cols))
    if len(nonzero_cols) > n_select:
        selected = rng.choice(nonzero_cols, size=n_select, replace=False)
    else:
        selected = nonzero_cols
    gene_tok[i, 1:1+n_select] = gene_ids_all[selected]
    val_tok[i, 1:1+n_select] = bin_values(x_row[selected], n_bins)
```
- nonzero 유전자 수 < max_seq_len-1: 전체 사용 (subset 간 동일, 무작위성 없음)
- nonzero 유전자 수 ≥ max_seq_len-1: rng로 랜덤 서브셋 (subset 간 다름 → n_subsets 평균 의미 있음)

### 핵심 구현: `normalize_scgpt()`

```python
def normalize_scgpt(X, target_sum=1e4):
    row_sums = X.sum(axis=1, keepdims=True)
    row_sums = np.where(row_sums == 0, 1.0, row_sums)
    return np.log1p(X / row_sums * target_sum).astype(np.float32)
```
- scanpy `sc.pp.normalize_total` + `sc.pp.log1p` 와 동일 (numpy 직접 구현)

### 실행 예시

```bash
# Step 1: Training
python3 scripts/rejection_finetune_end2end_v3.py finetune \
    --adata scgpt_training_data.h5ad \
    --model-dir models/pretrain_kidney \
    --label-col condition --positive-label Rejection \
    --output-base results/rejection_end2end_v3

# Step 2: Prediction (raw count → --normalize 필수)
python3 scripts/rejection_finetune_end2end_v3.py predict-ft \
    --adata E_MTAB_12051_pseudobulk.h5ad \
    --normalize \
    --model-dir models/pretrain_kidney \
    --checkpoint-dir results/rejection_end2end_v3/run_YYYYMMDD-HHMMSS \
    --output results/rejection_end2end_v3/predict_EMTAB.csv
```

### 출력 파일
- `data/scripts/rejection_finetune_end2end_v3.py`

---

## 완료: scgpt_training_data.h5ad 생성 (2026-05-26)

### 목표
GSE147089, GSE36059 두 마이크로어레이 데이터셋을 병합하여 scGPT 학습용 통합 데이터셋 생성

### 전처리 배경
- 원본 데이터: 마이크로어레이 CEL 파일 → RMA 정규화 (log2 스케일, 값 범위 ~5~15)
- **RMA 후 발현값 ≤ 5인 gene을 0으로 zeroing** — 발현이 미미한 gene을 미발현으로 처리하여 bulk RNA-seq처럼 zero-inflated 분포를 만들기 위한 의도적 전처리
- 결과: 각 샘플당 발현값이 **0 (미발현)** 또는 **5 초과 (발현)** 의 bimodal 분포

### 병합 상세

| 항목 | 내용 |
|------|------|
| 입력 1 | `GSE147089/GSE147089_rma_zeroed.h5ad` (224 samples) |
| 입력 2 | `GSE36059/GSE36059_rma_thresh5.h5ad` (403 samples) |
| 출력 | `data/scgpt_training_data.h5ad` (627 samples × 21,463 genes) |
| 유전자 | 두 데이터셋 완전 동일 (21,463개, join='inner' 손실 없음) |

### 메타데이터 구성

| obs 컬럼 | 내용 |
|----------|------|
| `sample` | 샘플 GSM ID |
| `condition` | `NR` (449개) / `Rejection` (178개) |
| `dataset` | `GSE36059` (403) / `GSE147089` (224) |

**condition 통합 매핑:**
- `non-rejecting`, `No_ABMR` → `NR`
- `ABMR`, `TCMR`, `DSApos`, `DSAneg`, `MIXED` → `Rejection`

### 발현값 (adata.X) 현재 상태
- RMA 원본값 그대로 (0.0 ~ 15.11, float32)
- 0값 비율: 24.07% (zeroing 처리된 미발현 gene)
- scGPT encoder가 binning을 담당하므로 추가 정규화 없이 보관

### 출력 파일
- `data/scgpt_training_data.h5ad` — 104MB

---
