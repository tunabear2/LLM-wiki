---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-14'
tags:
- wiki/paper
---

# TabOmics: A Small, Open Tabular Foundation Model for Wide Omics Data

## 기본 정보

- Citation key: `lopezGarciaTabOmicsSmallOpen2026`
- Item type: preprint
- Authors: Andrea López-García; Luis Bote-Curiel; Francisco Javier Gimeno-Blanes; José Luis Rojo-Álvarez; Sergio Muñoz-Romero
- arXiv: 2611.15329
- URL: [Link](https://arxiv.org/abs/2611.15329)
- Source/date: arXiv v1, submitted 2026-11-11

## 1. 한 줄 요약

TabOmics는 synthetic wide table로 pretraining한 7.3M-parameter tabular FM으로, 수만 feature의 omics classification과 feature importance를 한 forward pass에서 처리한다.

## 2. 왜 중요한가

46개 high-dimensional low-sample-size task에서 TabPFN 계열과 비교해 작은 공개 모델의 경쟁력을 보였고, 30,000 feature에서도 chance 이상을 유지했다. 다만 breast-cancer top gene은 label을 정의한 PAM50과의 일치이므로 독립적인 biological validation으로 해석할 수 없다.

## 3. 내 연구에 연결할 점

Patient-level kidney-transplant bulk·pseudobulk expression에서 scFM aggregation과 비교할 저비용 baseline이다. Donor split, clinical covariate baseline과 external-center calibration을 유지하고 feature importance를 기전 증거로 과해석하지 않아야 한다.

## 4. Bibliography

López-García, Andrea, Luis Bote-Curiel, Francisco Javier Gimeno-Blanes, José Luis Rojo-Álvarez, and Sergio Muñoz-Romero. "TabOmics: A Small, Open Tabular Foundation Model for Wide Omics Data." _arXiv_, 2026. [https://arxiv.org/abs/2611.15329](https://arxiv.org/abs/2611.15329).
