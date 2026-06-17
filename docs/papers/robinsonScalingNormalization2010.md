# A scaling normalization method for differential expression analysis of RNA-seq data

## 기본 정보

- Citation key: `robinsonScalingNormalization2010`
- Item type: journalArticle
- Authors: Mark D. Robinson; Alicia Oshlack
- DOI: 10.1186/gb-2010-11-3-r25
- PMID: 20196867
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/20196867/)
- Source/date: Genome Biology, 2010

## 1. 한 줄 요약

이 논문은 RNA composition bias를 보정하기 위한 TMM(trimmed mean of M-values) normalization을 제안한다.

## 2. 왜 중요한가

RNA-seq count는 library size만 맞추면 비교 가능해지는 것이 아니다. 일부 gene이 한 조건에서 크게 올라가면 전체 count composition이 바뀌어 나머지 gene의 상대 abundance가 왜곡된다. TMM은 이런 composition bias를 robust하게 줄이는 대표 normalization이다.

## 3. 분석에서 위치

edgeR의 `calcNormFactors(method = "TMM")`로 가장 흔히 사용된다. Bulk RNA-seq뿐 아니라 pseudobulk scRNA-seq differential expression에서도 sample-level count matrix에 적용할 수 있다.

## 4. 주의점

- TMM은 대부분 gene이 DE가 아니라는 가정을 암묵적으로 둔다.
- Cell type composition이 크게 다른 biopsy bulk에서는 normalization만으로 biological mixture 차이가 사라지지 않는다.
- TPM/CPM visualization과 DE model input normalization을 구분해서 기록해야 한다.

## 5. Bibliography

Robinson, Mark D., and Alicia Oshlack. "A scaling normalization method for differential expression analysis of RNA-seq data." _Genome Biology_, 2010. [https://doi.org/10.1186/gb-2010-11-3-r25](https://doi.org/10.1186/gb-2010-11-3-r25).
