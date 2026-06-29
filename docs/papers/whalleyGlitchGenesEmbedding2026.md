# Glitch genes: embedding geometry predicts functional fragility in single-cell foundation models

## 기본 정보

- Citation key: `whalleyGlitchGenesEmbedding2026`
- Item type: preprint
- Authors: J. P. Whalley
- DOI: 10.64898/2026.06.22.733850
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.22.733850v1)
- Source/date: bioRxiv, 2026-06-27

## Abstract

This paper introduces a weight-only geometric audit for gene embeddings in single-cell foundation models. It scores genes by embedding norm, centroid distance, cosine similarity, and isolation, then applies the audit to Geneformer, scGPT, and scFoundation. The analysis reports outlier enrichment for loss-of-function intolerance and disease association in discrete-tokenization models, and links embedding anomaly to perturbation sensitivity.

## 1. 한 줄 요약

%% begin one-line-summary %%
Glitch genes는 Geneformer, scGPT, scFoundation의 gene embedding geometry만으로 representational outlier를 찾아 downstream perturbation 해석에서 취약할 수 있는 gene을 표시하는 audit 방법이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
scFM의 gene embedding은 downstream perturbation prediction과 GRN inference의 기반이지만, embedding matrix 자체를 사전 점검하는 경우가 드물다. 논문은 norm, centroid distance, cosine similarity, isolation score로 outlier gene을 찾고, tokenization strategy가 어떤 gene을 불안정하게 표현하는지 비교한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Rejection marker나 perturbation 후보 gene을 scGPT/Geneformer attribution으로 고를 때 embedding outlier가 과도한 중요도로 보일 수 있다. IFNG, CXCL9/10, HLA genes, endothelial activation markers처럼 임상적으로 중요한 gene에 대해 embedding audit을 먼저 수행하면 false mechanistic claim을 줄일 수 있다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Glitch genes
- Gene embedding audit
- Single-cell foundation model
- Geneformer
- scGPT
- scFoundation
- Perturbation sensitivity
- Rejection marker validation
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Whalley, J. P. "Glitch genes: embedding geometry predicts functional fragility in single-cell foundation models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.22.733850](https://doi.org/10.64898/2026.06.22.733850).
