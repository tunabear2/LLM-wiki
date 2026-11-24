---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning

## 기본 정보

- Citation key: `mateoBernadoTabBioMedBenchmark2026`
- Item type: preprint
- Authors: Pau Mateo-Bernado; Saivenkata Nagavyjayanthi Polapragada; David Bonet; Pol Arbiol Rakuljic; Laia Mogas Pladevall; et al.
- arXiv: 2611.23779
- URL: [Link](https://arxiv.org/abs/2611.23779)
- Source/date: arXiv v1, submitted 2026-11-18

## 1. 한 줄 요약

TabBioMed는 single-cell omics를 포함한 94개 biomedical table에서 23개 classical, tree, neural과 tabular foundation model을 같은 preprocessing·split으로 비교한다.

## 2. 왜 중요한가

Foundation-model family의 평균 성능은 강했지만 data regime과 compute budget에 따라 tuned MLP와 tree가 우세한 task도 많았다. Biomedical prediction에서 모델 선택을 task·sample size·비용별로 분리해야 함을 보여주는 범용 benchmark다.

## 3. 내 연구에 연결할 점

Transplant bulk·pseudobulk·clinical feature prediction의 tabular FM baseline을 고르는 참고 자료다. Single-cell foundation model benchmark 자체는 아니므로 patient-level split과 kidney-specific feature leakage를 별도로 통제해야 한다.

## 4. Bibliography

Mateo-Bernado, Pau, et al. "TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning." _arXiv_, 2026. [https://arxiv.org/abs/2611.23779](https://arxiv.org/abs/2611.23779).
