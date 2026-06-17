# SAM: significance analysis of microarrays

## 기본 정보

- Citation key: `tusherSAM2001`
- Item type: journalArticle
- Authors: Virginia G. Tusher; Robert Tibshirani; Gilbert Chu
- DOI: 10.1073/pnas.091062498
- PMID: 11309499
- URL: [Link](https://www.pnas.org/doi/10.1073/pnas.091062498)
- Source/date: PNAS, 2001

## 1. 한 줄 요약

SAM은 microarray expression에서 gene별 변화 score를 계산하고 permutation으로 false discovery rate를 추정해 significant gene을 고르는 방법이다.

## 2. 왜 중요한가

Microarray 초창기 high-dimensional DEG 분석에서 multiple testing과 FDR을 실용적으로 다루는 대표 방법이었다. 현대 limma/DESeq2를 이해할 때도 "수천 개 gene을 동시에 테스트한다"는 통계적 문제의 출발점으로 유용하다.

## 3. 분석에서 위치

Normalized expression matrix와 class label을 입력으로 gene별 score, delta threshold, estimated FDR을 계산한다.

## 4. 주의점

- Permutation 기반이라 sample size와 label balance에 민감하다.
- 복잡한 design, covariate, paired sample 처리에는 limma 같은 linear model이 더 자연스럽다.
- 결과 gene list만 보지 말고 effect size와 validation cohort 재현성을 확인해야 한다.

## 5. Bibliography

Tusher, Virginia G., Robert Tibshirani, and Gilbert Chu. "Significance analysis of microarrays applied to the ionizing radiation response." _Proceedings of the National Academy of Sciences_, 2001. [https://doi.org/10.1073/pnas.091062498](https://doi.org/10.1073/pnas.091062498).
