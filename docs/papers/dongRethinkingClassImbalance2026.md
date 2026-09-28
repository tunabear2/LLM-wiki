---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-28'
tags:
- wiki/paper
---

# Rethinking Class Imbalance for Single-Cell Foundation Models: A Systematic Benchmark Across Architectures and Long-Tail Loss Functions

## 기본 정보

- Citation key: `dongRethinkingClassImbalance2026`
- Item type: preprint
- Authors: Zeyu Dong; Jiahui Zhong
- DOI: 10.48550/arXiv.2609.23325
- URL: [Link](https://doi.org/10.48550/arXiv.2609.23325)
- Source/date: arXiv v1, submitted 2026-09-20; newly surfaced after the previous watch run

## 1. 한 줄 요약

scGPT·scBERT·Geneformer와 6개 long-tail loss를 3개 dataset에서 비교해, 희귀 cell type 실패 양상은 pretraining보다 dataset geometry에 더 좌우되고 class-balanced loss와 LDAM이 가장 일관적임을 보인다.

## 2. 왜 중요한가

총 162개 controlled run에서 overall accuracy가 높아도 macro-F1과 rare-class recall이 낮을 수 있음을 분리해 보여준다. 희귀 class는 loss 변경으로 회복 가능한 경우와 embedding에서 다른 class neighborhood로 흡수돼 어떤 loss로도 회복되지 않는 경우로 나뉘므로, 단일 imbalance metric이나 aggregate accuracy만으로 scFM annotation을 평가하면 안 된다.

## 3. 내 연구에 연결할 점

Kidney transplant biopsy의 희귀 endothelial injury state, plasma cell, cytotoxic subset과 rejection-associated transitional cell을 donor-level split에서 별도 평가해야 한다. Class-balanced loss·LDAM뿐 아니라 class별 sample size, embedding neighborhood와 abstention을 함께 보고해야 한다.

## 4. Bibliography

Dong, Zeyu, and Jiahui Zhong. "Rethinking Class Imbalance for Single-Cell Foundation Models: A Systematic Benchmark Across Architectures and Long-Tail Loss Functions." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2609.23325](https://doi.org/10.48550/arXiv.2609.23325).
