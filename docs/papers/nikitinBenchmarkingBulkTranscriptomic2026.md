---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# Benchmarking bulk transcriptomic harmonization across platforms

## 기본 정보

- Citation key: `nikitinBenchmarkingBulkTranscriptomic2026`
- Item type: preprint
- Authors: Daniil Nikitin; Nikolay Borisov; Maria Savchenko; Anatoly Bobe; Mark Meerson; Alexander Nesmelov; Nazar Harutyunyan; Svetlana Paponova; Andrey Kravets; Alexandr Zaitsev; Alexandr Bagaev; Arsen Arakelyan
- DOI: 10.64898/2026.09.15.751825
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.15.751825v1); [DOI](https://doi.org/10.64898/2026.09.15.751825); [ComboBatch](https://github.com/Nikit357/ComboBatch); [pipeline](https://github.com/Nikit357/FL_harmonization)
- Source/date: bioRxiv v1, posted 2026-09-17; not peer reviewed
- 주 카테고리: Microarray
- 교차 카테고리: Bulk RNA-seq; Cancer Transcriptomics / Clinical Prediction; Transcriptomics / Platform

## 1. 한 줄 요약

ComboBatch는 4개 transcriptomic platform의 lymphoma cohort 88개를 대규모로 조합 평가해 multi-platform에서는 FSQN, RNA-seq-only에서는 SVA가 subtle subtype signal을 가장 잘 보존했다고 보고한다.

## 2. 연구 질문

Microarray와 RNA-seq를 포함한 retrospective multi-platform cohort에서 batch를 줄이면서 가까운 lymphoma subtype 사이의 약한 생물학적 차이를 보존하려면 어떤 harmonization 조합을 선택해야 하는가?

## 3. 데이터와 방법

Germinal-center B-cell lymphoma cohort 88개, sample 7,174개와 4개 platform을 사용했다. 14개 batch-removal strategy, 3개 imputation method, 33개 harmonization algorithm과 2개 post-removal 조건의 cross-product를 만들고, 실행 가능한 2,234개 접근을 87개 quality metric으로 평가했다. 다섯 scenario의 method-selection decision tree도 제시했다.

## 4. 핵심 결과

Harmonization 품질 변이에서 method 선택과 batch-removal strategy가 각각 R² 0.36과 0.26으로 가장 큰 비중을 차지했고 imputation은 0.016, post-removal은 0.01 미만이었다. Feature-specific quantile normalization은 multi-platform 구성, SVA는 RNA-seq-only 구성에서 follicular lymphoma, DLBCL과 정상 germinal-center B-cell 차이를 가장 잘 보존했다.

## 5. 한계

한 질환 계열에 집중돼 solid organ·inflammation transcriptome으로 일반화되지 않는다. 작은 batch에서는 kBET가 불안정했고 3시간을 넘긴 방법은 제외됐다. 서로 다른 metric subset으로 만든 composite score는 모든 scenario에서 직접 비교하기 어렵고, 저자 다수가 관련 산업체 소속이다. 현재 preprint다.

## 6. 재현 또는 활용 포인트

- Platform, cohort, diagnosis가 서로 confounded됐는지 먼저 표로 확인한다.
- Batch mixing과 biological subtype 보존을 여러 metric으로 동시에 평가한다.
- FSQN, SVA, ComBat와 no-correction을 외부 cohort prediction까지 비교한다.
- 공개 pipeline, Docker와 data manifest를 고정하고 시간·memory 실패도 결과에 포함한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Legacy kidney-transplant microarray와 신규 bulk RNA-seq cohort를 합칠 때 가장 직접적인 benchmark다. 거부반응 subtype과 center/platform이 겹치는 경우 batch correction이 disease signal을 지울 수 있으므로, 독립센터 holdout과 원래 platform별 성능을 반드시 함께 보고해야 한다.

## 8. 관련 키워드

- Microarray
- Bulk RNA-seq
- Cross-platform harmonization
- Batch correction
- FSQN
- SVA

## 9. Bibliography

Nikitin, Daniil, et al. “Benchmarking of Bulk Transcriptomic Harmonization Tools in a Multi-Platform B-Cell Lymphoma Cohort Identifies Feature-Specific Quantile Normalization and Surrogate Variable Analysis as Top-Performing Methods.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.15.751825](https://doi.org/10.64898/2026.09.15.751825). Preprint; not peer reviewed.
