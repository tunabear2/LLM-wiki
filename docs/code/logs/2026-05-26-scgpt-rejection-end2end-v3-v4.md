# 2026-05-26 - scGPT Rejection End-to-End Fine-tuning v3/v4

작성일: 2026-05-26

이 문서는 `rejection_finetune_end2end_v3.py`와 `rejection_finetune_end2end_v4.py`의 변경 내용을 정리한 코드 로그이다. v3는 scGPT 표준 동작에 가까운 nonzero gene tokenization과 raw count normalization을 정리한 버전이고, v4는 adapter와 L2 normalization의 ablation을 명시적으로 실험할 수 있게 만든 버전이다.

## 한 줄 결론

v3는 `include_zero_gene=False` 방식으로 per-sample nonzero gene만 tokenization하고, raw count prediction data에는 `--normalize`로 `normalize_total(1e4) -> log1p`를 적용한다. v4는 같은 pipeline 위에 `--no-adapter`, `--no-l2-norm` flag를 추가해 `DomainAdapter`와 `L2 norm`의 실제 기여도를 분리해서 볼 수 있게 한다.

## 스크립트

| 버전 | 파일명 | 핵심 목적 |
| --- | --- | --- |
| v3 | `scripts/rejection_finetune_end2end_v3.py` | nonzero gene tokenization, raw count normalization, training gene pool 제한 |
| v4 | `scripts/rejection_finetune_end2end_v4.py` | v3 기반 adapter/L2-norm ablation 및 checkpoint architecture metadata 저장 |

## v3 구조

```text
scGPT encoder
  -> CLS embedding
  -> DomainAdapter
  -> L2 normalize
  -> RejectionHead
  -> logit
```

v3의 핵심 변경점:

- `include_zero_gene=False`에 맞춰 sample마다 expression이 0보다 큰 gene만 tokenization한다.
- nonzero gene 수가 `max_seq_len - 1`보다 많으면 random subset을 뽑는다.
- raw count 입력을 위한 `normalize_scgpt()`를 추가했다.
- training data는 기본적으로 preprocessed log-normalized `.h5ad`를 가정한다.
- test/prediction data가 raw count이면 `predict-ft --normalize`를 사용한다.
- 기존 fixed column index 기반 gene subset 대신 per-sample nonzero filtering을 사용한다.
- `training_genes.json`을 저장하고 prediction 시 기본적으로 training gene pool로 제한한다.

## v3 tokenization

`make_token_batch_nonzero()`는 row마다 nonzero gene만 고른 뒤, 선택된 expression value를 quantile binning한다.

```text
sample row
  -> nonzero genes only
  -> random subset if too many genes
  -> quantile binning
  -> [CLS, gene1, ..., geneN, PAD, ...]
```

이 방식은 zero expression gene을 대량으로 넣어 sequence를 채우는 것보다 scGPT pretraining behavior에 가깝다. 다만 random subset을 쓰기 때문에 validation/prediction에서는 `n_subsets`를 충분히 크게 잡아 stochasticity를 줄인다.

## v3 normalization

`normalize_scgpt()`는 raw count matrix에 row-wise normalization을 적용한다.

```text
raw counts
  -> row sum normalization to 1e4
  -> log1p
```

사용 기준:

| 입력 데이터 | `--normalize` |
| --- | --- |
| 이미 log-normalized된 training `.h5ad` | 사용하지 않음 |
| raw count pseudobulk `.h5ad` | 사용 |
| single-cell raw count를 sample/patient로 pseudobulk한 데이터 | 사용 |
| RMA microarray처럼 이미 scale이 정리된 데이터 | 사용하지 않음 |

## v4 구조

v4는 v3의 기본 구조를 유지하되, `DomainAdapter`와 `L2 normalize`를 각각 끌 수 있게 했다.

| 옵션 | 구조 |
| --- | --- |
| default | `encoder -> CLS -> DomainAdapter -> L2 norm -> RejectionHead -> logit` |
| `--no-adapter` | `encoder -> CLS -> L2 norm -> RejectionHead -> logit` |
| `--no-l2-norm` | `encoder -> CLS -> DomainAdapter -> RejectionHead -> logit` |
| 둘 다 off | `encoder -> CLS -> RejectionHead -> logit` |

코드상으로는 `ScGPTRejectionModel`에 `use_adapter`, `use_l2norm` flag를 추가했다.

```python
class ScGPTRejectionModel(nn.Module):
    def forward(self, gene_ids: Tensor, values: Tensor, pad_mask: Tensor) -> Tensor:
        cls = self.encoder(gene_ids, values, pad_mask)
        if self.use_adapter:
            cls = self.adapter(cls)
        if self.use_l2norm:
            cls = F.normalize(cls, p=2, dim=1)
        return self.head(cls)
```

## v3 -> v4 변경점

| 영역 | v3 | v4 |
| --- | --- | --- |
| Adapter | 항상 사용 | `--no-adapter`로 제거 가능 |
| L2 normalization | 항상 사용 | `--no-l2-norm`으로 제거 가능 |
| Model wrapper | 고정 architecture | `use_adapter`, `use_l2norm` flag 기반 architecture |
| Optimizer group | encoder, adapter, head | adapter가 없으면 adapter group 생략 |
| Checkpoint metadata | `adapter_hidden`, `dropout`, `finetune_mode`, `last_n_layers` | `use_adapter`, `use_l2norm` 추가 저장 |
| Prediction loader | v3 architecture로만 복원 | checkpoint metadata를 읽어 architecture 자동 복원 |
| 실험 목적 | 안정적인 end-to-end fine-tuning | adapter/L2 norm의 독립 기여도 ablation |

## 왜 adapter와 L2 norm을 분리해서 보나?

