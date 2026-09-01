---
type: worklog
status: archive
rag_priority: low
updated: '2026-07-20'
tags:
- wiki/worklog
---

# 2026-06-01 - Prognosis Microarray-to-SC Adapter

작성일: 2026-06-01

이 로그는 `prognosis_microarray_adapter.py`를 기준으로 최종 microarray-to-scRNA 예후 예측 모델을 재현하기 위해 남기는 코드 기록이다.

## 목적

Bulk microarray에서 학습한 NR vs Rejection 예측 신호를 single-cell RNA-seq 환자 데이터에 전이한다. scGPT kidney pretrained encoder는 freeze하고, microarray-to-SC adapter와 prognosis head만 학습한다.

## 핵심 구조

```text
RMA/log2 microarray sample
  -> nonzero gene tokenization
  -> quantile-binned values
  -> frozen scGPT kidney encoder
  -> CLS embedding
  -> residual adapter
  -> L2 normalize
  -> binary probability and Cox risk output
```

Adapter:

```text
LayerNorm(512)
  -> Linear(512, 256)
  -> GELU
  -> Dropout(0.2)
  -> Linear(256, 512)
  -> residual add
```

Head:

```text
LayerNorm(512)
  -> Linear(512, 256)
  -> GELU
  -> Dropout(0.2)
  -> binary_out
  -> cox_out
```

현재 training command는 BCE-only mode다. Cox output은 저장되지만 `finetune`에서는 Cox loss가 비활성화되어 있다.

## 주요 구현 포인트

| 영역 | 구현 |
| --- | --- |
| Encoder | `models/pretrain_kidney`의 `vocab.json`, `args.json`, `best_model.pt`를 로드 |
| Trainable params | adapter와 head만 학습 |
| Tokenization | sample/cell별 nonzero gene만 사용 |
| Value encoding | per-sample quantile binning |
| CV | 5-fold stratified CV |
| Class imbalance | fold-wise `pos_weight` |
| Early stopping | validation AUROC 기준 |
| Final model | fold best epoch 평균만큼 전체 training data로 재학습 |
| Prediction ensemble | `fold_*/best_state.pt`와 `final_model.pt` 평균 |

## Commands

Fine-tuning:

```bash
python3 scripts/prognosis_microarray_adapter.py finetune \
  --adata scgpt_training_data.h5ad \
  --model-dir models/pretrain_kidney \
  --label-col condition \
  --positive-label Rejection \
  --output-base results/prognosis_adapter
```

Single-cell prediction:

```bash
python3 scripts/prognosis_microarray_adapter.py predict-cell \
  --adata E-MTAB-12051/E_MTAB_12051.h5ad \
  --normalize \
  --model-dir models/pretrain_kidney \
  --checkpoint-dir results/prognosis_adapter/run_YYYYMMDD-HHMMSS \
  --patient-col orig.ident \
  --label-col condition \
  --positive-label Rejection \
  --time-col sampling_time_point \
  --quantile 60 \
  --plot \
  --output results/prognosis_adapter/predict_cell_p60.csv
```

Pseudobulk prediction:

```bash
python3 scripts/prognosis_microarray_adapter.py predict-bulk \
  --adata E-MTAB-12051/E_MTAB_12051_pseudobulk.h5ad \
  --normalize \
  --model-dir models/pretrain_kidney \
  --checkpoint-dir results/prognosis_adapter/run_YYYYMMDD-HHMMSS \
  --label-col condition \
  --positive-label Rejection \
  --output results/prognosis_adapter/predict_bulk.csv
```

## Output Files

| 파일 | 내용 |
| --- | --- |
| `training_genes.json` | training에 사용된 gene list |
| `label_map.json` | label to class mapping |
| `args.json` | 실행 argument와 architecture hyperparameter |
| `fold_*/best_state.pt` | fold별 adapter/head best state |
| `oof_predictions.csv` | out-of-fold sample probability |
| `cv_metrics.json` | OOF AUROC, AUPRC, balanced accuracy, threshold, fold metrics |
| `final_model.pt` | 전체 training data로 학습한 final adapter/head |
| `predict_cell_p60.csv` | single-cell 환자별 p60 probability/risk |
| `predict_bulk.csv` | bulk 또는 pseudobulk sample probability/risk |

## OOF Adapter Comparison

![Prognosis adapter comparison](../../assets/reports/prognosis-adapter-comparison.png)

| 설정 | OOF AUROC | AUPRC | Balanced ACC |
| --- | ---: | ---: | ---: |
| Zeroed + L2 | 0.762 | 0.531 | 0.707 |
| Zeroed | 0.755 | 0.538 | 0.705 |
| RMA + L2 | 0.703 | 0.509 | 0.666 |
| RMA | 0.701 | 0.506 | 0.664 |
| MinMax + L2 | 0.746 | 0.523 | 0.693 |
| MinMax | 0.746 | 0.523 | 0.693 |

## 주의할 점

- RMA microarray 입력에는 `--normalize`를 기본적으로 사용하지 않는다.
- Raw count single-cell 또는 pseudobulk 입력에는 `--normalize`를 켠다.
- Prediction 시 `training_genes.json`이 있으면 training gene pool으로 제한한다.
- `predict-cell`의 patient-level 기본 score는 p60 probability다.
- Cox branch는 아직 survival loss로 학습되지 않았으므로 `cox_risk`는 보조 출력으로만 해석한다.

## 관련 문서

- [Microarray-to-scRNA Prognosis Adapter](../../reports/microarray-to-scrna-prognosis-adapter.md)
- [Transplant Prognosis Model Notes](../../reports/transplant-prognosis-model-notes.md)
- [scGPT Rejection End-to-End v3/v4](2026-05-26-scgpt-rejection-end2end-v3-v4.md)
