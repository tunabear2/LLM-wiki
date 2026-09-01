---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Elucidating the Design Space of Generative Models for Single-Cell Perturbation Prediction

## 기본 정보

- Citation key: `bhattacharyaDesignSpacePerturbation2026`
- Item type: preprint
- Authors: Sanjukta Bhattacharya; C. Gensbigler; S. Karim; J. Lees
- DOI: 10.64898/2026.06.15.732063
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.15.732063v1)
- Source/date: bioRxiv, 2026-06-18

## Abstract

The paper studies generative designs for single-cell perturbation prediction, arguing that next-token prediction is poorly matched to unordered gene expression. It introduces ExpressionVAE, a discrete-latent perturbation model using finite scalar quantization and a perturbation-conditioned discrete prior, and reports strong results on Replogle and Parse 1M benchmarks.

## 1. 한 줄 요약

%% begin one-line-summary %%
ExpressionVAE는 unordered gene expression을 discrete latent code sequence로 압축한 뒤 perturbation-conditioned prior로 single-cell response를 생성해, perturbation prediction에서 autoregressive token recipe의 한계를 피하려는 모델이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Gene expression에는 자연스러운 left-to-right token order가 없으므로 language-model식 next-token prediction을 그대로 쓰기 어렵다. 논문은 cell을 discrete latent code로 먼저 압축하고, perturbation condition을 반영한 prior가 그 code distribution을 예측하게 만들어 generative perturbation modeling의 설계 축을 분리한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서 cytokine, drug, donor-specific stimulation response를 예측하려면 perturbation model이 cell type과 baseline activation state를 분리해야 한다. ExpressionVAE식 discrete latent는 rejection-associated immune state를 compact code로 다루는 후보이며, steroid response나 anti-rejection therapy signature simulation에서 raw expression baseline과 비교할 수 있다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Single-cell perturbation prediction
- Generative model
- ExpressionVAE
- Discrete latent
- Finite scalar quantization
- Perturb-seq
- Virtual cell
- Transplant rejection response
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Bhattacharya, Sanjukta, C. Gensbigler, S. Karim, and J. Lees. "Elucidating the Design Space of Generative Models for Single-Cell Perturbation Prediction." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.15.732063](https://doi.org/10.64898/2026.06.15.732063).

