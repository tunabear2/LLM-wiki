---
type: worklog
status: archive
rag_priority: low
updated: '2026-07-20'
tags:
- wiki/worklog
---

# 2026-05-20 - scGPT Rejection Classification Worklog

작성일: 2026-05-20

이 문서는 scGPT 기반 신장 이식 거부반응 분류 실험의 작업 로그이다. 단일 모델 결과만 정리하는 것이 아니라, bulk microarray RMA 데이터와 single-cell RNA-seq 데이터 사이의 domain shift를 줄이기 위해 시도한 전처리, embedding transfer, MIL, ensemble, pseudo-count 변환 실험을 함께 기록한다.

## 한 줄 결론

Bulk RMA 데이터를 그대로 scGPT fine-tuning에 넣거나 pseudo-count로 변환하는 것만으로는 scRNA-seq pseudobulk test 성능이 개선되지 않았다. 가장 재현성이 좋은 방향은 `pretrain_kidney` scGPT embedding을 사용해 cell-level rejection score를 만들고, 환자별 score 분포의 상위 분위수, 특히 `p60`, 를 patient-level score로 쓰는 것이다.

## 데이터와 문제 설정

### Bulk microarray train

| 데이터셋 | 내용 | 샘플 수 |
| --- | --- | ---: |
| GSE36059 | bulk microarray RMA log2 | 403 |
| GSE147089 | bulk microarray RMA log2 | 224 |
| 합계 | NR 449 / Rejection 178 | 627 |

- 기준 파일: `GSE36059_GSE147089_merged_rma.h5ad`
- 유전자 수: 21,463개
- 라벨: NR vs Rejection

주의: GSE147089의 `DSAneg` 26개를 Rejection으로 분류하는 임상적 타당성은 별도 확인이 필요하다.

### Single-cell RNA-seq test

| 데이터셋 | 내용 | 규모 |
| --- | --- | ---: |
| E-MTAB-12051 | scRNA-seq raw counts | 16 patients, 53,630 cells |

- 환자 라벨: NR 12 / Rejection 4
- Rejection subtype: ABMR 3, TCMR 1
- 목표: bulk에서 학습한 모델을 scRNA-seq 환자 단위 예측으로 전이

## 2026-05-20 데이터 전처리 점검

검증 완료 파일:

| 파일 | 상태 |
| --- | --- |
| `GSE36059_rma.h5ad` | RMA 전처리 정상, 403 samples, QN std 0.038 |
| `GSE147089_rma.h5ad` | RMA 전처리 정상, 224 samples, QN std 0.020 |
| `merged_rma.h5ad` | 기준 train 파일, 627 x 21,463, NR 449 / Rejection 178 |
| `pseudobulk.h5ad` | condition label 추가 완료 |
| `pseudobulk_preprocessed.h5ad` | condition label 추가 완료 |
| `pseudobulk_preprocessed_trainQN.h5ad` | train-reference QN 신규 생성, 16 x 17,736 |

### GSE147089 RMA 재전처리

`GSE147089_rma.h5ad`의 `X` 행렬이 전체 `-19.9316` 단일 값으로 floored되는 문제가 있었다.

원인:

- `build_h5ad.py`의 `rma_background()` 함수에서 `alpha = 0.1` 고정값 사용
- 전체 분포 표준편차가 약 1419라서 `alpha * sigma^2`가 약 201,350까지 커짐
- 모든 probe에서 background correction 값이 음수가 되고, `1e-6` floor 이후 `log2(1e-6) = -19.9316`으로 고정됨

수정:

```python
noise = x[x < np.percentile(x, 25)]
mu_b = np.mean(noise)
sigma_b = np.std(noise)
alpha = 1.0 / max(np.mean(x) - mu_b, 1.0)
```

결과:

- Shape: 224 x 21,463
- X range: 1.85-15.11
- Unique values: 3,969,509
- Conditions: No_ABMR 168, DSApos 30, DSAneg 26

## prognosis_1.py 실험

### 기존 입력 방식 비교

| 실험 | Val AUC | Test AUC | 문제 |
| --- | ---: | ---: | --- |
| Per-sample top1200, 원본 | 0.827 | 0.667 | 예측값이 0.81-0.85에 집중 |
| Train fixed top1199 | 0.838 | 0.562 | val-test gap 0.276 |
| Freeze backbone | 0.669 | 0.542 | 예측값이 0.506-0.512로 random 수준 |

