# RMA: exploration, normalization, and summaries of high density oligonucleotide array probe level data

## 기본 정보

- Citation key: `irizarryRMA2003`
- Item type: journalArticle
- Authors: Rafael A. Irizarry; Bridget Hobbs; Francois Collin; Yasmin D. Beazer-Barclay; Kristen J. Antonellis; Uwe Scherf; Terence P. Speed
- DOI: 10.1093/biostatistics/4.2.249
- PMID: 12925520
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/12925520/)
- Source/date: Biostatistics, 2003

## 1. 한 줄 요약

RMA는 Affymetrix probe-level intensity에 background correction, quantile normalization, robust summarization을 적용해 expression measure를 만드는 방법이다.

## 2. 왜 중요한가

Microarray raw CEL 파일을 sample 간 비교 가능한 log2 expression matrix로 바꾸는 고전적 표준이다. Public Affymetrix cohort를 직접 재처리할 때 RMA가 무엇을 하는지 알아야 한다.

## 3. 분석에서 위치

Raw CEL 파일에서 probe set expression matrix를 만들고, 이후 probe annotation, gene-level collapse, limma differential expression, classifier training으로 이어진다.

## 4. 주의점

- RMA output은 platform-specific probe set 단위이므로 gene symbol 변환과 multiple-probe handling이 필요하다.
- Quantile normalization은 전체 분포를 같게 만들기 때문에 global biological shifts를 약화할 수 있다.
- 서로 다른 array platform을 직접 RMA 후 결합하는 것은 위험하며, platform별 처리와 batch correction을 분리해야 한다.

## 5. Bibliography

Irizarry, Rafael A., Bridget Hobbs, Francois Collin, Yasmin D. Beazer-Barclay, Kristen J. Antonellis, Uwe Scherf, and Terence P. Speed. "Exploration, normalization, and summaries of high density oligonucleotide array probe level data." _Biostatistics_, 2003. [https://doi.org/10.1093/biostatistics/4.2.249](https://doi.org/10.1093/biostatistics/4.2.249).
