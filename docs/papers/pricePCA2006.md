# Principal components analysis corrects for stratification in genome-wide association studies

## 기본 정보

- Citation key: `pricePCA2006`
- Item type: journalArticle
- Authors: Alkes L. Price; Nick J. Patterson; Robert M. Plenge; Michael E. Weinblatt; Nancy A. Shadick; David Reich
- DOI: 10.1038/ng1847
- PMID: 16862161
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/16862161/)
- Source/date: Nature Genetics, 2006

## 1. 한 줄 요약

이 논문은 genome-wide genotype PCA로 ancestry-driven population stratification을 감지하고 association model에서 보정하는 방법을 제시했다.

## 2. 왜 중요한가

GWAS에서 case/control의 ancestry 차이는 allele frequency 차이를 disease association처럼 보이게 만들 수 있다. PCA covariate는 현대 GWAS의 기본 confounding control이다.

## 3. 분석에서 위치

LD-pruned genotype matrix에서 principal components를 계산하고, ancestry outlier를 제거하거나 association regression covariate로 포함한다.

## 4. 주의점

- PCA는 batch effect와 ancestry를 함께 잡을 수 있어 interpretation이 필요하다.
- Related individuals, long-range LD region, genotyping batch를 처리하지 않으면 PCs가 왜곡될 수 있다.
- Transplant 연구에서는 donor와 recipient ancestry를 따로 또는 함께 모델링할지 설계해야 한다.

## 5. Bibliography

Price, Alkes L., Nick J. Patterson, Robert M. Plenge, Michael E. Weinblatt, Nancy A. Shadick, and David Reich. "Principal components analysis corrects for stratification in genome-wide association studies." _Nature Genetics_, 2006. [https://doi.org/10.1038/ng1847](https://doi.org/10.1038/ng1847).
