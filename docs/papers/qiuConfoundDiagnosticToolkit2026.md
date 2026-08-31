---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-31'
tags:
- wiki/paper
---

# A confound-diagnostic toolkit for in silico perturbation with single-cell foundation models

## 기본 정보

- Citation key: `qiuConfoundDiagnosticToolkit2026`
- Item type: preprint
- Authors: Ru Qiu; Max Mingqian Zhao
- DOI: 10.64898/2026.08.04.732812
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.08.04.732812v1)
- Source/date: bioRxiv v1, posted 2026-08-07

## 1. 한 줄 요약

Geneformer의 token deletion 기반 in silico perturbation이 gene identity, 반응성, token coverage, library size, circular scoring 같은 교란을 넘어 재현 가능한 정보를 주는지 진단하는 framework를 제안한다.

## 2. 왜 중요한가

Frangieh와 Replogle perturbation dataset에서 frozen Geneformer embedding delta는 gene identity만 사용한 대조군보다 held-out 성능을 안정적으로 높이지 못했다. 따라서 scFM perturbation 결과를 biological knockout 효과로 해석하기 전에 matched control, coverage gate, library-size 진단과 de-circularized score가 필요하다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection에서 HLA, IFN, endothelial activation gene의 in silico deletion을 비교할 때 donor-level holdout과 gene-identity baseline을 두고, expression depth와 state score에 같은 gene이 중복 사용되는 circularity를 제거해야 한다.

## 4. Bibliography

Qiu, Ru, and Max Mingqian Zhao. "A confound-diagnostic toolkit for in silico perturbation with single-cell foundation models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.08.04.732812](https://doi.org/10.64898/2026.08.04.732812).
