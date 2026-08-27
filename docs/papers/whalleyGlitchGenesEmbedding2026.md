---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-10'
tags:
- wiki/paper
---

# Do Geometric Outliers Identify Important Genes in Single-Cell Foundation Models?

## 기본 정보

- Citation key: `whalleyGlitchGenesEmbedding2026`
- Item type: preprint
- Authors: J. P. Whalley
- DOI: 10.64898/2026.06.22.733850
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.22.733850v2)
- Source/date: bioRxiv revised v2, 2026-08-03 (first posted 2026-06-27)

## Abstract

This paper compares gene-embedding outliers in Geneformer, scGPT, and scFoundation using four geometric metrics. The revised analysis finds weak agreement on individual outlier genes, model-dependent class-level patterns, and no standalone evidence that outlier status predicts annotation leverage or ClinVar disease relevance.

## 1. 한 줄 요약

%% begin one-line-summary %%
Geneformer, scGPT, scFoundation의 geometric outlier는 model-specific embedding structure를 보여주지만, 그 자체로 downstream leverage나 disease relevance를 뜻하지 않는다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Norm, centroid distance, cosine similarity, isolation score를 세 모델에 동일하게 적용한다. Ribosomal gene은 세 모델에서 class-level enrichment를 보이지만 개별 gene 합의는 약하고, mitochondrial enrichment도 Geneformer와 scGPT에 집중된다. Geneformer의 고-anomaly gene 삭제는 matched control보다 annotation을 더 악화시키지 않았고, covariate-adjusted outlier status도 ClinVar membership과 연관되지 않았다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
IFNG, CXCL9/10, HLA genes, endothelial activation markers가 embedding outlier인지 여부만으로 rejection 중요도를 주장하면 안 된다. Geometry audit은 model-specific representation 구조를 설명하는 보조 분석으로 두고, donor/center holdout, gene ablation, ClinVar·pathway annotation, perturbation evidence로 중요도를 독립 검증해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Geometric outliers
- Gene embedding audit
- Single-cell foundation model
- Geneformer
- scGPT
- scFoundation
- Downstream leverage
- Rejection marker validation
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Whalley, J. P. "Do Geometric Outliers Identify Important Genes in Single-Cell Foundation Models?" _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.22.733850](https://doi.org/10.64898/2026.06.22.733850).
