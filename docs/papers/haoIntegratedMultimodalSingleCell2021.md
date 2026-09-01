---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Integrated analysis of multimodal single-cell data

## 기본 정보

- Citation key: `haoIntegratedMultimodalSingleCell2021`
- Item type: journalArticle
- Authors: Yuhan Hao; Stephanie Hao; Erica Andersen-Nissen; William M. Mauck III; Shiwei Zheng; Andrew Butler; Maddie J. Lee; Aaron J. Wilk; Charlotte Darby; Michael Zager; et al.
- DOI: 10.1016/j.cell.2021.04.048
- PMID: 34062119
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/34062119/)
- Source/date: Cell, 2021

## 1. 한 줄 요약

이 논문은 RNA, protein, chromatin 등 여러 single-cell modality를 weighted-nearest neighbor(WNN) 방식으로 통합해 cell state를 정의하는 Seurat v4 framework를 제안한다.

## 2. 왜 중요한가

scRNA-seq만으로는 immune phenotype이나 regulatory state를 충분히 설명하기 어렵다. WNN은 각 cell에서 modality별 정보량을 다르게 가중해 multimodal cell identity를 만들 수 있게 한다.

## 3. 분석에서 위치

CITE-seq, Multiome RNA+ATAC, perturb-seq처럼 같은 cell에서 여러 modality가 측정된 경우, modality별 neighbor graph를 만들고 WNN graph로 통합 clustering/UMAP/annotation을 수행한다.

## 4. 주의점

- Modality별 QC가 먼저 좋아야 WNN 가중치가 의미 있다.
- RNA와 protein/chromatin signal이 서로 다른 biological axis를 담을 때 해석을 분리해야 한다.
- Kidney transplant biopsy에서는 CITE-seq/spatial/scATAC가 있을 때 rejection-associated cell state를 더 정밀하게 정의하는 데 쓸 수 있다.

## 5. Bibliography

Hao, Yuhan, Stephanie Hao, Erica Andersen-Nissen, William M. Mauck III, Shiwei Zheng, Andrew Butler, Maddie J. Lee, Aaron J. Wilk, Charlotte Darby, Michael Zager, et al. "Integrated analysis of multimodal single-cell data." _Cell_, 2021. [https://doi.org/10.1016/j.cell.2021.04.048](https://doi.org/10.1016/j.cell.2021.04.048).
