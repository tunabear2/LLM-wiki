---
type: paper
status: reference
rag_priority: high
updated: '2026-11-24'
tags:
- wiki/paper
---

# Model evaluation metrics of Virtual Cell Challenge 2026

## 기본 정보

- Citation key: `dobinModelEvaluationMetrics2026`
- Item type: preprint
- Authors: A. Dobin; A. Adduri; J. Sullivan; J. Lyda; R. Mehta; D. E. Leto; P. Datlinger; et al.
- DOI: 10.64898/2026.11.17.767214
- URL: [Link](https://doi.org/10.64898/2026.11.17.767214)
- Source/date: bioRxiv v1, posted 2026-11-23

## 1. 한 줄 요약

Virtual Cell Challenge 2026은 experimental repeat로 calibration하고 shortcut을 억제하는 여섯 Perturb-seq metric으로 zero-shot CRISPRi response prediction을 평가한다.

## 2. 왜 중요한가

두 metric은 predicted·measured pseudobulk를 비교하고 네 metric은 perturbation-responsive gene을 평가한다. 2025 metric에서 가능했던 shortcut이 score를 올리지 못하도록 설계했으며 구현을 cell-eval2로 공개했다.

## 3. 내 연구에 연결할 점

Rejection-relevant cytokine·gene perturbation 모델에서 평균 correlation 하나 대신 repeat ceiling, responsive-gene recovery와 shortcut control을 함께 쓰는 기준이다. Renal cell type·donor별 biological replicate calibration을 별도로 만들어야 한다.

## 4. Bibliography

Dobin, A., et al. "Model evaluation metrics of Virtual Cell Challenge 2026." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.17.767214](https://doi.org/10.64898/2026.11.17.767214).
