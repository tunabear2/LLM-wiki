---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# CellMAGE: cell-type deconvolution for multi-parent population analysis of gene expression

## 기본 정보

- Citation key: `ballCellMAGEDeconvolution2026`
- Item type: preprint
- Authors: Robyn L. Ball; Alyssa Klein; Ashley A. Auth; Daniel A. Skelly; Hao He; Vivek M. Philip; Leona H. Gagnon; Elissa J. Chesler
- DOI: 10.64898/2026.09.08.750196
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.08.750196v1); [DOI](https://doi.org/10.64898/2026.09.08.750196)
- Source/date: bioRxiv v1 preprint, posted 2026-09-12; not peer reviewed
- 주 카테고리: Bulk RNA-seq

## 1. 한 줄 요약

CellMAGE는 multiparent population에서 이미 알려진 각 progeny의 parental genetic composition으로 parental single-cell profile을 가중해, 별도 model training 없이 bulk RNA-seq를 cell-type-specific expression으로 분해한다.

## 2. 연구 질문

Single-cell RNA-seq 비용이 큰 multiparent population 연구에서, 개체별로 알려진 parental ancestry 정보를 이용하면 작은 표본에서도 bulk RNA-seq로부터 세포형별 발현을 복원할 수 있는가?

## 3. 데이터와 방법

CellMAGE(Cell-type deconvolution for Multi-parent Analysis of Gene Expression)는 progeny마다 알려진 parental contribution으로 parental cell-type expression profile을 가중한다. 학습용 bulk sample이나 최소 sample size를 요구하지 않는 구조다. 검증에는 Diversity Outbred mouse 16마리의 prefrontal cortex 자료를 사용했으며, 12개 cell type과 23,116개 gene에서 예측 발현과 측정 발현을 비교했다. 비교 대상으로 CIBERSORTx를 사용했다.

## 4. 핵심 결과

저자들은 예측값과 측정값이 모든 세포형에서 유의수준 0.05로 통계적으로 동등했고, 전체 pooled Spearman correlation이 0.923(95% CI 0.910–0.934)이었다고 보고했다. CIBERSORTx는 96개 추가 sample을 사용해도 최대 12.4%의 gene과 세 개 cell type만 해석했으며, 이 제한된 비교에서도 CellMAGE의 cell-type별 median correlation은 0.908–0.974로 CIBERSORTx의 0.353–0.641보다 높았다. 저자들은 parental single-cell data가 있는 diploid crop MAGIC population에도 적용할 수 있다고 제안했다.

## 5. 한계

검증은 mouse prefrontal cortex 16개체라는 작은 단일 조직 자료에 한정됐다. 알려진 parental contribution과 각 parent의 single-cell reference가 필수이므로 일반적인 인간 cohort나 유전적으로 익명인 혼합조직에는 그대로 적용할 수 없다. 초록만으로는 동등성 검정의 margin, ancestry 추정오차에 대한 민감도, 다른 조직·population의 외부검증을 확인할 수 없다. 현재 결과는 동료심사를 거치지 않은 v1 preprint다.

## 6. 재현 또는 활용 포인트

- Progeny별 parental contribution, parental single-cell reference와 bulk RNA-seq의 sample·gene identifier를 추적 가능하게 보존한다.
- Parent와 progeny 간 gene annotation 및 expression scale을 동일하게 맞추고, reference에 없는 cell type을 별도로 점검한다.
- 측정된 cell-type-specific expression을 완전히 hold-out해 pooled correlation과 cell-type별 성능을 함께 보고한다.
- 동등성 검정의 사전 margin, Spearman confidence interval과 실패한 gene·cell type 비율을 명시한다.
- CIBERSORTx 비교에서는 추가 sample 수와 실제로 평가 가능한 gene·cell type 범위를 동일한 기준으로 공개한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Genetically diverse mouse transplant model에서 strain composition이 알려졌다면 ancestry-aware deconvolution의 참고가 될 수 있다. 그러나 사람의 이식 biopsy는 multiparent progeny가 아니며 donor·recipient 세포 혼합도 CellMAGE의 parental-mixture 가정과 다르다. 신장이식에 적용하려면 donor-derived와 recipient-derived cell을 별도로 식별하는 자료, 조직별 single-cell reference와 독립 검증이 필요하고, 현재 결과를 임상 deconvolution 근거로 직접 사용할 수는 없다.

## 8. 관련 키워드

- Bulk RNA-seq
- Cell-type deconvolution
- Multiparent population
- Single-cell reference
- Genetic composition
- Diversity Outbred mice

## 9. Bibliography

Ball, Robyn L., et al. “CellMAGE: Cell-type Deconvolution for Multi-parent Population Analysis of Gene Expression.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.08.750196](https://doi.org/10.64898/2026.09.08.750196). Preprint; not peer reviewed.
