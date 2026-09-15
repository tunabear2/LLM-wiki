---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# LymphGen-Sig: Integrating Genetic and Transcriptional States to Predict Therapeutic Response in Diffuse Large B-Cell Lymphoma

## 기본 정보

- Citation key: `tumuluruLymphGenSigIntegrating2026`
- Item type: journalArticle
- Authors: Sravya Tumuluru; Alan Cooper; Yanwen Jiang; Connie Lee Batlevi; Will Harris; Gilles Salles; Marek Trneny; Georg Lenz; Franck Morschhauser; Fabrice Jardin; Sandhya Balasubramanian; Matthew Sugidono; Alex F. Herrera; Justin Kline; James K. Godfrey
- Journal: Journal of Clinical Oncology
- DOI: 10.1200/JCO-26-00451
- PMID: 42715516
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42715516/); [DOI](https://doi.org/10.1200/JCO-26-00451)
- Source/date: published online 2026-09-09; PubMed indexed 2026-09-10 01:03 KST
- 주 카테고리: Cancer Transcriptomics / Clinical Prediction
- 교차 카테고리: Bulk RNA-seq

## 1. 한 줄 요약

LGsig는 paired genomic·transcriptomic DLBCL 764례에서 만든 294-gene expression classifier로 기존 LymphGen 미분류 사례까지 subtype을 배정하고, POLARIX RNA-seq 678례에서 subtype별 치료반응 차이를 평가했다.

## 2. 연구 질문

복잡한 유전정보를 요구하면서 일부 종양을 분류하지 못하는 LymphGen의 한계를, gene-expression signature만으로 보완해 모든 diffuse large B-cell lymphoma(DLBCL)를 생물학적·치료반응 관련 subtype으로 분류할 수 있는가?

## 3. 데이터와 방법

National Cancer Institute/British Columbia Cancer Agency의 paired genomic·transcriptomic DLBCL 764례를 개발 자료로 사용했다. 모델 개발은 MCD, BN2, EZB, ST2로 유전 분류된 종양에 제한했고, subtype별 differential expression으로 후보를 고른 뒤 nearest shrunken centroid classifier에 최적인 294개 유전자를 선택했다. 최종 LGsig는 MCDsig, BN2sig, EZBsig, ST2sig를 출력하며, POLARIX trial의 archival RNA-seq 678례에 적용해 polatuzumab vedotin-R-CHP와 R-CHOP의 outcome을 subtype별로 비교했다.

## 4. 핵심 결과

LGsig는 전사체만으로 LymphGen subtype을 식별하고 기존 LymphGen 미분류 사례에도 분류를 확장했다. 새로 배정된 사례는 대응하는 유전 subtype의 전사 및 임상 특성과 유사했고, aneuploidy·TP53 alteration으로 정의된 A53 사례도 더 구체적인 LGsig cluster로 재배정됐다. POLARIX 분석에서는 기존 LymphGen보다 biomarker 구분력이 개선됐으며, LymphGen 분류 여부와 관계없이 pola-R-CHP와 R-CHOP 간 생존 이득이 다른 subtype을 찾아냈다.

## 5. 한계

개발 단계가 네 가지 LymphGen class에 한정돼 다른 유전 상태가 학습에 직접 반영된 것은 아니다. POLARIX 평가는 archival sample을 이용한 후향적 biomarker 분석이며, 초록에는 subtype별 치료효과 크기·신뢰구간과 분류 정확도의 상세 수치가 제시되지 않았다. 294-gene signature의 임상 이전에는 RNA 품질, 정규화, 결측 유전자와 플랫폼 차이에 대한 locked specification 및 전향적 검증이 필요하다.

## 6. 재현 또는 활용 포인트

- NCI/BCCA 개발 cohort와 POLARIX 평가 cohort를 섞지 않고 완전히 분리한다.
- 294개 유전자 목록뿐 아니라 정규화, scaling, centroid, shrinkage와 class assignment 규칙을 함께 고정해야 한다.
- 기존 LymphGen 미분류군과 A53 재배정군에서 전사 특성 및 임상 outcome이 함께 재현되는지 확인한다.
- 치료 예측 biomarker는 각 subtype 내부의 단순 유의성보다 treatment-by-subtype interaction과 불확실성을 보고한다.
- 다른 RNA-seq 또는 microarray 자료에 옮길 때 gene mapping, batch와 missing-feature 처리 규칙을 사전에 명시한다.

## 7. Transcriptomics·신장이식 연구와의 연결

유전 분류를 bulk-expression surrogate로 바꾸고 독립 임상시험 cohort에서 치료 연관성을 확인한 설계는 이식 biopsy의 molecular rejection subtype 개발에 참고할 수 있다. 신장이식에서는 DLBCL signature를 전이하지 말고 Banff·MMDx label로 rejection-specific centroid를 학습한 뒤, 기관·플랫폼·치료가 다른 외부 cohort에서 graft outcome 및 면역억제제 반응과 함께 검증해야 한다.

## 8. 관련 키워드

- Cancer Transcriptomics / Clinical Prediction
- Bulk RNA-seq
- Diffuse large B-cell lymphoma
- Molecular classification
- Treatment response
- External validation

## 9. Bibliography

Tumuluru, Sravya, et al. “LymphGen-Sig: Integrating Genetic and Transcriptional States to Predict Therapeutic Response in Diffuse Large B-Cell Lymphoma.” Journal of Clinical Oncology, 2026, JCO-26-00451. [https://doi.org/10.1200/JCO-26-00451](https://doi.org/10.1200/JCO-26-00451).