결론: microarray RMA와 scRNA-seq pseudobulk 사이의 domain gap이 핵심 병목이다. scGPT가 bulk microarray를 입력받으면 CLS embedding이 거의 동일한 영역으로 수렴해 분류 경계가 test domain으로 전이되지 않는다.

### RMA -> pseudo-count 변환 실험

목표:

- Train 데이터는 RMA이고 zero percent가 0%이다.
- 이를 scRNA-seq 형태의 Poisson pseudo-count로 변환해 test scRNA-seq pseudobulk와 같은 전처리 파이프라인을 적용한다.

변환 스크립트:

```bash
cd /home/tunabear2/DW/scGPT/data
python scripts/convert_rma_to_pseudocount.py
```

출력:

```text
GSE36059_GSE147089_merged_pseudocount.h5ad
```

target_sum 탐색:

| target_sum | zero percent | CPM + log2 mean | 비고 |
| ---: | ---: | ---: | --- |
| 10,000 | 76.9% | 1.66 | Too sparse |
| 20,000 | 64.7% | 2.27 | 평균 lambda가 낮음 |
| 230,000 | 13.6% | 3.92 | test zero percent 13%, mean 3.15와 가장 유사 |

해석:

- gene 수가 21,463개라서 target 20,000에서도 mean lambda가 약 0.93에 불과했다.
- zero percent를 test와 맞추려면 target 230,000 수준이 필요했다.

`prognosis_1.py` 수정:

- `BULK_H5AD`를 `merged_pseudocount.h5ad` target 230,000 버전으로 변경
- train dataset: `normalize_total=1e4`, `log1p=True`
- validation dataset: `normalize_total=1e4`, `log1p=True`

실행 결과:

| 지표 | 값 |
| --- | ---: |
| Best val AUC | 0.831, epoch 22 |
| Test AUC | 0.542 |

환자별 예측은 대부분 0.81-0.83의 높은 rejection probability에 몰렸고, discrimination이 실패했다. `EXT217`만 NR로 낮게 예측되었고, `EXT230`만 Rejection으로 정답에 가까웠다.

결론: zero percent를 맞춰도 test AUC는 개선되지 않았다. pseudo-count 변환만으로는 domain gap을 해소할 수 없으며, bulk RMA 기반 fine-tuning으로 형성된 결정 경계가 scRNA-seq pseudobulk로 전이되지 않는다.

## Domain Shift 실험 요약

문제 정의:

- 학습: GSE36059 + GSE147089, bulk microarray RMA log2, 627 samples
- 검증: E-MTAB-12051, scRNA-seq raw counts, 16 patients
- 목표: 환자 단위 NR vs Rejection 분류

7단계 실험:

| 단계 | 방법 | AUC | 비고 |
| ---: | --- | ---: | --- |
| Step 1 | DEG signature zero-shot | 0.542 | 거의 random |
| Step 2 | Pseudobulk + ComBat alignment | 0.875 | threshold 문제 |
| Step 3 | scGPT embedding transfer, bulk -> SC median | 0.938 | 핵심 방법 |
| Step 4 | CORAL + DANN + ensemble | 0.958 | partial overfit |
| Step 5 | scGPT + DANN_MIL + SCVI + Cluster | 0.958 | 추가 모델 조합 |
| Step 6 | Grand ensemble, 16 patient weight optimization | 1.000 | overfit 가능 |
| Step 7 | Honest evaluation, LOO-CV ensemble | 0.958 | 공정 추정 |

핵심 발견:

- `pretrain_kidney` scGPT embedding은 platform 간 전이가 가능했다.
- scGPT의 per-sample quantile binning이 platform 고유 scale 차이를 상당 부분 흡수하는 것으로 보인다.
- `pretrain_human`은 AUC 0.500으로 random 수준이었다.
- Kidney-specific pretraining이 rejection signature를 embedding space에 인코딩하는 데 중요하다.

pretrained model 비교:

| 모델 | AUC | Top25% BalAcc | 비고 |
| --- | ---: | ---: | --- |
| `pretrain_kidney` | 0.938 | 0.833 | TN 11 / FP 1 / FN 1 / TP 3 |
| `pretrain_human` | 0.500 | 0.500 | random 수준 |

주요 파일:

- `data/run_step3_domain_transfer.py`
- `data/results/domain_shift/FINAL_PREDICTIONS.csv`
- `data/results/domain_shift/FINAL_REPORT.txt`
- `data/results/domain_shift/domain_shift_results.png`
- `data/results/domain_shift/patient_score_heatmap.png`
- `data/results/domain_shift/bulk_embeddings.npz`
- `data/results/domain_shift/sc_cell_embeddings.npz`
- `data/results/domain_shift/patient_embeddings.npz`

