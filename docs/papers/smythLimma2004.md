---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# limma: linear models and empirical Bayes methods for microarray experiments

## 기본 정보

- Citation key: `smythLimma2004`
- Item type: journalArticle
- Authors: Gordon K. Smyth
- DOI: 10.2202/1544-6115.1027
- PMID: 16646809
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/16646809/)
- Source/date: Statistical Applications in Genetics and Molecular Biology, 2004

## 1. 한 줄 요약

limma는 microarray expression data에 linear model과 empirical Bayes variance moderation을 적용해 안정적인 differential expression statistics를 계산한다.

## 2. 왜 중요한가

Microarray DEG 분석의 표준 도구다. 샘플 수가 적은 실험에서 gene-wise variance를 서로 빌려 안정화하는 moderated t/F statistic이 핵심이다.

## 3. 분석에서 위치

Normalized log-expression matrix와 sample metadata를 입력으로 design matrix와 contrast를 만들고, `lmFit`, `eBayes`, `topTable`로 DEG table을 생성한다.

## 4. 주의점

- Design matrix에 batch, pairing, center, clinical covariate를 명시하지 않으면 confounding이 DEG로 나타날 수 있다.
- Probe-level matrix에서 gene-level로 collapse할지, probe set을 그대로 쓸지 분석 목적에 맞게 정해야 한다.
- RNA-seq에 쓸 때는 voom 또는 limma-trend 등 count-specific mean-variance 처리가 필요하다.

## 5. Bibliography

Smyth, Gordon K. "Linear models and empirical Bayes methods for assessing differential expression in microarray experiments." _Statistical Applications in Genetics and Molecular Biology_, 2004. [https://doi.org/10.2202/1544-6115.1027](https://doi.org/10.2202/1544-6115.1027).
