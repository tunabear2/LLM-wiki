---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-03'
tags:
- wiki/paper
---

# Inflammation-linked aging signals in frozen single-cell foundation models: donor-aware detection and robustness testing

## 기본 정보

- Citation key: `kendiukhovInflammationLinkedAging2026`
- Item type: journalArticle
- Authors: Ihor Kendiukhov
- DOI: 10.1007/s10522-026-10471-8
- PMID: 42509463
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42509463/)
- Source/date: PubMed / Biogerontology, published 2026-07-28

## 1. 한 줄 요약

Frozen scGPT와 Geneformer가 PBMC의 노화 관련 NF-κB·IFN-γ 염증 신호를 담지만 age prediction은 50-component PCA보다 낫지 않으며, donor와 cell-type composition을 맞춘 검증이 해석의 핵심임을 보인다.

## 2. 왜 중요한가

약 2,000 donors의 4–5 million cells에서 probe, sparse autoencoder, activation intervention, composition-matched resampling을 단계적으로 적용한다. FM의 장점은 단순 예측력보다 해석 가능한 feature와 개입 실험에 있었고, cell composition을 통제하면 효과가 약해져 donor-aware negative control의 필요성이 드러났다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection의 IFN, TNF/NF-κB, immune-aging signal은 rejection label뿐 아니라 recipient age와 infiltrating-cell composition의 영향을 받을 수 있다. Frozen scFM embedding을 해석할 때 donor-level split, cell-type-matched resampling, PCA baseline을 함께 두어 alloimmune signal과 confounding을 분리해야 한다.

## 4. Bibliography

Kendiukhov, Ihor. "Inflammation-linked aging signals in frozen single-cell foundation models: donor-aware detection and robustness testing." _Biogerontology_ 27, no. 4 (2026): 132. [https://doi.org/10.1007/s10522-026-10471-8](https://doi.org/10.1007/s10522-026-10471-8).