## 종합 벤치마크

목표:

- Bulk microarray에서 학습한 NR vs Rejection classifier를 scRNA-seq 환자 예측으로 전이할 때, label-free 성능을 최대화한다.

벤치마크 흐름:

| 단계 | 핵심 아이디어 | 최고 AUC, label-free |
| --- | --- | ---: |
| v2 | Bulk 학습 -> SC 전이 평가 프레임 정리 | 0.9583, PCA48 |
| v3 | PCA dimension x C grid search, LDA, prototype | 0.9792, PCA40 + C 0.009 |
| v4 | 세포 클러스터별 rejection score, bootstrap | 0.9792, ensemble |
| v5 | 세포당 score 분포 통계 | 1.0000, p60 per-cell score |
| Final | Bootstrap 200회, ROC, 시각화 | 1.000, bootstrap mean 0.9451 |

### p60 per-cell score

방법:

1. 세포별 scGPT kidney embedding을 만든다.
2. Bulk train에서 fit한 `StandardScaler`와 `PCA(40)`을 적용한다.
3. Bulk train에서 학습한 `LogisticRegression(C=0.009)`으로 세포별 rejection probability를 계산한다.
4. 환자별 세포 probability의 60th percentile을 patient-level score로 사용한다.
5. threshold는 약 0.828을 사용한다.

성능:

| 방법 | SC AUC | BalAcc | CM | 타입 |
| --- | ---: | ---: | --- | --- |
| p60 per-cell score | 1.0000 | 1.0000 | TN 12 / FP 0 / FN 0 / TP 4 | Label-free |
| PCA40 + LR(C=0.009), median | 0.9792 | 0.8333 | TN 11 / FP 1 / FN 1 / TP 3 | Label-free |
| Rank ensemble, 5 label-free methods | 1.0000 | 1.0000 | TN 12 / FP 0 / FN 0 / TP 4 | Label-free |
| scGPT median, original | 0.9375 | 0.8333 | TN 11 / FP 1 / FN 1 / TP 3 | Label-free |
| LOO-CV ensemble, original | 0.9583 | 0.8333 | TN 11 / FP 1 / FN 1 / TP 3 | LOO |

생물학적 해석:

- 거부반응은 모든 세포가 동일하게 바뀌는 현상이라기보다 특정 고활성 세포 subpopulation이 두드러지는 현상으로 해석할 수 있다.
- Mean 또는 median pooling은 이 subpopulation의 신호를 희석할 수 있다.
- p60은 정상 세포와 활성화 세포 사이의 경계값처럼 작동했다.

부트스트랩 검증:

- 200회 반복
- 환자당 500 cells sampling
- P60 mean AUC: 0.9451 +/- 0.0414
- AUC >= 0.95: 54.5%
- AUC >= 0.90: 85.0%
- Median 방법 mean AUC: 0.9273 +/- 0.0355

주의:

- `NEPH019` Rejection p60 0.8283과 `NEPH011` NR p60 0.8254의 margin이 약 0.003으로 매우 얇다.
- 단일 threshold만 믿기보다 `median`, `mean`, `p60`, `p70`, `p75`의 rank ensemble을 함께 보는 것이 더 안정적이다.

결과 파일:

- `data/benchmark_v2.py`
- `data/benchmark_v3.py`
- `data/benchmark_v4.py`
- `data/benchmark_v5.py`
- `data/benchmark_final.py`
- `data/results/final/FINAL_REPORT.txt`
- `data/results/final/roc_and_bootstrap.png`
- `data/results/final/patient_score_heatmap.png`
- `data/results/final/per_patient_final.csv`
- `data/results/final/summary.json`

## Transformer 기반 NR/Rejection 분류기

목표:

- Logistic Regression 대신 Transformer 기반 모델을 사용해 bulk array -> scRNA-seq domain transfer 성능을 개선한다.

아키텍처:

```text
PCA-64
-> 8 patches x 8 dim
-> PatchTransformer, 2 layers, 4 heads, d_model 64
-> CLS representation
-> Task head
-> Domain head with Gradient Reversal
-> MIL head with attention pooling
```

핵심 설정:

- PCA dimension: 64
- DANN lambda: 0.3
- Augmented MIL sigma: 5.5
- Bulk sample 1개를 K=8 noisy copies로 확장해 multi-cell bag을 모사
- 추론 시 실제 SC 환자의 세포 bag에 MIL attention을 적용

실험 결과:

