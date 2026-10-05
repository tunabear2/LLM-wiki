---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-05'
tags:
- wiki/paper
---

# PerturbCellRL: Aligning Distributions and Grounding Biology via Post-Training Perturbation Generators

## 기본 정보

- Citation key: `wuPerturbCellRLVerifierGuided2026`
- Item type: preprint
- Authors: Dongxia Wu; Mingyu Li; Yuhui Zhang; Anurendra Kumar; Emma Lundberg; Serena Yeung-Levy; Emily B. Fox
- DOI: 10.48550/arXiv.2606.27752
- URL: [Link](https://arxiv.org/abs/2606.27752)
- Source/date: arXiv v2, revised 2026-10-02

## Abstract

Single-cell perturbation models can reduce wet-lab screening by predicting transcriptional responses to interventions, but flow-matching can fail to recover target distributions even within the model family. PerturbCellRL post-trains perturbation generators with reinforcement learning, using a gene-expression energy witness to convert population-level discrepancy into per-cell feedback and calibrated rewards for expression plausibility and pathway response. The revised paper reports improved distributional alignment and pathway enrichment recovery across genetic and chemical perturbation benchmarks.

## 1. 한 줄 요약

%% begin one-line-summary %%
PerturbCellRL은 population discrepancy를 per-cell reward로 바꾸는 energy witness와 생물학적 calibration reward를 사용해 single-cell perturbation generator의 분포 정렬과 pathway fidelity를 함께 개선한다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
기존 flow-matching perturbation generator는 표현 가능한 target distribution도 최적화 과정에서 회복하지 못할 수 있다. Revised v2는 post-training이 이 분포를 회복할 수 있음을 이론적으로 보이고, gene-expression energy witness의 policy gradient가 더 나은 distribution alignment를 향하도록 설계한다. Real-cell calibration을 이용한 expression plausibility와 pathway-response reward를 더해 분포 정확도와 biological fidelity를 동시에 제약한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서는 steroid, cytokine, co-stimulation blockade 같은 perturbation response를 예측할 때 평균 expression만 맞추면 rejection-associated immune state나 endothelial injury program을 놓칠 수 있다. PerturbCellRL식 verifier reward는 IFN pathway, cytotoxic T/NK activation, antigen presentation, endothelial activation 같은 transplant-relevant pathway를 별도 reward 또는 holdout metric으로 두는 실험 설계에 참고된다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- PerturbCellRL
- Single-cell perturbation prediction
- Reinforcement learning
- Energy-witness reward
- Distribution alignment
- Transcriptomic generator
- Pathway activity reward
- DEG consistency
- Transplant rejection perturbation response
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 arXiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Wu, Dongxia, Mingyu Li, Yuhui Zhang, Anurendra Kumar, Emma Lundberg, Serena Yeung-Levy, and Emily B. Fox. "PerturbCellRL: Aligning Distributions and Grounding Biology via Post-Training Perturbation Generators." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2606.27752](https://doi.org/10.48550/arXiv.2606.27752).
