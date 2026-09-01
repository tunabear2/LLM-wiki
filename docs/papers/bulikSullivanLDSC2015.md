---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# LD Score regression distinguishes confounding from polygenicity in GWAS

## 기본 정보

- Citation key: `bulikSullivanLDSC2015`
- Item type: journalArticle
- Authors: Brendan K. Bulik-Sullivan; Po-Ru Loh; Hilary K. Finucane; Stephan Ripke; Jian Yang; Schizophrenia Working Group of the Psychiatric Genomics Consortium; Nick Patterson; Mark J. Daly; Alkes L. Price; Benjamin M. Neale
- DOI: 10.1038/ng.3211
- PMID: 25642630
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/25642630/)
- Source/date: Nature Genetics, 2015

## 1. 한 줄 요약

LD Score regression은 GWAS test statistic inflation이 polygenic signal 때문인지 confounding 때문인지 LD score와 chi-square statistic의 관계로 분리해 해석하는 방법이다.

## 2. 왜 중요한가

큰 GWAS에서는 QQ plot inflation이 항상 나쁜 것은 아니다. 많은 causal variants가 작은 효과를 가지면 polygenicity 때문에 inflation이 생긴다. LDSC는 summary statistics만으로 heritability, intercept, genetic correlation을 추정하는 post-GWAS 핵심 도구다.

## 3. 분석에서 위치

GWAS summary statistics QC 후 LD reference score와 결합해 LDSC intercept, SNP heritability, cross-trait genetic correlation을 계산한다.

## 4. 주의점

- LD reference panel은 ancestry에 맞아야 한다.
- LDSC intercept가 confounding의 전부를 완벽히 측정하는 것은 아니다.
- Sample size, trait prevalence, case/control imbalance, summary statistic QC가 추정에 영향을 준다.

## 5. Bibliography

Bulik-Sullivan, Brendan K., Po-Ru Loh, Hilary K. Finucane, Stephan Ripke, Jian Yang, Schizophrenia Working Group of the Psychiatric Genomics Consortium, Nick Patterson, Mark J. Daly, Alkes L. Price, and Benjamin M. Neale. "LD Score regression distinguishes confounding from polygenicity in genome-wide association studies." _Nature Genetics_, 2015. [https://doi.org/10.1038/ng.3211](https://doi.org/10.1038/ng.3211).
