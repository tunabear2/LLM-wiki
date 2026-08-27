---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-17'
tags:
- wiki/paper
---

# Systematic evaluation of single-cell foundation model interpretability: attention-derived edge scores add no incremental value over gene-level features for perturbation-target prediction

## 기본 정보

- Citation key: `kendiukhovSystematicEvaluationSingleCell2026`
- Item type: journalArticle
- Authors: Ihor Kendiukhov
- DOI: 10.1186/s12864-026-12965-8
- PMID: 42482180
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42482180/)
- Source/date: PubMed / BMC Genomics, published and indexed 2026-07-22

## 1. 한 줄 요약

scGPT와 Geneformer attention은 일부 curated GRN 구조를 담지만, CRISPR perturbation target prediction에서는 단순 gene-level 통계 이상의 추가 예측력을 보이지 않는다.

## 2. 왜 중요한가

두 architecture, 네 cell type, CRISPRi·CRISPRa를 대상으로 37개 분석과 153개 검정을 수행한다. Cell-state stratification은 curated GRN recovery를 개선하지만, perturbation outcome에서는 variance·mean expression·dropout rate baseline이 attention·correlation edge보다 강하며 attention-head ablation도 성능 저하를 만들지 않았다.

## 3. 내 연구에 연결할 점

Rejection biopsy에서 attention-derived TF–target edge를 기전으로 보고하기 전에 expression baseline, incremental-value test, ablation을 요구해야 한다. Attention은 rejection regulatory hypothesis 생성에는 쓸 수 있지만 CRISPR나 독립 cohort 검증 없이 causal biomarker로 해석하면 안 된다.

## 4. Bibliography

Kendiukhov, Ihor. "Systematic evaluation of single-cell foundation model interpretability: attention-derived edge scores add no incremental value over gene-level features for perturbation-target prediction." _BMC Genomics_, 2026. [https://doi.org/10.1186/s12864-026-12965-8](https://doi.org/10.1186/s12864-026-12965-8).
