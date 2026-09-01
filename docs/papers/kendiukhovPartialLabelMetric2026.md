---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Partial-label metric ceilings for evaluating gene regulatory networks inferred from single-cell foundation models

## 기본 정보

- Citation key: `kendiukhovPartialLabelMetric2026`
- Item type: journalArticle
- Authors: Ihor Kendiukhov
- DOI: 10.1016/j.biosystems.2026.105864
- PMID: [42379339](https://pubmed.ncbi.nlm.nih.gov/42379339/)
- URL: [Link](https://doi.org/10.1016/j.biosystems.2026.105864)
- Source/date: PubMed / BioSystems, 2026-06-30

## Abstract

This paper formalizes observed metric ceilings for gene regulatory network benchmarks when curated positive labels are incomplete. It reanalyzes 15 GRN inference methods, including scGPT-derived attention and gradient probes, across five references. The results show that single-cell foundation model probes can rank highly among tested methods, but still sit far below observable ceilings and only rarely exceed a random baseline after accounting for partial labels and study-biased missingness.

## 1. 한 줄 요약

%% begin one-line-summary %%
GRN benchmark reference가 incomplete하다는 점을 metric ceiling으로 보정해도 scGPT 기반 regulatory edge의 성능 gap은 크게 남아, single-cell foundation model GRN claim을 좁게 해석해야 한다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Curated TF-target reference는 모든 true edge를 담지 않기 때문에 observed F1/AUPR은 label coverage에 의해 ceiling이 생긴다. 논문은 MAR missingness와 study-biased missingness를 나누어 ceiling을 계산하고, scGPT attention/gradient probe와 classical GRN method의 benchmark score가 ceiling 대비 어느 정도인지 재평가한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Rejection-associated regulatory network를 평가할 때 TRRUST, DoRothEA, pathway database만 ground truth로 쓰면 literature-biased gene에 score가 몰릴 수 있다. Kidney transplant 분석에서는 Banff-relevant pathway, immune/endothelial marker, external cohort perturbation evidence를 나누고, AUPR 자체보다 coverage-normalized score와 random baseline 대비 개선을 같이 보고해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Gene regulatory network benchmark
- Partial labels
- Metric ceiling
- scGPT
- Single-cell foundation model
- AUPR
- Literature bias
- Rejection regulatory network
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 PubMed metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Kendiukhov, Ihor. "Partial-label metric ceilings for evaluating gene regulatory networks inferred from single-cell foundation models." _BioSystems_, 2026. [https://doi.org/10.1016/j.biosystems.2026.105864](https://doi.org/10.1016/j.biosystems.2026.105864).
