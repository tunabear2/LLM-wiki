---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-17'
tags:
- wiki/paper
---

# CellWorld: From Gene-Level Reconstruction to Latent Cell Prediction in Spatial Transcriptomics Foundation Models

## 기본 정보

- Citation key: `liuCellWorldGeneLevel2026`
- Item type: preprint
- Authors: Haiping Liu; Qian Zhao; Lijing Lin; Jingyuan Sun; Hongpeng Zhou
- DOI: 10.48550/arXiv.2608.06659
- URL: [Link](https://arxiv.org/abs/2608.06659)
- Source/date: arXiv v1, 2026-08-07

## 1. 한 줄 요약

CellWorld는 masked gene을 복원하는 대신 주변 spatial context와 일부 expression hint로 masked cell의 latent representation을 예측하는 spatial transcriptomics foundation model이다.

## 2. 왜 중요한가

46 million human cells로 크기가 다른 네 모델을 pretraining해 11개 linear-probe와 7개 fine-tuned spatial benchmark를 평가한다. Cell count 자체보다 충분한 optimization과 다양한 biological source coverage가 spatial transfer에 중요하며, 작은 frozen model도 강한 전이를 보일 수 있음을 제시한다.

## 3. 내 연구에 연결할 점

Kidney biopsy에서 immune infiltrate와 tubulitis·glomerulitis·microvascular inflammation 주변의 cell state를 latent prediction으로 연결할 후보 모델이다. Center, assay panel, lesion distribution이 다른 external spatial cohort에서 frozen transfer와 partial-expression hint 의존성을 검증해야 한다.

## 4. Bibliography

Liu, Haiping, Qian Zhao, Lijing Lin, Jingyuan Sun, and Hongpeng Zhou. "CellWorld: From Gene-Level Reconstruction to Latent Cell Prediction in Spatial Transcriptomics Foundation Models." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2608.06659](https://doi.org/10.48550/arXiv.2608.06659).