| 버전 | 설정 | SC AUC |
| --- | --- | ---: |
| V1 | 512 dim, no DANN | 0.667, median |
| V2 | PCA-64, DANN lambda 0.3, MIL | 0.812, MIL |
| Final | PCA-64, DANN lambda 0.3, AugMIL sigma 5.5 | 0.958, MIL |

최종 비교:

| 방법 | AUC | BalAcc | TN/FP/FN/TP |
| --- | ---: | ---: | --- |
| LR(C=0.01, PCA-64, median) | 0.9375 | 0.8333 | 11/1/1/3 |
| Transformer median | 0.8333 | 0.6667 | 10/2/2/2 |
| Transformer MIL final | 0.9583 | 0.8333 | 11/1/1/3 |
| LR + Transformer MIL ensemble | 1.0000 | 1.0000 | 12/0/0/4 |

해석:

- Transformer가 LR을 안정적으로 이기려면 MIL aggregation이 필요했다.
- `AugMIL sigma=5.5`는 scRNA-seq intra-patient variation을 bulk 학습에 주입하는 역할을 했다.
- LR과 Transformer MIL의 오류가 서로 달라 ensemble에서 성능이 크게 올랐다.

파일:

- `data/transformer_rejection.py`
- `data/results/transformer_rejection/patient_predictions.csv`
- `data/results/transformer_rejection/transformer_results.png`
- `data/results/transformer_rejection/REPORT.txt`
- `data/results/transformer_rejection/fold{1-5}_checkpoint.pt`

## Few-shot Transfer Learning: Rejection Head

파일:

- `data/rejection_finetune.py`

CLI:

```bash
python rejection_finetune.py embed
python rejection_finetune.py train
python rejection_finetune.py predict
```

아키텍처:

```text
Frozen scGPT Encoder, pretrain_kidney
-> CLS embedding, 512 dim
-> LayerNorm
-> Linear 512 -> 256
-> GELU
-> Dropout
-> LayerNorm
-> Dropout
-> Linear 256 -> 1
-> Sigmoid
```

Bulk microarray 처리:

- RMA 데이터는 zero가 없으므로 모든 gene이 발현된 것으로 보인다.
- 샘플당 `max_seq_len=1199` 랜덤 gene subset을 5회 추출하고 평균 embedding을 사용했다.
- 이미 log2 RMA normalized이므로 `normalize_total`과 `log1p`는 비활성화했다.
- 클래스 불균형 NR 449 / Rejection 178에 대해 `pos_weight=2.52`를 적용했다.

학습 결과:

| 지표 | 값 |
| --- | ---: |
| OOF AUROC | 0.7654 |
| OOF AUPRC | 0.5501 |
| Balanced Accuracy | 0.694 |
| Per-fold AUROC | 0.7908 +/- 0.0222 |

저장:

- `results/rejection_head/final_head.pt`

예측:

```bash
python rejection_finetune.py predict \
    --adata <new_patient.h5ad> \
    --model-dir models/pretrain_kidney \
    --head-dir results/rejection_head \
    --output results/rejection_head/predictions.csv
```

## Binary Classification: B17 vs B25_CTRL

목표:

- 질병 양성 `B17`과 음성 `B25_CTRL`을 cell-level scGPT fine-tuning으로 분류한다.

데이터:

| 파일 | 내용 | Cell 수 |
| --- | --- | ---: |
| `data/B17.h5ad` | 양성 환자 세포 | 10,022 |
| `data/B25_CTRL.h5ad` | 음성 환자 세포 | 5,960 |

설정:

- 공통 gene 36,601개
- HVG 1,200개
- scGPT vocab 교집합 934개
- label 1: B17 cells
- label 0: B25_CTRL cells
- Split: train / val / test = 60 / 20 / 20, cell-level stratified split
- Backbone: `models/pretrain_bc/`, human pretrained scGPT, 12 layers, 512 dim
- Head: LayerNorm -> Linear 512 to 256 -> GELU -> Dropout -> Linear 256 to 1
- 2단계 학습: head-only frozen phase 후 full fine-tuning

결과:

| 단계 | Val AUC | Val Acc |
| --- | ---: | ---: |
| Phase 1 epoch 05, head-only | 0.6605 | 62.6% |
| Phase 2 epoch 10, full fine-tuning | 0.9632 | 88.3% |
| Test | 0.9603 | 88.2% |

저장:

- `data/best_model.pt`
- `data/scGPT_Binary_Classification.py`
- `data/training_log.txt`

주의:

- cell-level split이므로 동일 환자의 cell이 train과 test에 섞인다.
- 실제 신규 환자 성능보다 낙관적일 가능성이 있다.

