---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# Benchmarking computational decontamination of ambient RNA

## 기본 정보

- Citation key: cargnelliBenchmarkingComputationalDecontamination2026
- Item type: journalArticle
- Authors: Cecilie Bøgh Cargnelli; Jakob Vennike Nielsen; Jesper Grud Skat Madsen
- Journal: Frontiers in Bioinformatics
- DOI: 10.3389/fbinf.2026.1844838
- PMID: 42688285
- PMCID: PMC13533975
- URL: [Open article](https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2026.1844838/full); [PubMed](https://pubmed.ncbi.nlm.nih.gov/42688285/)
- Source/date: published 2026-08-19; PubMed indexed 2026-09-03
- 주 카테고리: scRNA-seq

## 1. 한 줄 요약

Simulation과 여러 mixing ground truth에서 7개 ambient-RNA 제거법의 오염 제거와 endogenous signal 보존, downstream 분석 영향을 함께 비교한 benchmark다.

## 2. 연구 질문

Droplet single-cell·single-nucleus RNA-seq의 ambient transcript를 제거하면서 진짜 발현을 과도하게 지우지 않는 방법은 무엇이며, 정제 선택이 annotation과 integration에 어떻게 영향을 주는가?

## 3. 데이터와 방법

CellBender, DecontX, FastCAR, scAR, scCDC, SoupX, CellClear를 7개 dataset, 64개 sample, 135,561개 cell에서 비교했다. Simulation, species mixing, strain·genotype mixing, negative control을 이용하고 marker recovery, neighborhood, clustering, integration과 label transfer까지 평가했다.

## 4. 핵심 결과

모든 상황에서 이기는 단일 방법은 없었다. CellBender가 종합적으로 강했지만 계산 자원과 과보정 부담이 있었고, DecontX full과 SoupX reduced는 오염 제거와 endogenous signal 보존 사이에서 비교적 안정적인 절충을 보였다. 공격적인 제거는 downstream marker와 구조를 손상시킬 수 있었다.

## 5. 한계

Simulation은 실제 ambient RNA의 gene–gene covariance를 모두 재현하지 못하고 species mixing은 겹치지 않는 feature space를 쓴다. Strain mixing도 일부 SNP-bearing gene에만 truth가 있으며, 저품질 임상 biopsy와 모든 tissue complexity를 대변하지 않는다. 기본 parameter와 평가 metric에 따라 순위가 달라질 수 있다.

## 6. 재현 또는 활용 포인트

- 코드: [madsen-lab/AmbientRemovalBenchmark](https://github.com/madsen-lab/AmbientRemovalBenchmark)
- 공개 자료: GEO GSE218853, GSE207393, GSE147203; ArrayExpress E-MTAB-5061; 10x mixing data
- 제거율만 보지 말고 endogenous retention, marker stability, donor integration과 label transfer를 함께 점검한다.

## 7. Transcriptomics·신장이식 연구와의 연결

괴사·염증이 심한 신장이식 biopsy에서 ambient immune 또는 tubular RNA가 rejection marker와 세포형을 왜곡할 수 있다. 여러 방법을 작은 orthogonal marker set과 비교해 cohort별 정제 전략을 고르는 근거가 된다.

## 8. 관련 키워드

- scRNA-seq
- snRNA-seq
- Ambient RNA
- Decontamination
- Quality control
- Benchmark

## 9. Bibliography

Cargnelli, Cecilie Bøgh, Jakob Vennike Nielsen, and Jesper Grud Skat Madsen. “Benchmarking Computational Decontamination of Ambient RNA.” Frontiers in Bioinformatics 6 (2026): 1844838. [https://doi.org/10.3389/fbinf.2026.1844838](https://doi.org/10.3389/fbinf.2026.1844838).
