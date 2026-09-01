---
type: worklog
status: archive
rag_priority: low
updated: '2026-07-20'
tags:
- wiki/worklog
---

# 2026-05-22 - scGPT Rejection End-to-End Fine-tuning v1/v2

작성일: 2026-05-22

이 문서는 bulk microarray 또는 pseudobulk `.h5ad` 데이터를 입력으로 받아, pretrained scGPT Transformer encoder를 rejection classifier로 end-to-end fine-tuning하는 스크립트의 v1/v2 변경 기록이다.

## 한 줄 결론

v1은 `scGPT encoder -> CLS -> L2 normalize -> rejection head` 구조였고, v2는 그 사이에 `DomainAdapter`를 넣어 microarray/bulk domain shift를 흡수하도록 바꾼 버전이다. 또한 v2에서는 `pos_weight`를 전체 label이 아니라 각 CV fold의 train split에서 계산해 validation label leakage를 줄였다.

## 스크립트

| 버전 | 파일명 | 핵심 구조 |
| --- | --- | --- |
| v1 | `scripts/rejection_finetune_end2end.py` | scGPT encoder + rejection head |
| v2 | `scripts/rejection_finetune_end2end_v2.py` | scGPT encoder + domain adapter + rejection head |

## 목적

Bulk microarray 또는 pseudobulk 데이터를 patient/sample 단위로 입력해 NR vs Rejection을 예측한다. 기존 frozen-embedding pipeline과 달리, scGPT encoder 자체를 head와 함께 fine-tuning할 수 있도록 설계했다.

지원 명령:

- `finetune`: labeled `.h5ad` -> stratified CV -> fold checkpoint와 final checkpoint 저장
- `predict-ft`: new `.h5ad` -> fold/final checkpoint ensemble -> prediction CSV 저장

## 데이터 가정

- `.h5ad`의 row는 patient/sample 단위이다.
- `adata.var_names`는 pretrained scGPT vocab과 맞는 gene symbol이어야 한다.
- 기본 label column은 `condition`이고, positive label은 `Rejection`이다.
- Prediction 시에는 기본적으로 `training_genes.json`을 이용해 training gene pool로 gene set을 제한한다.

## v1 구조

```text
scGPT encoder
  -> CLS embedding
  -> L2 normalize
  -> RejectionHead
  -> logit
```

핵심 model wrapper:

```python
class ScGPTRejectionModel(nn.Module):
    def __init__(self, encoder: ScGPTEncoder, d_model: int, hidden_dim: int, dropout: float) -> None:
        super().__init__()
        self.encoder = encoder
        self.head = RejectionHead(d_model, hidden_dim, dropout)

    def forward(self, gene_ids: Tensor, values: Tensor, pad_mask: Tensor) -> Tensor:
        cls = self.encoder(gene_ids, values, pad_mask)
        cls = F.normalize(cls, p=2, dim=1)
        return self.head(cls)
```

v1의 중요한 특징:

- `finetune-mode`로 `full`, `last-n`, `none`을 선택할 수 있다.
- `last-n`에서는 마지막 N개 Transformer layer와 value encoder만 업데이트한다.
- Random gene subset을 forward pass마다 sampling할 수 있다.
- `fixed-genes-file`을 주면 random sampling 대신 고정 gene subset으로 학습/추론한다.
- CV fold checkpoint와 all-data final checkpoint를 모두 저장한다.

## v2 구조

```text
scGPT encoder
  -> CLS embedding
  -> DomainAdapter
  -> L2 normalize
  -> RejectionHead
  -> logit
```

추가된 domain adapter:

```python
class DomainAdapter(nn.Module):
    def __init__(self, d_model: int, adapter_hidden: int, dropout: float) -> None:
        super().__init__()
        self.norm = nn.LayerNorm(d_model)
        self.fc1 = nn.Linear(d_model, adapter_hidden)
        self.act = nn.GELU()
        self.drop = nn.Dropout(dropout)
        self.fc2 = nn.Linear(adapter_hidden, d_model)

    def forward(self, x: Tensor) -> Tensor:
        return x + self.fc2(self.drop(self.act(self.fc1(self.norm(x)))))
```

v2 model wrapper:

```python
class ScGPTRejectionModel(nn.Module):
    def __init__(
        self,
        encoder: ScGPTEncoder,
        d_model: int,
        adapter_hidden: int,
        hidden_dim: int,
        dropout: float,
    ) -> None:
        super().__init__()
        self.encoder = encoder
        self.adapter = DomainAdapter(d_model, adapter_hidden, dropout)
        self.head = RejectionHead(d_model, hidden_dim, dropout)

    def forward(self, gene_ids: Tensor, values: Tensor, pad_mask: Tensor) -> Tensor:
        cls = self.encoder(gene_ids, values, pad_mask)
        cls = self.adapter(cls)
        cls = F.normalize(cls, p=2, dim=1)
        return self.head(cls)
```

## v1 -> v2 변경점

