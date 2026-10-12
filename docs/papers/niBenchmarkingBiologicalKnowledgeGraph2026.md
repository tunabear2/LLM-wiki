---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# Benchmarking biological knowledge-graph priors against single-cell foundation models for Perturb-seq prediction

## 기본 정보

- Citation key: `niBenchmarkingBiologicalKnowledgeGraph2026`
- Item type: journal article
- Authors: Jie Ni; Xinting Zhang; Mingyang Li; Yuhan Cai; Zhuoying Xie; Yun Liu
- DOI: 10.1016/j.compbiolchem.2026.109480
- PMID: 42860076
- URL: [Link](https://doi.org/10.1016/j.compbiolchem.2026.109480)
- Source/date: PubMed / Computational Biology and Chemistry, published 2026-10-09; indexed 2026-10-11

## 1. 한 줄 요약

동일한 Perturb-seq split·gene panel·metric에서 STRING/GO graph prior와 dense·rewired control, GEARS, scGPT, Geneformer를 비교해 graph prior의 이득이 작고 gene-space가 커질수록 감소함을 보인다.

## 2. 왜 중요한가

Architecture와 split을 함께 바꾸는 비교 대신 matched protocol과 rewired control로 biological prior의 추가 가치를 분리한다. 대부분의 external-model contrast가 ±0.03 범위였다는 결과는 작은 Pearson 차이를 실질적 biological improvement로 과장하지 말아야 함을 시사한다.

## 3. 내 연구에 연결할 점

Kidney rejection perturbation model에서 renal GRN·pathway prior를 쓸 때 dense, self-edge, degree-rewired control과 scGPT·Geneformer를 같은 donor/cell-type holdout에서 비교하고 effect-size와 DE recovery를 함께 보고해야 한다.

## 4. Bibliography

Ni, Jie, Xinting Zhang, Mingyang Li, Yuhan Cai, Zhuoying Xie, and Yun Liu. "Benchmarking biological knowledge-graph priors against single-cell foundation models for Perturb-seq prediction." _Computational Biology and Chemistry_, 2026. [https://doi.org/10.1016/j.compbiolchem.2026.109480](https://doi.org/10.1016/j.compbiolchem.2026.109480).
