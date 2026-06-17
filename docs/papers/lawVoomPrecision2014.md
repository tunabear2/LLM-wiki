# voom: precision weights unlock linear model analysis tools for RNA-seq read counts

## 기본 정보

- Citation key: `lawVoomPrecision2014`
- Item type: journalArticle
- Authors: Charity W. Law; Yunshun Chen; Wei Shi; Gordon K. Smyth
- DOI: 10.1186/gb-2014-15-2-r29
- PMID: 24485249
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/24485249/)
- Source/date: Genome Biology, 2014

## 1. 한 줄 요약

voom은 RNA-seq log-count의 mean-variance trend를 추정해 observation-level precision weight를 만들고, 이를 limma linear model에 넣는 방법이다.

## 2. 왜 중요한가

복잡한 experimental design, covariate, batch, paired design을 다룰 때 limma 생태계의 안정적인 linear modeling 도구를 RNA-seq count에 적용할 수 있게 한다. Bulk RNA-seq와 pseudobulk scRNA-seq 분석에서 널리 쓰이는 baseline이다.

## 3. 분석에서 위치

Count matrix를 TMM 등으로 normalization한 뒤 `voom`으로 precision weight를 계산하고, `lmFit`/`eBayes` 또는 `duplicateCorrelation` 같은 limma workflow에 연결한다.

## 4. 주의점

- Low-count gene filtering을 먼저 해야 mean-variance trend가 안정적이다.
- voom 결과는 logCPM 기반 모델이므로 raw count NB model인 DESeq2/edgeR와 가정이 다르다.
- 환자 반복 측정이나 batch가 있으면 design matrix와 correlation structure를 명확히 써야 한다.

## 5. Bibliography

Law, Charity W., Yunshun Chen, Wei Shi, and Gordon K. Smyth. "voom: precision weights unlock linear model analysis tools for RNA-seq read counts." _Genome Biology_, 2014. [https://doi.org/10.1186/gb-2014-15-2-r29](https://doi.org/10.1186/gb-2014-15-2-r29).
