---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-07'
tags:
- wiki/paper
---

# scRep: A Latent-Space Self-Distilled Foundation Model for Single-Cell Representation Learning

## 기본 정보

- Citation key: `wangScRepLatentSpace2026`
- Item type: preprint
- Authors: Shengjie Wang; Zongyong Hu; Yunlong Bie; Qijin Yin; Hechang Chen; Qiuyi Li
- DOI: 10.64898/2026.08.31.747784
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.08.31.747784v1)
- Source/date: bioRxiv v1, posted 2026-09-03

## 1. 한 줄 요약

scRep은 raw expression reconstruction 대신 momentum teacher–student self-distillation로 cell·gene 수준의 안정적인 latent representation을 학습한다.

## 2. 왜 중요한가

약 280만 cell로 pretrain한 compact model이 frozen-representation benchmark에서 강한 성능을 보였고, 3,072만 cell 확장 실험에서는 cell 수보다 biological diversity와 objective가 효율에 중요함을 보였다. Marker gene, TF-associated program, pseudotime structure도 보존했다.

## 3. 내 연구에 연결할 점

Kidney transplant scRNA-seq에서 dropout과 cohort shift에 강한 embedding 후보로 평가하되, rejection subtype·cell state 분류는 donor/center holdout과 PCA·scVI·기존 scFM baseline을 함께 비교해야 한다.

## 4. Bibliography

Wang, Shengjie, Zongyong Hu, Yunlong Bie, Qijin Yin, Hechang Chen, and Qiuyi Li. "scRep: A Latent-Space Self-Distilled Foundation Model for Single-Cell Representation Learning." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.08.31.747784](https://doi.org/10.64898/2026.08.31.747784).
