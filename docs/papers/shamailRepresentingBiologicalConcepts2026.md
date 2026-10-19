---
type: paper
status: reference
rag_priority: high
updated: '2026-10-19'
tags:
- wiki/paper
---

# Representing Biological Concepts as Directions in Foundation Model Embeddings

## 기본 정보

- Citation key: `shamailRepresentingBiologicalConcepts2026`
- Item type: preprint
- Authors: A. Shamail; C. D. McWhite
- DOI: 10.64898/2026.10.10.758204
- URL: [Link](https://doi.org/10.64898/2026.10.10.758204)
- Source/date: bioRxiv v1, posted 2026-10-12

## 1. 한 줄 요약

Concept activation vector로 protein 및 single-cell foundation-model embedding의 생물학적 개념을 방향 벡터로 추출하고 암 연관 expression transition을 분리한다.

## 2. 왜 중요한가

Task-specific black-box predictor 대신 재사용 가능한 linear direction으로 GO, domain, interaction interface와 cellular-state 변화를 비교한다. Single-cell concept axis에서 변하는 gene은 전통적 differential expression과 상당 부분 일치하지만 계산적으로는 별도 접근이다.

## 3. 내 연구에 연결할 점

Rejection, quiescence, IFN response 같은 concept direction을 donor holdout으로 학습해 cell-state score와 gene loading을 동시에 얻을 수 있다. 다만 batch·cell composition direction과 분리하고 DEG, spatial lesion 및 external cohort로 검증해야 한다.

## 4. Bibliography

Shamail, A., and C. D. McWhite. "Representing Biological Concepts as Directions in Foundation Model Embeddings." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.10.758204](https://doi.org/10.64898/2026.10.10.758204).
