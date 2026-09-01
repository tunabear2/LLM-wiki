---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Systematic benchmarking of zero-shot utility and robustness in single-cell transcriptomic foundation models

## 기본 정보

- Citation key: `liuSystematicBenchmarkingZeroShot2026`
- Item type: preprint
- Authors: T. Liu; T. Feng; X. Pan; Y. Chen; L. Ren; X. Ye; T. Sakurai; H. Lin; Y. Zhang
- DOI: 10.64898/2026.06.18.733285
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.18.733285v1)
- Source/date: bioRxiv, 2026-06-23

## Abstract

This paper benchmarks zero-shot single-cell transcriptomic representations across 20 methods, 6 downstream tasks, and 1,607 datasets comprising nearly 21.8 million cells. It reports that utility and robustness can decouple, no model is uniformly best across tasks, and classical highly variable gene representations remain competitive in several zero-shot settings.

## 1. 한 줄 요약

%% begin one-line-summary %%
20개 single-cell transcriptomic representation을 1,607개 dataset에서 비교해, scFM zero-shot 성능은 task별로 불안정하며 classical HVG 기반 representation도 여전히 경쟁적임을 보인 benchmark다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
scFM은 reusable representation으로 홍보되지만 fine-tuning 없이 바로 쓰는 상황에서는 utility와 robustness가 함께 좋아진다고 보장할 수 없다. 논문은 task, dataset structure, robustness shift를 분리해 평가하고 model selection decision framework를 제안한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Transplant rejection dataset에서 scFM embedding을 zero-shot feature로 쓸 때는 single-center accuracy보다 cross-center, protocol shift, rare immune state robustness가 중요하다. 이 benchmark는 scGPT/Geneformer류 embedding을 HVG PCA, pseudobulk, pathway score와 반드시 함께 비교해야 한다는 근거를 준다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Single-cell transcriptomic foundation model
- Zero-shot benchmark
- Robustness
- Highly variable genes
- Representation selection
- Cross-dataset transfer
- Rejection prediction
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Liu, T., T. Feng, X. Pan, Y. Chen, L. Ren, X. Ye, T. Sakurai, H. Lin, and Y. Zhang. "Systematic benchmarking of zero-shot utility and robustness in single-cell transcriptomic foundation models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.18.733285](https://doi.org/10.64898/2026.06.18.733285).
