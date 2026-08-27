---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-17'
tags:
- wiki/paper
---

# Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation

## 기본 정보

- Citation key: `chenHarmonisedBenchmarkingFoundation2026`
- Item type: preprint
- Authors: Sally Chen; Roxana Zahedi; Lucy Chhuo; Ricky Nguyen; Marjan BaghGolshani; Amin Beheshti; Mark Grosser; Min Yang; Nona Farbehi; Nigel Lovell; Ahmadreza Argha; Fatemeh Vafaee; Youqiong Ye; Hamid Alinejad-Rokny
- DOI: 10.48550/arXiv.2607.17227
- URL: [Link](https://arxiv.org/abs/2607.17227)
- Source/date: arXiv v1, 2026-07-19

## 1. 한 줄 요약

Single-cell·spatial transcriptomics foundation model 여섯 개를 공통 전처리와 task로 비교해, modality와 domain shift에 따라 순위가 달라지고 모든 task를 지배하는 모델은 없음을 보인다.

## 2. 왜 중요한가

Nicheformer, CellPLM, scGPT-spatial, GenePT, scELMo, Novae를 clustering, annotation, marker concordance, perturbation prediction에서 zero-shot 및 continual pretraining 조건으로 평가한다. 모델 규모보다 modality, tokenization, biological prior, metric 선택이 일반화 성능을 좌우한다는 실무적 benchmark다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection에서는 cell annotation, spatial lesion 보존, perturbation response를 하나의 점수로 합치지 말고 task별로 모델과 baseline을 다시 선택해야 한다. Donor·center holdout과 biopsy platform shift를 포함한 공통 protocol로 scGPT 계열, spatial model, PCA/HVG baseline을 비교하는 근거가 된다.

## 4. Bibliography

Chen, Sally, et al. "Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2607.17227](https://doi.org/10.48550/arXiv.2607.17227).
