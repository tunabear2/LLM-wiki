---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-31'
tags:
- wiki/paper
---

# Benchmarking single-cell foundation models in a zero-shot setting

## 기본 정보

- Citation key: `gaballaBenchmarkingSingleCell2026`
- Item type: preprint
- Authors: Yasmine Gaballa; Somaia Ahmed; Tamim Abdelaal
- DOI: 10.64898/2026.08.03.739553
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.08.03.739553v1)
- Source/date: bioRxiv v1, posted 2026-08-07

## 1. 한 줄 요약

scGPT, SCimilarity, UCE, TranscriptFormer의 zero-shot embedding을 annotation, human/cross-species integration, protein expression prediction에서 전통 baseline과 비교한다.

## 2. 왜 중요한가

Cell type annotation과 integration에서는 classical baseline 또는 scVI가 대체로 강했고, protein expression prediction에서는 scFM embedding이 이점을 보였다. 단일 foundation model이 모든 downstream task를 대체한다는 가정보다 task별 utility를 검증해야 함을 보여준다.

## 3. 내 연구에 연결할 점

Rejection cell annotation과 cohort integration에서는 PCA/HVG, scVI 같은 baseline을 유지하고, CITE-seq protein 또는 pathway score 예측처럼 scFM이 유리할 가능성이 있는 task를 분리해 평가해야 한다.

## 4. Bibliography

Gaballa, Yasmine, Somaia Ahmed, and Tamim Abdelaal. "Benchmarking single-cell foundation models in a zero-shot setting." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.08.03.739553](https://doi.org/10.64898/2026.08.03.739553).
