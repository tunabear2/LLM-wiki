# HoloCell: A Generative Foundation Model for Holistic Cellular Modeling

## 기본 정보

- Citation key: `jiangHoloCellGenerativeFoundation2026`
- Item type: preprint
- Authors: Q. Jiang; Z. Li; B. Hu; Y. Bie; K. Li; Q. Li; P. Jin; Y. He; P. Deng; Z. Wang; X. Chen; T. Qin; H. Liu; R. Jiang; Q. Yin
- DOI: 10.64898/2026.06.07.730684
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.07.730684v1)
- Source/date: bioRxiv, 2026-06-11

## Abstract

HoloCell is presented as a generative foundation model for joint representation learning and generative modeling across epigenomic, transcriptomic, and proteomic single-cell modalities. It has over 860 million parameters and is pretrained on a Human-Multi-Omics-Corpus of about 468 million single-cell profiles.

## 1. 한 줄 요약

%% begin one-line-summary %%
HoloCell은 epigenome, transcriptome, proteome을 함께 다루는 8.6억 parameter 규모의 multimodal generative single-cell foundation model이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Single-cell multi-omics는 modality missingness와 paired measurement 부족이 큰 문제다. HoloCell은 세 주요 omics layer를 같은 generative framework에서 학습해 joint representation, missing modality handling, modality-aware generation을 목표로 한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection은 scRNA-seq, CITE-seq, snATAC-seq, spatial data가 cohort마다 부분적으로만 존재하기 쉽다. HoloCell류 모델은 missing modality를 전제로 immune activation, endothelial injury, fibrosis program을 공통 latent space에서 비교하는 후보가 될 수 있다. 단, transplant-specific cell state가 pretraining corpus에 충분한지 external cohort 검증이 필요하다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- HoloCell
- Generative foundation model
- Single-cell multi-omics
- Transcriptomics
- Epigenomics
- Proteomics
- Missing modality
- Transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Jiang, Q., Z. Li, B. Hu, Y. Bie, K. Li, Q. Li, P. Jin, et al. "HoloCell: A Generative Foundation Model for Holistic Cellular Modeling." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.07.730684](https://doi.org/10.64898/2026.06.07.730684).

