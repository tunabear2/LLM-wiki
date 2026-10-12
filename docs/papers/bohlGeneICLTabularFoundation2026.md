---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# GeneICL: A Tabular Foundation Model for Bulk Transcriptomics

## 기본 정보

- Citation key: `bohlGeneICLTabularFoundation2026`
- Item type: preprint
- Authors: Michael Bohl; Alexander Theus; David Wissel; Valentina Boeva
- DOI: 10.48550/arXiv.2610.08694
- URL: [Link](https://doi.org/10.48550/arXiv.2610.08694)
- Source/date: arXiv v1, submitted 2026-10-06

## 1. 한 줄 요약

GeneICL은 실제 bulk expression에서 만든 semi-synthetic prior로 420만 parameter tabular FM을 pretrain해 80개 임상 outcome task에서 self-supervised transcriptomic FM과 tuned baseline을 비교한다.

## 2. 왜 중요한가

Transcriptomics에서 단순한 supervised baseline을 넘지 못하는 대규모 self-supervised FM의 한계를 지적하고, domain-aware pretraining과 inference-time in-context learning이 규모보다 중요할 수 있음을 보여준다. 다만 single-cell model이 아니라 bulk clinical transcriptomics 모델이다.

## 3. 내 연구에 연결할 점

Kidney transplant bulk 또는 pseudobulk cohort의 rejection, graft function, time-to-event 예측에서 GeneICL과 scFM-derived aggregation을 같은 patient split으로 비교하면 single-cell pretraining의 추가 가치를 분리할 수 있다.

## 4. Bibliography

Bohl, Michael, Alexander Theus, David Wissel, and Valentina Boeva. "GeneICL: A Tabular Foundation Model for Bulk Transcriptomics." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2610.08694](https://doi.org/10.48550/arXiv.2610.08694).
