---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Stack: In-Context Learning of Single-Cell Biology

## 기본 정보

- Citation key: `dongStackInContextSingleCell2026`
- Item type: preprint
- Authors: M. Dong; A. Adduri; D. Gautam; L. Wu; C. Kernick; M. M. Coons; Y.-C. Chih; C. Carpenter; R. Shah; C. Ricci-Tam; P.-Y. Tung; N. Li; A. Dobin; Y. Kluger; D. P. Burke; T. Roth; Y. H. Roohani
- DOI: 10.64898/2026.01.09.698608
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.01.09.698608v2)
- Source/date: bioRxiv revised v2, 2026-06-08

## Abstract

Stack is a foundation model trained on 149 million uniformly processed human single cells. It uses tabular attention so representations for each cell are informed by surrounding context cells, enabling in-context learning from unlabeled cells that represent arbitrary conditions such as perturbations or donor differences.

## 1. 한 줄 요약

%% begin one-line-summary %%
Stack은 1.49억 human single cell로 학습한 tabular-attention foundation model로, fine-tuning 없이 context cell 예시를 보고 perturbation이나 donor effect를 예측하려는 in-context scFM이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
기존 scFM이 고정된 supervised downstream task에 의존하는 한계를 줄이기 위해, Stack은 target cell뿐 아니라 같은 context에 놓인 unlabeled cells를 함께 사용한다. 이 구조는 chemical, cytokine, genetic perturbation 또는 donor condition을 예시로 받아 target cell population의 변화를 예측하는 in-context learning을 목표로 한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Transplant rejection에서는 donor, immunosuppression, DSA status, rejection subtype 같은 condition이 강한 context effect를 만든다. Stack식 in-context setup은 한 환자/코호트의 unlabeled biopsy cells를 context로 주고 다른 환자 cell state 변화를 예측하는 실험에 맞으며, steroid response나 cytokine stimulation signature 전이에 특히 유용할 수 있다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Stack
- In-context learning
- Single-cell foundation model
- Perturbation prediction
- Donor-specific effect
- Tabular attention
- DiseasePert
- Kidney transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv v2 metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Dong, M., A. Adduri, D. Gautam, L. Wu, C. Kernick, M. M. Coons, et al. "Stack: In-Context Learning of Single-Cell Biology." _bioRxiv_, revised 2026. [https://doi.org/10.64898/2026.01.09.698608](https://doi.org/10.64898/2026.01.09.698608).

