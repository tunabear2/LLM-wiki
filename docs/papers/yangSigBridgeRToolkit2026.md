---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# SigBridgeR: Standardized Identification of Phenotype-Associated Cell Subpopulations

## 기본 정보

- Citation key: `yangSigBridgeRToolkit2026`
- Item type: journal article
- Authors: Yuxi Yang; Hongqian Qian; Zeyu Yan; Chunyang Wang; Liping Du; Xiaoxiao Shen; Yun Peng; Xiaoyun Bu; Ting Li; Jian-Guo Zhou; Shixiang Wang
- Source: _GigaScience_, published 2026-11-10
- Original: [DOI 10.1093/gigascience/giag100](https://doi.org/10.1093/gigascience/giag100)
- PubMed: [PMID 43008316](https://pubmed.ncbi.nlm.nih.gov/43008316/)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

SigBridgeR는 bulk RNA-seq phenotype과 scRNA-seq를 연결하는 8개 알고리즘을 표준화하고 네 암종의 binary·survival phenotype에서 정확도·안정성·계산비용을 함께 비교한 R framework다.

## 2. 연구 질문

서로 다른 입력·parameter·출력 형식을 가진 phenotype-associated cell-subpopulation 방법을 동일한 preprocessing과 positive/negative control 아래에서 공정하게 비교할 수 있는가?

## 3. 데이터와 방법

여덟 알고리즘을 registry 기반 공통 interface에 통합했다. 네 암종의 paired bulk RNA-seq·scRNA-seq에서 binary 및 survival phenotype을 사용해 positive/negative control, accuracy, Hallmark pathway enrichment, parameter sensitivity, runtime·memory를 평가했다.

## 4. 핵심 결과

- 방법 간 robustness, biological consistency, efficiency, parameter sensitivity 차이가 컸다.
- 여러 평가축을 합쳤을 때 Scissor와 scAB가 가장 균형적인 성능을 보였다.
- 일부 방법은 scalability, parameter sensitivity, phenotype detection stability에서 뚜렷한 약점을 보였다.

## 5. 한계

평가는 네 암종과 포함된 8개 방법에 한정되며 phenotype label과 bulk–single-cell dataset pairing에 의존한다. 신장이식처럼 암이 아닌 조직 손상·면역 outcome에서 순위가 유지되는지는 검증되지 않았다.

## 6. 재현 또는 활용 포인트

Bulk cohort와 single-cell reference의 조직·질환 일치도, phenotype definition, donor split, parameter grid를 함께 기록한다. Positive control뿐 아니라 label permutation·negative control과 runtime·memory를 같이 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

대규모 allograft bulk cohort의 rejection·graft-failure phenotype을 작은 biopsy scRNA atlas의 세포상태와 연결할 때 방법 선택 기준으로 직접 재사용할 수 있다. Reference mismatch와 donor-level validation을 별도 stress test해야 한다.

## 8. 관련 키워드

- bulk–single-cell integration
- phenotype-associated subpopulation
- survival analysis
- benchmark

## 9. Bibliography

Yang, Yuan, et al. “SigBridgeR: An R Toolkit for Standardized Identification and Benchmarking of Phenotype-Associated Cell Subpopulations in Single-Cell Transcriptomics.” _GigaScience_, 2026. [https://doi.org/10.1093/gigascience/giag100](https://doi.org/10.1093/gigascience/giag100).
