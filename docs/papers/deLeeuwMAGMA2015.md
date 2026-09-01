---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# MAGMA: generalized gene-set analysis of GWAS data

## 기본 정보

- Citation key: `deLeeuwMAGMA2015`
- Item type: journalArticle
- Authors: Christiaan A. de Leeuw; Joris M. Mooij; Tom Heskes; Danielle Posthuma
- DOI: 10.1371/journal.pcbi.1004219
- PMID: 25885710
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/25885710/)
- Source/date: PLOS Computational Biology, 2015

## 1. 한 줄 요약

MAGMA는 SNP-level GWAS result를 gene-level statistic과 gene-set/pathway association으로 요약하는 framework다.

## 2. 왜 중요한가

GWAS hit은 대부분 noncoding SNP이며 effect size가 작다. MAGMA는 LD와 gene size를 고려해 SNP signal을 gene/pathway 단위로 올려 biological interpretation을 돕는다.

## 3. 분석에서 위치

GWAS summary statistics, SNP-to-gene mapping, LD reference를 입력으로 gene analysis와 gene-set analysis를 수행한다.

## 4. 주의점

- SNP-to-gene window 선택과 LD reference ancestry가 결과에 영향을 준다.
- Gene-set enrichment는 causal pathway 증명이 아니라 signal aggregation hypothesis다.
- Transcriptomics와 연결할 때는 cell-type expression, eQTL, colocalization을 별도 분석으로 확인해야 한다.

## 5. Bibliography

de Leeuw, Christiaan A., Joris M. Mooij, Tom Heskes, and Danielle Posthuma. "MAGMA: generalized gene-set analysis of GWAS data." _PLOS Computational Biology_, 2015. [https://doi.org/10.1371/journal.pcbi.1004219](https://doi.org/10.1371/journal.pcbi.1004219).
