---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-03'
tags:
- wiki/paper
---

# scMIR: a vision-language foundation model for single-cell light microscopy image representation

## 기본 정보

- Citation key: `shangScMIRVisionLanguage2026`
- Item type: preprint
- Authors: Yifan Shang; Jiahui Tan; Xiangxiang Zeng; Renjie Zhou
- DOI: 10.48550/arXiv.2607.22712
- URL: [Link](https://arxiv.org/abs/2607.22712)
- Source/date: arXiv revised v2, 2026-07-28 (first posted 2026-07-21)

## 1. 한 줄 요약

scMIR은 207,957개의 single-cell microscopy image–text pair에서 image reconstruction과 text-guided alignment를 함께 학습해 다양한 현미경 modality와 phenotype task에 전이하는 vision-language foundation model이다.

## 2. 왜 중요한가

16개 benchmark에서 cell classification, clustering, phenotype inference, batch correction을 평가하며 task-specific fine-tuning 없이도 일반화를 목표로 한다. Transcriptome token model이 아니라 morphology–text representation을 학습한다는 점에서 single-cell FM의 modality 범위를 넓힌다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection transcriptomics에는 직접 적용되는 모델이 아니다. 다만 biopsy의 immune-cell morphology나 imaging phenotype을 scRNA/spatial embedding과 결합하는 후속 multimodal 연구에서는 보조 encoder 후보가 될 수 있으며, transcriptomics 성능 근거로 혼동해서는 안 된다.

## 4. Bibliography

Shang, Yifan, Jiahui Tan, Xiangxiang Zeng, and Renjie Zhou. "scMIR: a vision-language foundation model for single-cell light microscopy image representation." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2607.22712](https://doi.org/10.48550/arXiv.2607.22712).
