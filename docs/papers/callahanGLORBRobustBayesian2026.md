---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# GLORB: Robust Bayesian Inference for Differential Expression under Global Expression Shifts

## 기본 정보

- Citation key: `callahanGLORBRobustBayesian2026`
- Item type: bioRxiv preprint
- Authors: Rowan Callahan; Stephen D. Coleman; Thuy T. M. Ngo
- Source: bioRxiv v1, posted 2026-09-02; newly indexed in PubMed 2026-10-25
- Original: [DOI: 10.64898/2026.08.28.747928](https://doi.org/10.64898/2026.08.28.747928); [PMID: 42922649](https://pubmed.ncbi.nlm.nih.gov/42922649/)
- 주 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

GLORB는 다수 gene이 한 방향으로 움직이는 global expression shift에서 standard library normalization이 fold change를 왜곡하는 문제를 Bayesian generalized linear model로 다룬다.

## 2. 연구 질문

Spike-in control이 없어도 total RNA 변화나 대규모 동방향 regulation이 있는 RNA-seq에서 differential expression coefficient를 안정적으로 추정할 수 있는가?

## 3. 데이터와 방법

Library-size variance를 포함하는 두 Bayesian generalized linear model을 만들고, 소수 gene만 변하는 조건과 대부분 gene이 증가·감소하는 조건에서 DESeq2 median-of-ratios와 edgeR TMM을 비교했다. Geometric mean을 계산하지 않아 sparse count에도 적용할 수 있게 설계했다.

## 4. 핵심 결과

- 소수 gene이 변할 때는 DESeq2·edgeR과 일관된 library-size 보정을 보였다.
- 대부분 gene이 같은 방향으로 변할 때 기존 정규화보다 DEG와 coefficient 왜곡을 줄였다.
- Geometric mean 의존성을 없애 높은 sparsity의 dataset도 처리했다.

## 5. 한계

Global shift의 크기와 model assumption에 민감할 수 있다. 현재 공개 초록에서 독립 wet-lab spike-in validation과 재현용 code repository를 확인하지 못했고, preprint 단계다.

## 6. 재현 또는 활용 포인트

TMM·median-ratio의 “대부분 gene은 불변” 가정을 진단하고, spike-in 또는 cell-count 기반 sensitivity analysis와 함께 GLORB coefficient를 비교한다. Posterior uncertainty와 direction stability를 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

급성 rejection biopsy처럼 광범위한 immune activation과 parenchymal loss가 동시에 일어나는 상황에서 compositional normalization의 방향 왜곡을 점검하는 후보다. Cell composition 변화와 per-cell global shift는 분리해야 한다.

## 8. 관련 키워드

- Bulk RNA-seq
- differential expression
- global expression shift
- Bayesian model

## 9. Bibliography

Callahan, Rowan, Stephen D. Coleman, and Thuy T. M. Ngo. “GLORB: Robust Bayesian Inference for Differential Expression under Global Expression Shifts.” bioRxiv, 2026. [https://doi.org/10.64898/2026.08.28.747928](https://doi.org/10.64898/2026.08.28.747928).
