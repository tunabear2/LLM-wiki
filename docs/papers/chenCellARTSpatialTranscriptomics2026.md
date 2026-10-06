---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# CellART: a unified framework for extracting single-cell information from high-resolution spatial transcriptomics

## 기본 정보

- Citation key: `chenCellARTSpatialTranscriptomics2026`
- Item type: journalArticle
- Authors: Yuheng Chen; Yuyao Liu; Zhiwei Wang; Yeqin Zeng; Zitong Chao; Peiqi Jiang; Hao Chen; Jiguang Wang; Jiashun Xiao; Can Yang
- Journal: Nature Computational Science (version of record 2026-10-05)
- DOI: [10.1038/s43588-026-01054-1](https://doi.org/10.1038/s43588-026-01054-1); PMID: [42834230](https://pubmed.ncbi.nlm.nih.gov/42834230/)
- Code/data: [GitHub](https://github.com/YangLabHKUST/CellART); processed data in the repository
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

CellART는 image, high-resolution spatial transcriptomics와 scRNA reference를 결합해 cell boundary·cell type·gene expression을 함께 추출하는 통합 framework다.

## 2. 연구 질문

플랫폼마다 다른 subcellular transcript와 noisy image를 하나의 probabilistic/deep-learning pipeline에서 세포 단위 정보로 안정적으로 변환할 수 있는가?

## 3. 데이터와 방법

image와 spatial count를 joint segmentation·annotation 문제로 모델링하고 scRNA reference를 이용해 cell identity와 transcript assignment를 추정했다. Xenium, Visium HD, MERFISH, Stereo-seq 및 cancer tissue에서 기존 platform-specific pipeline과 비교했다.

## 4. 핵심 결과

고해상도 플랫폼 간 cell boundary와 annotation을 공통 출력으로 만들고, 여러 조직·플랫폼에서 single-cell 수준 expression을 추출하는 통합성을 보였다. 공개 저장소와 archive가 있어 reference 구성과 parameter를 고정한 재현이 가능하다.

## 5. 한계

scRNA reference 품질과 tissue-specific marker에 의존하며, 평가한 platform·ground truth 범위가 제한적이다. 새로운 chemistry나 심한 necrosis·autofluorescence가 있는 biopsy에서의 robustness와 임상 outcome utility는 검증되지 않았다.

## 6. 재현 또는 활용 포인트

같은 section의 image·count·reference를 함께 보존하고 cell boundary, transcript assignment, annotation을 각각 평가한다. 플랫폼별 resolution·capture efficiency와 reference mismatch를 ablation으로 분리한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장 생검의 high-resolution ST에서 tubular–immune 접촉과 rejection cell state를 공통 cell table로 만들 수 있는 후보다. donor·recipient reference와 injury-induced state를 분리한 annotation validation이 필요하며, CellART 출력은 bulk/pseudobulk·clinical model의 입력으로 사용할 수 있다.

## 8. 관련 키워드

- high-resolution spatial transcriptomics
- joint segmentation
- cell annotation
- scRNA reference

## 9. Bibliography

Chen, Yuheng, et al. “CellART: A Unified Framework for Extracting Single-cell Information from High-resolution Spatial Transcriptomics.” *Nature Computational Science*, 2026. [https://doi.org/10.1038/s43588-026-01054-1](https://doi.org/10.1038/s43588-026-01054-1).
