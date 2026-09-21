---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-21'
tags:
- wiki/paper
---

# Pretrained gene representations transfer mean expression more broadly than spatial patterns in virtual spatial transcriptomics

## 기본 정보

- Citation key: `chenPretrainedGeneRepresentations2026`
- Item type: preprint
- Authors: Tingjun Chen; Stephanie C. Hicks
- DOI: 10.64898/2026.09.15.751768
- URL: [Link](https://doi.org/10.64898/2026.09.15.751768)
- Source/date: bioRxiv v1, posted 2026-09-18

## 1. 한 줄 요약

Decima·scGPT gene representation을 쓴 virtual spatial transcriptomics의 held-out-gene 이득 중 91% 이상이 spatial pattern보다 gene mean-expression 오차 감소에서 왔음을 보인다.

## 2. 왜 중요한가

Held-out individual과 held-out gene을 함께 분리하고, image를 쓰지 않는 mean-only model과 비교해 cross-gene generalization을 평균 발현과 공간 변이 복원으로 분해했다. Full-matrix correlation만 보고 spatial prediction 능력을 주장하면 pretrained embedding의 mean-expression prior를 공간 신호로 오해할 수 있음을 보여준다.

## 3. 내 연구에 연결할 점

Kidney transplant H&E·spatial 분석에서는 HLA·IFN·endothelial gene의 평균 발현과 lesion-localized pattern을 별도 metric으로 평가해야 한다. Donor·section holdout, mean-only baseline과 spatially variable gene subset을 고정해 rejection lesion 복원 여부를 확인해야 한다.

## 4. Bibliography

Chen, Tingjun, and Stephanie C. Hicks. "Pretrained gene representations transfer mean expression more broadly than spatial patterns in virtual spatial transcriptomics." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.09.15.751768](https://doi.org/10.64898/2026.09.15.751768).
