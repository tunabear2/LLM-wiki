---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# Comprehensive evaluation of structural variation detection for germline and somatic analysis with long-read sequencing data

## 기본 정보

- Citation key: `shiComprehensiveEvaluationStructural2026`
- Item type: journalArticle
- Authors: Hua Shi; Yihang Lin; Dachen Liu; Hongfeng Wu; Ashidi Nor Mat Isa; Leyi Wei; Quan Zou; Xiang Chen
- Journal: Briefings in Bioinformatics 27(5)
- DOI: 10.1093/bib/bbag530
- PMID: 42803633
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42803633/); [DOI](https://doi.org/10.1093/bib/bbag530); [benchmark](https://github.com/model-lab/LR-SV-Benchmark)
- Source/date: journal publication 2026-09-01; PubMed indexed 2026-09-28
- 주 카테고리: DNA-seq / Variant Analysis

## 1. 한 줄 요약

PacBio CLR·CCS와 Oxford Nanopore의 20개 dataset에서 14개 long-read structural-variant caller를 germline·somatic, genotyping, complex event와 coverage 조건별로 함께 평가한 실용적 benchmark다.

## 2. 연구 질문

Long-read platform, sequencing depth와 germline·somatic 목적이 달라질 때 어떤 SV caller가 안정적인 detection·genotyping 성능을 보이며, 복합 SV와 tumor sample에서는 도구 선택이 어떻게 달라져야 하는가?

## 3. 데이터와 방법

PacBio Continuous Long Reads, Circular Consensus Sequencing과 Oxford Nanopore를 포함한 20개 core dataset에서 14개 caller를 비교했다. Sensitivity·precision 외에 baseline artefact rate, Mendelian discordance rate와 Mendelian inheritance error rate를 포함한 12개 차원으로 germline, somatic, genotyping 및 inversion·duplication·translocation 성능을 평가했다.

## 4. 핵심 결과

Germline SV detection에서는 DeBreak, cuteSV2와 SVDF가 안정적이고 정확했다. cuteSV2와 SVHunter는 depth 변화에도 genotyping accuracy가 비교적 일정했으며, Severus와 cuteSV2는 inversion·duplication·translocation 같은 complex SV에 강했다. Tumor dataset에서는 somatic 전용 caller가 germline caller보다 우수했고, Severus와 SAVANA가 전반적으로 강한 반면 nanomonsv는 low-coverage 조건에서 장점이 있었다.

## 5. 한계

순위는 사용한 truth set, platform, coverage, sample type, caller version과 parameter에 종속된다. 제한된 benchmark sample이 실제 임상 종양의 purity·heterogeneity나 다양한 ancestry의 germline complexity를 모두 대표하지 않는다. 이후 caller update나 새로운 chemistry에는 동일 framework로 재평가가 필요하다.

## 6. 재현 또는 활용 포인트

- Code와 benchmark resource: [model-lab/LR-SV-Benchmark](https://github.com/model-lab/LR-SV-Benchmark)
- Platform, read N50, depth, truth-set version과 caller parameter를 함께 고정한다.
- Detection과 genotyping, simple과 complex SV, germline과 somatic 결과를 분리해 보고한다.
- 한 caller의 평균 순위보다 연구 조건과 가장 가까운 benchmark stratum을 기준으로 선택한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Transcriptomics와 직접 연결은 약하지만 donor·recipient genome의 SV를 eQTL·gene-expression 변화와 통합하거나 이식 후 clonal·malignant complication을 long-read로 분석할 때 caller 선택 근거가 된다. 낮은 coverage의 임상 sample에서는 전체 평균보다 low-coverage somatic 결과를 우선 참고해야 한다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- Long-read sequencing
- Structural variant
- Germline calling
- Somatic calling
- Benchmark
- Genotyping

## 9. Bibliography

Shi, Hua, Yihang Lin, Dachen Liu, Hongfeng Wu, Ashidi Nor Mat Isa, Leyi Wei, Quan Zou, and Xiang Chen. “Comprehensive Evaluation of Structural Variation Detection for Germline and Somatic Analysis with Long-Read Sequencing Data.” Briefings in Bioinformatics 27, no. 5 (2026). [https://doi.org/10.1093/bib/bbag530](https://doi.org/10.1093/bib/bbag530).