`DomainAdapter`는 microarray/bulk/pseudobulk 같은 training domain이 scGPT pretraining domain과 다를 때, CLS embedding을 task/domain에 맞게 작은 residual MLP로 조정하는 역할을 한다.

`L2 normalize`는 classifier head가 embedding magnitude보다 direction을 보도록 만드는 장치다. Domain shift 상황에서는 scale 차이를 줄여 안정적일 수 있지만, 예후나 rejection signal이 embedding norm에 담기는 경우에는 정보를 잃을 수 있다.

따라서 v4의 ablation은 아래 질문을 분리해서 답하려는 목적이다.

- 성능 개선이 adapter 때문인가?
- L2 normalization이 domain transfer에 도움이 되는가?
- adapter와 L2 norm을 같이 쓸 때만 안정적인가?
- non-single-cell training data에서는 encoder freeze + adapter가 full fine-tuning보다 나은가?

## 권장 실험 매트릭스

동일한 seed, fold split, gene filter, `max_seq_len`, `final_eval_subsets`를 고정하고 아래 조합을 비교한다.

| 실험 | 주요 옵션 | 목적 |
| --- | --- | --- |
| v4 default | adapter on, L2 on | v3와 동일한 기준선 |
| no adapter | `--no-adapter` | adapter가 domain shift를 흡수하는지 확인 |
| no L2 norm | `--no-l2-norm` | embedding magnitude 정보가 필요한지 확인 |
| plain CLS head | `--no-adapter --no-l2-norm` | 가장 단순한 head baseline |
| frozen encoder | `--finetune-mode none` | non-single-cell training에서 pretrained encoder 보존 효과 확인 |
| last-n | `--finetune-mode last-n --last-n-layers 2` | encoder 일부만 task에 맞게 조정 |
| full | `--finetune-mode full` | end-to-end fine-tuning upper bound와 overfit risk 확인 |

## 실행 예시

v4 default fine-tuning:

```bash
python3 scripts/rejection_finetune_end2end_v4.py finetune \
  --adata scgpt_training_data.h5ad \
  --model-dir models/pretrain_kidney \
  --output-base results/rejection_end2end_v4 \
  --sample-col sample \
  --label-col condition \
  --positive-label Rejection \
  --n-folds 5 \
  --max-seq-len 1200 \
  --finetune-mode full \
  --batch-size 8 \
  --eval-batch-size 8
```

Adapter ablation:

```bash
python3 scripts/rejection_finetune_end2end_v4.py finetune \
  --adata scgpt_training_data.h5ad \
  --model-dir models/pretrain_kidney \
  --output-base results/rejection_end2end_v4_no_adapter \
  --no-adapter
```

L2 norm ablation:

```bash
python3 scripts/rejection_finetune_end2end_v4.py finetune \
  --adata scgpt_training_data.h5ad \
  --model-dir models/pretrain_kidney \
  --output-base results/rejection_end2end_v4_no_l2norm \
  --no-l2-norm
```

Prediction with raw count pseudobulk:

```bash
python3 scripts/rejection_finetune_end2end_v4.py predict-ft \
  --adata E_MTAB_12051_pseudobulk.h5ad \
  --normalize \
  --model-dir models/pretrain_kidney \
  --checkpoint-dir results/rejection_end2end_v4/run_YYYYMMDD-HHMMSS \
  --positive-label Rejection \
  --batch-size 8 \
  --n-subsets 30 \
  --output results/rejection_end2end_v4/predictions.csv
```

## Output files

| 파일 | 내용 |
| --- | --- |
| `training_genes.json` | training에 사용된 gene name list |
| `fold_*/best_state.pt` | fold별 early stopping best state |
| `fold_*/model.pt` | fold별 end-to-end checkpoint |
| `fold_*/training_history.csv` | epoch별 train/validation metric |
| `fold_*/val_predictions.csv` | fold validation prediction |
| `oof_predictions.csv` | out-of-fold probability |
| `cv_metrics.json` | OOF metric, optimal threshold, fold metric |
| `final_model.pt` | 전체 training data로 다시 학습한 final model |
| `finetune_config.json` | 실행 argument 기록 |
| `run_manifest.json` | run path와 입력 파일 기록 |

v4 checkpoint에는 아래 architecture metadata가 추가된다.

```text
use_adapter
use_l2norm
adapter_hidden
hidden_dim
dropout
finetune_mode
last_n_layers
max_seq_len
final_eval_subsets
```

## 주의할 점

- v4에서 `--no-adapter`로 학습한 checkpoint는 adapter parameter가 없으므로, prediction loader가 반드시 `use_adapter=False`를 읽어 같은 architecture로 복원해야 한다.
- `--no-l2-norm`은 embedding scale까지 head가 사용하게 하므로 overfit 여부와 calibration을 같이 확인한다.
- `train_eval_subsets`는 training 중 validation 시간을 크게 늘릴 수 있으므로 작게 두고, 최종 OOF/prediction은 `final_eval_subsets` 또는 `n_subsets`를 크게 둔다.
- raw count prediction data에는 `--normalize`를 빼먹지 않는다.
- `training_genes.json`으로 prediction gene pool을 제한하는 것이 train/test gene sampling 차이를 줄이는 데 중요하다.
- 작은 cohort에서는 fold AUROC보다 OOF probability, threshold 안정성, per-sample prediction variance를 같이 본다.

## 관련 문서

- [scGPT Rejection End-to-End v1/v2](2026-05-22-scgpt-rejection-end2end-v1-v2.md)
- [scGPT Rejection Worklog](2026-05-20-scgpt-rejection-worklog.md)
- [Transplant Prognosis Model Notes](../../reports/transplant-prognosis-model-notes.md)
