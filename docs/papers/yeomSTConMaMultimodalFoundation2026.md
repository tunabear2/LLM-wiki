---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-05'
tags:
- wiki/paper
---

# ST-ConMa: a multimodal foundation framework for spatial transcriptomics via image-gene contrastive and matching learning

## 기본 정보

- Citation key: `yeomSTConMaMultimodalFoundation2026`
- Item type: journal article
- Authors: Taelim Yeom; Dongha Choi; Hyunju Lee
- DOI: 10.1093/bib/bbag535
- PMID: 42803631
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42803631/)
- Source/date: Briefings in Bioinformatics 27(5), published 2026-09-01; PubMed indexed 2026-09-28

## 1. 한 줄 요약

ST-ConMa는 spot-level tissue image와 gene expression을 contrastive·matching objective 및 cross-attention으로 공동 pretraining해 spatial transcriptomics용 multimodal fusion representation을 학습한다.

## 2. 왜 중요한가

Image와 gene embedding을 따로 만드는 대신 multimodal encoder가 joint representation을 학습하며, histopathology classification, gene-expression prediction과 spatial clustering에서 기존 방법과 비교된다. 여러 ST data로의 일반 backbone을 목표로 하지만 platform·resolution·tissue shift와 pretraining overlap을 확인해야 한다.

## 3. 내 연구에 연결할 점

Routine kidney H&E와 spatial transcriptomics를 연결해 rejection lesion과 expression program을 함께 모델링할 후보이다. Slide·patient 단위 split, stain·scanner·center shift와 HLA·IFN·endothelial program 보존을 독립 cohort에서 검증해야 한다.

## 4. Bibliography

Yeom, Taelim, Dongha Choi, and Hyunju Lee. "ST-ConMa: A Multimodal Foundation Framework for Spatial Transcriptomics via Image-Gene Contrastive and Matching Learning." _Briefings in Bioinformatics_ 27, no. 5 (2026). [https://doi.org/10.1093/bib/bbag535](https://doi.org/10.1093/bib/bbag535).
