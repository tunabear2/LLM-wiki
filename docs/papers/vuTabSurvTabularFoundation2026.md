---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# TabSurv: Tabular Foundation Model for Breast Cancer Prognosis Using Gene Expression Data

## 기본 정보

- Citation key: `vuTabSurvTabularFoundation2026`
- Item type: journal article
- Authors: Tuyen Vu; Ha Xuan Tran; Xiaomei Li; Sindy Pinero; Lin Liu; Jiuyong Li; Jia Tina Du; Thuc Duy Le
- Source: Computer Methods and Programs in Biomedicine, online 2026-10-28
- Original: [DOI: 10.1016/j.cmpb.2026.109693](https://doi.org/10.1016/j.cmpb.2026.109693); [PMID: 42962386](https://pubmed.ncbi.nlm.nih.gov/42962386/)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

TabSurv는 TabPFN의 in-context learning에 censoring-aware survival-time imputation을 결합해 12개 breast-cancer expression cohort에서 재학습 없이 비교적 안정적인 OOD 예후 예측을 수행했다.

## 2. 연구 질문

Right-censored time-to-event data를 tabular foundation model에 맞게 표현해 cohort heterogeneity와 distribution shift에 강한 gene-expression survival model을 만들 수 있는가?

## 3. 데이터와 방법

Event가 관찰된 환자로부터 censored 환자의 censoring time 이후 plausible survival time을 여러 번 생성하고, 각 imputed dataset을 TabPFN context로 사용한 예측을 결합했다. Gradient training이나 task-specific hyperparameter tuning 없이 작동한다. 12개 breast-cancer gene-expression cohort에서 in-distribution과 OOD setting으로 8개 survival model과 비교했다. METABRIC에서는 random-survival-forest risk를 context로 한 hypothetical treatment reassignment를 탐색했다.

## 4. 핵심 결과

- 8개 기존 survival model과 경쟁하거나 더 높은 예후 성능을 보였다.
- Cohort heterogeneity 아래 predictive stability가 가장 높았다.
- 탐색적 METABRIC 분석에서는 TabSurv 권고와 실제 치료가 일치한 환자군의 restricted mean survival time 차이가 비교 방법 중 가장 컸다.

## 5. 한계

Treatment recommendation은 observational data의 exploratory counterfactual 비교이며 prospective treatment assignment가 아니다. Censoring imputation 가정에 민감하고 검증은 breast cancer cohort에 한정된다.

## 6. 재현 또는 활용 포인트

Patient/cohort 단위 split, censoring distribution, imputation 수와 uncertainty aggregation을 고정한다. OOD cohort별 C-index뿐 아니라 calibration, decision curve와 clinical covariate-only baseline을 함께 평가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

다기관 biopsy expression으로 graft failure·rejection-free survival을 예측할 때 cohort-held-out 평가와 censoring 처리를 설계하는 직접적인 참고다. 치료 권고 모듈은 이식 면역억제제 데이터에서 별도 causal validation이 필요하다.

## 8. 관련 키워드

- Cancer Transcriptomics / Clinical Prediction
- Bulk RNA-seq
- survival analysis
- tabular foundation model

## 9. Bibliography

Vu, Tuyen, et al. “TabSurv: Tabular Foundation Model for Breast Cancer Prognosis Using Gene Expression Data.” _Computer Methods and Programs in Biomedicine_ 288 (2026): 109693. [https://doi.org/10.1016/j.cmpb.2026.109693](https://doi.org/10.1016/j.cmpb.2026.109693).
