---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# Multimodal Machine Learning Prognosis in the MONALEESA Trials

## 기본 정보

- Citation key: `wangMultimodalMachineLearning2026`
- Item type: medRxiv preprint
- Authors: Craig Wang; Rahul Paul; Yutong Li; Sean Smith; Qian Cao; et al.
- Source: medRxiv v1, posted 2026-10-13 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.09.26364892](https://doi.org/10.64898/2026.10.09.26364892)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

세 phase III MONALEESA trial의 임상변수, archival-tumor gene expression과 plasma ctDNA를 결합한 late-fusion model이 metastatic HR+/HER2− breast cancer의 PFS risk를 held-out 환자에서 구분했다.

## 2. 연구 질문

임상변수만이 아니라 baseline transcriptome과 ctDNA를 결합하면 CDK4/6 inhibitor trial 환자의 진행 위험 예측이 개선되는가?

## 3. 데이터와 방법

MONALEESA-2, -3, -7의 자료를 training, development evaluation(n=242), 최종 held-out test(n=382)로 stratified split했다. Modality별 sample 수는 달랐고 재학습에는 최대 1,355명이 쓰였다. Elastic net, survival random forest와 MLP를 비교하고, complete-case early fusion(n=336)과 modality별 prediction을 Weibull regression으로 합치는 late fusion을 평가했다.

## 4. 핵심 결과

- Test C-index는 late fusion 0.727(95% CI 0.641–0.799), early fusion 0.718(0.631–0.791)이었다.
- Median risk split의 low- 대 high-risk PFS hazard ratio는 0.28(0.20–0.38)이었다.
- 상위 40개 feature에는 18개 임상변수, 20개 expression feature, 2개 ctDNA feature가 포함됐다.

## 5. 한계

Treatment arm을 feature로 넣어 순수 prognostic effect와 treatment-predictive effect가 섞일 수 있다. 같은 trial pool 내부의 held-out test이며 독립 trial/real-world external validation은 없다. Trial 선정 기준 때문에 일상 진료 population으로 일반화가 제한되고, conflict disclosure는 최종 출판 때 추가 예정이라고만 명시됐다.

## 6. 재현 또는 활용 포인트

Feature selection과 tuning을 training/development 안에서 끝내고 test를 한 번만 여는 구조, missing modality 때문에 early와 late fusion의 유효 sample size가 달라지는 점을 기록한다. Code와 환자 수준 data 공개 정보는 원문에서 확인되지 않았다.

## 7. Transcriptomics·신장이식 연구와의 연결

Biopsy expression, donor-derived cell-free DNA와 임상변수를 graft survival에 결합할 때 late fusion과 locked test 설계를 참고할 수 있다. 치료군을 포함한 risk score는 예후와 치료효과 수정 여부를 별도로 검정해야 한다.

## 8. 관련 키워드

- Cancer Transcriptomics / Clinical Prediction
- multimodal survival model
- ctDNA
- gene expression

## 9. Bibliography

Wang, Craig, et al. “Multimodal Machine Learning-Based Clinical and Genomic Prognostic Factors for Progression-Free Survival in Metastatic Breast Cancer Using Phase III MONALEESA Trials.” medRxiv, 2026. [https://doi.org/10.64898/2026.10.09.26364892](https://doi.org/10.64898/2026.10.09.26364892).
