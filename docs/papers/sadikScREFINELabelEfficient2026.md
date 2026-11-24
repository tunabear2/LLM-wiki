---
type: paper
status: reference
rag_priority: high
updated: '2026-11-24'
tags:
- wiki/paper
---

# scREFINE: Label-efficient refinement of frozen scGPT embeddings for single-cell RNA-seq clustering

## 기본 정보

- Citation key: `sadikScREFINELabelEfficient2026`
- Item type: journal article
- Authors: Shahriar Sadik; Yan Liu; Mohammad Maruf Hasan; Sharmin Jahan Shorna; Sheng Guan; Zarin Tasnim Progga
- DOI: 10.1016/j.compbiolchem.2026.109535
- PMID: 43025064
- URL: [Link](https://doi.org/10.1016/j.compbiolchem.2026.109535)
- Source/date: Computational Biology and Chemistry, published 2026-11-11; PubMed indexed 2026-11-14

## 1. 한 줄 요약

scREFINE은 frozen scGPT embedding을 5% label과 stability-aware neighborhood regularization으로 보정해 소량 지도학습 single-cell clustering을 수행한다.

## 2. 왜 중요한가

다섯 scRNA-seq dataset에서 동일한 leakage-free protocol 아래 비교했으며, 성능 향상의 주된 원인은 pretrained embedding 자체보다 task-specific refinement였다. Dataset 수가 적어 paired test는 관행적 유의수준을 넘지 못했다는 한계도 명시한다.

## 3. 내 연구에 연결할 점

소수의 병리·cell-state label만 있는 rejection cohort에서 활용할 수 있지만, 5% label을 cell 단위로 무작위 추출하면 donor leakage가 생길 수 있다. Donor 단위 label budget과 unseen-center clustering으로 다시 평가해야 한다.

## 4. Bibliography

Sadik, Shahriar, Yan Liu, Mohammad Maruf Hasan, Sharmin Jahan Shorna, Sheng Guan, and Zarin Tasnim Progga. "scREFINE: Label-efficient refinement of frozen scGPT embeddings for single-cell RNA-seq clustering." _Computational Biology and Chemistry_ 126 (2026): 109535. [https://doi.org/10.1016/j.compbiolchem.2026.109535](https://doi.org/10.1016/j.compbiolchem.2026.109535).
