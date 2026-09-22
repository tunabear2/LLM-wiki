---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# A real-data-driven framework for evaluating differential transcript usage

## 기본 정보

- Citation key: `zhangRealDataDrivenFramework2026`
- Item type: journalArticle
- Authors: Chenxing Zhang; Jun Liu; Qi Zhao; Huilong Yin; Angang Yang; Minhua Zheng; Rui Zhang
- Journal: Advanced Science
- DOI: 10.1002/advs.77756
- PMID: 42755034
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42755034/); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13586480/); [DOI](https://doi.org/10.1002/advs.77756)
- Source/date: electronically published 2026-09-17; PubMed indexed 2026-09-18
- 주 카테고리: Transcriptomics / Platform
- 교차 카테고리: Bulk RNA-seq; scRNA-seq

## 1. 한 줄 요약

RBP perturbation과 검증된 RBP–transcript interaction으로 실제 생물학적 reference를 만들고 transcript-set enrichment score를 도입해, short/long-read bulk·single-cell·spatial DTU 방법 10개를 비교했다.

## 2. 연구 질문

Simulation 가정에 의존하지 않고 실제 조절기전으로 differential transcript usage method를 평가하며, data type에 따라 달라지는 method ranking을 생물학적으로 해석할 수 있는가?

## 3. 데이터와 방법

RBP knockout/knockdown RNA-seq와 실험적으로 검증된 RBP–transcript interaction을 결합해 reference transcript set을 정의했다. Ranked result에서 reference transcript가 얼마나 우선되는지 측정하는 transcript set enrichment score를 제안하고 reliability, unbiasedness, stability와 robustness를 검증했다. Long/short-read bulk, single-cell과 spatial data에서 대표 DTU method 10개를 평가했다.

## 4. 핵심 결과

Method 사이 성능은 data type에 따라 달랐고, 제안 framework는 simulation-only benchmark가 놓치는 생물학적 우선순위를 구분했다. Transcript-level RBP activity prediction으로 확장했을 때 gene-level differential-expression strategy보다 실제로 perturb된 RBP를 더 일관되게 회수했다. 동료심사 논문이며 full text가 PMC에 공개돼 있다.

## 5. 한계

Reference가 알려진 RBP perturbation과 interaction에 의존하므로 모든 질환성 DTU의 완전한 truth set은 아니다. Perturbation의 off-target effect, expression change와 direct splicing regulation을 완전히 분리하기 어렵고, 결과를 clinical isoform biomarker 성능으로 곧바로 일반화할 수 없다.

## 6. 재현 또는 활용 포인트

- RBP perturbation, interaction evidence와 transcript annotation version을 고정한다.
- Reference-set 구성과 평가 대상 method 결과를 분리해 circularity를 점검한다.
- Short/long-read, bulk/single-cell/spatial 결과를 같은 평균 점수로 뭉개지 않는다.
- Top transcript뿐 아니라 rank 전체의 enrichment, FDR과 method overlap을 함께 본다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection-associated isoform·splicing signal을 short-read discovery와 long-read validation 사이에서 비교할 benchmark 기준을 제공한다. 이식 적용에는 immune activation RBP perturbation과 kidney-specific isoform truth, independent cohort가 추가로 필요하다.

## 8. 관련 키워드

- Transcriptomics / Platform
- Differential transcript usage
- Long-read RNA-seq
- Alternative splicing
- RBP perturbation

## 9. Bibliography

Zhang, Chenxing, et al. “A Real-Data-Driven Framework for Evaluating Differential Transcript Usage Methods Across Long-Read Bulk, Single-Cell, and Spatial Transcriptomics.” Advanced Science (2026): e77756. [https://doi.org/10.1002/advs.77756](https://doi.org/10.1002/advs.77756).
