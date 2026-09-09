---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# Benchmarking RNA-seq with the Quartet and MAQC reference materials to establish best practices for accurate alternative splicing analysis

## 기본 정보

- Citation key: wangBenchmarkingRNASeqAlternative2026
- Item type: journalArticle
- Authors: Duo Wang; Jiaxin Zhao; Qingwang Chen; Yanxi Han; Yaqing Liu; Yuanfeng Zhang; Cong Liu; Wanwan Hou; Ying Yu; Leming Shi; Yuanting Zheng; Jinming Li; Rui Zhang
- Journal: Nature Communications
- DOI: 10.1038/s41467-026-76380-z
- PMID: 42702621
- URL: [Publisher](https://www.nature.com/articles/s41467-026-76380-z); [PubMed](https://pubmed.ncbi.nlm.nih.gov/42702621/)
- Source/date: published 2026-08-08; PubMed completed/indexed 2026-09-06–07
- 주 카테고리: Bulk RNA-seq
- 교차 카테고리: Transcriptomics / Platform

## 1. 한 줄 요약

Quartet·MAQC reference와 orthogonal truth를 이용해 42개 실험실, 207개 short-read RNA-seq pipeline의 isoform·alternative-splicing 정확도를 비교한 대규모 benchmark다.

## 2. 연구 질문

Short-read RNA-seq에서 splice junction, isoform abundance, differential isoform과 event-level splicing을 얼마나 정확히 측정할 수 있으며 어떤 실험·분석 조합이 최선인가?

## 3. 데이터와 방법

Quartet와 MAQC RNA reference를 42개 실험실에서 측정하고 207개 bioinformatics pipeline을 비교했다. 통합 long-read reference의 10,218개 isoform과 6,032개 splicing event, RT-qPCR로 확인한 121개 isoform·59개 event, 알려진 mixing ratio를 ground truth로 사용했다.

## 4. 핵심 결과

데이터 품질과 sequencing depth가 junction 검출과 isoform·event 정량 및 차등분석을 일관되게 개선했다. 최적 pipeline의 isoform-level 정량 Pearson correlation은 0.79, differential analysis MCC는 0.68이었지만 event-level 값은 각각 0.41로 더 낮았다. Novel junction의 평균 false-negative rate도 45.1%로 높아 short-read의 한계를 드러냈다.

## 5. 한계

Reference material과 제한된 sample composition을 사용했으므로 임상조직의 degradation·heterogeneity를 완전히 대변하지 않는다. 낮은 발현·coverage와 높은 compositional complexity는 pipeline 최적화 후에도 남았으며, 도구 버전과 annotation 선택에 따라 순위가 달라질 수 있다.

## 6. 재현 또는 활용 포인트

- 실험 QC, isoform/event quantification, differential analysis를 분리해 평가한다.
- Long-read consensus, RT-qPCR, mixing truth처럼 서로 다른 ground truth를 함께 두는 설계가 강점이다.
- 신장 biopsy에서는 library strandedness, depth, RNA quality와 annotation version을 성능표와 함께 기록해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

거부반응에서 alternative splicing과 isoform biomarker를 탐색할 때 gene-level DEG 정확도를 그대로 기대하면 안 된다는 기준을 제공한다. 후보 event는 short-read discovery 후 targeted PCR 또는 long-read로 확인하는 것이 안전하다.

## 8. 관련 키워드

- Bulk RNA-seq
- Alternative splicing
- Isoform quantification
- MAQC
- Quartet
- Benchmark

## 9. Bibliography

Wang, Duo, et al. “Benchmarking RNA-seq with the Quartet and MAQC Reference Materials to Establish Best Practices for Accurate Alternative Splicing Analysis.” Nature Communications 17 (2026): 9535. [https://doi.org/10.1038/s41467-026-76380-z](https://doi.org/10.1038/s41467-026-76380-z).
