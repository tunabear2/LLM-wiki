---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# EMBER: Contextualized gene representations enable compositional prediction across cellular perturbations

## 기본 정보

- Citation key: `hoEMBERContextualizedGene2026`
- Item type: preprint
- Authors: N. Ho; E. P. Xing; J. Ma
- DOI: 10.64898/2026.10.28.762655
- URL: [Link](https://doi.org/10.64898/2026.10.28.762655)
- Source/date: bioRxiv v2, revised 2026-11-01

## 1. 한 줄 요약

EMBER는 interaction-guided contrastive learning과 masked expression reconstruction으로 context-dependent gene embedding을 pretrain해 여러 perturbation task에 frozen representation을 재사용한다.

## 2. 왜 중요한가

같은 encoder를 single-gene response, digenic interaction과 multi-target drug response에 compositional probe로 연결한다. Task-specific predictor와 representation learning을 분리하면서 cross-context transfer와 genetic-interaction ranking을 개선했다.

## 3. 내 연구에 연결할 점

Rejection에서 cytokine·immunosuppressant·gene perturbation 조합을 공유 gene representation으로 비교할 수 있지만, renal cell type와 donor를 완전히 holdout하고 interaction 후보를 실험으로 검증해야 한다.

## 4. Bibliography

Ho, N., E. P. Xing, and J. Ma. "EMBER: Contextualized gene representations enable compositional prediction across cellular perturbations." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.28.762655](https://doi.org/10.64898/2026.10.28.762655).
