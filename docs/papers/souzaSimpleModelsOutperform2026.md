---
type: paper
status: reference
rag_priority: high
updated: '2026-11-14'
tags:
- wiki/paper
---

# Simple models outperform single-cell foundation models on downstream benchmarks

## 기본 정보

- Citation key: `souzaSimpleModelsOutperform2026`
- Item type: preprint
- Authors: H. Souza; P. Mehta
- DOI: 10.64898/2026.02.11.705358
- URL: [Link](https://doi.org/10.64898/2026.02.11.705358)
- Source/date: bioRxiv v2, revised 2026-11-10 (v1 posted 2026-02-13; revised title)

## 1. 한 줄 요약

Careful normalization과 linear representation만으로 TranscriptFormer 계열 scFM benchmark에서 SOTA 또는 근접 성능을 내고 일부 OOD task에서는 foundation model을 앞섰다.

## 2. 왜 중요한가

새 cell type과 organism을 포함한 downstream benchmark에서 계산량이 큰 pretrained embedding의 이득이 단순한 expression structure를 넘어서는지 묻는다. Model scale보다 split, normalization과 강한 linear baseline이 결론을 좌우할 수 있음을 직접 보여준다.

## 3. 내 연구에 연결할 점

Kidney-transplant rejection annotation과 outcome prediction에서 raw/log-normalized expression, HVG/PCA와 linear probe를 scFM과 같은 donor·center holdout에 놓아야 한다. 특히 OOD 개선을 주장할 때 preprocessing과 label composition을 고정해야 한다.

## 4. Bibliography

Souza, H., and P. Mehta. "Simple models outperform single-cell foundation models on downstream benchmarks." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.02.11.705358](https://doi.org/10.64898/2026.02.11.705358).
