---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# VCBench: A Multi-Dimensional Benchmark for Single-Cell Foundation Models

## 기본 정보

- Citation key: `weidenerVCBenchMultiDimensional2026`
- Item type: preprint
- Authors: L. S. Weidener; M. Brkic; M. Jovanovic; E. Ulgac; A. Meduri
- DOI: 10.64898/2026.06.18.733146
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.18.733146v1)
- Source/date: bioRxiv, 2026-06-23

## Abstract

VCBench is a multi-dimensional benchmark for single-cell foundation models as virtual cells. It evaluates capability dimensions including perturbation response prediction, cross-species universality, GRN inference, modality integration, temporal dynamics, multi-scale integration, and in silico experimentation, and compares Geneformer, scGPT, UCE, TranscriptFormer, and Arc State against linear and nearest-neighbor baselines.

## 1. 한 줄 요약

%% begin one-line-summary %%
VCBench는 virtual cell 관점에서 scFM을 7개 capability dimension으로 평가하고, 여러 차원에서 단순 baseline이 foundation model과 비슷하거나 더 좋을 수 있음을 보인다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Single-task benchmark는 scFM이 어디서 실제로 baseline을 넘는지 가리기 쉽다. VCBench는 perturbation, cross-species, GRN, modality, temporal 등 capability를 나눠 pre-registered baseline과 비교하고, training manifest 부재로 인한 contamination reporting 문제도 별도 schema로 다룬다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Rejection 연구에서 scFM을 virtual cell처럼 쓰려면 perturbation response, modality integration, temporal progression, cross-cohort transfer를 분리 평가해야 한다. VCBench의 capability rubric은 transplant cohort에서 어떤 claim을 할 수 있고 어떤 claim은 아직 end-to-end로 test 불가능한지 정리하는 체크리스트가 된다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- VCBench
- Virtual cell
- Single-cell foundation model benchmark
- Geneformer
- scGPT
- UCE
- TranscriptFormer
- Contamination reporting
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Weidener, L. S., M. Brkic, M. Jovanovic, E. Ulgac, and A. Meduri. "VCBench: A Multi-Dimensional Benchmark for Single-Cell Foundation Models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.18.733146](https://doi.org/10.64898/2026.06.18.733146).
