# Pooling across cells to normalize single-cell RNA sequencing data with many zero counts

## 기본 정보

- Citation key: `lunPoolingNormalizeSingleCell2016`
- Item type: journalArticle
- Authors: Aaron T. L. Lun; Karsten Bach; John C. Marioni
- DOI: 10.1186/s13059-016-0947-7
- PMID: 27122128
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/27122128/)
- Source/date: Genome Biology, 2016

## 1. 한 줄 요약

이 논문은 sparse scRNA-seq count에서 cell-specific size factor를 안정적으로 추정하기 위해 cell pools를 만들고 deconvolution하는 normalization 방법을 제안한다.

## 2. 왜 중요한가

Single-cell count는 zero가 많고 cell마다 capture efficiency가 달라 단순 library-size normalization이 불안정할 수 있다. scran deconvolution normalization은 scRNA-seq 기본 전처리의 중요한 고전 방법이다.

## 3. 분석에서 위치

QC와 cell filtering 후 clustering 또는 rough grouping을 만들고, pool-based size factor를 deconvolve해 cell-level normalized expression을 얻는다. 이후 HVG selection, PCA, clustering, marker detection으로 이어진다.

## 4. 주의점

- 너무 이질적인 cell type을 한 번에 normalize하면 composition effect가 남을 수 있다.
- UMI droplet data와 full-length protocol에서 count distribution이 다르므로 normalization 결과를 QC plot으로 확인해야 한다.
- 환자 단위 pseudobulk DE에는 cell-level normalized value보다 raw count aggregation 후 bulk-style normalization을 쓰는 편이 더 자연스럽다.

## 5. Bibliography

Lun, Aaron T. L., Karsten Bach, and John C. Marioni. "Pooling across cells to normalize single-cell RNA sequencing data with many zero counts." _Genome Biology_, 2016. [https://doi.org/10.1186/s13059-016-0947-7](https://doi.org/10.1186/s13059-016-0947-7).
