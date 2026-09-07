---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-07'
tags:
- wiki/paper
---

# A systematic assessment of single-cell language model configurations

## 기본 정보

- Citation key: `deWaeleSystematicAssessment2026`
- Item type: journalArticle
- Authors: Gaetan De Waele; Gerben Menschaert; Willem Waegeman
- DOI: 10.1093/nargab/lqag095
- PMID: 42626084
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42626084/)
- Source/date: PubMed / NAR Genomics and Bioinformatics, published 2026-08-20; indexed 2026-08-21

## 1. 한 줄 요약

bento-sc는 single-cell language model의 입력, count loss, masking과 pretraining task를 분리 비교해 구성별 best practice를 찾는다.

## 2. 왜 중요한가

Single-cell LM이 단순 task-specific model을 일관되게 넘지는 못했지만, 최소 전처리 count 입력, count distribution을 반영한 reconstruction loss, 높은 masking rate와 복수 pretraining objective가 더 나은 조합으로 나타났다.

## 3. 내 연구에 연결할 점

Kidney transplant corpus를 domain-adaptive pretraining할 때 normalization·binning·masking을 한꺼번에 바꾸지 말고 ablation해야 한다. Rejection annotation과 prognosis에서 scLM 이득을 PCA·scVI·supervised baseline 대비 검증할 설계 기준을 준다.

## 4. Bibliography

De Waele, Gaetan, Gerben Menschaert, and Willem Waegeman. "A systematic assessment of single-cell language model configurations." _NAR Genomics and Bioinformatics_ 8, no. 3 (2026): lqag095. [https://doi.org/10.1093/nargab/lqag095](https://doi.org/10.1093/nargab/lqag095).
