---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Finetuning masking challenges narrow-task evaluation of cell foundation models

## 기본 정보

- Citation key: `shakeelFinetuningMaskingCellFM2026`
- Item type: preprint
- Authors: Muhammad Haroon Shakeel; Meng Shen; Stefano Mangiola
- DOI: 10.64898/2026.06.04.730272
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.04.730272v1)
- Source/date: bioRxiv, 2026-06-06

## Abstract

Single-cell foundation models are expected to improve transfer across biological domains, but common fine-tuned benchmark tasks may hide differences in representation quality. This paper tests downstream performance across large reductions in pretraining data and reports that fine-tuning can mask the value of additional pretraining scale under narrow evaluation tasks.

## 1. 한 줄 요약

%% begin one-line-summary %%
Cell foundation model benchmark에서 fine-tuning이 pretraining scale 차이를 가려, 좁은 downstream task만으로는 representation quality를 제대로 평가하기 어렵다는 문제를 제기한다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
대규모 pretraining data가 항상 downstream 성능 향상으로 보이는지 확인하기 위해 reduced corpus로 pretrained model을 비교한다. Fine-tuning을 허용하면 좁은 task에서는 pretraining 규모에 따른 표현 차이가 성능 지표에 잘 드러나지 않아, benchmark가 foundation model의 장점을 과소 또는 왜곡 평가할 수 있다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection task에서 scFM을 평가할 때 fine-tuned classifier accuracy만 보면 embedding의 transfer 가치를 놓칠 수 있다. Frozen embedding, zero-shot/linear probe, cross-center transfer, unseen disease state generalization을 같이 두어야 fine-tuning으로 덮인 성능과 실제 pretrained representation 효과를 분리할 수 있다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Cell foundation model
- Benchmarking
- Fine-tuning
- Pretraining scale
- Representation quality
- Transfer learning
- Rejection prediction
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Shakeel, Muhammad Haroon, Meng Shen, and Stefano Mangiola. "Finetuning masking challenges narrow-task evaluation of cell foundation models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.04.730272](https://doi.org/10.64898/2026.06.04.730272).

