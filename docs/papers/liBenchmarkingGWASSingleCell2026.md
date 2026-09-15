---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# Benchmarking methods integrating GWAS and single-cell transcriptomic data for mapping trait-cell type associations

## 기본 정보

- Citation key: liBenchmarkingGWASSingleCell2026
- Item type: medRxiv preprint
- Authors: An Li; Patrick Allen; Yang Wang; Hongxiang Cui; Tong Lin; Yujie Sun; Xiaoyu Wang; Xiaoyu Tan; Abigail Walker; Shijie Wang; Zilong Yao; Rui Zhao; Jian Yang; Shiquan Yao; Jörgen Hjerling-Leffler; Patrick F. Sullivan; Naomi R. Wray; Jian Zeng
- DOI: 10.1101/2025.05.24.25328275
- URL: [medRxiv v3](https://www.medrxiv.org/content/10.1101/2025.05.24.25328275v3); [DOI](https://doi.org/10.1101/2025.05.24.25328275)
- Source/date: medRxiv revised v3, 2026-09-12; first posted 2025-05-25
- 주 카테고리: GWAS
- 교차 카테고리: scRNA-seq

## 1. 한 줄 요약

GWAS와 scRNA-seq를 통합해 trait-associated cell type을 찾는 20개 방법을 비교하고, 상보적 결과를 Cauchy 방식으로 결합한 CATCH가 power와 false-positive control 사이에서 가장 일관된 성능을 보였다고 보고한 preprint다.

## 2. 연구 질문

Single-cell-specific gene에서 GWAS enrichment를 검사하는 접근과 GWAS-prioritized gene으로 cell type을 scoring하는 접근 중 어떤 방법이 안정적인가, 그리고 서로 다른 방법을 결합하면 trait–cell-type mapping을 개선할 수 있는가?

## 3. 데이터와 방법

저자들은 `single cell to GWAS`와 `GWAS to single cell`의 두 전략에 속한 20개 trait–cell-type mapping method를 문헌 기반으로 정리했다. PubMed evidence와 LLM-assisted literature synthesis를 이용해 benchmark를 구성하고 simulation과 real-data evaluation을 수행했다. 또한 상보적인 방법의 p-value를 Cauchy combination으로 합치는 CATCH를 제안했다.

## 4. 핵심 결과

CATCH는 simulation과 real-data benchmark 전반에서 높은 statistical power와 효과적인 false-positive control을 가장 일관되게 유지했다고 보고됐다. Cell-type specificity metric, GWAS statistical power, scRNA-seq reference dataset의 다양성이 성능을 좌우하는 핵심 요인으로 확인됐다.

## 5. 한계

2026-09-12에 개정된 peer-review 전 preprint다. 초록에는 simulation parameter, 사용 trait와 scRNA-seq atlas, method별 정량 결과, real-data reference label 구성과 독립 검증 세부사항이 없다. Literature-informed benchmark에 LLM-assisted synthesis가 포함되므로 재현에는 검색 corpus, prompt와 model 설정의 명시가 필요하지만 이 정보도 초록에서는 확인되지 않는다.

## 6. 재현 또는 활용 포인트

- 20개 방법을 같은 GWAS summary statistic, gene annotation과 scRNA-seq reference에 적용해 입력 차이를 통제한다.
- Null simulation에서 type-I error를, causal-cell simulation에서 power를 분리해 보고한다.
- GWAS sample size·heritability와 cell-type specificity metric을 바꾸는 sensitivity analysis를 수행한다.
- CATCH를 구성하는 개별 방법과 결합 결과를 함께 공개해 특정 component가 결과를 지배하는지 확인한다.
- PubMed 검색식, 문헌 cutoff, LLM model·prompt·출력 검수 절차와 software version을 기록한다.

## 7. Transcriptomics·신장이식 연구와의 연결

이식 outcome GWAS를 kidney 또는 peripheral-immune scRNA-seq atlas와 연결해 T cell, B cell, myeloid, endothelial compartment 중 유전 신호가 집중되는 세포 유형을 우선순위화하는 데 직접 활용할 수 있다. 다만 rejection-associated expression과 유전적 인과 cell type을 혼동하지 않도록 독립 cohort와 기능 검증이 필요하다.

## 8. 관련 키워드

- GWAS
- scRNA-seq
- Trait–cell-type association
- Functional interpretation
- Benchmark
- Cauchy combination test
- CATCH

## 9. Bibliography

Li, An, et al. “Benchmarking Methods Integrating GWAS and Single-cell Transcriptomic Data for Mapping Trait-cell Type Associations.” medRxiv, revised September 12, 2026. [https://doi.org/10.1101/2025.05.24.25328275](https://doi.org/10.1101/2025.05.24.25328275).
