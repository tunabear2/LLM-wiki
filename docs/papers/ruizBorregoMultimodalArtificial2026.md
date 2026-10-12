---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# Multimodal AI Predicts Response and Prognosis in HER2-Positive Early Breast Cancer

## 기본 정보

- Citation key: `ruizBorregoMultimodalArtificial2026`
- Item type: preprint
- Authors: Manuel Ruiz Borrego; Javier Cortés; Arianna Stradella; Begoña Bermejo; et al.
- Source: medRxiv v1, posted 2026-10-07 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.05.26364736](https://doi.org/10.64898/2026.10.05.26364736); PHERGain [NCT03161353](https://clinicaltrials.gov/study/NCT03161353); PHERGain-2 [NCT04733118](https://clinicaltrials.gov/study/NCT04733118)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

Ataraxis Breast는 H&E whole-slide image와 임상변수를 결합해 두 phase II trial에서 HER2-positive 조기 유방암의 병리학적 완전반응을, 한 trial에서 장기 outcome을 예측했다.

## 2. 연구 질문

Chemotherapy de-escalation 상황에서 routine H&E 기반 AI score가 dual HER2 blockade의 반응과 재발 위험을 사전에 구분할 수 있는가?

## 3. 데이터와 방법

NEO model을 PHERGain 306명과 PHERGain-2 383명의 pCR에 평가하고, RISK model을 PHERGain 309명의 prognosis에 평가했다. 사전 지정 cutoff로 반응 가능성을 세 군, 재발 위험을 두 군으로 분류했다. Logistic regression, Cox model, Kaplan–Meier와 Harrell C-index를 사용했다. 이 모델은 H&E와 임상변수 기반이며 transcriptome input은 사용하지 않았다.

## 4. 핵심 결과

- NEO score 1-SD 증가당 pCR odds ratio는 PHERGain 1.28, PHERGain-2 1.30이었다.
- 사전 지정 군의 pCR은 각각 19.2%→48.3%, 29.5%→70.1%로 증가했다.
- PHERGain에서 RISK score의 event-free survival HR은 1-SD당 1.56, C-index는 0.66이었다. 5년 EFS는 low-risk 93.9%, high-risk 83.1%였다.

## 5. 한계

Biomarker 분석은 전향적으로 수집된 phase II trial 자료를 썼지만 후향적이었다. NEO discrimination은 중간 수준이고 prognosis는 PHERGain 한 cohort와 적은 event에 제한됐다. Raw data는 공개되지 않고 통제 접근이며 모델을 단독 의사결정 도구로 쓰기에는 추가 검증이 필요하다.

## 6. 재현 또는 활용 포인트

사전 고정 cutoff, trial별 독립 평가, pCR과 time-to-event endpoint 분리를 참고한다. Calibration, decision curve, clinical-only baseline 위의 순증분 가치와 center-held-out 성능이 추가로 필요하다.

## 7. Transcriptomics·신장이식 연구와의 연결

이식 biopsy H&E와 분자·임상변수를 결합할 때 모델을 고정한 뒤 별도 cohort에서 반응·예후를 검증하는 설계가 직접 참고된다. 다만 이 논문 자체에는 transcriptomics나 신장이식 자료가 없다.

## 8. 관련 키워드

- multimodal clinical prediction
- pathological complete response
- prognosis
- HER2-positive breast cancer

## 9. Bibliography

Ruiz Borrego, Manuel, et al. “Multimodal Artificial Intelligence Predicts Pathological Response and Prognosis in HER2-Positive Early Breast Cancer Treated with Chemotherapy De-escalation Strategies.” medRxiv, 2026. [https://doi.org/10.64898/2026.10.05.26364736](https://doi.org/10.64898/2026.10.05.26364736).
