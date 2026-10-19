---
type: paper
status: reference
rag_priority: high
updated: '2026-10-19'
tags:
- wiki/paper
---

# SubcellPert: Benchmarking Subcellular Perturbation Prediction

## 기본 정보

- Citation key: `wangSubcellPertBenchmarkingSubcellular2026`
- Item type: preprint
- Authors: J. Wang; H. Cao; X. Dang; T. Zhou; Y. Zhao; C.-Y. Hsieh; C. Gu; P. A. Heng
- DOI: 10.64898/2026.10.11.758305
- URL: [Link](https://doi.org/10.64898/2026.10.11.758305)
- Source/date: bioRxiv v1, posted 2026-10-17

## 1. 한 줄 요약

SubcellPert는 1,388만 cell과 36.5억 RNA molecule의 14개 imaging dataset으로 perturbation 뒤 RNA abundance와 subcellular localization을 함께 예측하는 benchmark다.

## 2. 왜 중요한가

정확한 target count가 주어진 Oracle task와 abundance까지 예측하는 Joint task를 분리하고, foundation-model adapter를 포함한 여덟 baseline을 OOD holdout에서 평가한다. Count 정확도만으로는 centroid와 radial distribution 같은 공간 오류를 놓칠 수 있음을 보여준다.

## 3. 내 연구에 연결할 점

Kidney biopsy virtual-cell claim을 expression count에만 두지 않고 tubular polarity, immune synapse 및 compartment geometry까지 확장하는 평가 틀이다. 다만 현재 2D imaging 기반이므로 renal spatial assay와 perturbation condition으로 재검증해야 한다.

## 4. Bibliography

Wang, J., et al. "SubcellPert: Benchmarking Subcellular Perturbation Prediction." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.11.758305](https://doi.org/10.64898/2026.10.11.758305).
