---
type: paper
status: reference
rag_priority: high
updated: '2026-11-24'
tags:
- wiki/paper
---

# Population-level learning of non-additive effects enables accurate and efficient prediction of combinatorial perturbation responses

## 기본 정보

- Citation key: `anPopulationLevelLearning2026`
- Item type: preprint
- Authors: S. An; Q. Gong; K. Cao
- DOI: 10.64898/2026.11.20.768136
- URL: [Link](https://doi.org/10.64898/2026.11.20.768136)
- Source/date: bioRxiv v1, posted 2026-11-23

## 1. 한 줄 요약

GAIN은 두 single-perturbation pseudobulk의 합에 population-level interaction term만 학습해 복잡한 cell-level·foundation model보다 빠르게 조합 response를 예측한다.

## 2. 왜 중요한가

세 single-cell genetic·drug combination dataset에서 additive baseline의 deviation을 직접 모델링해 여러 generalization setting에서 cell-level 방법을 앞섰고 training은 3–64배 빨랐다. 조합 perturbation에서 단순 baseline의 강도를 다시 보여준다.

## 3. 내 연구에 연결할 점

면역억제제·cytokine 조합이나 gene-pair 후보 평가에서 scFM 이전에 반드시 둘 additive pseudobulk baseline으로 사용할 수 있다. Donor와 renal cell state를 holdout하고 interaction gain이 biological replicate noise를 넘는지 확인해야 한다.

## 4. Bibliography

An, S., Q. Gong, and K. Cao. "Population-level learning of non-additive effects enables accurate and efficient prediction of combinatorial perturbation responses." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.20.768136](https://doi.org/10.64898/2026.11.20.768136).
