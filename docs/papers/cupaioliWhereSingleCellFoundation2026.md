---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Where single-cell foundation models help: a benchmark of annotation, perturbation and regulatory inference against simple baselines

## 기본 정보

- Citation key: `cupaioliWhereSingleCellFoundation2026`
- Item type: preprint
- Authors: F. A. Cupaioli; I. Merelli
- DOI: 10.64898/2026.11.03.763968
- URL: [Link](https://doi.org/10.64898/2026.11.03.763968)
- Source/date: bioRxiv v1, posted 2026-11-04

## 1. 한 줄 요약

다섯 scFM과 단순 baseline을 같은 task에서 비교하자 cross-species annotation에는 이득이 있었지만 within-species annotation과 organoid perturbation에서는 단순 설명과 replication 한계가 컸다.

## 2. 왜 중요한가

scGPT, Geneformer V1/V2, Nicheformer와 scFoundation을 annotation, zero-shot perturbation과 GRN inference에서 비교했다. Cross-species transfer는 강했지만 같은 species에서는 PCA와 비슷했고, organoid knockout 효과의 상당 부분은 target expression으로 설명되어 expression-matched control이 필요했다.

## 3. 내 연구에 연결할 점

Rejection 분석에서는 donor·clone·library replication을 확보하고 PCA·raw-count·target-expression baseline을 유지해야 한다. FM의 이득은 cross-center·cross-species·low-data 같은 조건별로 분리 보고하는 것이 적절하다.

## 4. Bibliography

Cupaioli, F. A., and I. Merelli. "Where single-cell foundation models help: a benchmark of annotation, perturbation and regulatory inference against simple baselines." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.03.763968](https://doi.org/10.64898/2026.11.03.763968).
