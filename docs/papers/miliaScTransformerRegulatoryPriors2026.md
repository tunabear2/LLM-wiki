---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Integrating gene regulatory priors into Transformer attention with scTransformer for interpretable scRNA-seq analysis

## 기본 정보

- Citation key: `miliaScTransformerRegulatoryPriors2026`
- Item type: preprint
- Authors: Mikele Milia; Louis Fabrice Tshimanga; Henning Mueller; Manfredo Atzori; Barbara Di Camillo
- DOI: 10.48550/arXiv.2606.09558
- URL: [Link](https://arxiv.org/abs/2606.09558)
- Source/date: arXiv, 2026-06-08

## Abstract

Transformer-based models are increasingly applied to large-scale single-cell transcriptomics, but many treat genes as independent features and ignore prior regulatory structure. scTransformer constrains attention with gene regulatory priors, aiming to improve interpretability and robustness while preserving performance in disease-relevant single-nucleus RNA-seq cell-type classification.

## 1. 한 줄 요약

%% begin one-line-summary %%
scTransformer는 gene regulatory prior를 attention pattern에 직접 넣어 single-cell Transformer embedding의 해석성과 cell type classification 성능을 함께 개선하려는 방법이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
일반 Transformer가 gene 간 연결을 데이터에서만 학습하는 대신, known regulatory structure에 따라 정보 흐름을 제한한다. 이 구조적 제약은 embedding space에서 cell type separation을 강화하고 attention pattern이 알려진 regulatory program과 맞도록 유도한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Transplant rejection scRNA/snRNA-seq에서 T cell exhaustion, IFN response, endothelial injury 같은 regulatory program을 해석하려면 attention을 그대로 regulatory evidence로 읽기보다 prior-constrained model과 비교하는 편이 안전하다. Rejection subtype annotation에서 GRN prior를 넣은 Transformer가 scGPT/Geneformer embedding보다 marker program을 더 안정적으로 분리하는지 확인할 수 있다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- scTransformer
- Single-cell transformer
- Gene regulatory prior
- Interpretable attention
- scRNA-seq
- snRNA-seq
- Cell type classification
- Transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 arXiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Milia, Mikele, Louis Fabrice Tshimanga, Henning Mueller, Manfredo Atzori, and Barbara Di Camillo. "Integrating gene regulatory priors into Transformer attention with scTransformer for interpretable scRNA-seq analysis." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2606.09558](https://doi.org/10.48550/arXiv.2606.09558).

