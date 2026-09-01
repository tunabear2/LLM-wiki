---
type: report
status: active
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/report
---

# scGPT Prognosis Progress Map

작성일: 2026-06-16

이 문서는 server에서 가져온 `WORKLOG.md`와 `SESSIONS.md`를 바탕으로, 신장 이식 거부반응/예후 예측 작업의 현재 상태를 위키용으로 재정리한 최신 요약이다. 원문은 [2026-06-16 scGPT prognosis worklog](../code/logs/2026-06-16-scgpt-prognosis-worklog.md)와 [2026-06-16 sessions log](../code/logs/2026-06-16-sessions-log.md)에 보존했다.

## 한 줄 결론

현재 가장 안정적인 축은 bulk microarray에서 학습한 frozen `pretrain_kidney` scGPT encoder + residual adapter + prognosis head를 single-cell 환자 데이터에 적용하고, cell-level probability를 환자 단위 p60 score로 집계하는 방향이다. E-MTAB-12051에서는 환자 단위 AUROC 0.875, 외부 scRNA-seq 중 GSE195719에서는 AUROC 1.000을 얻었고, 24개 kidney microarray RMA/라벨링을 통해 다음 단계인 19개 cohort multi-dataset 학습 기반도 준비했다.

## 현재 작업 지도

| 축 | 현재 상태 | 핵심 결론 |
| --- | --- | --- |
| Bulk microarray -> scRNA-seq 예측 | `prognosis_adapter_8000`을 E-MTAB 및 외부 scRNA-seq 5개 파일에 적용 | `pretrain_kidney` backbone과 p60 aggregation이 가장 일관적이다. |
| 외부 single-cell 검증 | E-MTAB 16명 + 외부 9명 통합 CSV/plot 작성 | 외부 Rejection 환자는 대체로 높은 p60 확률을 보였고, GSE195719 2-class에서는 AUROC 1.000이다. |
| Common-gene 재학습 | 외부 5개 파일별 train/test 공통 gene으로 Run2 완료 | train-only gene 의존이 큰 dataset에서는 Rejection 확률이 +0.06~0.10 올라갔다. |
| Microarray 데이터 기반 확장 | kidney microarray 24개 RMA, 22개 minmax h5ad, 19개 NR/Rejection training h5ad 생성 | 총 2,179 샘플(NR 1,209 / Rejection 970)로 multi-dataset 학습 가능 상태다. |
| Multi-dataset finetune | `prognosis_microarray_adapter_multidataset.py` 작성, 실행 전 | GSE 단위 Leave-One-Dataset-Out CV로 플랫폼/배치 누설을 줄이는 설계다. |
| scRNA-seq -> microarray zero-shot | 5월 말 v2~v18 전수 탐색 완료 | label-free sc -> array 전사는 AUROC 0.748 근처에서 포화된다. array label 또는 biology prior가 필요하다. |

## 모델 계열별 판정

### 1. 현재 권장 모델: microarray-to-scRNA prognosis adapter

기본 구조는 다음과 같다.

```text
bulk microarray RMA/log2 sample
  -> nonzero gene tokenization
  -> per-sample quantile binning
  -> frozen scGPT pretrain_kidney encoder
  -> CLS embedding
  -> residual Microarray-to-SC adapter
  -> L2 normalization
  -> binary prognosis/rejection head
  -> single-cell에서는 cell probability의 p60 patient score
```

중요한 해석상 주의점은 Cox branch다. 코드에는 Cox risk output이 있지만, 현재 핵심 실험은 BCE 기반 NR vs Rejection objective가 중심이다. 따라서 현 단계의 score는 time-to-event survival score라기보다 rejection/prognosis risk proxy로 해석하는 편이 안전하다.

### 2. Backbone 비교: kidney-specific pretraining이 결정적

동일한 `adapter_8000` 설정에서 `models/pretrain_kidney`와 `models/pretrain_human`만 바꿔 비교했다.

| 지표 | Kidney backbone | Human backbone |
| --- | ---: | ---: |
| 5-fold OOF AUROC | 0.776 | 0.799 |
| E-MTAB predict-cell p60 AUROC | 0.875 | 0.500 |
| Rejection recall | 4/4 | 1/4 |

Human backbone은 microarray OOF에서는 더 좋아 보였지만 single-cell 전이에서는 붕괴했다. 이 결과는 in-domain fit과 cross-domain transfer가 별개의 문제이며, 신장 특화 pretraining이 실제 전이에 더 중요하다는 판단을 강화한다.

