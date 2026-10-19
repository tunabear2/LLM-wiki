---
type: paper
status: reference
rag_priority: high
updated: '2026-10-19'
tags:
- wiki/paper
---

# BioMod: Biological Module Tokenization for Single-Cell Foundation Modeling

## 기본 정보

- Citation key: `mengBioModBiologicalModule2026`
- Item type: preprint
- Authors: L. Meng; J. Zhu; B. Han; Y. Zang; W. Li; K. Zong; J. Zhong; Y. Yang; J. Liu; J. Jia; R. Sun; G. Yu; J. Han; Y. Chen; L. Zhang; J. Xu
- DOI: 10.64898/2026.10.12.758490
- URL: [Link](https://doi.org/10.64898/2026.10.12.758490)
- Source/date: bioRxiv v1, posted 2026-10-13

## 1. 한 줄 요약

BioMod는 gene 대신 660개 중첩 biological module을 token으로 사용해 7,300만 human cell에서 pretrain한 5천만-parameter scFM이다.

## 2. 왜 중요한가

Curated pathway와 data-driven gene program을 중간 표현 단위로 삼아 입력을 압축하고 single-GPU inference를 가능하게 한다. Cell-type annotation, zero-shot batch integration, perturbation 및 drug-response task에서 compact architecture의 경쟁력을 제시한다.

## 3. 내 연구에 연결할 점

Rejection의 IFN, cytotoxicity, endothelial injury 및 tubular stress module을 직접 추적할 수 있어 해석 가능한 경량 후보 모델이다. Module 정의가 renal biology를 누락하거나 label 정보를 새지 않는지 donor·center holdout과 gene-level ablation으로 확인해야 한다.

## 4. Bibliography

Meng, L., et al. "BioMod: Biological Module Tokenization for Single-Cell Foundation Modeling." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.12.758490](https://doi.org/10.64898/2026.10.12.758490).
