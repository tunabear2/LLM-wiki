# Gene Expression Omnibus: NCBI gene expression and hybridization array data repository

## 기본 정보

- Citation key: `barrettGEO2002`
- Item type: journalArticle
- Authors: Tanya Barrett; Ron Edgar
- DOI: 10.1093/nar/30.1.207
- PMID: 11752295
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/11752295/)
- Source/date: Nucleic Acids Research, 2002

## 1. 한 줄 요약

GEO는 microarray와 high-throughput functional genomics data를 raw data, processed data, platform annotation, sample metadata와 함께 저장하는 public repository다.

## 2. 왜 중요한가

Public transplant microarray cohort 대부분은 GEO accession을 통해 찾고 재분석한다. GEO 구조를 이해하면 GSE, GSM, GPL, supplementary files, series matrix의 관계를 추적할 수 있다.

## 3. 분석에서 위치

Dataset discovery, metadata curation, raw CEL/IDAT 다운로드, platform annotation 확인, external validation cohort 구축에 사용한다.

## 4. 주의점

- Series matrix는 저자가 처리한 값이라 preprocessing이 dataset마다 다를 수 있다.
- GSM metadata의 label은 자유 텍스트라 phenotype harmonization이 필요하다.
- 같은 환자/샘플이 여러 GSE에 중복 deposit될 수 있어 sample deduplication을 확인해야 한다.

## 5. Bibliography

Barrett, Tanya, and Ron Edgar. "Gene Expression Omnibus: NCBI gene expression and hybridization array data repository." _Nucleic Acids Research_, 2002. [https://doi.org/10.1093/nar/30.1.207](https://doi.org/10.1093/nar/30.1.207).
