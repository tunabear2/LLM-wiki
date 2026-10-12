---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# scStable: Assessing scRNA-seq Analysis Stability under Bulk-Derived Between-Sample Variation

## 기본 정보

- Citation key: `jiangScStableAssessing2026`
- Item type: preprint
- Authors: Chenling Jiang; Jingyi Jessica Li
- Source: bioRxiv v1, posted 2026-10-08 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.01.755876](https://doi.org/10.64898/2026.10.01.755876); [code](https://github.com/cfjiang123/scStable); [Zenodo](https://doi.org/10.5281/zenodo.23050848)
- 주 카테고리: `scRNA-seq`
- 관련 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

scStable은 한 개 scRNA-seq reference의 cell-level heterogeneity를 유지하면서 bulk RNA-seq에서 배운 표본 간 변이를 주입해 분석 결과의 안정성을 stress-test한다.

## 2. 연구 질문

생물학적 replicate가 거의 없는 scRNA-seq 연구에서 clustering·DE 결과가 표본 간 변이에 견디는지 현실적으로 평가할 수 있는가?

## 3. 데이터와 방법

한 sample의 scRNA count matrix와 선택적 multi-sample bulk reference를 입력한다. 같은 연구의 bulk 또는 GTEx tissue-matched bulk에서 변이를 학습하고, negative-binomial marginal model과 Gaussian copula gene dependence를 사용해 동일한 cell set에 sample-specific 변이를 주입한다. 위암의 matched scRNA/bulk 21개 표본에서 ZINB-WaVE, subsampling, Gaussian noise와 비교했다.

## 4. 핵심 결과

- 실제 위암 표본 간 변이를 비교 방법보다 더 잘 재현했다.
- 합성 replicate를 이용해 안정적인 DEG를 우선순위화하고 clustering method와 hyperparameter를 선택할 수 있었다.
- 동일한 cell을 보존하므로 cell별 cluster assignment 변동을 직접 추적할 수 있다.

## 5. 한계

결과는 bulk reference가 대상 tissue·condition을 얼마나 잘 대표하는지에 의존한다. 고정된 cell set을 쓰므로 실제 표본 간 cell-type composition 차이를 완전히 재현하지 못한다. 합성 표본은 독립 생물학적 replicate의 대체물이 아니다.

## 6. 재현 또는 활용 포인트

Bulk-reference와 GTEx-reference-free mode를 구분하고 variation scale을 sensitivity analysis한다. DEG overlap만 보지 말고 cluster assignment, marker ranking, pathway 결과와 hyperparameter 선택의 안정성을 함께 기록한다.

## 7. Transcriptomics·신장이식 연구와의 연결

표본 수가 적은 kidney-allograft scRNA-seq에서 donor 간 변이에 따라 rejection-associated cluster와 DEG가 얼마나 흔들리는지 사전 점검할 수 있다. 가능하면 같은 cohort의 matched bulk biopsy를 쓰고 GTEx kidney를 쓸 때 disease mismatch를 명시해야 한다.

## 8. 관련 키워드

- scRNA-seq stability
- between-sample variation
- synthetic replicates
- bulk RNA-seq reference

## 9. Bibliography

Jiang, Chenling, and Jingyi Jessica Li. “scStable: Assessing scRNA-seq Analysis Stability under Bulk-Derived Between-Sample Variation.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.01.755876](https://doi.org/10.64898/2026.10.01.755876).
