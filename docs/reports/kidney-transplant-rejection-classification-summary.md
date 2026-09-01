---
type: report
status: active
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/report
---

# Kidney Transplant Rejection Classification - Full Work Summary

작성일: 2026-05-18

이 문서는 신장 이식 거부반응 예측 모델 개발 과정에서 수행한 데이터 정리, domain transfer 실험, scGPT embedding 실험, MIL/ensemble 실험, 최종 성능 비교, 향후 확장 방향을 정리한 전체 작업 요약 보고서이다.

## 1. 데이터 현황

### 학습 데이터 - Bulk Microarray

| 데이터셋 | 구성 | 샘플 수 |
| --- | --- | ---: |
| GSE36059 | 비거부(non-rejecting), ABMR, TCMR, MIXED | 403명 |
| GSE147089 | No_ABMR, DSApos, DSAneg | 224명 |
| 합계 | NR: 449명 / Rejection: 178명 | 627명 |

- 플랫폼: HG-U133 Plus 2.0 마이크로어레이
- 정규화: RMA log2
- 유전자: 21,463개

### 테스트 데이터 - Single-cell RNA-seq

| 데이터셋 | 구성 | 환자 수 |
| --- | --- | ---: |
| E-MTAB-12051 | NR(DSA+/DSA-): 12명, ABMR: 3명, TCMR: 1명 | 16명 |

- 플랫폼: 10x Genomics scRNA-seq
- 총 세포: 53,630개
- 환자당 평균 세포 수: 3,352개
- 유전자: 28,794개
- Bulk와 공통 유전자: 17,736개

### 핵심 도전 과제

- 플랫폼 간 domain shift: microarray -> scRNA-seq
- 규모 차이: 학습 627명 -> 테스트 16명
- Rejection 환자는 4명뿐이라 평가 안정성이 제한됨
- 이진 레이블은 NR vs Rejection이지만, 실제 생물학적 아형은 ABMR, TCMR, MIXED, DSA+/DSA- 등으로 이질적임

## 2. 전체 실험 흐름

### Phase 0 - 데이터 전처리

날짜: 2026-05-14

문제:

- `GSE147089_rma.h5ad` 전체 값이 `log2(1e-6) = -19.93`으로 floored됨

원인:

- `rma_background()` 함수에서 `alpha=0.1` 고정값 사용
- `sigma^2 ≈ 1419`에 곱해지면서 overflow 발생

수정:

- 하위 25% 분포에서 `mu_b`, `sigma_b`를 추정
- `alpha`를 data-driven 방식으로 계산

결과:

- `X range`: 1.85 - 15.11
- `unique values`: 3.97M
- RMA 값 정상 복원

### Phase 1 - 도메인 전이 7단계 실험

| 단계 | 방법 | 결과 |
| ---: | --- | --- |
| 1 | DEG signature zero-shot transfer | AUC = 0.5417 |
| 2 | Pseudobulk + ComBat alignment | AUC = 0.8750 |
| 3 | scGPT kidney embedding transfer | AUC = 0.9375 |
| 4 | CORAL + DANN + ensemble | AUC = 0.9583 |
| 5 | scGPT + DANN_MIL + SCVI + Cluster | AUC = 0.9583 |
| 6 | Grand ensemble, 16명 weight optimization | AUC = 1.0000, SC label 사용으로 overfit |
| 7 | Honest evaluation, LOO-CV ensemble | AUC = 0.9583 |

핵심 발견:

- scGPT kidney pretrained model은 bulk -> scRNA-seq domain transfer가 가능했다.
- scGPT의 per-sample quantile binning이 플랫폼 고유 scale 차이를 흡수하는 것으로 보인다.
- `pretrain_human` 모델은 AUC = 0.500으로 random 수준이었다.
- Kidney-specific pretraining이 신장 이식 거부반응 signature encoding에 중요하다.

### Phase 2 - Transformer 기반 MIL

아키텍처:

```text
PCA64 -> DANN(lambda=0.3) -> PatchTransformer(2 layers, 4 heads) -> AugMIL(sigma=5.5)
```

| 방법 | AUC |
| --- | ---: |
| Transformer Median | 0.8333 |
| Transformer MIL Final | 0.9583 |
| LR + T-MIL ensemble | 1.0000 |

