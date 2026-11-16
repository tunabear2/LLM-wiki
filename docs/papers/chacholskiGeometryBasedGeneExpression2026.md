---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# Geometry-based gene-expression signatures detect cancer treatment responders

## 기본 정보

- Citation key: `chacholskiGeometryBasedGeneExpression2026`
- Item type: journal article
- Authors: Wojciech Chachólski; Ryan Ramanujam
- Source: _BMC Cancer_ 26(1), published 2026-11-10
- Original: [DOI 10.1186/s12885-026-17312-4](https://doi.org/10.1186/s12885-026-17312-4)
- PubMed: [PMID 43009859](https://pubmed.ncbi.nlm.nih.gov/43009859/)
- Full text: [PMC13749694](https://pmc.ncbi.nlm.nih.gov/articles/PMC13749694/)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

신세포암 Phase III trial의 tumor expression geometry로 avelumab+axitinib 치료효과 이질성을 포착하고 leave-one-out 방식으로 responder 분류를 예측했다.

## 2. 연구 질문

개별 유전자 signature 대신 발현 데이터의 기하학적 구조를 사용하면 면역항암·표적치료 병용의 responder를 분류하고 out-of-sample 예측할 수 있는가?

## 3. 데이터와 방법

JAVELIN Renal 101의 advanced renal-cell carcinoma 726명 tumor gene-expression 자료로 여러 geometry 기반 signature와 synthetic response subgroup을 구성했다. 각 환자를 제외한 나머지로 response scaffold를 만든 leave-one-out 평가를 수행하고, 세 기존 gene-expression signature 및 penalized regression과 비교했다.

## 4. 핵심 결과

- Median split responder label 예측 accuracy 82.9%, AUC 0.880(95% CI 0.855–0.905)을 보고했다.
- 두~다섯 co-expression module의 out-of-fold AUC는 0.74–0.76으로 전체 22,955 gene penalized regression의 0.73보다 높았다.
- 14개월 adjusted RMST의 treatment interaction은 +2.10개월(p=0.004)이었고, permutation 기반 continuous interaction은 family-wise adjusted p=0.042였다.

## 5. 한계

한 trial cohort 내부의 leave-one-out 평가이며 독립 외부 trial 검증이 아니다. 내부에서 만든 responder classification과 실제 임상 endpoint를 구분해야 하고, cutpoint·geometry 선택의 이동 가능성도 외부 cohort에서 확인해야 한다.

## 6. 재현 또는 활용 포인트

Treatment arm, endpoint, censoring, geometry와 cutpoint 선택을 training fold 안에서만 결정한다. Leave-one-out뿐 아니라 trial·기관 외부검증, clinical-covariate baseline, calibration, decision-curve analysis를 추가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Renal tissue expression의 co-expression geometry로 치료효과 이질성을 찾는 사례라 신장이식 rejection treatment-response 모델과 가깝다. 다만 allograft에서는 therapy selection bias와 반복 biopsy를 고려한 patient-level external validation이 필요하다.

## 8. 관련 키워드

- renal cell carcinoma
- gene-expression geometry
- treatment response
- survival analysis

## 9. Bibliography

Chachólski, Wojciech, and Ryan Ramanujam. “Geometry based gene-expression signatures detect cancer treatment responders in clinical trials.” _BMC Cancer_ 26, 2026. [https://doi.org/10.1186/s12885-026-17312-4](https://doi.org/10.1186/s12885-026-17312-4).
