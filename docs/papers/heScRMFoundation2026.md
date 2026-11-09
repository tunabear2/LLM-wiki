---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# scRM: A single-cell foundation model trained on scRNA-seq reads

## 기본 정보

- Citation key: `heScRMFoundation2026`
- Item type: preprint
- Authors: D. He; R. Patro; M. Nassar; H. Wu; Q. Yan; G. Xu; K. Torkenczy; J. Liu; S. Tyanova
- DOI: 10.64898/2026.10.24.761590
- URL: [Link](https://doi.org/10.64898/2026.10.24.761590)
- Source/date: bioRxiv v2, revised 2026-11-03

## 1. 한 줄 요약

scRM은 count matrix가 아니라 scRNA-seq sequencing read 자체를 pretraining input으로 사용해 raw-data foundation modeling의 가능성을 보인다.

## 2. 왜 중요한가

정량화 단계에서 버려지는 read-level 정보를 직접 학습 대상으로 삼고, count-based model보다 적은 계산으로 경쟁력 있는 representation을 목표로 한다. Dataset-specific raw-data pretraining과 scale-up이라는 새로운 scFM 설계 축을 제시한다.

## 3. 내 연구에 연결할 점

Kidney biopsy에서 isoform, mapping ambiguity와 intronic signal을 활용할 여지가 있지만, protocol·read length·chemistry shift가 rejection biology보다 먼저 학습되지 않는지 엄격한 center holdout이 필요하다.

## 4. Bibliography

He, D., R. Patro, M. Nassar, H. Wu, Q. Yan, G. Xu, K. Torkenczy, J. Liu, and S. Tyanova. "scRM: A single-cell foundation model trained on scRNA-seq reads." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.24.761590](https://doi.org/10.64898/2026.10.24.761590).
