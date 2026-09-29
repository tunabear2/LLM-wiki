---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# Ultra-fast and scalable high-resolution full-length single-cell RNA sequencing using CHART-seq

## 기본 정보

- Citation key: `zhangCHARTSeqFullLength2026`
- Item type: preprint
- Authors: Wenyi Zhang; Aiqun Chen; Kun Ye; Hong Wang; Jing Shen; Zheng Jiao; Yifan Guo; Yuchen Xu; Dong Zhang; Yanyi Huang; Lin He; Xiang Gao; Xi Zhao
- DOI: 10.64898/2026.09.18.752546
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.18.752546v1); [DOI](https://doi.org/10.64898/2026.09.18.752546); [code](https://github.com/DuDuDuDu-du/Chartseq_tools)
- Source/date: bioRxiv v1, posted 2026-09-24; not peer reviewed
- 주 카테고리: Transcriptomics / Platform
- 교차 카테고리: scRNA-seq

## 1. 한 줄 요약

CHART-seq은 orthogonally indexed recombinant Tn5로 RNA/cDNA heteroduplex를 tagment하고 일찍 pooling해, full-length single-cell RNA library를 3시간 이내·cell당 US$1 미만으로 만드는 plate-based assay다.

## 2. 연구 질문

Cell마다 독립 library를 만들어야 하는 기존 full-length scRNA-seq의 비용과 처리량 병목을 줄이면서 gene·annotated isoform detection, genebody coverage와 expression reproducibility를 유지할 수 있는가?

## 3. 데이터와 방법

서로 직교하는 index를 가진 Tn5 complex로 RNA/cDNA heteroduplex를 tagment해 purification, gap filling과 PCR 전에 well을 pooling한다. Library당 최대 96 cells를 처리하고 384-well 확장을 지원한다. HEK293T·HepG2 RNA와 vascular smooth-muscle cell 자료에서 matched sequencing depth로 Smart-seq2, Smart-seq3, Flash-seq와 SHERRY2를 비교했으며, PDGF-BB와 TGF-β1 처리에 따른 gene program과 transcript usage도 탐색했다.

## 4. 핵심 결과

Library preparation은 3시간 이내였고 시약비는 cell당 US$1 미만이었다. 같은 depth에서 CHART-seq은 비교 protocol보다 더 많은 gene과 annotated isoform을 검출하면서 넓은 genebody coverage와 재현 가능한 expression estimate를 유지했다. Vascular smooth-muscle cell에서는 TGF-β1 pretreatment가 PDGF-associated inflammatory program을 억제하고 일부 contractile feature를 회복시키며 별도의 metabolic–matrix response와 transcript-usage 변화를 유도했다.

## 5. 한계

6-nt UMI는 4,096개 조합이라 고발현 molecule이나 deep sequencing에서 saturation할 수 있다. 약한 3′ bias, barcode conflict, index skip과 cross-well contamination을 추가 평가해야 한다. Vascular smooth-muscle cell 응용에는 독립 biological replicate가 없고 추정 isoform은 transcript-specific long-read로 직접 검증되지 않았다. 현재 preprint다.

## 6. 재현 또는 활용 포인트

- HEK293T·HepG2 sequencing data: SRA `PRJNA1531701`
- Code와 분석 script: [Chartseq_tools](https://github.com/DuDuDuDu-du/Chartseq_tools)
- Species-mixing과 blank well로 barcode collision·cross-well contamination을 측정한다.
- UMI saturation, intronic fraction, genebody coverage와 matched-depth gene·isoform sensitivity를 함께 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney-biopsy immune·tubular cell에서 gene expression과 candidate isoform을 동시에 얻는 저비용 plate assay 후보다. 적은 세포를 선별하는 임상 sample에 유리할 수 있지만, tissue dissociation·RNA integrity, 384-well batch, UMI saturation과 rejection-associated isoform의 long-read 검증을 먼저 수행해야 한다.

## 8. 관련 키워드

- Transcriptomics / Platform
- Full-length scRNA-seq
- Tn5 tagmentation
- Early pooling
- Isoform profiling
- Plate-based assay

## 9. Bibliography

Zhang, Wenyi, Aiqun Chen, Kun Ye, et al. “Ultra-Fast and Scalable High-Resolution Full-Length Single-Cell RNA Sequencing Using CHART-seq.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.18.752546](https://doi.org/10.64898/2026.09.18.752546). Preprint; not peer reviewed.
