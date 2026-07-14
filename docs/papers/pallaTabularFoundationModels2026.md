# Tabular Foundation Models Are Competitive Cellular Perturbation Predictors Across Biological Scales

## 기본 정보

- Citation key: `pallaTabularFoundationModels2026`
- Item type: preprint
- Authors: G. Palla, A. Hillsley, Y.-J. Kim, and L. A. Royer
- DOI: 10.64898/2026.06.28.735106
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.28.735106v2)
- Source/date: bioRxiv revised v2, 2026-07-02

## Abstract

This paper evaluates general-purpose tabular foundation models such as TabICL and TabPFN against specialized cellular perturbation models, including PRESAGE, scGPT, scLAMBDA, STACK, and Prophet. It covers cell-level cross-cell-type prediction, pseudobulk Perturb-seq prediction, a genome-wide CRISPR screen in primary human CD4+ T cells, and embryo-level cell-type composition prediction. The main claim is that tabular in-context learning is competitive with, and often stronger than, bespoke single-cell perturbation models across several biological scales.

## 1. 한 줄 요약

%% begin one-line-summary %%
Tabular foundation model이 여러 perturbation prediction setting에서 scGPT, STACK 같은 domain-specific single-cell model과 비슷하거나 더 좋은 성능을 보일 수 있음을 보인 benchmark 논문이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Single-cell perturbation response prediction에서 복잡한 biological architecture가 항상 이득을 주는지 직접 비교한다. 논문은 cell-level, pseudobulk, primary T cell CRISPR screen, zebrafish embryo atlas를 포함한 여러 scale에서 general tabular FM과 specialized scFM/perturbation model을 같은 evaluation frame에 놓는다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection perturbation simulation이나 therapy response prediction을 할 때 scGPT/STACK 계열만 baseline으로 두면 과대평가 위험이 있다. TabPFN/TabICL, CatBoost, linear model, pathway-score model을 같은 split에서 비교해 scFM embedding의 실질적 추가 가치를 확인해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Tabular foundation model
- Single-cell perturbation prediction
- scGPT
- STACK
- Perturb-seq
- Primary human CD4+ T cells
- Kidney transplant rejection baseline
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Palla, G., A. Hillsley, Y.-J. Kim, and L. A. Royer. "Tabular Foundation Models Are Competitive Cellular Perturbation Predictors Across Biological Scales." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.28.735106](https://doi.org/10.64898/2026.06.28.735106).
