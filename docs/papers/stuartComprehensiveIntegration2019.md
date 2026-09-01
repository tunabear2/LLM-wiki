---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Comprehensive integration of single-cell data

## 기본 정보

- Citation key: `stuartComprehensiveIntegration2019`
- Item type: journalArticle
- Authors: Tim Stuart; Andrew Butler; Paul Hoffman; Christoph Hafemeister; Efthymia Papalexi; William M. Mauck III; Yuhan Hao; Marlon Stoeckius; Peter Smibert; Rahul Satija
- DOI: 10.1016/j.cell.2019.05.031
- PMID: 31178118
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/31178118/)
- Source/date: Cell, 2019

## 1. 한 줄 요약

Seurat v3 anchor integration은 서로 다른 scRNA-seq dataset 또는 modality 사이에서 대응되는 cell state anchor를 찾아 integrated representation과 label transfer를 수행한다.

## 2. 왜 중요한가

여러 donor, batch, platform, tissue dataset을 합치는 scRNA-seq 분석의 표준적 사고방식을 만들었다. Reference mapping, query annotation, cross-modality transfer를 이해하는 핵심 논문이다.

## 3. 분석에서 위치

각 dataset을 normalize/HVG/PCA한 뒤 anchor를 찾고, integrated embedding을 만들어 clustering과 visualization에 사용한다. Reference atlas에 새 kidney biopsy scRNA-seq를 map하거나 annotation label을 transfer할 때 특히 중요하다.

## 4. 주의점

- Integration은 batch effect를 줄이지만 disease-specific signal도 약화할 수 있다.
- 공유 cell state가 충분히 없으면 anchor가 잘못 잡힐 수 있다.
- Differential expression은 integrated assay가 아니라 raw/count 또는 appropriately normalized assay에서 수행해야 한다.

## 5. Bibliography

Stuart, Tim, Andrew Butler, Paul Hoffman, Christoph Hafemeister, Efthymia Papalexi, William M. Mauck III, Yuhan Hao, Marlon Stoeckius, Peter Smibert, and Rahul Satija. "Comprehensive integration of single-cell data." _Cell_, 2019. [https://doi.org/10.1016/j.cell.2019.05.031](https://doi.org/10.1016/j.cell.2019.05.031).
