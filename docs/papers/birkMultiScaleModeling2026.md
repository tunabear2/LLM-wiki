---
type: paper
status: reference
rag_priority: high
updated: '2026-08-31'
tags:
- wiki/paper
---

# Multi-scale modeling of human tissues from spatial transcriptomics with TERRA

## 기본 정보

- Citation key: `birkMultiScaleModeling2026`
- Item type: preprint
- Authors: Sebastian Birk et al.
- DOI: 10.64898/2026.07.29.741565
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.07.29.741565v1)
- Source/date: bioRxiv v1, posted 2026-08-04

## 1. 한 줄 요약

TERRA는 1억 1,200만 spatially resolved human cell로 pretraining해 gene, cell, neighborhood embedding과 spatial in silico perturbation을 하나의 backbone에서 제공한다.

## 2. 왜 중요한가

JEPA objective와 neighborhood-aware gene tokenization으로 unseen tissue에 zero-shot transfer한다. Kidney section에서 immune-checkpoint target knockout이 nephrotoxicity-associated gene program을 예측했고, 치료 노출 tissue와 blood에서 이를 검증했다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection의 immune–endothelial–tubular niche와 면역억제/면역활성 perturbation을 spatial context에서 연결할 직접적인 후보 모델이다. 다만 checkpoint nephrotoxicity와 alloimmune rejection의 차이를 분리하고 donor·center·assay holdout으로 검증해야 한다.

## 4. Bibliography

Birk, Sebastian, et al. "Multi-scale modeling of human tissues from spatial transcriptomics with TERRA." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.07.29.741565](https://doi.org/10.64898/2026.07.29.741565).
