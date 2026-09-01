---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Raw-count embeddings improve single-cell foundation models

## 기본 정보

- Citation key: `schledeRawCountEmbeddings2026`
- Item type: preprint
- Authors: S. Schlede, T. P. Muruganandan, S. Gojjam Kantharaju, I. Kisis, M. Boecker, M. Kim Alves Carpinteiro, A. Schmitz, L. M. Buchwald, V. Sakthivelu, G. S. Gulculer Balta, M. Anstotz, M. A. Rueger, R. K. Thomas, and F. Beleggia
- DOI: 10.64898/2026.06.29.735389
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.29.735389v1)
- Source/date: bioRxiv, 2026-07-03

## Abstract

This paper questions common preprocessing choices in single-cell transformer foundation models, including rank-based gene ordering and library-size normalization. Across seven preprocessing strategies, it reports that non-normalized log-transformed counts work best, while gene order contributes little. The proposed Gene Intelligence model projects log1p raw counts directly onto token embeddings and jointly predicts masked tokens and counts without normalization, positional encoding, or read-depth tokens, matching or improving larger models in several tested tasks with far fewer parameters.

## 1. 한 줄 요약

%% begin one-line-summary %%
Raw-count 기반 embedding과 단순한 token design만으로도 대형 single-cell transformer foundation model과 경쟁할 수 있음을 보이며, rank/normalization preprocessing 관행을 재검토하게 한다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
scFM 성능 차이가 architecture scale보다 expression input representation에서 크게 갈릴 수 있다는 점을 실험적으로 확인한다. Gene Intelligence는 log1p raw count를 token embedding에 직접 투영하고 masked token/count prediction을 함께 학습해, gene rank ordering이나 read-depth token 없이도 gene-level task와 cell classification에서 강한 성능을 보인다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant scRNA-seq는 donor, platform, tissue quality, dissociation bias 때문에 normalization choice가 rejection signal을 바꿀 수 있다. scGPT/Geneformer embedding을 쓰기 전 raw-count/log-count representation, library-size normalization, rank tokenization을 같은 split에서 비교하고, HLA/IFN/endothelial activation marker 보존성을 별도 점검해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Raw-count embedding
- Single-cell transformer
- Gene Intelligence
- Tokenization
- Normalization
- scGPT
- Geneformer
- Kidney transplant scRNA-seq
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Schlede, S., T. P. Muruganandan, S. Gojjam Kantharaju, I. Kisis, M. Boecker, M. Kim Alves Carpinteiro, A. Schmitz, L. M. Buchwald, V. Sakthivelu, G. S. Gulculer Balta, M. Anstotz, M. A. Rueger, R. K. Thomas, and F. Beleggia. "Raw-count embeddings improve single-cell foundation models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.29.735389](https://doi.org/10.64898/2026.06.29.735389).
