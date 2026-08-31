---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-31'
tags:
- wiki/paper
---

# Locked Evaluation Surfaces: Transfer Failure and Sampling-Depth Entanglement in CRISPRi Perturbation-Effect Prediction

## 기본 정보

- Citation key: `shoeibiLockedEvaluationSurfaces2026`
- Item type: preprint
- Authors: Mehrdad Shoeibi; Niloofar Yousefi
- DOI: 10.48550/arXiv.2608.00152
- URL: [Link](https://arxiv.org/abs/2608.00152)
- Source/date: arXiv revised v2, 2026-08-28

## 1. 한 줄 요약

Pre-registered locked protocol에서 frozen Geneformer perturbation representation의 cross-screen transfer failure와 evaluation endpoint의 sampling-depth confounding을 확인한다.

## 2. 왜 중요한가

Virtual Cell Challenge 내부에서는 random-feature control보다 정보가 있었지만 두 external CRISPRi screen으로의 zero-shot transfer는 실패했다. Cell count만으로도 endpoint 분산의 큰 부분을 설명해, 복잡한 model의 apparent signal이 sampling depth와 얽힐 수 있음을 보인다.

## 3. 내 연구에 연결할 점

Rejection perturbation 예측에서는 donor·center·platform을 완전히 분리한 external test와 cell-count-only control을 고정하고, 모델·endpoint 선택을 test 결과 확인 전에 잠그는 것이 필요하다.

## 4. Bibliography

Shoeibi, Mehrdad, and Niloofar Yousefi. "Locked Evaluation Surfaces: Transfer Failure and Sampling-Depth Entanglement in CRISPRi Perturbation-Effect Prediction." _arXiv_, revised 2026. [https://doi.org/10.48550/arXiv.2608.00152](https://doi.org/10.48550/arXiv.2608.00152).
