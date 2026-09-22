---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# Incremental Predictive Value of Transcriptomic Features for Immunotherapy Response

## 기본 정보

- Citation key: `hanIncrementalPredictiveValue2026`
- Item type: preprint
- Authors: Grace Y. Han; Hansen Tai; Fusheng Wang
- DOI: 10.64898/2026.09.14.26363060
- URL: [medRxiv](https://www.medrxiv.org/content/10.64898/2026.09.14.26363060v1); [DOI](https://doi.org/10.64898/2026.09.14.26363060); [code](https://github.com/StonyBrookDB/urothelial-immunotherapy-transcriptomic-value)
- Source/date: medRxiv v1, posted 2026-09-21; not peer reviewed
- 주 카테고리: Cancer Transcriptomics / Clinical Prediction
- 교차 카테고리: Bulk RNA-seq

## 1. 한 줄 요약

Advanced urothelial carcinoma에서 knowledge-guided tumor-microenvironment gene set은 임상변수만 쓸 때 면역치료 반응 예측을 개선했지만, TMB·PD-L1을 포함하면 transcriptomics의 순증분 이득은 작아졌다.

## 2. 연구 질문

Transcriptomic feature가 이미 사용할 수 있는 임상·종양 biomarker를 넘어 면역치료 반응 예측에 실제 추가 가치를 주며, pathway 중심 표현이 fold마다 불안정한 gene-wise selection보다 나은가?

## 3. 데이터와 방법

Atezolizumab을 받은 IMvigor210의 advanced urothelial carcinoma 298명을 분석했다. Clinical-only, TMB·PD-L1을 더한 standard-biomarker, neoantigen burden·immune phenotype까지 더한 research-enriched baseline에 transcriptomic feature를 단계적으로 추가했다. Knowledge-guided TME gene set과 transcriptome-wide data-driven gene selection을 비교하고 GSE176307 87명에서 외부평가했다.

## 4. 핵심 결과

Knowledge-guided feature는 clinical-only 대비 AUPRC를 0.058 높였지만 standard biomarker 포함 뒤의 추가 이득은 0.011, research-enriched baseline 뒤에는 0.016이었다. Data-driven gene selection의 fold 간 평균 Jaccard는 0.227로 불안정했고 clinical-plus-biomarker 설정에서 knowledge-guided 표현보다 AUPRC가 0.150 낮았다. 외부 cohort에서도 추가 이득은 clinical-only 대비 0.128, clinical-plus-biomarker 대비 0.019로 같은 패턴이었다.

## 5. 한계

단일 암종이며 responder 수와 외부 cohort가 작다. 두 cohort가 공유하는 feature 범위도 제한적이고 bulk RNA-seq는 세포·공간 이질성을 평균화한다. Pathway 선택과 model tuning이 완전히 locked됐는지, calibration·decision utility와 prospective performance는 추가 검증이 필요하다. 현재 preprint다.

## 6. 재현 또는 활용 포인트

- Clinical-only → 표준 biomarker → transcriptomics 순서로 nested model의 순증분 성능을 보고한다.
- Feature selection과 tuning은 각 training fold 안에서만 수행한다.
- AUROC뿐 아니라 class imbalance에 민감한 AUPRC, calibration과 decision curve를 함께 본다.
- Gene-level feature stability와 pathway-level stability를 fold·external cohort에서 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 rejection/prognosis에서 transcriptome이 histology, DSA, creatinine, 임상변수 위에 실제 추가 가치를 주는지 평가하는 설계와 거의 같다. Molecular model 단독 성능보다 clinical baseline 위의 ΔAUPRC·calibration과 외부센터 재현성을 우선해야 한다.

## 8. 관련 키워드

- Cancer Transcriptomics / Clinical Prediction
- Bulk RNA-seq
- Immunotherapy response
- Incremental predictive value
- External validation

## 9. Bibliography

Han, Grace Y., Hansen Tai, and Fusheng Wang. “Incremental Predictive Value and Representation of Transcriptomic Features for Immunotherapy Response in Advanced Urothelial Carcinoma.” medRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.14.26363060](https://doi.org/10.64898/2026.09.14.26363060). Preprint; not peer reviewed.
