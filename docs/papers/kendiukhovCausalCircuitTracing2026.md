---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Causal circuit tracing reveals distinct computational architectures in single-cell foundation models

## 기본 정보

- Citation key: `kendiukhovCausalCircuitTracing2026`
- Item type: journalArticle
- Authors: Ihor Kendiukhov
- DOI: 10.1093/bioinformatics/btag379
- PMID: 42296381
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42296381/)
- Source/date: PubMed / Bioinformatics, 2026-06 watch window

## Abstract

Sparse autoencoders can decompose single-cell foundation model activations into interpretable features, but the causal interactions among those internal features are less clear. This paper uses feature ablation-based circuit tracing in Geneformer V2-316M and scGPT whole-human to compare model-internal computational architecture, biological coherence, inhibitory dominance, cross-model convergence, and agreement with CRISPRi perturbation evidence.

## 1. 한 줄 요약

%% begin one-line-summary %%
Geneformer와 scGPT 내부 SAE feature를 ablation해 model-internal circuit을 추적하고, 두 scFM이 생물학적 coherence는 일부 갖지만 causal regulatory encoding은 제한적임을 보인 해석 연구다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
논문은 single-cell foundation model embedding을 성능 지표로만 보지 않고, 모델 내부 activation feature 사이의 인과적 영향 관계를 직접 perturbation한다. Geneformer와 scGPT에서 공통적으로 inhibitory interaction이 우세하고, 일부 cross-model consensus feature pair가 disease-associated domain과 연결되지만, CRISPRi validation과의 방향 일치는 제한적이라고 해석한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서 scGPT/Geneformer attribution이나 attention을 marker discovery에 사용할 때, 모델 내부 회로가 실제 생물학적 causal regulation을 그대로 담는다고 가정하면 위험하다. Rejection-associated T cell, monocyte, endothelial state에서 후보 gene을 뽑더라도 CRISPR perturbation, external cohort, DEG/GRN evidence로 별도 검증해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Single-cell foundation model
- Geneformer
- scGPT
- Sparse autoencoder
- Mechanistic interpretability
- Circuit tracing
- CRISPRi
- Transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 PubMed abstract와 arXiv 검색 metadata를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Kendiukhov, Ihor. "Causal circuit tracing reveals distinct computational architectures in single-cell foundation models: inhibitory dominance, biological coherence, and cross-model convergence." _Bioinformatics_, 2026. [https://doi.org/10.1093/bioinformatics/btag379](https://doi.org/10.1093/bioinformatics/btag379).

