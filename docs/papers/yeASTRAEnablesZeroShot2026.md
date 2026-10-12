---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# ASTRA enables zero-shot super-resolution of spatial transcriptomics across capture geometries

## 기본 정보

- Citation key: `yeASTRAEnablesZeroShot2026`
- Item type: preprint
- Authors: J. Ye; Q. Cui
- DOI: 10.64898/2026.09.30.755663
- URL: [Link](https://doi.org/10.64898/2026.09.30.755663)
- Source/date: bioRxiv v1, posted 2026-10-06

## 1. 한 줄 요약

ASTRA는 다양한 모양의 count-bearing region으로 histology와 measured RNA를 함께 pretrain해, 하나의 frozen checkpoint로 서로 다른 spatial capture geometry를 zero-shot super-resolution한다.

## 2. 왜 중요한가

Section마다 모델을 다시 학습하는 비용을 줄이면서 Visium HD와 일반 Visium, nucleus-associated analysis에 같은 checkpoint를 적용한다. 성능 주장은 colorectal·breast cancer 중심이므로 tissue와 platform을 동시에 바꾸는 외부 검증이 중요하다.

## 3. 내 연구에 연결할 점

Kidney biopsy의 Visium·고해상도 spatial data에서 Banff lesion boundary와 immune–tubular niche를 복원할 후보지만, donor·slide holdout과 measured-count fidelity, HLA·IFN signal 보존을 우선 확인해야 한다.

## 4. Bibliography

Ye, J., and Q. Cui. "ASTRA enables zero-shot super-resolution of spatial transcriptomics across capture geometries." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.09.30.755663](https://doi.org/10.64898/2026.09.30.755663).