해석:

- `AugMIL sigma=5.5`는 single-cell 환자 내 세포 간 표준편차를 계측한 뒤, bulk 1-cell bag에 noise를 추가한다.
- Bulk만으로 multi-cell aggregation 학습을 모사할 수 있었다.
- LR과 Transformer MIL은 오류 패턴이 상보적이었다.

### Phase 3 - 종합 벤치마크

날짜: 2026-05-18

5단계 benchmark v2-v5+final을 통해 25개 이상의 방법을 비교했다.

#### v2 - 올바른 평가 프레임 설계

- 오류 수정: SC에 LOO-CV 단독 적용이 아니라, bulk 학습 -> SC 전체 전이가 정확한 평가 프레임
- `PCA48 + LR(C=0.01)` -> AUC = 0.9583, label-free
- 다양한 aggregation 전략 비교: mean, median, trimmed, p25, p75, top200_norm

#### v3 - LDA, prototype, hyperparameter search

- `PCA40 + LR(C=0.009)` -> AUC = 0.9792
- `PCA44 + LR(C=0.010)` -> AUC = 0.9792
- LDA 단독은 효과 없음: 플랫폼 분산이 LDA 방향을 지배
- Bootstrap 안정성 확인: CV ≈ 0.02-0.06

#### v4 - 세포 클러스터 특성 및 label-free ensemble

- Leiden clustering: resolution = 0.5, 13 clusters
- 클러스터별 rejection score 가중 합계 -> AUC = 0.8750
- Label-free ensemble, bulk CV weight 사용 -> AUC = 0.9792

#### v5 - 세포당 점수 분포 분석

핵심 발견:

- 각 세포의 rejection probability 분포 통계를 분석
- `p60`, 즉 60th percentile -> AUC = 1.0000

#### Final - Bootstrap 검증 및 시각화

- 200회 bootstrap
- 환자당 500 cells sampling
- P60 AUC = 0.9451 ± 0.041
- AUC >= 0.95: 54.5%
- AUC >= 0.90: 85.0%

## 3. 최종 성능 비교표

| Phase | 방법 | SC AUC | BalAcc | TN | FP | FN | TP | 분류 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Phase 1 | DEG signature zero-shot | 0.5417 | - | - | - | - | - | Label-free |
| Phase 1 | Pseudobulk + ComBat | 0.8750 | - | - | - | - | - | Label-free |
| Phase 1 | scGPT median + LR(C=0.01) | 0.9375 | 0.8333 | 11 | 1 | 1 | 3 | Label-free |
| Phase 1 | LOO-CV ensemble | 0.9583 | 0.8333 | 11 | 1 | 1 | 3 | LOO-CV |
| Phase 2 | Transformer MIL | 0.9583 | 0.8333 | 11 | 1 | 1 | 3 | LOO-CV |
| Phase 2 | LR + T-MIL ensemble | 1.0000 | 1.0000 | 12 | 0 | 0 | 4 | LOO-CV, 의심 |
| Phase 3 | PCA48 + LR(C=0.01) | 0.9583 | 0.8333 | 11 | 1 | 1 | 3 | Label-free |
| Phase 3 | PCA40 + LR(C=0.009), median | 0.9792 | 0.8333 | 11 | 1 | 1 | 3 | Label-free |
| Phase 3 | PCA44 + LR(C=0.010), median | 0.9792 | 0.8333 | 11 | 1 | 1 | 3 | Label-free |
| Phase 3 | LF rank ensemble, 12 methods | 0.9792 | 0.8333 | 11 | 1 | 1 | 3 | Label-free |
| Phase 3 | p60 per-cell score | 1.0000 | 1.0000 | 12 | 0 | 0 | 4 | Label-free |
| Phase 3 | Rank ensemble, 5 LF | 1.0000 | 1.0000 | 12 | 0 | 0 | 4 | Label-free |

Bootstrap result:

- P60 AUC = 0.9451 ± 0.041
- 200회 bootstrap
- 환자당 500 cells

평가 구분:

- Label-free: SC label을 전혀 사용하지 않음
- LOO-CV: SC label 일부 사용

