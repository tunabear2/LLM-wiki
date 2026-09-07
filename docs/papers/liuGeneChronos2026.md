---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-07'
tags:
- wiki/paper
---

# Gene-Chronos: parameter-efficient developmental time inference using a pretrained single-cell foundation model

## 기본 정보

- Citation key: `liuGeneChronos2026`
- Item type: journalArticle
- Authors: Yinbo Liu; Handi Gao; Tian Tian
- DOI: 10.1093/bib/bbag469
- PMID: 42696754
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42696754/)
- Source/date: PubMed / Briefings in Bioinformatics, published and indexed 2026-09-04

## 1. 한 줄 요약

Gene-Chronos는 frozen Geneformer에 temporal prompt와 contrastive objective를 붙여 single-cell transcriptome에서 연속 biological time을 추정한다.

## 2. 왜 중요한가

Full backbone fine-tuning 없이 cross-attention adapter와 time regression·temporal contrastive loss를 학습해 species와 developmental stage가 다른 dataset으로 일반화한다. Attention 분석으로 progression-associated gene 후보도 제시한다.

## 3. 내 연구에 연결할 점

Biopsy 시점이 불규칙한 rejection cohort에서 acute-to-chronic transition이나 treatment-response trajectory를 연속 축으로 추정할 후보지만, post-transplant time을 그대로 학습한 누수와 donor·therapy confounding을 분리해야 한다.

## 4. Bibliography

Liu, Yinbo, Handi Gao, and Tian Tian. "Gene-Chronos: parameter-efficient developmental time inference using a pretrained single-cell foundation model." _Briefings in Bioinformatics_ 27, no. 5 (2026): bbag469. [https://doi.org/10.1093/bib/bbag469](https://doi.org/10.1093/bib/bbag469).
