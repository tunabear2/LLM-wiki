---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Live Droplet Single-Cell RNA Sequencing

## 기본 정보

- Citation key: `reynoldsLiveDropletSingleCell2026`
- Item type: preprint
- Authors: D. E. Reynolds; S. Lee; D. Oh; S. S. Kumar; E. Huynh; R.-T. T. Morales; S. Bracht; P. Vallapureddy; C. N. Lee; J. Lim; R. J. Agosto Nieves; S. Liu; G. Jin; X. Xu; B. Lim; Y. Deng; J. Kim; Y. H. Roh; S. Shaffer; J. Ko
- Source: bioRxiv v1, posted 2026-11-04 (not peer reviewed)
- Original: [DOI: 10.64898/2026.11.03.763484](https://doi.org/10.64898/2026.11.03.763484)
- 주 카테고리: `Transcriptomics / Platform`
- 관련 카테고리: `scRNA-seq`

## 1. 한 줄 요약

Live D-seq는 살아 있는 barcoded cell을 droplet에서 일시적으로 투과화해 RNA 일부를 반복 채취하고 같은 lineage의 transcriptome 변화를 시간에 따라 연결한다.

## 2. 연구 질문

Cell lysis 없이 많은 single cell에서 transcriptome-wide RNA를 반복 측정해 동일 cell lineage의 시간적 state transition을 추적할 수 있는가?

## 3. 데이터와 방법

CloneSweeper cell barcode, split-pool barcoded hydrogel bead, particle-templated emulsification, mild hypotonic/permeabilization sampling을 결합했다. Cross-species mixture로 cross-talk을 평가하고 cell–bead barcode mapping을 검증했으며 A549 epithelial-to-mesenchymal transition을 longitudinal하게 추적했다.

## 4. 핵심 결과

- Cross-species 실험에서 single-cell resolution과 낮은 cross-contamination을 보였다.
- Cellular barcode와 hydrogel-bead barcode를 연결해 반복 sampling의 lineage를 추적했다.
- 두 번 sampling한 cell은 unsampled control과 유사한 transcriptional profile을 유지했고 A549 EMT의 시간 변화를 포착했다.

## 5. 한계

Cell–bead pairing 때문에 capture efficiency가 낮고 세포당 RNA 일부만 얻어 conventional scRNA-seq보다 gene detection과 mapping efficiency가 낮다. Abundant transcript에 편향되며 cell type별 membrane sensitivity에 맞춘 조건 최적화가 필요하다. 현재 검증은 제한된 model system과 time point에 머문다.

## 6. 재현 또는 활용 포인트

Sampling 전후 viability, growth, transcriptome drift, RNA fraction, genes/cell, cross-talk, barcode collision을 보고한다. 동일 lineage 연결 정확도와 unsampled control을 포함하고 conventional endpoint scRNA-seq로 주요 state transition을 교차 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Biopsy 자체보다 ex-vivo immune·tubular culture나 organoid에서 steroid·cytokine·drug response를 같은 lineage에서 반복 추적하는 플랫폼 후보다. 살아 있는 tissue 적용성, low-input sensitivity, sampling-induced stress를 먼저 검증해야 한다.

## 8. 관련 키워드

- longitudinal scRNA-seq
- live-cell RNA sampling
- droplet barcoding
- epithelial-to-mesenchymal transition

## 9. Bibliography

Reynolds, D. E., et al. “Live Droplet Single-Cell RNA Sequencing.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.03.763484](https://doi.org/10.64898/2026.11.03.763484).
