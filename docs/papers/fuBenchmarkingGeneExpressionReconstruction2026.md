# Benchmarking gene expression reconstruction from single-cell latent representations

## 기본 정보

- Citation key: `fuBenchmarkingGeneExpressionReconstruction2026`
- Item type: preprint
- Authors: X. Fu; D. Klein; E. Antipov; A. Palma; A. Tejada-Lapuerta; M. Bahrami; L. B. Kummerle; M. Lubetzki; F. P. Casale; M. D. Luecken; F. J. Theis
- DOI: 10.64898/2026.06.15.731445
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.15.731445v1)
- Source/date: bioRxiv, 2026-06-18

## Abstract

Low-dimensional single-cell latent representations are widely used for integration, cell-state discovery, perturbation prediction, and virtual cell models, but downstream biological interpretation often requires reconstructing gene expression from latent space. This paper introduces ReconEval to benchmark reconstruction from end-to-end and foundation-model-derived latent representations.

## 1. 한 줄 요약

%% begin one-line-summary %%
ReconEval은 PCA/autoencoder류 latent와 single-cell foundation model embedding에서 gene expression을 얼마나 충실히 복원할 수 있는지 체계적으로 평가하는 benchmark다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Latent space에서 batch correction, perturbation prediction, virtual cell simulation을 하더라도 최종 해석은 gene-level expression으로 돌아가야 한다. 논문은 representation 선택을 단순 구현 세부사항이 아니라 reconstruction faithfulness를 좌우하는 핵심 모델링 결정으로 보고, latent-to-expression decoder 평가 기준을 제안한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Rejection biopsy scFM embedding으로 predicted perturbed state나 corrected cell state를 만들 경우, DEG/pathway 해석은 decoder 품질에 의존한다. ReconEval식 평가를 적용해 rejection marker, IFN pathway, endothelial activation gene이 latent reconstruction에서 보존되는지 확인해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- ReconEval
- Single-cell latent representation
- Foundation model embedding
- Gene expression reconstruction
- Virtual cell
- Perturbation prediction
- Batch correction
- Rejection marker preservation
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Fu, X., D. Klein, E. Antipov, A. Palma, A. Tejada-Lapuerta, M. Bahrami, L. B. Kummerle, et al. "Benchmarking gene expression reconstruction from single-cell latent representations." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.15.731445](https://doi.org/10.64898/2026.06.15.731445).

