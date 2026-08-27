---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-17'
tags:
- wiki/paper
---

# BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells

## 기본 정보

- Citation key: `wangBioMJEPAJointEmbedding2026`
- Item type: preprint
- Authors: Yuhao Wang; Zelin Zang; Yuxuan Liu; Zhen Lei; Stan Z. Li
- DOI: 10.48550/arXiv.2608.05928
- URL: [Link](https://arxiv.org/abs/2608.05928)
- Source/date: arXiv v1, 2026-08-06

## 1. 한 줄 요약

BioM-JEPA는 개별 gene reconstruction 대신 protein-association·co-expression graph로 연결된 gene block의 latent representation을 예측해 single-cell embedding을 학습한다.

## 2. 왜 중요한가

Student가 남은 gene으로 target block을 예측하고 teacher가 전체 관측 gene에서 target을 제공하는 JEPA 구조다. Frozen embedding의 expression·pathway·neighborhood 보존, perturbation response, effective rank를 평가하며 linear attention으로 scFoundation 대비 처리량 개선도 보고한다.

## 3. 내 연구에 연결할 점

HLA, IFN, cytotoxicity, endothelial injury처럼 block 단위로 움직이는 rejection program을 gene-by-gene reconstruction보다 잘 보존하는지 시험할 후보다. 다만 protein/co-expression graph에 test biology가 새어들지 않도록 prior provenance와 donor·center holdout을 함께 관리해야 한다.

## 4. Bibliography

Wang, Yuhao, Zelin Zang, Yuxuan Liu, Zhen Lei, and Stan Z. Li. "BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2608.05928](https://doi.org/10.48550/arXiv.2608.05928).
