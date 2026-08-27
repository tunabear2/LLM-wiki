---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-17'
tags:
- wiki/paper
---

# Auditing pretraining contamination in single-cell foundation model benchmarks

## 기본 정보

- Citation key: `aliAuditingPretrainingContamination2026`
- Item type: preprint
- Authors: Sarwan Ali
- DOI: 10.48550/arXiv.2607.20572
- URL: [Link](https://arxiv.org/abs/2607.20572)
- Source/date: arXiv v1, 2026-07-21

## 1. 한 줄 요약

scContam은 pretraining corpus fingerprint와 loss-based membership inference를 결합해 single-cell foundation model benchmark의 cell-level·distribution-level contamination을 감사한다.

## 2. 왜 중요한가

Geneformer, scGPT, UCE의 공개 pretraining corpus와 널리 쓰이는 scIB benchmark 사이의 중복을 구분하고, donor-matched 분석과 post-cutoff negative control로 embedding 밀집 효과를 점검한다. 모델 성능을 일반화로 해석하기 전에 training manifest와 dataset provenance를 확인해야 함을 정량화한다.

## 3. 내 연구에 연결할 점

Kidney transplant atlas나 public biopsy cohort가 scFM pretraining에 포함됐는지 먼저 감사하고, 가능하면 release cutoff 이후의 독립 center를 최종 test로 남겨야 한다. Rejection embedding 성능은 donor-matched clean subset과 contamination-stratified 결과를 함께 보고하는 것이 안전하다.

## 4. Bibliography

Ali, Sarwan. "Auditing pretraining contamination in single-cell foundation model benchmarks." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2607.20572](https://doi.org/10.48550/arXiv.2607.20572).
