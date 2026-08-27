---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-17'
tags:
- wiki/paper
---

# scYeast: a biological-knowledge-guided foundation model on yeast single-cell transcriptomics

## 기본 정보

- Citation key: `fanScYeastBiologicalKnowledge2026`
- Item type: journalArticle
- Authors: Xingcun Fan; Wenbin Liao; Luchi Xiao; Xuefeng Yan; Hongzhong Lu
- DOI: 10.1016/j.synbio.2026.05.014
- PMID: 42502841
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42502841/)
- Source/date: PubMed / Synthetic and Systems Biotechnology, e-published 2026-07-16; indexed 2026-07-26

## 1. 한 줄 요약

scYeast는 transcriptional regulatory prior를 Transformer attention에 주입해 yeast single-cell transcriptomics의 zero-shot regulation inference, phenotype prediction, perturbation response와 proteomics transfer를 수행한다.

## 2. 왜 중요한가

Human·mouse 중심 scFM과 달리 organism-specific regulatory knowledge를 asymmetric parallel architecture로 결합한다. Cell state와 growth prediction, unseen TF perturbation response, proteomics transfer를 함께 평가해 작은 생물종 corpus에서 prior-guided pretraining을 구성하는 사례를 제공한다.

## 3. 내 연구에 연결할 점

Kidney transplant에 직접 적용되는 모델은 아니지만, Banff·immune signaling·kidney-specific GRN prior를 generic transcriptome encoder와 결합하는 설계에 참고된다. Yeast에서의 성능을 사람 biopsy로 일반화할 수 없으므로 prior leakage와 tissue-specific external validation을 별도로 다뤄야 한다.

## 4. Bibliography

Fan, Xingcun, Wenbin Liao, Luchi Xiao, Xuefeng Yan, and Hongzhong Lu. "scYeast: a biological-knowledge-guided foundation model on yeast single-cell transcriptomics." _Synthetic and Systems Biotechnology_, 2026. [https://doi.org/10.1016/j.synbio.2026.05.014](https://doi.org/10.1016/j.synbio.2026.05.014).
