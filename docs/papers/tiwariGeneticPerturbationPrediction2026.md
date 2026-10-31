---
type: paper
status: reference
rag_priority: high
updated: '2026-10-31'
tags:
- wiki/paper
---

# Genetic Perturbation Prediction Models Fail Out-of-Distribution: A Rigorous Benchmark and Systematic Evaluation

## 기본 정보

- Citation key: `tiwariGeneticPerturbationPrediction2026`
- Item type: preprint
- Authors: K. Tiwari; G. Mahajan; R. P. Bellad; N. K. Dhruw; A. K. Jha
- DOI: 10.64898/2026.10.16.759604
- URL: [Link](https://doi.org/10.64898/2026.10.16.759604)
- Source/date: bioRxiv v1, posted 2026-10-19

## 1. 한 줄 요약

EL-PERTURB는 기능적으로 분리된 OOD split에서 20개 perturbation model을 비교해 single-cell foundation model embedding을 포함한 복잡한 architecture가 단순 baseline보다 일관된 우위를 보이지 않음을 확인했다.

## 2. 왜 중요한가

Random split이 가리는 extrapolation 실패를 essential-gene 및 genome-wide Perturb-seq에서 난이도별로 드러낸다. Wet-lab screen을 대체한다는 주장에는 평균 성능보다 기능적으로 먼 perturbation에 대한 일반화 검증이 필요하다는 직접적인 benchmark다.

## 3. 내 연구에 연결할 점

Rejection regulator나 drug target 예측은 donor, cell type, pathway family를 동시에 분리한 OOD split에서 scFM embedding과 raw-count·linear baseline을 비교해야 한다. 가까운 perturbation의 interpolation 성능을 임상적 target discovery로 확대 해석하지 않는 기준이 된다.

## 4. Bibliography

Tiwari, K., G. Mahajan, R. P. Bellad, N. K. Dhruw, and A. K. Jha. "Genetic Perturbation Prediction Models Fail Out-of-Distribution: A Rigorous Benchmark and Systematic Evaluation." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.16.759604](https://doi.org/10.64898/2026.10.16.759604).
