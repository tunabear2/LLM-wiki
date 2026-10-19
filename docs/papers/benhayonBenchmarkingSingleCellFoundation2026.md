---
type: paper
status: reference
rag_priority: high
updated: '2026-10-19'
tags:
- wiki/paper
---

# Benchmarking Single-Cell Foundation Models Reveals an Advantage in the Low-Data Regime for Cell-Type and Disease-State Prediction

## 기본 정보

- Citation key: `benhayonBenchmarkingSingleCellFoundation2026`
- Item type: preprint
- Authors: H. Benhayon; M. M. Danziger; D. Ben-Zvi; M. Rosen-Zvi
- DOI: 10.64898/2026.10.12.758421
- URL: [Link](https://doi.org/10.64898/2026.10.12.758421)
- Source/date: bioRxiv v1, posted 2026-10-12

## 1. 한 줄 요약

82개 disease dataset과 65개 cell-type dataset에서 scFM 이득은 full-data보다 class당 약 102개 이하의 label이 있는 low-data regime에 집중됐다.

## 2. 왜 중요한가

Full-data에서는 log-normalized count가 cell-type task에서 가장 좋은 foundation model보다 강했고 disease task에서도 비슷했지만, 소수 label 조건에서는 TranscriptFormer-Sapiens가 두 task 모두에서 우세했다. scFM의 적용 가치를 data regime별로 분리한 대규모 zero-shot benchmark다.

## 3. 내 연구에 연결할 점

희귀 rejection subtype이나 제한된 biopsy label에서 TranscriptFormer embedding의 sample-efficiency를 평가할 근거다. Label 수별 learning curve, donor-level split, class imbalance와 raw-count/PCA baseline을 함께 보고해야 한다.

## 4. Bibliography

Benhayon, H., M. M. Danziger, D. Ben-Zvi, and M. Rosen-Zvi. "Benchmarking Single-Cell Foundation Models Reveals an Advantage in the Low-Data Regime for Cell-Type and Disease-State Prediction." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.12.758421](https://doi.org/10.64898/2026.10.12.758421).
