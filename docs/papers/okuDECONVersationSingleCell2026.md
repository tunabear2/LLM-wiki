---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# DECONVersation: Single Cell Foundation Model-Derived Embeddings for Robust Cell Type Deconvolution of Bulk RNA-seq

## 기본 정보

- Citation key: `okuDECONVersationSingleCell2026`
- Item type: preprint
- Authors: A. Oku; H. Geiger; N. Robine; R. Fu
- DOI: 10.64898/2026.10.02.756356
- URL: [Link](https://doi.org/10.64898/2026.10.02.756356)
- Source/date: bioRxiv v1, posted 2026-10-09

## 1. 한 줄 요약

DECONVersation은 pretrained 또는 fine-tuned scFM embedding과 non-negative least squares를 결합해 marker 선택 없이 bulk RNA-seq cell-type proportion을 추정한다.

## 2. 왜 중요한가

Single-cell FM의 representation을 bulk deconvolution이라는 새로운 downstream task로 확장하고 MuSiC, DWLS, BayesPrism과 비교한다. Tissue-specific fine-tuning이 성능을 높였다는 결과는 범용 embedding만으로 충분하지 않을 수 있음을 보여준다.

## 3. 내 연구에 연결할 점

Kidney transplant bulk biopsy에서 immune, endothelial, tubular composition을 추정할 직접 후보지만, donor-level split과 rejection-associated state 누락, reference imbalance, absolute-fraction calibration을 별도로 검증해야 한다.

## 4. Bibliography

Oku, A., H. Geiger, N. Robine, and R. Fu. "DECONVersation: Single Cell Foundation Model-Derived Embeddings for Robust Cell Type Deconvolution of Bulk RNA-seq." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.02.756356](https://doi.org/10.64898/2026.10.02.756356).
