---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# METAL: fast and efficient meta-analysis of genomewide association scans

## 기본 정보

- Citation key: `willerMETAL2010`
- Item type: journalArticle
- Authors: Cristen J. Willer; Yun Li; Goncalo R. Abecasis
- DOI: 10.1093/bioinformatics/btq340
- PMID: 20616382
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/20616382/)
- Source/date: Bioinformatics, 2010

## 1. 한 줄 요약

METAL은 여러 GWAS cohort의 summary statistics를 빠르게 meta-analysis하는 도구다.

## 2. 왜 중요한가

GWAS power는 sample size에 크게 의존하므로 cohort-level summary statistics를 합치는 meta-analysis가 핵심이다. METAL은 sample-size weighted 또는 inverse-variance 방식 meta-analysis를 실용적으로 수행한다.

## 3. 분석에서 위치

각 cohort에서 QC된 summary statistics를 allele alignment 후 meta-analysis하고, heterogeneity, direction, effective sample size를 확인한다.

## 4. 주의점

- Effect allele, non-effect allele, strand, genome build, allele frequency를 맞추지 않으면 방향이 뒤집힌다.
- Cohort overlap이 있으면 standard error와 P-value가 과도하게 좋아질 수 있다.
- Ancestry가 다른 cohort를 합칠 때 fixed-effect 해석과 heterogeneity를 함께 봐야 한다.

## 5. Bibliography

Willer, Cristen J., Yun Li, and Goncalo R. Abecasis. "METAL: fast and efficient meta-analysis of genomewide association scans." _Bioinformatics_, 2010. [https://doi.org/10.1093/bioinformatics/btq340](https://doi.org/10.1093/bioinformatics/btq340).
