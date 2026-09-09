---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# cellGeometry: ultra-fast single-cell deconvolution of bulk RNA-Seq using a geometric solution

## 기본 정보

- Citation key: lauCellGeometryUltraFast2026
- Item type: journalArticle
- Authors: Rachel Lau; Cankut Çubuk; Athina Spiliopoulou; Pedro Martínez-Paz; Anna E. A. Surace; Liliane Fossati-Jimack; Soumya Raychaudhuri; Costantino Pitzalis; Myles J. Lewis
- Journal: Nature Communications
- DOI: 10.1038/s41467-026-75762-7
- PMID: 42642367
- URL: [Publisher](https://www.nature.com/articles/s41467-026-75762-7); [PubMed](https://pubmed.ncbi.nlm.nih.gov/42642367/)
- Source/date: published 2026-07-23; PubMed completed/indexed 2026-08-25–26
- 주 카테고리: Bulk RNA-seq
- 교차 카테고리: scRNA-seq

## 1. 한 줄 요약

cellGeometry는 single-cell reference의 cell-type vector projection과 non-negative matrix regularization으로 bulk RNA-seq 세포 조성을 빠르게 추정하는 R package다.

## 2. 연구 질문

수백만 cell 규모의 atlas를 reference로 사용하면서도 기존 deconvolution보다 계산량을 크게 줄이고 실제 조직의 세포 조성을 유지할 수 있는가?

## 3. 데이터와 방법

300만 개 이상의 simulated single-cell reference, Tabula Sapiens, Human Brain Cell Atlas, 류마티스관절염 활막과 혈액·조직 bulk RNA-seq를 사용했다. Cell-specific gene을 고차원 기하에서 선택하고 bulk vector를 signature에 투영한 뒤 non-negative regularization으로 fraction을 추정했다.

## 4. 핵심 결과

5,000개 sample 실험에서 저자 보고 기준 DWLS보다 약 1,600배 빨랐고 대규모 atlas에서도 MuSiC·DWLS보다 빠르게 실행됐다. 류마티스 활막에서 macrophage, T cell, B cell, plasmablast 추정치는 독립 immunohistology 측정과 유의하게 상관했고 병리형을 더 잘 반영했다.

## 5. 한계

Bulk RNA와 조직절편 histology가 완전히 같은 검체 단위가 아니며, 유사한 세포 아형과 reference에 없는 세포는 정확도를 떨어뜨린다. Cryopreservation으로 빠지기 쉬운 neutrophil처럼 reference 구성 자체의 편향이 fraction 추정에 전달된다.

## 6. 재현 또는 활용 포인트

- CRAN R package와 vignette 제공
- 코드: [myles-lewis/cellGeometry](https://github.com/myles-lewis/cellGeometry)
- Benchmark scripts: [Zenodo 20810081](https://doi.org/10.5281/zenodo.20810081)
- 신장 reference에서 leave-one-cell-type-out와 closely related subtype stress test를 먼저 수행한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Single-cell allograft atlas를 reference로 삼아 큰 bulk biopsy·legacy cohort의 immune·tubular fraction을 추정하는 데 직접 활용할 수 있다. Center·protocol별 reference coverage와 histology 또는 flow cytometry 기반 검증이 필요하다.

## 8. 관련 키워드

- Bulk RNA-seq
- scRNA-seq
- Deconvolution
- Cell composition
- Reference atlas
- R package

## 9. Bibliography

Lau, Rachel, et al. “cellGeometry: Ultra-fast Single-cell Deconvolution of Bulk RNA-Seq Using a Geometric Solution.” Nature Communications 17 (2026). [https://doi.org/10.1038/s41467-026-75762-7](https://doi.org/10.1038/s41467-026-75762-7).