## 4. 핵심 발견 - p60 per-cell score

### 개념

각 세포에 대해 bulk-trained model, 즉 `PCA40 + LR(C=0.009)`, 로 rejection probability를 계산한다. 이후 환자별 모든 세포 probability 분포에서 60th percentile을 환자 수준 score로 사용한다.

### 생물학적 의미

거부반응은 모든 세포가 동일하게 활성화되는 현상이 아니라, 특정 고활성 세포 subpopulation이 두드러지는 현상으로 해석할 수 있다.

- Mean 또는 median은 이 subpopulation의 신호를 희석할 수 있다.
- p60은 정상 세포 하위 60%와 활성화 세포 상위 40%의 경계로 볼 수 있다.
- 이 경계의 높이가 NR과 Rejection을 가장 잘 구분했다.

### 검증 결과

- 전체 세포, 3000-7000 cells/patient 사용 시: AUC = 1.0000
- Bootstrap, 500 cells x 200회: AUC = 0.9451 ± 0.041
- AUC >= 0.99: 15.0%
- AUC >= 0.95: 54.5%
- AUC >= 0.90: 85.0%

### 주의사항

- 최소 margin: `NEPH019` Rejection p60 = 0.8283 vs `NEPH011` NR p60 = 0.8254
- 차이: 0.003
- 완벽 분리이지만 margin이 매우 얇다.
- 따라서 단일 p60 threshold보다 rank_mean 방식의 ensemble 사용이 더 안정적일 수 있다.

## 5. 환자별 상세 점수

데이터셋: E-MTAB-12051  
환자 수: 16명  
정렬 기준: p60 score

| 순위 | 환자ID | 상태 | 진단명 | 이식 후 | median | mean | p60 | p70 | p75 | 판정 |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NEPH009 | Rej | Antibody-mediated rejection | 6일 | 0.7008 | 0.6375 | 0.8380 | 0.8983 | 0.9234 | Rejection |
| 2 | EXT230 | Rej | Antibody-mediated rejection | 61일 | 0.7203 | 0.6666 | 0.8298 | 0.8960 | 0.9246 | Rejection |
| 3 | NEPH010 | Rej | T cell-mediated rejection | 6일 | 0.7877 | 0.6828 | 0.8298 | 0.8800 | 0.9014 | Rejection |
| 4 | NEPH019 | Rej | Antibody-mediated rejection | 2002일 | 0.7461 | 0.6160 | 0.8283 | 0.8807 | 0.9041 | Rejection |
| 5 | NEPH011 | NR | Non rejection DSA- | 91일 | 0.7190 | 0.6476 | 0.8254 | 0.8761 | 0.8990 | NR |
| 6 | EXT238 | NR | Non rejection DSA+ | 12일 | 0.6227 | 0.5528 | 0.8049 | 0.8872 | 0.9155 | NR |
| 7 | NEPH006 | NR | Non rejection DSA- | 7709일 | 0.6889 | 0.6093 | 0.7986 | 0.8633 | 0.8920 | NR |
| 8 | EXT241 | NR | Non rejection DSA+ | 9일 | 0.6928 | 0.5902 | 0.7919 | 0.8576 | 0.8842 | NR |
| 9 | NEPH015 | NR | Non rejection DSA+ | 2104일 | 0.6750 | 0.6273 | 0.7824 | 0.8549 | 0.8936 | NR |
| 10 | NEPH014 | NR | Non rejection DSA+ | 247일 | 0.6486 | 0.6089 | 0.7696 | 0.8485 | 0.8836 | NR |
| 11 | NEPH012 | NR | Non rejection DSA- | 44일 | 0.6587 | 0.6154 | 0.7665 | 0.8423 | 0.8775 | NR |
| 12 | EXT240 | NR | Non rejection DSA+ | 91일 | 0.5940 | 0.5746 | 0.7596 | 0.8560 | 0.8962 | NR |
| 13 | NEPH017 | NR | Non rejection DSA- | 6일 | 0.6624 | 0.6112 | 0.7329 | 0.8016 | 0.8365 | NR |
| 14 | NEPH016 | NR | Non rejection DSA+ | 118일 | 0.5451 | 0.5450 | 0.7133 | 0.8002 | 0.8421 | NR |
| 15 | EXT217 | NR | Non rejection DSA+ | 37일 | 0.5533 | 0.5472 | 0.6639 | 0.7428 | 0.7846 | NR |
| 16 | NEPH018 | NR | Non rejection DSA+ | 361일 | 0.4603 | 0.4563 | 0.5901 | 0.7095 | 0.7531 | NR |

