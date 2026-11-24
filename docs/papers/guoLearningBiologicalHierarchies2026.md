---
type: paper
status: reference
rag_priority: high
updated: '2026-11-24'
tags:
- wiki/paper
---

# Learning Biological Hierarchies in Single-Cell Foundation Models

## 기본 정보

- Citation key: `guoLearningBiologicalHierarchies2026`
- Item type: preprint
- Authors: Xiangyu Guo; Ricardo Henao
- arXiv: 2611.10838
- URL: [Link](https://arxiv.org/abs/2611.10838)
- Source/date: arXiv v1, submitted 2026-11-07; backfilled 2026-11-24

## 1. 한 줄 요약

scOntoFM은 cell ontology의 lowest-common-ancestor 거리를 representation learning에 넣어 local neighborhood와 lineage hierarchy를 함께 보존하는 single-cell foundation model이다.

## 2. 왜 중요한가

Offline triplet sampling과 hierarchical objective를 결합해 cell-level·gene-level benchmark와 zero-shot task에서 기존 embedding보다 일관된 개선을 보고한다. 단순 cell-type label을 넘어 ontology 구조를 embedding geometry에 명시적으로 반영한다는 점이 핵심이다.

## 3. 내 연구에 연결할 점

Kidney rejection의 immune·endothelial·tubular subtype을 ontology 계층으로 정렬하는 후보지만, 진단 label보다 lineage proximity를 잘 맞춘 결과가 rejection-state 분리나 prognosis 향상을 보장하지는 않는다. Donor·center holdout과 rare-state recall을 별도로 검증해야 한다.

## 4. Bibliography

Guo, Xiangyu, and Ricardo Henao. "Learning Biological Hierarchies in Single-Cell Foundation Models." _arXiv_, 2026. [https://arxiv.org/abs/2611.10838](https://arxiv.org/abs/2611.10838).
