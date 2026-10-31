---
type: paper
status: reference
rag_priority: high
updated: '2026-10-31'
tags:
- wiki/paper
---

# Predicting Cell-State-Specific Gene Regulation from DNA across Species

## 기본 정보

- Citation key: `liuPredictingCellStateSpecific2026`
- Item type: preprint
- Authors: H. Liu; S. Mao; T. Gallent; Y. Chen; Z. Yan; I. Vogel; L. Traunmuller; R. Zhang; J. D. Buenrostro; J. Zhou; M. E. Greenberg
- DOI: 10.64898/2026.10.19.760026
- URL: [Link](https://doi.org/10.64898/2026.10.19.760026)
- Source/date: bioRxiv v1, posted 2026-10-20

## 1. 한 줄 요약

Bolero는 atlas-scale cell-state embedding으로 sequence-to-function model의 parameter를 조건화해 DNA에서 cell-state별 chromatin accessibility와 transcript abundance를 예측한다.

## 2. 왜 중요한가

33개 dataset, 6개 mammal의 1,070만 cell로 학습해 보지 못한 cell state와 species로 확장하고 non-coding variant의 효과를 작동 cell type에 연결한다. Single-cell representation과 regulatory sequence model을 하나의 conditional predictor로 결합한 접근이다.

## 3. 내 연구에 연결할 점

Kidney immune·endothelial·tubular state에 따른 rejection-risk variant와 AP-1/IFN regulatory response를 연결할 후보지만, transplant-specific state가 pretraining atlas에 포함됐는지와 donor·species OOD calibration을 먼저 확인해야 한다.

## 4. Bibliography

Liu, H., S. Mao, T. Gallent, Y. Chen, Z. Yan, I. Vogel, L. Traunmuller, R. Zhang, J. D. Buenrostro, J. Zhou, and M. E. Greenberg. "Predicting Cell-State-Specific Gene Regulation from DNA across Species." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.19.760026](https://doi.org/10.64898/2026.10.19.760026).
