---
type: paper
status: reference
rag_priority: high
updated: '2026-10-31'
tags:
- wiki/paper
---

# Fine-Grained and Reliable Cell Classification from Pathology Images

## 기본 정보

- Citation key: `ogutFineGrainedReliable2026`
- Item type: preprint
- Authors: S. Ogut; A. Merchant; A. Vahidi; D. Jeong; S. Birk; A. Boxall; A. Miraki Feriz; M. R. Sallese; Y. Chang; P. Frossard; D. Thanou; M. Lotfollahi
- DOI: 10.64898/2026.10.20.760347
- URL: [Link](https://doi.org/10.64898/2026.10.20.760347)
- Source/date: bioRxiv v1, posted 2026-10-24

## 1. 한 줄 요약

CellBridge는 paired H&E–spatial profile 1,600만 cell로 multimodal contrastive pretraining하고 ontology-aware conformal prediction으로 근거가 부족한 세부 cell type을 상위 분류로 보수적으로 반환한다.

## 2. 왜 중요한가

Molecular supervision을 morphology representation에 옮기면서 in-domain과 OOD에서 pathology foundation model보다 fine-grained classification을 개선한다. 모든 세포에 과도하게 구체적인 label을 강제하지 않고 molecular assay가 필요한 경우를 uncertainty와 hierarchy로 표시한다.

## 3. 내 연구에 연결할 점

Kidney allograft H&E에서 immune·tubular subtype을 추정할 때 확신이 낮으면 lineage 수준으로 후퇴하는 안전한 annotation 설계에 맞다. Patient·center·scanner holdout과 measured spatial transcriptomics 검증이 필요하다.

## 4. Bibliography

Ogut, S., A. Merchant, A. Vahidi, D. Jeong, S. Birk, A. Boxall, A. Miraki Feriz, et al. "Fine-Grained and Reliable Cell Classification from Pathology Images." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.20.760347](https://doi.org/10.64898/2026.10.20.760347).