### 3. Negative control과 dropout 검증

무관한 대장암 microarray GSE39582에 랜덤 NR/Rejection 라벨을 붙인 음성 대조에서는 OOF AUROC 0.515, E-MTAB predict-cell AUROC 0.458로 우연 수준에 머물렀다. 기존 `adapter_8000`의 OOF 0.776, patient AUROC 0.875와 대비되므로 pipeline artifact나 단순 누수 가능성을 낮추는 대조가 성립한다.

MC-dropout sweep에서는 dropout 0.00~0.30에서 patient ranking과 AUROC가 거의 유지되고, uncertainty만 선형적으로 증가했다. 즉 현재 p60 patient score는 dropout perturbation에는 비교적 robust하다.

## Single-cell predict-cell 최신 결과

### Run1: 기존 adapter 그대로 적용

기존 `prognosis_adapter_8000/run_20260528-022429` checkpoint를 재학습 없이 적용했다.

| Dataset | 환자 구성 | Run1 결과 |
| --- | --- | --- |
| E-MTAB-12051 | 16명, NR 12 / Rejection 4 | AUROC 0.875, BalAcc 0.875, Rejection 4/4 검출 |
| GSE195719 | 3명, NR 1 / Rejection 2 | AUROC 1.000, NR이 최저 p60 score |
| GSE109564 | Rejection 1명 | p60 0.676 |
| GSE145927 | Rejection 3명 | p60 0.528 / 0.548 / 0.588 |
| GSE151671 AK1/AK2 | Rejection 2명 | p60 0.717 / 0.638 |

2026-06-16에는 E-MTAB과 외부 4개 series를 합쳐 25환자 통합 CSV와 Run1-only bar plot을 만들었다. 통합 그림에서는 외부 Rejection 환자들이 상위권을 차지했고, E-MTAB 환자는 0.47~0.54의 좁은 범위에서 Rejection/NR이 섞였다.

### Run2: test dataset별 common-gene 재학습

각 외부 scRNA-seq 파일과 training data가 공유하는 gene만 남겨 처음부터 재학습했다.

| Dataset | Run1 -> Run2 변화 | 해석 |
| --- | --- | --- |
| GSE145927 | +0.06~0.07 | common-gene 재학습 이득이 뚜렷하다. |
| GSE109564 | +0.001 | 이미 공통 gene 비율이 높아 변화가 거의 없다. |
| GSE151671 AK1 | +0.062 | train-only gene 의존 제거 효과로 보인다. |
| GSE151671 AK2 | +0.097 | 가장 큰 상승폭이다. |
| GSE195719 | +0.01~0.02 | 순위와 AUROC 1.000을 유지했다. |

Run2의 bulk OOF는 대체로 0.755~0.780으로 Run1 0.776과 비슷하거나 소폭 낮다. 즉 in-domain OOF를 약간 포기하더라도 cross-domain single-cell 적용에서는 더 나을 수 있다는 trade-off가 보인다.

## Microarray 데이터 확장

### GEO 정리와 RMA 전처리

`data/kidney/`의 31개 GEO series를 `scRNA-seq`, `bulk_RNA-seq`, `microarray`로 재분류했다. 이후 microarray 24개 series를 플랫폼에 맞게 전처리했다.

| 플랫폼 | 처리 방식 | 결과 |
| --- | --- | --- |
| Affy 3' IVT 17개 | `affy::rma` | RMA gene matrix 생성 |
| Affy Gene/Exon ST 5개 | `oligo::rma(target="core")` | RMA gene matrix 생성 |
| Illumina HT-12 V4 2개 | `log2 + quantile normalization` | RMA 대신 normalized matrix 생성 |

최종적으로 24/24 series 전처리에 성공했고 총 4,578 샘플을 확인했다. 이후 Illumina를 제외한 22개 Affymetrix series에는 기존 학습데이터 방식과 맞춘 `RMA < 5 -> 0` 및 per-sample min-max 변환을 적용해 h5ad를 만들었다.

### NR/Rejection 라벨링

시리즈별 원본 diagnosis를 수동 큐레이션해 파생 h5ad 19개를 만들었다. 원본 라벨은 `diagnosis_raw`에 보존하고, 통합 binary label은 `diagnosis = NR/Rejection`으로 저장했다.

