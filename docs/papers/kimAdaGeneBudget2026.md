---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-07'
tags:
- wiki/paper
---

# AdaGeneBudget: Cell-Adaptive Gene-Token Allocation for Efficient Single-Cell Foundation Models

## 기본 정보

- Citation key: `kimAdaGeneBudget2026`
- Item type: preprint
- Authors: Dohee Kim; Uiwon Hwang
- DOI: 10.64898/2026.08.06.743174
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.08.06.743174v1)
- Source/date: bioRxiv v1, posted 2026-08-12

## 1. 한 줄 요약

AdaGeneBudget은 cell별 발현과 biological relevance에 따라 제한된 gene-token budget을 배분해 기존 scFM embedding 추출 비용을 줄인다.

## 2. 왜 중요한가

고정 top-gene 또는 HVG 선택과 달리 cell state에 맞춘 token allocation으로 희귀 cell identity, lineage marker와 stimulation-induced embedding direction을 보존하려 한다. 일부 annotation에서는 HVG가 더 강해 효율성과 task 성능의 trade-off도 드러난다.

## 3. 내 연구에 연결할 점

대규모 transplant biopsy cell atlas에 scGPT·Geneformer·scPRINT를 적용할 때 HLA·IFN·cytotoxicity·endothelial marker가 token compression 뒤에도 유지되는지 점검하는 실용적 후보이며, 희귀 rejection cell state를 별도로 평가해야 한다.

## 4. Bibliography

Kim, Dohee, and Uiwon Hwang. "AdaGeneBudget: Cell-Adaptive Gene-Token Allocation for Efficient Single-Cell Foundation Models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.08.06.743174](https://doi.org/10.64898/2026.08.06.743174).
