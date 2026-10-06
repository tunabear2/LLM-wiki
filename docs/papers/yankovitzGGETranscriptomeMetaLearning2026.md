---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# GGE: General-purpose deep meta-learning for classification of human transcriptomes with limited data

## 기본 정보

- Citation key: `yankovitzGGETranscriptomeMetaLearning2026`
- Item type: preprint
- Authors: David Yankovitz; Neta Gat-Viks
- Source: bioRxiv (posted 2026-10-02; not peer reviewed)
- DOI: [10.64898/2026.09.27.754054](https://doi.org/10.64898/2026.09.27.754054); [bioRxiv v1](https://www.biorxiv.org/content/10.64898/2026.09.27.754054v1)
- 주 카테고리: `Bulk RNA-seq`
- 교차 카테고리: `Bio AI`

## 1. 한 줄 요약

GGE는 MAML과 TabNet을 결합해 public bulk RNA-seq task 사이의 공통 구조를 meta-learn하고, 작은 새 cohort의 몇 개 labeled sample로 분류기를 적응한다.

## 2. 연구 질문

기관·질환·platform이 다른 transcriptome에서 label이 적어도 meta-learned representation이 일반 supervised 학습보다 안정적인가?

## 3. 데이터와 방법

1,779개 human public bulk RNA-seq dataset에서 5,220개 classification task를 구성하고, MAML episode로 빠른 adaptation을 학습했다. TabNet attention을 사용해 task별 중요한 gene을 해석하고 ProtoNet·일반 baseline과 비교했다.

## 4. 핵심 결과

제한된 support sample에서 여러 tissue·platform에 걸친 classification이 개선되었고, attention으로 반복적으로 선택되는 gene set을 제시했다. 작은 transplant cohort처럼 label이 적은 setting에서 cross-task initialization을 사용할 수 있는 직접적인 설계 예시다.

## 5. 한계

공개 GEO 중심의 task 구성은 cohort·platform 편향을 가질 수 있고 subtle batch leakage 가능성이 있다. 저자가 설명한 구현 세부와 비교 코드는 일부 확인되지만, 독립적으로 내려받을 수 있는 고정 GGE checkpoint/완전한 pipeline은 확인되지 않아 재현성은 제한적이다.

## 6. 재현 또는 활용 포인트

patient-level split을 먼저 고정하고, support/query 간 cohort·platform leakage를 차단한다. attention gene을 생물학적 중요도로 단정하지 말고 permutation·external cohort에서 안정성을 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 rejection grade나 graft prognosis처럼 labeled biopsy가 적은 분류 문제에서 meta-learning initialization을 시험할 수 있다. 센터와 library protocol을 episode 단위로 분리하고, clinical-only 및 일반 elastic-net baseline 대비 이득을 보고해야 한다.

## 8. 관련 키워드

- bulk RNA-seq
- meta-learning
- few-shot classification
- TabNet

## 9. Bibliography

Yankovitz, David, and Neta Gat-Viks. “GGE: General-purpose Deep Meta-learning for Classification of Human Transcriptomes with Limited Data.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.27.754054](https://doi.org/10.64898/2026.09.27.754054).
