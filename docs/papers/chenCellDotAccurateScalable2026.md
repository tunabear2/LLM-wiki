---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# CellDot: optimal-transport decontamination for imaging spatial transcriptomics

## 기본 정보

- Citation key: `chenCellDotAccurateScalable2026`
- Item type: preprint
- Authors: Yuheng Chen; Yuyao Liu; Zitong Chao; Shi Han; Yeqin Zeng; Baichen Yu; Fan Zhang; Angela Ruohao Wu; Jiguang Wang; Hao Chen; Jiashun Xiao; Can Yang
- DOI: 10.64898/2026.09.09.750350
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.09.750350v1); [DOI](https://doi.org/10.64898/2026.09.09.750350); [code](https://github.com/YangLabHKUST/CellDot); [Zenodo](https://doi.org/10.5281/zenodo.22489061)
- Source/date: bioRxiv v1, posted 2026-09-15; indexed after the prior watch; not peer reviewed
- 주 카테고리: Transcriptomics / Platform
- 교차 카테고리: scRNA-seq; Cancer Transcriptomics / Clinical Prediction

## 1. 한 줄 요약

CellDot는 imaging-based spatial transcriptomics의 각 molecule을 원래 cell에 유지, 이웃 cell로 재할당 또는 background 제거하는 capacitated entropic optimal-transport 문제로 풀어 오염을 교정한다.

## 2. 연구 질문

Segmentation error, transcript spillover와 3D cell overlap으로 잘못 배정된 molecule을 단순 제거하지 않고, reference expression과 공간정보를 이용해 biologically plausible한 cell로 추적 가능하게 재배정할 수 있는가?

## 3. 데이터와 방법

Reference-guided expression compatibility, spatial proximity와 data-adaptive capacity constraint를 결합해 molecule별 세 가지 fate를 최적화한다. 네 human tumor imaging-ST dataset에서 다섯 baseline과 비교했고 matched Visium·Visium HD로 spatial pattern을 교차 검증했다. Cell state, cell–cell communication, spatial niche recovery와 whole-transcriptome Atera dataset 확장성도 평가했다.

## 4. 핵심 결과

시험한 real dataset에서 기존 decontamination method보다 우수했고 독립 cross-platform 측정과 맞는 spatial expression pattern을 복원했다. Cellular-state identification, intercellular communication과 spatial-niche program 회복을 개선했다. 비교 방법 중 whole-transcriptome Atera data에 적용 가능한 유일한 방법이었다.

## 5. 한계

대부분 cell에서 contamination이 소수라는 가정과 신뢰할 수 있는 cell annotation·matched single-cell reference가 필요하다. Reference에서 빠진 cell type 또는 질환 특이 state는 진짜 transcript를 다른 cell이나 background로 보낼 수 있다. Human tumor 중심 v1 preprint이며 kidney tissue에서 검증되지 않았다.

## 6. 재현 또는 활용 포인트

- Segmentation, molecule coordinate, cell annotation과 reference version을 함께 보존한다.
- Synthetic contamination뿐 아니라 matched independent platform으로 pattern restoration을 검증한다.
- Retain/reassign/remove molecule 수를 cell type·gene·거리별로 audit한다.
- Reference cell type을 의도적으로 제거하는 sensitivity analysis를 수행한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Allograft imaging-ST에서 tubular RNA spillover가 immune cell expression으로, 또는 그 반대로 오인되는 문제와 가짜 ligand-sender를 줄이는 데 직접적이다. Rejection-specific rare state가 reference에서 누락되지 않았는지 먼저 확인해야 한다.

## 8. 관련 키워드

- Transcriptomics / Platform
- Imaging-based spatial transcriptomics
- Decontamination
- Optimal transport
- Molecule reassignment

## 9. Bibliography

Chen, Yuheng, et al. “Accurate and Scalable Decontamination of Imaging-Based Spatial Transcriptomics via Optimal Transport.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.09.750350](https://doi.org/10.64898/2026.09.09.750350). Preprint; not peer reviewed.
