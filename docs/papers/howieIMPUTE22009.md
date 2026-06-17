# IMPUTE2: flexible and accurate genotype imputation for next-generation GWAS

## 기본 정보

- Citation key: `howieIMPUTE22009`
- Item type: journalArticle
- Authors: Bryan N. Howie; Peter Donnelly; Jonathan Marchini
- DOI: 10.1371/journal.pgen.1000529
- PMID: 19543373
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/19543373/)
- Source/date: PLOS Genetics, 2009

## 1. 한 줄 요약

IMPUTE2는 typed genotype과 reference haplotype panel을 결합해 untyped variants의 genotype dosage를 추정하는 flexible imputation method다.

## 2. 왜 중요한가

GWAS array는 genome의 일부 SNP만 직접 측정한다. Imputation은 reference panel을 이용해 variant density를 높여 power, fine mapping, cross-study meta-analysis를 개선한다.

## 3. 분석에서 위치

Pre-phasing 또는 imputation 전 QC 후 reference panel에 맞춰 strand/build를 정렬하고, imputed dosage와 INFO/R2 quality metric을 얻는다. 이후 dosage-based association test에 사용한다.

## 4. 주의점

- Reference panel ancestry가 study cohort와 맞지 않으면 imputation accuracy가 떨어진다.
- Palindromic SNP, strand flip, genome build mismatch는 반드시 QC해야 한다.
- Imputed variants는 hard call보다 dosage와 uncertainty metric을 함께 다루는 것이 좋다.

## 5. Bibliography

Howie, Bryan N., Peter Donnelly, and Jonathan Marchini. "A flexible and accurate genotype imputation method for the next generation of genome-wide association studies." _PLOS Genetics_, 2009. [https://doi.org/10.1371/journal.pgen.1000529](https://doi.org/10.1371/journal.pgen.1000529).
