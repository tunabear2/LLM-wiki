---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# scDiagnostics: systematic assessment of cell type annotation in single-cell transcriptomics data

## 기본 정보

- Citation key: christidisScDiagnosticsSystematic2026
- Item type: journalArticle
- Authors: Anthony Christidis; Andrew R. Ghazi; Smriti Chawla; Nitesh Turaga; Robert Gentleman; Ludwig Geistlinger
- Journal: Briefings in Bioinformatics
- DOI: 10.1093/bib/bbag496
- PMID: 42704272
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42704272/); [DOI](https://doi.org/10.1093/bib/bbag496)
- Source/date: published 2026-09-01; PubMed indexed 2026-09-07
- 주 카테고리: scRNA-seq

## 1. 한 줄 요약

scDiagnostics는 reference와 query의 불일치, label-transfer 이상, 새로운 질병 상태의 강제 배정을 사후 진단하는 single-cell annotation QC framework다.

## 2. 연구 질문

자동 cell-type annotation 결과가 그럴듯해 보여도 query에 없는 reference label이나 reference에 없는 query state가 있을 때, 신뢰하기 어려운 배정을 체계적으로 찾을 수 있는가?

## 3. 데이터와 방법

Projection, reference–query alignment와 annotation anomaly 진단을 결합했다. Label noise, class imbalance, batch effect를 조절한 simulation과 brain, COVID immune, colitis 등 실제 dataset에서 여러 annotation 계열의 결과를 평가했다.

## 4. 핵심 결과

단순 전체 accuracy만으로 놓치기 쉬운 reference–query mismatch와 의심스러운 label을 진단하고, 조건별로 어떤 세포군의 annotation을 재검토해야 하는지 보여줬다. Annotation algorithm을 하나 더 제안하기보다 결과의 적합성과 실패 모드를 평가하는 층을 제공한다는 점이 핵심이다.

## 5. 한계

새 annotation을 생성하거나 biological ground truth를 보장하지 않는다. 진단 품질은 reference 선택, feature space와 upstream 전처리에 의존하며, 진단된 anomaly가 새로운 생물학인지 기술 artifact인지는 별도 실험과 marker 검토가 필요하다.

## 6. 재현 또는 활용 포인트

- 도구: [ccb-hms/scDiagnostics](https://github.com/ccb-hms/scDiagnostics)
- 재현 분석: [ccb-hms/scDiagnosticsManuscript](https://github.com/ccb-hms/scDiagnosticsManuscript)
- Annotation 전후에 donor·batch·disease state별 anomaly를 비교하고, rare state는 pseudobulk marker와 원자료로 재검토한다.

## 7. Transcriptomics·신장이식 연구와의 연결

정상 신장 atlas를 reference로 rejection biopsy를 label-transfer할 때 activated, intermediate, 희귀 immune state를 기존 cell type으로 억지 배정하는 오류를 찾는 데 직접 유용하다.

## 8. 관련 키워드

- scRNA-seq
- Cell type annotation
- Label transfer
- Reference mapping
- Quality control
- Benchmark

## 9. Bibliography

Christidis, Anthony, et al. “scDiagnostics: Systematic Assessment of Cell Type Annotation in Single-cell Transcriptomics Data.” Briefings in Bioinformatics 27, no. 5 (2026): bbag496. [https://doi.org/10.1093/bib/bbag496](https://doi.org/10.1093/bib/bbag496).
