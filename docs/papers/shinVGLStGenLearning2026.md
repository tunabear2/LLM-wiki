---
type: paper
status: reference
rag_priority: high
updated: '2026-10-31'
tags:
- wiki/paper
---

# VGL-stGen: Learning a Shared Multimodal Model for Lung Histology and Spatial Transcriptomics

## 기본 정보

- Citation key: `shinVGLStGenLearning2026`
- Item type: preprint
- Authors: H. Shin; D. Lee; S. Bae; K. J. Na; D. Lee; H. Choi
- arXiv: 2610.28266
- URL: [Link](https://arxiv.org/abs/2610.28266)
- Source/date: arXiv v1, submitted 2026-10-20

## 1. 한 줄 요약

VGL-stGen은 pretrained medical vision-language model을 paired lung H&E, spatial transcriptomics와 single-cell reference로 적응시켜 하나의 checkpoint로 cell type, gene prediction과 conditional expression completion을 수행한다.

## 2. 왜 중요한가

Image–expression과 expression–cell-type pair를 shared generative space에 넣어 13개 task를 지원한다. Image permutation으로 morphology의 추가 정보를 확인했지만 external label이 공유된 annotation lineage에 의존하고 일부 H&E가 이전 학습에 노출된 한계도 명시한다.

## 3. 내 연구에 연결할 점

Kidney H&E와 spatial rejection program을 연결하는 multimodal backbone 후보지만 lung-to-kidney transfer, pretraining exposure, patient·center holdout과 measured-gene calibration을 엄격히 점검해야 한다.

## 4. Bibliography

Shin, H., D. Lee, S. Bae, K. J. Na, D. Lee, and H. Choi. "VGL-stGen: Learning a Shared Multimodal Model for Lung Histology and Spatial Transcriptomics." _arXiv_, 2026. [https://arxiv.org/abs/2610.28266](https://arxiv.org/abs/2610.28266).
