---
type: paper
status: reference
rag_priority: high
updated: '2026-11-24'
tags:
- wiki/paper
---

# Zero-shot virtual knock-out rankings do not recover causal genes from observational single-cell data

## 기본 정보

- Citation key: `cuiZeroShotVirtualKnockout2026`
- Item type: preprint
- Authors: J. Cui; M. Li; R. Zhou; H. Zhang; S. Xu; L. Li; R. Zhang
- DOI: 10.64898/2026.11.21.768293
- URL: [Link](https://doi.org/10.64898/2026.11.21.768293)
- Source/date: bioRxiv v1, posted 2026-11-23

## 1. 한 줄 요약

Observational single-cell data의 scTenifoldKnk, CellOracle와 Geneformer zero-shot virtual knockout ranking은 실제·synthetic·DepMap knockout에서 causal gene을 신뢰성 있게 회수하지 못했다.

## 2. 왜 중요한가

Knockout별 top-20 list가 과도하게 겹쳤고 scTenifoldKnk ranking은 network out-degree를 주로 반영했다. Geneformer shift도 token coverage와 일관되게 연결되지 않아 representation displacement를 causal intervention으로 해석하는 위험을 정량화했다.

## 3. 내 연구에 연결할 점

Rejection target ranking을 observational biopsy와 virtual knockout만으로 결정하면 안 된다는 직접 근거다. CRISPR·drug perturbation, donor·cell-type OOD와 단순 expression/network baseline을 통과한 후보만 후속 실험으로 넘겨야 한다.

## 4. Bibliography

Cui, J., M. Li, R. Zhou, H. Zhang, S. Xu, L. Li, and R. Zhang. "Zero-shot virtual knock-out rankings do not recover causal genes from observational single-cell data." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.21.768293](https://doi.org/10.64898/2026.11.21.768293).
