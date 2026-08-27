---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-10'
tags:
- wiki/paper
---

# Clifti-GPT: privacy-preserving federated fine-tuning and transferable inference of foundation models on clinical single-cell data

## 기본 정보

- Citation key: `bakhtiariCliftiGPTPrivacyPreserving2026`
- Item type: journalArticle
- Authors: Mohammad Bakhtiari; Maria Louise Elkjaer; Ali Oğuz Can; Fabian Theis; Mhaned Oubounyt; Jan Baumbach
- DOI: 10.1186/s13040-026-00582-w
- PMID: 42557585
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42557585/)
- Source/date: PubMed / BioData Mining, published 2026-08-05; indexed 2026-08-06

## 1. 한 줄 요약

Clifti-GPT는 secure multi-party computation을 결합한 federated scGPT fine-tuning과 reference mapping으로 임상 scRNA-seq를 중앙화하지 않고도 중앙집중식 baseline에 가까운 성능을 낸다.

## 2. 왜 중요한가

여섯 dataset에서 cell-type classification과 reference mapping을 평가하며, 최대 30개 client에서도 중앙집중식 scGPT 대비 성능 저하를 작게 유지한다. Raw patient data, embedding, local model을 공유하지 않는 설계는 다기관 임상 single-cell 연구의 privacy와 governance 제약을 직접 다룬다.

## 3. 내 연구에 연결할 점

기관 간 원자료 이동이 어려운 kidney transplant biopsy cohort에서 rejection cell-state annotation과 reference mapping을 공동 학습하는 후보 구조다. 다만 center별 batch effect, gene vocabulary 정렬, donor-level holdout을 federated protocol 안에서 별도로 검증해야 한다.

## 4. Bibliography

Bakhtiari, Mohammad, Maria Louise Elkjaer, Ali Oğuz Can, Fabian Theis, Mhaned Oubounyt, and Jan Baumbach. "Clifti-GPT: privacy-preserving federated fine-tuning and transferable inference of foundation models on clinical single-cell data." _BioData Mining_, 2026. [https://doi.org/10.1186/s13040-026-00582-w](https://doi.org/10.1186/s13040-026-00582-w).
