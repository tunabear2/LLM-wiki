---
type: paper
status: reference
rag_priority: high
updated: '2026-10-19'
tags:
- wiki/paper
---

# From Closed-Set Annotation to In-Context Discovery: Biologically Grounded LLMs for Cellular Profiling

## 기본 정보

- Citation key: `gelardClosedSetAnnotation2026`
- Item type: preprint
- Authors: M. Gelard; H. Benkirane; T. Pierrot; P.-H. Cournede; B. P. de Almeida
- DOI: 10.64898/2026.10.07.757352
- URL: [Link](https://doi.org/10.64898/2026.10.07.757352)
- Source/date: bioRxiv v1, posted 2026-10-14

## 1. 한 줄 요약

CellScribe는 frozen scFM embedding을 pretrained LLM에 연결해 cell type과 transcriptional meta-program을 생성하고 in-context example로 미학습 cell type을 추론한다.

## 2. 왜 중요한가

AdaLN adapter와 multitask fine-tuning, ontology·meta-program 기반 reinforcement learning을 결합해 cell identity와 state를 하나의 generative interface에서 다룬다. Closed-set annotation을 넘어 supervised vocabulary 밖의 cell type 발견을 목표로 한다.

## 3. 내 연구에 연결할 점

Rejection biopsy에서 cell identity와 alloimmune state 설명을 함께 생성하는 interface 후보지만, 생성 text를 donor-level 통계로 간주해서는 안 된다. Ontology distance, program agreement, unknown-cell calibration과 external kidney cohort 검증이 필요하다.

## 4. Bibliography

Gelard, M., H. Benkirane, T. Pierrot, P.-H. Cournede, and B. P. de Almeida. "From Closed-Set Annotation to In-Context Discovery: Biologically Grounded LLMs for Cellular Profiling." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.07.757352](https://doi.org/10.64898/2026.10.07.757352).
