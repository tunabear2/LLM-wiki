---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# CellOS: Learning a World Model of Cellular State through Joint Embedding Prediction

## 기본 정보

- Citation key: `zhouCellOSWorldModel2026`
- Item type: preprint
- Authors: Q. Zhou; Y. Le; X. Qi; S. Chang; H. Lu; Y. Wu; H. Wang; R. Ran; X. Li
- DOI: 10.64898/2026.06.18.733163
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.18.733163v2)
- Source/date: bioRxiv revised v2, 2026-06-25

## Abstract

CellOS is a multi-view single-cell foundation model for cellular state. It uses paired expression and perception views, dense-to-mixture-of-experts expansion, and latent-space alignment via an LLM-JEPA objective. The reported model has 12 billion parameters and was trained on 390.5 million single-cell transcriptomes, with evaluations on annotation, batch integration, and perturbation-response prediction.

## 1. 한 줄 요약

%% begin one-line-summary %%
CellOS는 expression view와 perception view를 joint embedding prediction으로 맞추는 12B 규모 multi-view single-cell foundation model이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Reconstruction이나 next-token prediction만으로는 cell state의 complementary view를 명시적으로 맞추기 어렵다. CellOS는 causal cell-sentence modeling, dense-to-MoE expansion, LLM-JEPA alignment를 결합해 representation 중심의 cellular world model을 만들려 한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection은 annotation, batch integration, perturbation-response prediction이 모두 필요한 문제다. CellOS류 multi-view model은 patient context와 expression state를 함께 정렬하는 후보지만, 12B 규모 모델인 만큼 실제 연구에서는 frozen embedding, adapter, external validation 비용을 먼저 따져야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- CellOS
- Cellular world model
- Multi-view foundation model
- Joint embedding prediction
- Mixture of experts
- Perturbation response
- Kidney transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv v2 metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Zhou, Q., Y. Le, X. Qi, S. Chang, H. Lu, Y. Wu, H. Wang, R. Ran, and X. Li. "CellOS: Learning a World Model of Cellular State through Joint Embedding Prediction." _bioRxiv_, revised 2026. [https://doi.org/10.64898/2026.06.18.733163](https://doi.org/10.64898/2026.06.18.733163).
