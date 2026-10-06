---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# Platform-specific count-matrix preprocessing workflows for spatial transcriptomics data analysis

## 기본 정보

- Citation key: `duPlatformSpecificSpatialPreprocessing2026`
- Item type: preprint
- Authors: Yixuan Du; et al.
- Source: bioRxiv (posted 2026-09-29; not peer reviewed)
- DOI: [10.64898/2026.09.24.753981](https://doi.org/10.64898/2026.09.24.753981); [code](https://github.com/YSTLab/ST-data-preprocessing-benchmark.git)
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

11개 spatial transcriptomics platform과 45개 dataset에서 371개 count-matrix preprocessing workflow를 비교해 universal pipeline보다 platform-specific 선택이 중요함을 보였다.

## 2. 연구 질문

segmentation·transcript processing·normalization 조합이 platform과 downstream task에 따라 얼마나 달라지며, 공통된 선택 기준을 만들 수 있는가?

## 3. 데이터와 방법

11개 ST platform, 45개 dataset, 371개 workflow를 대상으로 z-score·delta transform과 여러 segmentation/count processing 조합을 평가했다. gene panel size, gene-expression level per unit, downstream consistency와 workflow runtime을 비교했다.

## 4. 핵심 결과

단일 universal winner는 없었고 platform과 data structure에 맞춘 workflow가 일관성을 높였다. z-score가 큰 영향 요인이었으며 delta transform 계열이 여러 setting에서 강했지만, panel size와 expression level이 선택을 좌우했다.

## 5. 한계

매우 큰 dataset에서는 일부 방법이 6시간 내 완료되지 않았고, 모든 platform에서 동일한 cell-volume ground truth를 얻지 못했다. 일부 비교는 scRNA matching에 의존하며 preprint 결과이므로 새 chemistry에는 재검증이 필요하다.

## 6. 재현 또는 활용 포인트

신장 biopsy를 platform·section·donor 단위로 분리해 segmentation부터 count transform까지 workflow를 고정한다. 최종 downstream marker뿐 아니라 cell boundary, runtime, panel size와 normalization sensitivity를 함께 기록한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Visium HD·Xenium 등 신장 생검 spatial data의 cell-state 비교에서 preprocessing 선택이 biological signal인지 artifact인지 구분하는 기준을 제공한다. rejection cohort에서는 동일 tissue block의 workflow sensitivity와 scRNA reference transfer를 함께 점검할 수 있다.

## 8. 관련 키워드

- spatial transcriptomics
- preprocessing benchmark
- segmentation
- platform effect

## 9. Bibliography

Du, Yixuan, et al. “Platform-specific Count-matrix Preprocessing Workflows for Spatial Transcriptomics Data Analysis.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.24.753981](https://doi.org/10.64898/2026.09.24.753981).