| 영역 | v1 | v2 |
| --- | --- | --- |
| Architecture | CLS embedding을 바로 L2 normalize 후 head 입력 | CLS와 L2 normalize 사이에 residual bottleneck `DomainAdapter` 추가 |
| Domain adaptation | Encoder/value encoder fine-tuning에 의존 | Adapter가 microarray/bulk domain shift를 흡수하도록 설계 |
| Trainable modules | Encoder mode에 따라 encoder + head | Encoder mode에 따라 encoder + adapter + head |
| Optimizer groups | encoder params, head params | encoder params, adapter params, head params |
| `pos_weight` | 전체 label 분포로 한 번 계산 | fold train split마다 계산 |
| Final model loss | CV에서 만든 global criterion 재사용 | all-data label 분포로 final criterion 재계산 |
| Checkpoint metadata | `hidden_dim`, `dropout`, `finetune_mode`, `last_n_layers` | `adapter_hidden` 추가 저장 |
| Prediction compatibility | v1 checkpoint만 대응 | `adapter_hidden` default 128로 backward-compatible load |

## Label leakage 수정

v1에서는 CV 전에 전체 label 분포로 `pos_weight`를 계산했다.

```python
pos = int((labels == 1).sum())
neg = int((labels == 0).sum())
pos_weight = torch.tensor([neg / max(pos, 1)], device=device)
criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
```

v2에서는 fold마다 train split만 사용한다.

```python
fold_pos = int((labels[train_idx] == 1).sum())
fold_neg = int((labels[train_idx] == 0).sum())
fold_pos_weight = torch.tensor([fold_neg / max(fold_pos, 1)], device=device)
criterion = nn.BCEWithLogitsLoss(pos_weight=fold_pos_weight)
```

Final all-data model에서는 전체 학습 데이터로 다시 계산한다.

```python
all_pos = int((labels == 1).sum())
all_neg = int((labels == 0).sum())
final_pos_weight = torch.tensor([all_neg / max(all_pos, 1)], device=device)
final_criterion = nn.BCEWithLogitsLoss(pos_weight=final_pos_weight)
```

## 실행 예시

Fine-tuning:

```bash
python3 scripts/rejection_finetune_end2end_v2.py finetune \
  --adata <train.h5ad> \
  --model-dir <pretrained_scgpt_model_dir> \
  --output-base results/rejection_end2end \
  --sample-col sample \
  --label-col condition \
  --positive-label Rejection \
  --n-folds 5 \
  --max-seq-len 1200 \
  --finetune-mode full \
  --batch-size 8 \
  --eval-batch-size 8
```

Prediction:

```bash
python3 scripts/rejection_finetune_end2end_v2.py predict-ft \
  --adata <test.h5ad> \
  --model-dir <pretrained_scgpt_model_dir> \
  --checkpoint-dir <results/rejection_end2end/run_YYYYMMDD-HHMMSS> \
  --positive-label Rejection \
  --batch-size 8 \
  --n-subsets 30 \
  --output <predictions.csv>
```

## Output files

| 파일 | 내용 |
| --- | --- |
| `training_genes.json` | 학습에 사용한 gene name list |
| `fold_*/best_state.pt` | fold별 early stopping best state |
| `fold_*/model.pt` | fold별 end-to-end checkpoint |
| `fold_*/training_history.csv` | epoch별 train/validation metric |
| `fold_*/val_predictions.csv` | fold validation prediction |
| `oof_predictions.csv` | out-of-fold probability |
| `cv_metrics.json` | OOF metric, optimal threshold, fold metric |
| `final_model.pt` | 전체 학습 데이터로 다시 학습한 final model |
| `finetune_config.json` | 실행 argument 기록 |
| `run_manifest.json` | run path와 입력 파일 기록 |

## 주의할 점

- `train_eval_subsets`는 validation 시간이 선형으로 늘어나므로 training 중에는 작게 유지한다.
- 최종 OOF probability와 threshold 안정성이 중요하면 `final_eval_subsets`를 30 이상으로 둔다.
- `fixed-genes-file`을 쓰면 prediction에서도 같은 파일을 넘겨야 train/test gene sampling 차이가 줄어든다.
- `training_genes.json`이 있으면 prediction은 기본적으로 training gene pool로 제한된다.
- v2 checkpoint를 v1 스크립트로 읽을 수는 없다. v2 loader는 `adapter_hidden` default를 둬 v1 checkpoint 일부와의 backward compatibility를 고려했다.
- scGPT checkpoint의 `Wqkv` key는 PyTorch `MultiheadAttention`의 `in_proj` key로 rename해서 로드한다.

## 연구 맥락

이 스크립트는 [scGPT rejection worklog](2026-05-20-scgpt-rejection-worklog.md)의 domain shift 실험 이후, frozen embedding transfer가 아니라 encoder 자체를 rejection task에 맞게 조정하려는 방향의 실험 기록이다.

후속 버전인 v3/v4에서는 nonzero gene tokenization, raw count normalization, adapter/L2-norm ablation을 추가했다. 자세한 내용은 [scGPT rejection end-to-end fine-tuning v3/v4](2026-05-26-scgpt-rejection-end2end-v3-v4.md)에 정리한다.