| 항목 | 값 |
| --- | ---: |
| 원본 Affymetrix minmax series | 22개 |
| 최종 training_labeled h5ad | 19개 |
| 총 사용 샘플 | 2,179 |
| NR | 1,209 |
| Rejection | 970 |
| 미사용 series | GSE50058, GSE93659, GSE9493 |
| Illumina 별도 제외 | GSE181757, GSE69677 |

단일 클래스 dataset도 3개 있다: GSE106675, GSE21374, GSE48581. 이들은 validation fold로는 쓸 수 없지만 train에는 넣어 Rejection signal을 보강할 수 있다.

## Multi-dataset 학습 준비

`prognosis_microarray_adapter_multidataset.py`는 기존 adapter script를 보존한 채 복사/수정한 새 실험용 스크립트다.

핵심 설계:

- `merge`: 19개 h5ad를 union gene set으로 outer-join하고, 없는 gene은 0으로 채운다.
- `dataset`: 파일명에서 GSE를 파싱해 group column으로 저장한다.
- `finetune --cv logo`: two-class GSE를 하나씩 validation으로 빼는 Leave-One-Dataset-Out CV를 기본값으로 둔다.
- 단일 클래스 GSE는 validation에서 제외하고 항상 train에 고정한다.
- pooled OOF뿐 아니라 per-dataset AUROC와 single-class dataset 목록을 `cv_metrics.json`에 기록한다.

아직 실행하지 않은 다음 명령이 다음 단계다.

```bash
python3 scripts/prognosis_microarray_adapter_multidataset.py merge \
  --input-dir rma_out/training_labeled --pattern '*.h5ad' \
  --label-col diagnosis --group-col dataset \
  --output rma_out/training_labeled_merged.h5ad

python3 scripts/prognosis_microarray_adapter_multidataset.py finetune \
  --adata rma_out/training_labeled_merged.h5ad \
  --model-dir models/pretrain_kidney \
  --label-col diagnosis --positive-label Rejection \
  --group-col dataset --cv logo \
  --output-base results/prognosis_adapter_multidataset
```

주의: 이 데이터는 RMA log2/minmax 계열이므로 `--normalize`를 쓰지 않는다. scGPT tokenization의 per-sample quantile binning이 platform scale 차이를 흡수하는 설계다.

## 실패에서 남은 결론

scRNA-seq에서 microarray로 직접 전사하는 방향은 매우 많이 탐색했다. Frozen embedding, encoder fine-tuning, domain adaptation, self-training, UDA, gene-embedding projection, signature prior까지 비교한 결과, label-free sc -> array 전이는 AUROC 0.748 근처에서 포화된다는 결론이다.

핵심 이유는 sc source에서 학습한 rejection 축과 array target에서 최적인 rejection 축이 잘 맞지 않기 때문이다. 반대로 array label을 쓰면 AUROC 0.840 수준까지 가능하므로, target signal 자체가 없는 것은 아니다. 0.80 이상이 필요하면 array label supervision 또는 scGPT-weighted rejection signature 같은 biology prior가 필요하다.

## 다음 우선순위

1. 19개 labeled microarray h5ad를 merge하고 LOGO finetune을 실행한다.
2. per-dataset AUROC를 보고 어떤 cohort가 일반화 병목인지 확인한다.
3. multi-dataset checkpoint를 E-MTAB 및 외부 scRNA-seq predict-cell에 다시 적용해 `adapter_8000` 대비 개선 여부를 본다.
4. p60 score뿐 아니라 calibration, dataset별 threshold stability, false positive 환자 특성을 함께 점검한다.
5. survival/time-to-event endpoint가 충분해지면 Cox branch를 실제 loss에 연결할지 별도 실험으로 분리한다.

## 관련 문서

- [Microarray-to-scRNA Prognosis Adapter](microarray-to-scrna-prognosis-adapter.md)
- [scGPT Worklog Summary](scgpt-worklog-summary.md)
- [Transplant Prognosis Model Notes](transplant-prognosis-model-notes.md)
- [Kidney Transplant Rejection Classification](kidney-transplant-rejection-classification-summary.md)
- [2026-06-16 scGPT prognosis worklog](../code/logs/2026-06-16-scgpt-prognosis-worklog.md)
- [2026-06-16 sessions log](../code/logs/2026-06-16-sessions-log.md)
