---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Benchmarking Statistical Methods for Differential Composition Analysis in Population-Scale Single-Cell Data

## 기본 정보

- Citation key: `wuBenchmarkingStatisticalMethods2026`
- Item type: preprint
- Authors: Weiwei Wu; Mengyu He; Yi-Juan Hu; Chang Su
- Source: bioRxiv v1, posted 2026-11-05 (not peer reviewed)
- Original: [DOI: 10.64898/2026.11.04.764099](https://doi.org/10.64898/2026.11.04.764099)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

세 population-scale scRNA-seq dataset의 real-data permutation과 simulation에서 12개 differential-composition 방법을 비교해 다수 방법의 false discovery inflation을 드러냈다.

## 2. 연구 질문

Zero inflation, overdispersion, compositional constraint, covariate가 있는 donor-level cell count에서 condition별 cell-type proportion 차이를 어떤 방법이 보정력 있게 검정하는가?

## 3. 데이터와 방법

ROSMAP snRNA-seq, ILD scRNA-seq, OneK1K cohort를 사용했다. DCATS, propeller, sccomp, scCODA, LOCOM, ANCOM-BC/BC2, DESeq2, CLR 기반 regression·Wilcoxon, quasi-binomial 등 12개 방법을 real-data agreement, label permutation, data-informed simulation으로 비교했다.

## 4. 핵심 결과

- 실제 dataset에서 방법 간 발견 일치도가 낮았다.
- Permutation과 simulation에서 대부분 방법이 과도한 false discovery를 보였다.
- LOCOM이 FDR을 제어하면서 좋은 power를 유지해 가장 안정적이었고, ANCOM-BC와 CLR-transformed linear regression이 뒤를 이었다.

## 5. 한계

결론은 세 cohort의 cell-count 구조와 simulation mechanism에 의존한다. 일부 Bayesian method의 calibration은 계산비용 때문에 완전히 평가하지 못했다. 재현 코드는 심사자용 archive로만 제공되며 공개 repository는 출판 시점으로 미뤄져 있다.

## 6. 재현 또는 활용 포인트

Cell이 아니라 donor를 추론 단위로 두고 cell-type count matrix에 biological·technical covariate를 포함한다. Negative-control permutation, FDR calibration, power, runtime을 함께 보고 rare cell type과 zero-heavy setting을 별도 층화한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection과 cell-type proportion의 연관을 단순 cell-level test로 검정하지 말아야 한다는 기준이다. Donor 수가 적고 조성이 크게 바뀌는 biopsy에서는 LOCOM·ANCOM-BC·CLR regression을 비교하고 histology/CyTOF count로 방향을 확인해야 한다.

## 8. 관련 키워드

- differential composition
- population-scale scRNA-seq
- false discovery rate
- compositional data

## 9. Bibliography

Wu, Weiwei, et al. “Benchmarking Statistical Methods for Differential Composition Analysis in Population-Scale Single-Cell Data.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.04.764099](https://doi.org/10.64898/2026.11.04.764099).
