---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# scAnyOmics: Foundation-Model Distillation for Any-to-Any Completion of Multi-omics Virtual Cells

## 기본 정보

- Citation key: `songScAnyOmicsFoundationModel2026`
- Item type: preprint
- Authors: Zhaoqi Song; Ye Du; Yusuke Iwasawa; Yutaka Matsuo; Qian Niu
- arXiv: 2610.41399
- URL: [Link](https://arxiv.org/abs/2610.41399)
- Source/date: arXiv v1, submitted 2026-10-30; backfilled in this watch

## 1. 한 줄 요약

scAnyOmics는 frozen scFM 지식을 multimodal student로 distill해 RNA, protein과 ATAC 사이의 any-to-any completion 및 shared virtual-cell representation을 학습한다.

## 2. 왜 중요한가

여섯 연구의 paired·partially paired 690,880개 cell을 통합하고 held-out donor에서 cross-modal reconstruction을 평가했다. Missing modality 보완뿐 아니라 annotation, perturbation response와 biological-age prediction으로 transfer 범위를 넓힌다.

## 3. 내 연구에 연결할 점

Kidney rejection에서 scRNA, CITE-seq와 scATAC이 일부 donor에만 있을 때 유용하지만, modality completion이 HLA·IFN·chromatin signal을 과도하게 평활화하지 않는지 완전 donor holdout으로 검증해야 한다.

## 4. Bibliography

Song, Zhaoqi, Ye Du, Yusuke Iwasawa, Yutaka Matsuo, and Qian Niu. "scAnyOmics: Foundation-Model Distillation for Any-to-Any Completion of Multi-omics Virtual Cells." _arXiv_, 2026. [https://arxiv.org/abs/2610.41399](https://arxiv.org/abs/2610.41399).
