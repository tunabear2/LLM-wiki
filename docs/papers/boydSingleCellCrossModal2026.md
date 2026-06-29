# Single-Cell Cross-Modal Transfer by Adversarial Fine-Tuning of Foundation Models

## 기본 정보

- Citation key: `boydSingleCellCrossModal2026`
- Item type: preprint
- Authors: Joseph Boyd; Matthew Lyon; Martino Mansoldo; Christian Hurry; Finnian Firth
- DOI: 10.48550/arXiv.2606.07676
- URL: [Link](https://arxiv.org/abs/2606.07676)
- Source/date: arXiv, 2026-06-04

## Abstract

Spatial transcriptomics can profile tissue structure but often measures fewer genes than scRNA-seq. This paper proposes cross-modal translation between unpaired spatial transcriptomics and scRNA-seq, showing that a single-cell foundation model can support the translation through adversarial fine-tuning and perform competitively against multi-omics translation methods.

## 1. 한 줄 요약

%% begin one-line-summary %%
Unpaired ST와 scRNA-seq 사이의 cross-modal translation을 single-cell foundation model의 adversarial fine-tuning으로 수행해 spatial context 복원 가능성을 평가한 논문이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
scRNA-seq cell에는 원래 tissue neighborhood 정보가 일부 남아 있다는 가정 아래, paired data가 부족한 ST-scRNA setting을 unpaired domain translation 문제로 둔다. Foundation model embedding을 fine-tuning해 scRNA-seq와 spatial transcriptomics modality 사이의 표현을 맞추고, multi-omics translation baseline과 비교한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant biopsy에서는 matched spatial transcriptomics가 부족한 경우가 많으므로, scRNA-seq immune cell state를 spatial biopsy signal과 연결하는 후보 접근이다. Rejection lesion 주변 immune neighborhood를 추정할 때 paired ST가 없는 cohort에서도 pseudo-spatial transfer를 실험해볼 수 있지만, Banff lesion score나 marker ISH/IHC 같은 외부 spatial validation이 필요하다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Single-cell foundation model
- Spatial transcriptomics
- scRNA-seq
- Cross-modal transfer
- Adversarial fine-tuning
- Unpaired translation
- Kidney transplant biopsy
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 arXiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Boyd, Joseph, Matthew Lyon, Martino Mansoldo, Christian Hurry, and Finnian Firth. "Single-Cell Cross-Modal Transfer by Adversarial Fine-Tuning of Foundation Models." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2606.07676](https://doi.org/10.48550/arXiv.2606.07676).

