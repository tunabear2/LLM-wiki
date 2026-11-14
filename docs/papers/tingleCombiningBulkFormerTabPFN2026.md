---
type: paper
status: reference
rag_priority: high
updated: '2026-11-14'
tags:
- wiki/paper
---

# Combining BulkFormer and TabPFN to predict post-transplant function from kidney biopsies during normothermic machine perfusion or cold storage

## 기본 정보

- Citation key: `tingleCombiningBulkFormerTabPFN2026`
- Item type: journal article
- Authors: Samuel J. Tingle; Georgios Kourounis; Sofia Kazerouni; Harry V. M. Spiers; Miguel Larraz; Maithili Mehta; Serena MacMillan; Sarah A. Hosgood; Michael L. Nicholson; Neil S. Sheerin; Colin H. Wilson
- DOI: 10.1038/s41598-026-68541-3
- PMID: 43019191
- URL: [Link](https://doi.org/10.1038/s41598-026-68541-3)
- Source/date: Scientific Reports, published 2026-08-27; PubMed indexed 2026-11-12

## 1. 한 줄 요약

BulkFormer gene embedding과 TabPFN을 결합한 zero-shot pipeline이 normothermic machine perfusion kidney biopsy RNA-seq에서 delayed graft function을 예측했다.

## 2. 왜 중요한가

세 donated-kidney cohort를 사용해 재학습 없이 count data를 예측에 넣었고, NMP biopsy에서 c-statistic 0.82를 보고했지만 cold-storage biopsy에서는 성능이 낮았다. Cytokine-filter 처리에 따라 prediction이 변해 치료 surrogate 가능성을 탐색했으나 연구는 exploratory하다.

## 3. 내 연구에 연결할 점

Kidney transplantation과 transcriptomics FM을 직접 연결한 사례다. Rejection 자체가 아니라 delayed graft function 예측이며 cohort가 작고 storage context 의존성이 크므로, rejection label·donor·center·preservation protocol별 외부 검증 없이 확장 해석하면 안 된다.

## 4. Bibliography

Tingle, Samuel J., Georgios Kourounis, Sofia Kazerouni, Harry V. M. Spiers, Miguel Larraz, Maithili Mehta, Serena MacMillan, Sarah A. Hosgood, Michael L. Nicholson, Neil S. Sheerin, and Colin H. Wilson. "Combining BulkFormer and TabPFN to predict post-transplant function from kidney biopsies during normothermic machine perfusion or cold storage." _Scientific Reports_ 16 (2026): 36430. [https://doi.org/10.1038/s41598-026-68541-3](https://doi.org/10.1038/s41598-026-68541-3).
