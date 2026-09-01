---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# PLINK: a tool set for whole-genome association and population-based linkage analyses

## 기본 정보

- Citation key: `purcellPLINK2007`
- Item type: journalArticle
- Authors: Shaun Purcell; Benjamin Neale; Kathe Todd-Brown; Lori Thomas; Manuel A. R. Ferreira; David Bender; Julian Maller; Pamela Sklar; Paul I. W. de Bakker; Mark J. Daly; Pak C. Sham
- DOI: 10.1086/519795
- PMID: 17701901
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/17701901/)
- Source/date: American Journal of Human Genetics, 2007

## 1. 한 줄 요약

PLINK는 large-scale genotype data management, QC, association testing, population structure analysis, IBD estimation을 제공하는 GWAS 기본 toolset이다.

## 2. 왜 중요한가

GWAS를 처음 배울 때 가장 많이 만나는 command-line 도구다. Binary genotype format, sample/SNP filtering, allele frequency, missingness, association test, clumping 같은 기본 작업을 빠르게 수행한다.

## 3. 분석에서 위치

Raw genotype call에서 sample/SNP QC를 수행하고, ancestry PCA 준비, association test, LD clumping, summary statistics export에 사용한다.

## 4. 주의점

- Allele coding, strand flip, genome build mismatch를 제대로 처리하지 않으면 meta-analysis와 imputation에서 큰 오류가 생긴다.
- Relatedness와 ancestry outlier filtering 기준을 분석 전에 명시해야 한다.
- PLINK result는 QC 로그와 함께 보관해야 재현 가능하다.

## 5. Bibliography

Purcell, Shaun, Benjamin Neale, Kathe Todd-Brown, Lori Thomas, Manuel A. R. Ferreira, David Bender, Julian Maller, Pamela Sklar, Paul I. W. de Bakker, Mark J. Daly, and Pak C. Sham. "PLINK: a tool set for whole-genome association and population-based linkage analyses." _American Journal of Human Genetics_, 2007. [https://doi.org/10.1086/519795](https://doi.org/10.1086/519795).
