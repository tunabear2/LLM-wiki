# PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction

## 기본 정보

- Citation key: `wuPerturbCellRLVerifierGuided2026`
- Item type: preprint
- Authors: Dongxia Wu; Mingyu Li; Yuhui Zhang; Anurendra Kumar; Emma Lundberg; Serena Yeung-Levy; Emily B. Fox
- DOI: 10.48550/arXiv.2606.27752
- URL: [Link](https://arxiv.org/abs/2606.27752)
- Source/date: arXiv, 2026-06-26

## Abstract

Single-cell perturbation models can reduce wet-lab screening by predicting transcriptional responses to interventions, but generated individual cells are often not explicitly checked for biological consistency. PerturbCellRL post-trains a pretrained single-cell transcriptomic generator with reinforcement learning, using verifier rewards for Pearson top-k similarity, RMSE top-k proximity, DE Spearman agreement, and pathway activity. The paper evaluates genetic and chemical perturbation benchmarks and reports improved verifier-aligned single-cell consistency while remaining competitive on population-level metrics.

## 1. 한 줄 요약

%% begin one-line-summary %%
PerturbCellRL은 pretrained single-cell transcriptomic generator를 verifier reward 기반 RL로 post-training해, perturbation prediction에서 개별 generated cell의 pathway와 DEG 일관성을 높이려는 방법이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
기존 perturbation generator는 population-level expression distribution을 맞추는 데 집중해 개별 cell이 생물학적으로 그럴듯한지 직접 제약하지 않을 수 있다. 논문은 Pearson/RMSE top-k, DE Spearman, pathway activity verifier를 reward로 두고 RL post-training을 수행해, 생성된 perturbation response가 gene-level 및 pathway-level 기준을 동시에 만족하도록 유도한다.
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
- Verifier-guided generation
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

Wu, Dongxia, Mingyu Li, Yuhui Zhang, Anurendra Kumar, Emma Lundberg, Serena Yeung-Levy, and Emily B. Fox. "PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2606.27752](https://doi.org/10.48550/arXiv.2606.27752).