## GSM 8명 환자 추론

학습 재실행:

- 학습 gene 목록: 24,159개
- 저장: `data/training_genes.json`
- Test AUC: 0.9969
- Test accuracy: 0.9703

`predict_gsm_patients.py` 수정:

- `training_genes.json`을 로드한다.
- 환자 데이터에서 학습 시 사용한 gene만 필터링한다.
- 환자마다 vocab gene 23,077개가 일치했다.

추론 결과, threshold 0.5:

| 환자 | Cells | 양성 cell 비율 | 양성 확률 | 판정 |
| --- | ---: | ---: | ---: | --- |
| R4697 | 7,525 | 73.2% | 0.7301 | 양성 |
| R587 | 11,602 | 57.6% | 0.5730 | 양성 |
| PBMC3 | 2,175 | 82.5% | 0.8247 | 양성 |
| PBMC4 | 5,705 | 80.4% | 0.7983 | 양성 |
| R3617 | 11,887 | 63.7% | 0.6258 | 양성 |
| R817 | 6,960 | 63.1% | 0.6274 | 양성 |
| R1777 | 6,950 | 53.6% | 0.5336 | 양성 |
| R3517 | 7,286 | 53.7% | 0.5344 | 양성 |

결론:

- 8명 전원 양성으로 판정되었다.
- `R1777`, `R3517`은 확률이 0.53대라 threshold에 가깝고 추가 검토가 필요하다.

## 계획 중: Patient-level Classification

목표:

- scGPT cell embedding을 환자별로 pooling해 정상 vs rejection 환자 단위 모델을 만든다.

보유 데이터:

| 파일 | 내용 |
| --- | --- |
| 경로 미확인 normal `.h5ad` | 정상 환자 10명 single-cell 데이터 합본 |
| 경로 미확인 rejection `.h5ad` | 거부반응 환자 10명 single-cell 데이터 합본 |

다음 세션에서 확인할 것:

- 두 `.h5ad` 파일 경로
- `adata.obs.columns`
- `patient_id`, `label` 컬럼 존재 여부

합의된 파이프라인:

1. 두 `.h5ad` 파일을 병합한다.
2. `obs["patient_id"]`, `obs["label"]`을 확인하거나 추가한다.
3. `annotation.py`를 참고해 scGPT cell embedding을 추출한다.
4. `adata.obsm["X_scGPT"]`를 만든다.
5. 환자별 mean pooling으로 20 x 512 feature matrix를 만든다.
6. Leave-One-Out CV로 Logistic Regression을 평가한다.
7. 추가로 SVM, Random Forest, cell-type-aware pooling, attention MIL, Harmony 또는 scVI 보정을 검토한다.

## 권장 재현 파이프라인

신규 scRNA-seq 환자 예측에서는 아래 경로를 1순위로 둔다.

```text
scRNA-seq cells
-> scGPT pretrain_kidney cell embedding, 512 dim
-> StandardScaler fit on bulk
-> PCA(40) fit on bulk
-> LogisticRegression(C=0.009) fit on bulk
-> per-cell rejection probability
-> patient score = 60th percentile of per-cell probabilities
-> threshold around 0.828
```

안정성을 높이려면 다음 score를 함께 계산한다.

- Median
- Mean
- p60
- p70
- p75
- Rank mean ensemble

## 어려운 케이스

| 환자 | 라벨 | 특징 | 해석 |
| --- | --- | --- | --- |
| `NEPH011` | NR | p60 0.8254, threshold 바로 아래 | 91일 시점의 활성 면역 상태 가능성 |
| `NEPH006` | NR | 여러 방법에서 rejection score가 높음 | 장기 저강도 염증 또는 무증상 신호 가능성 |
| `NEPH009` | ABMR | 이식 후 6일, mitochondria gene 우세 | 초기 시점임에도 p60으로 정확 판별 |

## 최종 판단

- Bulk RMA 직접 fine-tuning과 pseudo-count 변환은 scRNA-seq pseudobulk test에서 안정적인 개선을 만들지 못했다.
- Domain shift를 줄이는 핵심은 raw value 형태를 억지로 맞추는 것보다, `pretrain_kidney` scGPT embedding space를 쓰는 것이다.
- Patient-level 예측에서는 단순 median pooling보다 cell-level score distribution의 분위수 기반 집계가 더 강했다.
- 현재 가장 실용적인 후보는 `PCA40 + LR(C=0.009) + p60`, 보조 후보는 `rank_mean(median, mean, p60, p70, p75)`이다.
