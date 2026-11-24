---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# Spatial single cell multi-omics identifies divergent melanoma-cell states associated with metastatic outcomes in thin primary melanomas

## 기본 정보

- Citation key: `antoranzSpatialSingleCell2026`
- Item type: preprint
- Authors: Asier Antoranz et al.
- Source: bioRxiv v1, posted 2026-11-20 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.19.767941](https://doi.org/10.64898/2026.11.19.767941)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

같은 조직 절편의 single-cell spatial transcriptomics와 protein imaging으로 얇은 원발성 melanoma의 두 cell-state trajectory를 찾고, metastasis outcome과의 연관을 다기관·bulk 자료에서 검증했다.

## 2. 연구 질문

두께가 1 mm 이하인데도 전이하는 melanoma를 spatially organized tumor-cell state와 neighborhood로 구분할 수 있는가?

## 3. 데이터와 방법

Thin primary melanoma에서 same-section RNA·protein profiling을 결합해 7개 melanoma-cell state와 공통 trunk에서 갈라지는 두 inferred trajectory를 정의했다. Mesenchymal-invasive·nevus-like terminal state의 neighborhood, immune·ECM·angiogenesis program을 비교하고 국제 다기관 H&E-inferred spatial transcriptomics 및 독립 primary-melanoma bulk transcriptomic dataset에서 outcome association을 확인했다.

## 4. 핵심 결과

- IFN-associated stress를 거쳐 mesenchymal-invasive state로 이어지는 lineage는 metastasizing tumor, immune-hot neighborhood, ECM remodeling·angiogenesis에 풍부했다.
- Melanocytic feature를 유지하는 cohesive nevus-like lineage는 non-metastasizing tumor와 immune-cold neighborhood에 더 많았다.
- 핵심 state–outcome 연관은 다기관 image-inferred spatial 자료와 독립 bulk expression dataset에서도 같은 방향으로 확인됐다.

## 5. 한계

Trajectory는 단면 관찰자료에서 추론했으므로 실제 계통·시간 경로를 증명하지 않는다. Thin melanoma의 희귀 전이 때문에 표본수와 center별 treatment 차이에 민감할 수 있고, H&E로 추정한 expression은 직접 측정한 spatial transcriptome과 구분해야 한다. 임상 biomarker로 쓰려면 prospective cohort가 필요하다.

## 6. 재현 또는 활용 포인트

환자 단위 split과 center holdout을 사용하고 same-section RNA–protein registration, state signature, trajectory root 선택을 고정한다. Breslow thickness 등 임상변수 위에 spatial state가 주는 incremental value와 calibration을 보고, bulk validation에서는 cell composition confounding을 점검한다.

## 7. Transcriptomics·신장이식 연구와의 연결

얇은 biopsy에서도 면역·ECM neighborhood가 임상 진행을 구분할 수 있다는 설계는 subclinical rejection과 이후 graft decline 연구에 직접 참고된다. Spatial signature를 bulk cohort에 전이할 때는 immune infiltration과 tissue damage를 별도 축으로 검증해야 한다.

## 8. 관련 키워드

- melanoma
- spatial multi-omics
- metastatic outcome
- tumor-cell state
- external validation

## 9. Bibliography

Antoranz, Asier, et al. “Spatial Single Cell Multi-Omics Identifies Divergent Melanoma-Cell States Associated with Metastatic Outcomes in Thin Primary Melanomas.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.19.767941](https://doi.org/10.64898/2026.11.19.767941).
