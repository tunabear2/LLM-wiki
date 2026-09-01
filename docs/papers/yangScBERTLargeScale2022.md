---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# scBERT as a large-scale pretrained deep language model for cell type annotation of single-cell RNA-seq data

## 기본 정보

- Citation key: `yangScBERTLargeScale2022`
- Item type: journalArticle
- Authors: Fan Yang; Wencheng Wang; Fang Wang; Yong Yu; etc.
- DOI: 10.1038/s42256-022-00534-z
- URL: [Link](https://www.nature.com/articles/s42256-022-00534-z)
- Source/date: Nature Machine Intelligence, 2022

## 1. 한 줄 요약

scBERT는 BERT식 pretraining을 scRNA-seq에 적용해 gene-gene interaction representation을 학습하고, cell type annotation으로 transfer한 초기 single-cell language model이다.

## 2. 왜 중요한가

Transformer와 masked/pretrained language model 개념이 single-cell genomics로 들어오는 초기 사례다. 이후 scGPT, Geneformer, scFoundation 논문을 읽을 때 역사적 baseline으로 유용하다.

## 3. 내 연구에 연결할 점

Transplant biopsy cell type annotation에서 scBERT류 모델은 reference label이 부족한 상황의 transfer baseline이 될 수 있지만, batch와 cell-type imbalance에 민감한지 확인해야 한다.

## 4. Bibliography

Yang, Fan, et al. "scBERT as a large-scale pretrained deep language model for cell type annotation of single-cell RNA-seq data." _Nature Machine Intelligence_, 2022. [https://doi.org/10.1038/s42256-022-00534-z](https://doi.org/10.1038/s42256-022-00534-z).

