---
type: paper
status: reference
rag_priority: high
updated: '2026-10-19'
tags:
- wiki/paper
---

# Beyond the Final Layer: Evaluating Single-Cell Foundation Model Representations for Molecular Prediction

## 기본 정보

- Citation key: `wenBeyondFinalLayer2026`
- Item type: preprint
- Authors: M.-C. C. Wen; Y. Lyu; A. Robbins
- DOI: 10.64898/2026.10.05.756880
- URL: [Link](https://doi.org/10.64898/2026.10.05.756880)
- Source/date: bioRxiv v1, posted 2026-10-12

## 1. 한 줄 요약

Geneformer, scBERT, scGPT, scFoundation의 layer별 frozen embedding을 비교해 최종 layer가 항상 최선은 아니며 task와 readout에 따라 유효 깊이가 달라짐을 보인다.

## 2. 왜 중요한가

Cell-type 및 perturbation-response prediction에서 extraction layer, pooling, leave-one-dataset-out 선택을 함께 통제해 scFM representation 평가의 숨은 자유도를 드러낸다. 특히 perturbation task에서는 네 모델 모두 이른 layer가 최종 layer와 동등한 후보가 될 수 있었다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection 예측에서 마지막 layer만 고정하지 말고 layer와 readout을 donor-level validation fold 안에서 선택해야 한다. Raw expression, PCA 및 pathway score와 비교하고 HLA·IFN·endothelial program 보존을 별도로 점검한다.

## 4. Bibliography

Wen, M.-C. C., Y. Lyu, and A. Robbins. "Beyond the Final Layer: Evaluating Single-Cell Foundation Model Representations for Molecular Prediction." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.05.756880](https://doi.org/10.64898/2026.10.05.756880).
