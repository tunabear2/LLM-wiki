---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-24'
tags:
- wiki/paper
---

# CytoFormer: A Molecularly Supervised Cell Foundation Model for Histopathology Cell Classification

## 기본 정보

- Citation key: `yaoCytoFormerMolecularlySupervised2026`
- Item type: preprint
- Authors: Jialu Yao; Songhao Li; Alina Yu; Zhi Huang
- DOI: 10.48550/arXiv.2608.16718
- URL: [Link](https://arxiv.org/abs/2608.16718)
- Source/date: arXiv v1, 2026-08-17

## 1. 한 줄 요약

CytoFormer는 16개 장기의 paired H&E–Xenium 1,540만 개 cell에서 spatial-transcriptomic cell identity로 형태학을 감독해, routine histology의 cell-level 분류와 label-efficient transfer를 위한 foundation representation을 학습한다.

## 2. 왜 중요한가

Pathologist가 수작업으로 붙인 morphology label 대신 같은 cell에서 측정한 spatial transcriptomics로 supervision을 만든다. 81개 paired section과 23개 cell type으로 pretraining한 뒤 spatially held-out tissue에서 성능을 평가하고, frozen encoder의 linear probe가 organ·cell type shift를 포함한 네 benchmark에서 여섯 pathology foundation model보다 높은 transfer 성능을 보였다고 보고한다. Transcriptomics encoder 자체는 아니지만 molecular identity를 대규모 histology representation에 연결한다는 점에서 single-cell multimodal foundation model의 중요한 변형이다.

## 3. 내 연구에 연결할 점

Kidney transplant biopsy의 routine H&E에서 immune, epithelial, endothelial cell composition과 lesion architecture를 추정하고, 제한된 Xenium·spatial transcriptomics subset으로 label을 보정하는 후보가 될 수 있다. 다만 rejection 적용 전에는 kidney 및 transplant tissue의 pretraining 포함 여부, stain·scanner·center shift, inflammatory look-alike cell의 오류, donor-level holdout을 별도로 검증해야 한다.

## 4. Bibliography

Yao, Jialu, Songhao Li, Alina Yu, and Zhi Huang. "CytoFormer: A Molecularly Supervised Cell Foundation Model for Histopathology Cell Classification." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2608.16718](https://doi.org/10.48550/arXiv.2608.16718).
