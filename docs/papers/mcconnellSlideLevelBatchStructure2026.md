---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# Slide-level batch structure limits histology-guided supervision of transcriptomic foundation models

## 기본 정보

- Citation key: `mcconnellSlideLevelBatchStructure2026`
- Item type: preprint
- Authors: U. McConnell; K. Nonchev; V. H. Koelzer; G. Rätsch
- DOI: 10.64898/2026.09.30.755585
- URL: [Link](https://doi.org/10.64898/2026.09.30.755585)
- Source/date: bioRxiv v1, posted 2026-10-05

## 1. 한 줄 요약

세 transcriptomic FM에서 matched H&E supervision은 cross-donor annotation을 일관되게 개선하지 못했고, slide identity가 지배하는 저차원 expression embedding과 held-out gene predictivity 저하가 한계로 나타났다.

## 2. 왜 중요한가

Morphology-guided supervision이 frozen representation의 기존 정보를 재배치할 수는 있어도 보존되지 않은 신호를 복구하지는 못한다는 실증적 경고다. Aggregate 성능만 보면 일부 형태적으로 뚜렷한 class의 이득과 transcriptome 전반의 손실을 함께 놓칠 수 있다.

## 3. 내 연구에 연결할 점

Kidney transplant H&E–spatial model에서는 slide·center·donor identity를 먼저 probe하고, donor-held-out annotation과 HLA·IFN·endothelial gene predictivity를 동시에 평가해야 한다. Slide-random split은 피해야 한다.

## 4. Bibliography

McConnell, U., K. Nonchev, V. H. Koelzer, and G. Rätsch. "Slide-level batch structure limits histology-guided supervision of transcriptomic foundation models." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.09.30.755585](https://doi.org/10.64898/2026.09.30.755585).
