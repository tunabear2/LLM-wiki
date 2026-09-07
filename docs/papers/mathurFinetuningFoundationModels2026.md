---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-07'
tags:
- wiki/paper
---

# Finetuning Foundation Models for Temporal Clinical Transcriptomics Data

## 기본 정보

- Citation key: `mathurFinetuningFoundationModels2026`
- Item type: journalArticle
- Authors: Sachin Mathur; Alexander Kagan; Peyman Passban; Hamid Mattoo; Euxhen Hasanaj; Ziv Bar-Joseph
- DOI: 10.1093/bioinformatics/btag640
- PMID: 42658019
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42658019/)
- Source/date: PubMed / Bioinformatics, published and indexed 2026-08-27

## 1. 한 줄 요약

Foundation-model gene embedding을 healthy tissue expression으로 fine-tune한 뒤 temporal GNN에 넣어 네 염증성 질환의 치료 반응 경로를 모델링한다.

## 2. 왜 중요한가

Noise가 크고 표본이 작은 longitudinal clinical transcriptomics에서 pretrained gene representation과 interaction graph를 결합해 responder/non-responder의 시간적 pathway 차이를 찾는다. Single-cell FM 자체의 benchmark보다는 foundation gene embedding의 임상 시계열 전이 사례다.

## 3. 내 연구에 연결할 점

이식 전후 또는 rejection 치료 전후 bulk/pseudobulk expression에서 response trajectory를 모델링하는 직접적인 설계 참고다. Healthy-tissue fine-tuning이 transplant-specific immune program을 지우지 않는지와 patient-level temporal split을 검증해야 한다.

## 4. Bibliography

Mathur, Sachin, Alexander Kagan, Peyman Passban, Hamid Mattoo, Euxhen Hasanaj, and Ziv Bar-Joseph. "Finetuning Foundation Models for Temporal Clinical Transcriptomics Data." _Bioinformatics_, 2026, btag640. [https://doi.org/10.1093/bioinformatics/btag640](https://doi.org/10.1093/bioinformatics/btag640).
