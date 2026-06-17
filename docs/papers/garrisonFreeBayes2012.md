# FreeBayes: haplotype-based variant detection from short-read sequencing

## 기본 정보

- Citation key: `garrisonFreeBayes2012`
- Item type: preprint
- Authors: Erik Garrison; Gabor Marth
- DOI: 없음 또는 확인 필요
- arXiv: 1207.3907
- URL: [Link](https://arxiv.org/abs/1207.3907)
- Source/date: arXiv, 2012

## 1. 한 줄 요약

FreeBayes는 short-read sequencing data에서 haplotype을 직접 모델링해 SNP, indel, complex variant를 Bayesian framework로 calling하는 도구다.

## 2. 왜 중요한가

GATK 외의 대표적인 small variant caller로, population/cohort 또는 non-diploid sample에서도 flexible하게 사용할 수 있다. Variant caller별 assumption과 output 차이를 비교하는 데 좋은 기준점이다.

## 3. 분석에서 위치

Sorted/indexed BAM과 reference genome을 입력으로 받아 VCF를 생성한다. 이후 quality filtering, normalization, decomposition, annotation을 거친다.

## 4. 주의점

- Caller별 genotype likelihood, allele balance, complex allele representation이 다르므로 VCF normalization이 중요하다.
- GATK HaplotypeCaller와 결과가 다를 때 read-level evidence를 IGV로 확인해야 한다.
- Clinical-grade germline calling에는 validated pipeline과 benchmark truth set 비교가 필요하다.

## 5. Bibliography

Garrison, Erik, and Gabor Marth. "Haplotype-based variant detection from short-read sequencing." _arXiv_, 2012. [https://arxiv.org/abs/1207.3907](https://arxiv.org/abs/1207.3907).