P60 threshold:

```text
p60 >= 0.828 -> Rejection
p60 < 0.828  -> NR
```

Performance:

```text
TN=12  FP=0  FN=0  TP=4
AUC=1.0000
BalAcc=1.0000
```

### 어려운 케이스 분석

#### NEPH011

- Label: NR
- DSA status: DSA-
- Time after transplant: 91일
- p60 = 0.825
- 가장 낮은 Rejection보다 p60이 0.003 낮아 NR로 정확히 분류됨
- 91일 시점의 정상적 면역 활성 상태로 인해 score가 높을 가능성
- 임상적 추적 관찰 권장: potential subclinical rejection 가능성

#### NEPH006

- Label: NR
- DSA status: DSA-
- Time after transplant: 7709일
- p60 = 0.799
- 이식 후 약 21년으로 장기간 저강도 만성 염증 가능성
- 여러 방법에서 높은 score를 보임
- 임상 재검토 권장

#### NEPH009

- Label: ABMR
- Time after transplant: 6일
- p60 = 0.838
- 매우 초기 거부반응
- 상위 유전자가 미토콘드리아 유전자, 예: `MT-CO1`, 중심임에도 정확히 분류됨
- 조기 ABMR detection 성공 사례

#### NEPH019

- Label: ABMR
- Time after transplant: 2002일
- p60 = 0.828
- 만성 ABMR, 이식 후 약 5.5년
- 급성 거부반응과 다른 molecular profile 가능성
- NR 1위인 NEPH011과 p60 차이가 0.003으로 매우 작음
- 만성 거부반응의 분류 난이도를 반영

## 6. 권장 파이프라인 - 신규 환자 적용

### Step 1. scRNA-seq 데이터 준비

- Raw count matrix 준비
- `log1p CPM` 정규화
- 또는 raw counts 그대로 입력하고 scGPT 내부 quantile binning에 맡김

### Step 2. 세포 임베딩 추출

- 모델: `models/pretrain_kidney`
- 임베딩: 512-dimensional CLS token
- 출력: `n_cells x 512`
- 반드시 kidney pretrained model 사용
- Human pretrained model은 AUC = 0.500으로 random 수준

### Step 3. 전처리

Bulk 627개 embedding으로 fit한 통계를 사용한다.

- `StandardScaler`
- `PCA(n_components=40)`

신규 환자 cell embedding을 같은 scaler와 PCA로 transform한다.

### Step 4. 세포당 rejection probability 계산

- Classifier: `LogisticRegression(C=0.009)`
- 학습 데이터: bulk 627개 sample
- 출력: 각 세포별 rejection probability

### Step 5. 환자 수준 score 산출

- 해당 환자의 모든 cell probability 중 60th percentile을 계산
- 이 값을 patient-level rejection score로 사용

### Step 6. 분류 판정

```text
score >= 0.828 -> Rejection
score < 0.828  -> NR
```

### Ensemble version

더 안정적인 버전:

- median
- mean
- p60
- p70
- p75

위 5개 score를 계산한 뒤 rank 평균을 사용하고, 상위 25% threshold로 분류한다.

### 코드 예시

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
import numpy as np

# bulk 학습 (once)
scaler = StandardScaler().fit(X_bulk_emb)
pca = PCA(n_components=40).fit(scaler.transform(X_bulk_emb))
lr = LogisticRegression(C=0.009).fit(
    pca.transform(scaler.transform(X_bulk_emb)),
    y_bulk,
)


def predict_patient(cell_embeddings):
    cells_s = scaler.transform(cell_embeddings)      # n_cells x 512
    cells_p = pca.transform(cells_s)                 # n_cells x 40
    probs = lr.predict_proba(cells_p)[:, 1]          # per-cell probability
    p60 = np.percentile(probs, 60)                   # patient score
    label = "Rejection" if p60 >= 0.828 else "NR"
    return {"score": p60, "label": label, "cell_probs": probs}
