---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-31'
tags:
- wiki/paper
---

# Single-cell foundation models identify shared and divergent transcriptomic signatures of aging across invertebrates and mammals

## 기본 정보

- Citation key: `alAminSingleCellFoundation2026`
- Item type: preprint
- Authors: Mohammad Aman Ullah Al Amin; Khoi Le; Hong Qin
- DOI: 10.64898/2026.07.24.740647
- PMID: 42619888
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42619888/)
- Source/date: PubMed indexed 2026-08-20; bioRxiv v2

## 1. 한 줄 요약

scGPT와 Geneformer를 네 종 130만 cell에 fine-tuning해 cross-species aging signal을 예측하고, model encoding에 따라 중요 gene 해석이 달라짐을 보인다.

## 2. 왜 중요한가

두 모델 모두 age class를 예측했지만 scGPT는 모든 종에서 ribosomal gene을, Geneformer는 invertebrate에서 signaling·chromatin gene을 더 강조했다. 같은 task 성능이라도 tokenization과 attribution 방식이 biological interpretation을 바꿀 수 있다.

## 3. 내 연구에 연결할 점

Recipient/donor age가 rejection embedding을 교란할 수 있으므로 age-stratified donor holdout을 두고, scGPT와 Geneformer가 공통으로 지지하는 gene program과 model-specific attribution을 구분해야 한다.

## 4. Bibliography

Al Amin, Mohammad Aman Ullah, Khoi Le, and Hong Qin. "Single-cell foundation models identify shared and divergent transcriptomic signatures of aging across invertebrates and mammals." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.07.24.740647](https://doi.org/10.64898/2026.07.24.740647).
