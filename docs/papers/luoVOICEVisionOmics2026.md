---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-17'
tags:
- wiki/paper
---

# VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression

## 기본 정보

- Citation key: `luoVOICEVisionOmics2026`
- Item type: preprint
- Authors: Xin Luo; Yicheng Tao; Haoxuan Zeng; Suyuan Wang; Chenzi Ouyang; Meiqi Zhu; Kai Liu; Shuibing Chen; Jie Liu
- DOI: 10.48550/arXiv.2608.08366
- URL: [Link](https://arxiv.org/abs/2608.08366)
- Source/date: arXiv v1, 2026-08-08

## 1. 한 줄 요약

VOICE는 pathology image와 transcriptome foundation model embedding을 23 million Xenium cells에서 정렬하고, direct regression과 reference retrieval을 gene별로 융합해 H&E에서 single-cell expression을 예측한다.

## 2. 왜 중요한가

Morphology로 예측 가능한 gene은 direct branch가, 형태 신호가 약한 gene은 유사 reference cell retrieval이 보완하도록 설계한다. Held-out patient·slide와 부분적으로 겹치는 gene panel에서 일반화를 평가해 pathology–spatial transcriptomics 연결을 atlas 규모로 확장한다.

## 3. 내 연구에 연결할 점

Routine kidney allograft H&E에서 Xenium reference를 이용해 rejection 관련 HLA·IFN·endothelial·cytotoxic program을 보조 추정하는 후보 접근이다. Institution별 staining과 scanner shift, retrieval reference leakage, Banff lesion별 calibration을 독립 biopsy cohort에서 검증해야 한다.

## 4. Bibliography

Luo, Xin, et al. "VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2608.08366](https://doi.org/10.48550/arXiv.2608.08366).
