---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-05'
tags:
- wiki/paper
---

# CellMSA: Context Modeling for Single-Cell Representation Learning

## 기본 정보

- Citation key: `zhaoCellMSAContextModeling2026`
- Item type: preprint
- Authors: Suyuan Zhao; Minghao Liu; Yizhen Luo; Zaiqing Nie
- DOI: 10.48550/arXiv.2609.38908
- URL: [Link](https://doi.org/10.48550/arXiv.2609.38908)
- Source/date: arXiv v1, submitted 2026-09-30

## 1. 한 줄 요약

CellMSA는 다른 batch와 연관 cell type의 세포를 context로 검색하고 gene-pair 표현을 만들어, 약 1억 900만 cell의 pretraining에서 독립 cell encoding을 넘어서는 single-cell representation을 학습한다.

## 2. 왜 중요한가

기존 scFM이 각 cell을 독립적으로 처리하거나 같은 batch 안의 관계만 쓰는 한계를 지적하고, protein MSA에서 착안한 cross-cell context를 gene-level encoder에 주입한다. 여러 benchmark에서 기존 방법보다 높은 성능을 보고하지만, 검색 context가 label이나 test donor 정보를 노출하는지와 primary observation 중복 여부는 별도 감사가 필요하다.

## 3. 내 연구에 연결할 점

Kidney transplant biopsy에서는 donor·center·rejection phenotype이 섞이지 않도록 retrieval pool을 train donor로 제한한 뒤, 희귀 immune–endothelial–tubular state의 표현이 개선되는지 확인할 수 있다. Patient-level split, no-retrieval ablation과 PCA·scVI·기존 scFM baseline을 함께 두어야 한다.

## 4. Bibliography

Zhao, Suyuan, Minghao Liu, Yizhen Luo, and Zaiqing Nie. "CellMSA: Context Modeling for Single-Cell Representation Learning." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2609.38908](https://doi.org/10.48550/arXiv.2609.38908).
