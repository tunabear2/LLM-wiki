---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# GLARE: Genomic Language Model for Automated Repetitive Element Classification

## 기본 정보

- Citation key: `haasGLAREGenomicLanguage2026`
- Item type: preprint
- Authors: Nathaniel Haas; Tomas Bruna
- Source: bioRxiv v1, posted 2026-10-11 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.06.757139](https://doi.org/10.64898/2026.10.06.757139); [code](https://code.jgi.doe.gov/NHaas/glare)
- 주 카테고리: `Bio AI`
- 관련 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

GLARE는 harmonized PanTEon·Repbase reference로 Nucleotide Transformer v3를 fine-tune해 taxon·database·sequence degradation shift에 강한 transposable-element 분류기를 만든다.

## 2. 연구 질문

Reference label 불일치와 taxonomic shift, 오래되어 훼손된 서열에서도 genomic language model이 기존 TE classifier보다 안정적으로 superfamily를 분류할 수 있는가?

## 3. 데이터와 방법

PanTEon benchmark v1.6.1과 Repbase 31.03의 label을 11 order·32 superfamily vocabulary로 통합했다. 여러 genomic LM backbone을 비교해 Nucleotide Transformer v3를 선택하고 reverse-complement augmentation과 긴 서열의 overlapping-window aggregation을 적용했다. 아홉 기존 classifier, source별 test set, Poales·Arthropoda·Fungi clade holdout, synthetic decay와 독립 degraded library에서 평가했다.

## 4. 핵심 결과

- PanTEon 23,043 records와 Repbase 11,778 records에서 weighted superfamily F1이 각각 0.965와 0.946이었다.
- PanTEon의 30-superfamily 비교에서 weighted F1 0.966으로 아홉 classifier를 앞섰다.
- 세 taxonomic rank holdout과 sequence-decay 평가에서 가장 강한 일반화를 보였고, 두 database를 함께 학습하면 source 이동 손실이 줄었다.

## 5. 한계

Record-level random split에는 가까운 서열이 train/test에 함께 들어갈 수 있다. Clade holdout은 rank마다 하나뿐이고 synthetic decay가 실제 진화율을 직접 모사하지 않는다. GLARE는 TE를 탐지하거나 boundary를 정하는 도구가 아니며 완전한 de novo annotation workflow 검증은 남아 있다.

## 6. 재현 또는 활용 포인트

Random split보다 taxonomic holdout을 우선하고 database별 결과를 따로 보고한다. Reverse-complement 처리, window overlap, label mapping table, non-TE rejection을 고정한 뒤 de novo repeat library에서 detection tool과 결합해 평가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

RNA-seq에서 transposable-element expression을 해석할 때 reference annotation의 누락·오분류를 점검하는 upstream 도구가 될 수 있다. 다만 human transplant cohort에서 expression 또는 rejection association을 직접 검증한 연구는 아니다.

## 8. 관련 키워드

- genomic language model
- transposable element
- repetitive-element annotation
- taxonomic generalization

## 9. Bibliography

Haas, Nathaniel, and Tomas Bruna. “GLARE: Genomic Language Model for Automated Repetitive Element Classification.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.06.757139](https://doi.org/10.64898/2026.10.06.757139).
