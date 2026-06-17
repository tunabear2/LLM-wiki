# ComBat: adjusting batch effects in microarray expression data using empirical Bayes methods

## 기본 정보

- Citation key: `johnsonComBat2007`
- Item type: journalArticle
- Authors: W. Evan Johnson; Cheng Li; Ariel Rabinovic
- DOI: 10.1093/biostatistics/kxj037
- PMID: 16632515
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/16632515/)
- Source/date: Biostatistics, 2007

## 1. 한 줄 요약

ComBat은 microarray expression data에서 batch별 location/scale effect를 empirical Bayes 방식으로 추정해 보정하는 방법이다.

## 2. 왜 중요한가

Public microarray cohort를 합치면 lab, date, scanner, platform, preprocessing 차이가 disease signal보다 커질 수 있다. ComBat은 small batch에서도 안정적인 batch correction을 제공해 multi-cohort analysis의 기본 도구가 되었다.

## 3. 분석에서 위치

Log-expression matrix, batch label, biological covariate design을 입력으로 batch-adjusted expression matrix를 만든다. 이후 clustering, classifier training, DEG analysis 등에 사용한다.

## 4. 주의점

- Batch와 phenotype이 완전히 confounded되어 있으면 ComBat이 biological signal까지 제거하거나 artifact를 만들 수 있다.
- Train/test split 밖에서 ComBat을 fit하면 external validation leakage가 생길 수 있다.
- 보정 전후 PCA, density plot, label separation을 함께 확인해야 한다.

## 5. Bibliography

Johnson, W. Evan, Cheng Li, and Ariel Rabinovic. "Adjusting batch effects in microarray expression data using empirical Bayes methods." _Biostatistics_, 2007. [https://doi.org/10.1093/biostatistics/kxj037](https://doi.org/10.1093/biostatistics/kxj037).
