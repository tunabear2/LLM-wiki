---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# Quantification Method Affects Replicability of eQTL Analysis, Colocalization and TWAS

## 기본 정보

- Citation key: `headQuantificationMethodAffects2026`
- Item type: journal article
- Authors: S. Taylor Head; Sean T. Bresnahan; Yung-Han Chang; Vihan M. Shah; Nolan R. Cole; William Wu; Arjun Bhattacharya
- Source: Nature Genetics, online 2026-10-26
- Original: [DOI: 10.1038/s41588-026-02827-0](https://doi.org/10.1038/s41588-026-02827-0); [PMID: 42934278](https://pubmed.ncbi.nlm.nih.gov/42934278/)
- 주 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

GTEx 48개 tissue와 7개 phenotype에서 short-read RNA-seq reference annotation과 quantification 선택만으로 eQTL, expression prediction, colocalization, TWAS 재현성이 크게 달라짐을 보였다.

## 2. 연구 질문

Upstream RNA-seq reference annotation과 quantification method의 차이가 downstream genetic association 해석에 얼마나 전파되는가?

## 3. 데이터와 방법

GTEx 48개 tissue의 short-read RNA-seq를 서로 다른 transcript reference annotation과 quantification 선택으로 처리했다. Pipeline별 eQTL detection과 gene-expression prediction을 비교하고 7개 다양한 phenotype에서 colocalization과 TWAS 결과의 일치도를 평가했다.

## 4. 핵심 결과

- Annotation과 quantification 선택이 eQTL detection과 expression prediction을 실질적으로 바꿨다.
- 차이는 colocalization과 TWAS 결과까지 이어졌다.
- Pipeline 간 일치하는 결과는 더 긴 gene, isoform 수가 많은 gene, expression heritability가 높은 gene에 치우쳤다.

## 5. 한계

GTEx short-read tissue와 7개 phenotype을 중심으로 한 분석이라 disease biopsy, long-read quantification, ancestry·platform 변화까지 포괄하지 않는다. Pipeline 간 일치가 biological truth를 보장하지도 않는다.

## 6. 재현 또는 활용 포인트

Reference annotation version과 quantifier를 provenance에 고정하고 최소 두 pipeline의 eQTL·TWAS sensitivity analysis를 남긴다. Gene length, isoform count, expression heritability에 따른 concordance bias를 함께 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient eQTL이나 rejection TWAS를 biopsy RNA-seq와 연결할 때 quantification 선택이 결론을 바꿀 수 있음을 직접 경고한다. Candidate locus는 다른 annotation·quantifier와 independent cohort에서 재현해야 한다.

## 8. 관련 키워드

- Bulk RNA-seq
- GWAS
- eQTL
- TWAS
- transcript quantification

## 9. Bibliography

Head, S. Taylor, et al. “Quantification Method Affects Replicability of eQTL Analysis, Colocalization and TWAS.” _Nature Genetics_, 2026. [https://doi.org/10.1038/s41588-026-02827-0](https://doi.org/10.1038/s41588-026-02827-0).
