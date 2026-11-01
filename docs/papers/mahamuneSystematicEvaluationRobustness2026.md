---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# Robustness of Spatial Transcriptomics Deconvolution to Cell-Type Mismatch

## 기본 정보

- Citation key: `mahamuneSystematicEvaluationRobustness2026`
- Item type: journal article
- Authors: Utkarsh M. Mahamune; Aldo Jongejan; Antoine H. C. van Kampen; Lisa G. M. van Baarsen; Perry D. Moerland
- Source: Briefings in Bioinformatics 27(5), 2026; PubMed indexed 2026-10-28
- Original: [DOI: 10.1093/bib/bbag594](https://doi.org/10.1093/bib/bbag594); [PMID: 42949539](https://pubmed.ncbi.nlm.nih.gov/42949539/)
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

두 reference dataset의 simulation에서 ST deconvolution 6종과 bulk deconvolution 2종 모두 reference에 cell type이 빠질수록 비슷하게 악화되고, 누락 cell을 전사적으로 가까운 type에 잘못 배분했다.

## 2. 연구 질문

Spatial transcriptomics reference에 실제 tissue의 cell type이 없을 때 현재 deconvolution method 중 어느 것이 더 견고한가?

## 3. 데이터와 방법

두 scRNA-seq reference dataset으로 cell-type mismatch scenario를 단계적으로 simulation했다. ST용 CARD, cell2location, RCTD, Seurat, SPOTlight, Stereoscope와 bulk용 MuSiC, SCDC를 비교하고 cell-type proportion 추정 성능과 누락 cell의 재배분 양상을 분석했다.

## 4. 핵심 결과

- Mismatch가 없을 때 cell2location이 가장 강했고 Seurat가 가장 낮았다.
- Reference에서 빠진 cell type 수에 비례해 모든 방법의 성능이 감소했다.
- Baseline 대비 상대 감소는 방법 간 비슷해 특별히 견고한 방법은 없었고, 누락 proportion은 transcriptionally similar한 남은 cell type으로 이동했다.

## 5. 한계

핵심 결론은 두 reference dataset의 simulation에 기반하며 실제 diseased tissue의 unknown state와 technical artifact를 모두 재현하지는 않는다. 새 deconvolution algorithm을 제안한 연구도 아니다.

## 6. 재현 또는 활용 포인트

Known cell type을 하나씩 제거하는 leave-one-type-out stress test를 적용하고 total proportion뿐 아니라 잘못 흡수한 recipient cell type을 기록한다. Reference composition과 marker overlap을 함께 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

정상 신장 reference에 rejection-specific activated tubular·endothelial·immune state가 없으면 기존 cell type으로 강제 배분될 수 있음을 보여준다. Allograft ST 분석 전 mismatch stress test와 unknown component가 필요하다.

## 8. 관련 키워드

- Transcriptomics / Platform
- scRNA-seq
- spatial transcriptomics
- deconvolution benchmark

## 9. Bibliography

Mahamune, Utkarsh M., et al. “Systematic Evaluation of Robustness of Deconvolution Methods for Spatial Transcriptomics Data in Case of Cell Type Mismatch.” _Briefings in Bioinformatics_ 27, no. 5 (2026): bbag594. [https://doi.org/10.1093/bib/bbag594](https://doi.org/10.1093/bib/bbag594).