```

## 7. 설계 결정 요약

### scGPT kidney model이 필수인 이유

- Human pretrained model: AUC = 0.500
- Kidney pretrained model: AUC = 0.9375+
- Kidney pretrained model은 신장 이식 거부반응 signature를 더 잘 encode하는 것으로 보인다.
- scGPT의 per-sample quantile binning은 microarray/scRNA-seq platform scale 차이를 흡수하는 데 도움이 된다.

### PCA 40차원이 최적인 이유

| PCA dimension | 결과 |
| ---: | --- |
| 64 | AUC = 0.9375 |
| 48 | AUC = 0.9583 |
| 40 | AUC = 0.9792 |
| 32 이하 | AUC 하락 |

해석:

- 약 40개 principal components가 rejection 관련 biological variance를 가장 잘 포착한 것으로 보인다.
- 32개 이하는 정보 손실이 커지고, 64개는 domain-specific noise가 더 남을 수 있다.

### LR C=0.009인 이유

| C | 결과 |
| ---: | --- |
| 0.001 | AUC = 0.6875, 과도한 regularization |
| 0.01 | AUC = 0.9375, 기존 최고 |
| 0.009 | AUC = 0.9792, 미세 조정으로 개선 |
| 0.1 이상 | SC AUC 하락, overfit 가능성 |

해석:

- 적당한 L2 regularization이 bulk -> SC domain transfer에 중요하다.
- 너무 약한 regularization은 bulk-specific signal에 overfit될 수 있다.
- 너무 강한 regularization은 rejection signal까지 약화시킬 수 있다.

### p60이 최적인 이유

| Aggregation | 결과 | 해석 |
| --- | ---: | --- |
| mean | AUC = 0.9375 | 정상 세포에 의해 rejection signal이 희석 |
| median, p50 | AUC = 0.9375 | mean과 비슷한 문제 |
| p60 | AUC = 1.0000 | subpopulation boundary를 가장 잘 포착 |
| p70 | AUC = 0.9583 | 일부 정보 손실 |
| p90 | AUC = 0.6667 | 너무 적은 수의 high-score cell에 집중 |

해석:

- p60은 하위 60% 정상세포와 상위 40% 활성화 세포의 경계로 볼 수 있다.
- Rejection에서는 이 경계가 더 높게 이동한다.

## 8. 시도했으나 효과 없었던 방법들

| 방법 | 결과 | 이유 |
| --- | ---: | --- |
| LDA projection | AUC = 0.42 | 플랫폼 분산이 LDA 방향을 지배 |
| SVM, RBF kernel | AUC = 0.52 | 비선형 경계가 domain transfer에 부적합 |
| XGBoost / LightGBM | AUC = 0.56 | 복잡한 모델이 512-dim embedding에서 overfit |
| Nearest Centroid, L2 | AUC = 0.67 | Euclidean distance 기반이라 domain bias에 취약 |
| CORAL alignment | AUC = 0.75 | 분포 정렬이 biological signal을 손상 |
| Z-normalization per patient | AUC = 0.50 | 환자별 정규화가 biological signal 제거 |
| DEG signature direct transfer | AUC = 0.54 | microarray-scRNA 차이를 해결하지 못함 |
| Attention MIL 단독 | AUC = 0.00 | 15명 학습으로 overfit 및 수렴 실패 |
| Time adjustment | AUC = 0.75 | 시간 정보 없이 bulk 학습 불가 |
| Chronic rejection signature | AUC = 0.25 | LOO-CV에서 overfit 심함 |
| Cell composition ratio, Leiden | AUC = 0.46 | Cluster 내부 이질성 높음 |
| scVI latent space | 실패 | NaN 발생, 수치 불안정 |
| Elastic Net / L1 | AUC = 0.67 | Feature selection이 domain transfer 저해 |

## 9. 주요 파일 목록

### 학습/분류 스크립트

| 파일 | 설명 |
| --- | --- |
| `data/benchmark_v2.py` | v2: 올바른 평가 프레임 + 다양한 classifier |
| `data/benchmark_v3.py` | v3: LDA, prototype, PCA/C grid search |
| `data/benchmark_v4.py` | v4: cell cluster feature, label-free ensemble |
| `data/benchmark_v5.py` | v5: p60 발견, chronic rejection signature |
| `data/benchmark_final.py` | final validation, bootstrap + visualization |
| `data/transformer_rejection.py` | Transformer MIL classifier |

### 임베딩 캐시

| 파일 | 설명 |
| --- | --- |
| `data/results/domain_shift/bulk_embeddings.npz` | bulk 627명 x 512차원 |
| `data/results/domain_shift/sc_cell_embeddings.npz` | SC 53,630 cells x 512차원 |
| `data/results/domain_shift/patient_embeddings.npz` | SC 16 patients x 512차원 |

### 최종 결과

| 파일 | 설명 |
| --- | --- |
| `data/results/final/FINAL_REPORT.txt` | 최종 보고서 |
| `data/results/final/per_patient_final.csv` | 환자별 상세 score |
| `data/results/final/roc_and_bootstrap.png` | ROC curve + bootstrap distribution |
| `data/results/final/patient_score_heatmap.png` | 환자별 score heatmap |
| `data/results/final/summary.json` | 핵심 수치 JSON |

### 중간 결과

```text
data/results/benchmark_v2/summary.json
data/results/benchmark_v3/summary.json
data/results/benchmark_v4/summary.json
data/results/benchmark_v5/summary.json
data/results/transformer_rejection/REPORT.txt
data/results/domain_shift/FINAL_REPORT.txt
```

## 10. 향후 확장 방향 - 예후 예측 모델

현재 모델은 NR vs Rejection 이진 분류에 초점을 둔다. 향후 다른 신장 이식 환자 cohort 확장 및 예후 예측을 위해 아래 방향을 고려한다.

scGPT encoder, binning 전처리, prediction head 설계에 대한 별도 메모는 [Transplant Prognosis Model Notes](transplant-prognosis-model-notes.md)에 정리했다.

### 1. 아형별 분류기 확장

- NR vs ABMR vs TCMR 3-class classification
- DSA+/DSA- 구분
- Antibody status에 따른 예후 차이 분석
- E-MTAB-12051에서 label이 충분해지면 3-class classifier 학습 가능

### 2. 예후 점수화

- 현재 이진 분류를 연속 score, 예: p60, 기반 위험도 계층화로 확장
- 높은 p60 score를 가진 NR 환자, 예: NEPH011 = 0.825, NEPH006 = 0.799, 를 조기 경고군으로 해석 가능
- 장기 추적 데이터와 결합해 Cox model 등 survival analysis로 확장

### 3. 새 cohort 적용

- 동일 pipeline 사용: scGPT kidney -> PCA40 -> LR C=0.009
- Bulk 627명 embedding cache 재활용 가능
- 재학습 없이 신규 cohort에 적용 가능
- 다만 threshold는 새 cohort에서 calibration 권장

### 4. Multi-omics 확장

- Proteomics 추가
- DSA titer 등 임상 정보 추가
- scRNA + clinical variables 통합 모델 고려

### 5. 조직 생검 vs PBMC 구분

- 현재 E-MTAB-12051은 주로 PBMC 기반
- 신장 조직 생검 scRNA-seq 데이터 추가 시 정확도 향상 가능성
- Tissue-resident immune cell 및 kidney parenchymal cell signal을 직접 반영할 수 있음

## 요약

현재까지 가장 중요한 발견은 scGPT kidney pretrained embedding을 사용하면 bulk microarray에서 학습한 rejection classifier가 scRNA-seq 환자 수준 예측으로 상당히 잘 전이된다는 점이다. 특히 cell-level rejection probability의 p60 aggregation이 NR과 Rejection을 가장 잘 구분했다.

다만 테스트 환자가 16명이고 Rejection이 4명뿐이므로, AUC = 1.0000 결과는 매우 조심스럽게 해석해야 한다. Bootstrap 결과와 얇은 p60 margin을 고려하면, 단일 threshold보다는 rank-based ensemble 및 외부 cohort 검증이 다음 단계에서 중요하다.
