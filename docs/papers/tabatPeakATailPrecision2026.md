---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# PeakATail: precision-first poly(A)-site calling and calibrated alternative polyadenylation analysis in single-cell RNA-seq

## 기본 정보

- Citation key: `tabatPeakATailPrecision2026`
- Item type: preprint
- Authors: Alireza A. Tabat; Elmira B. Zendeh; Yağız Kaymaz
- DOI: 10.64898/2026.09.18.752791
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.18.752791v1); [DOI](https://doi.org/10.64898/2026.09.18.752791); [code](https://github.com/BMGLab/PeakATail)
- Source/date: bioRxiv v1, posted 2026-09-24; not peer reviewed
- 주 카테고리: scRNA-seq
- 교차 카테고리: Transcriptomics / Platform

## 1. 한 줄 요약

PeakATail은 scRNA-seq read에 남은 poly(A) tail 증거와 molecule 수를 이용해 polyadenylation site를 보수적으로 호출하고, label permutation으로 오류율을 확인한 alternative polyadenylation 분석 도구다.

## 2. 연구 질문

희소한 3′ single-cell read에서 internal priming을 실제 cleavage site로 오인하지 않으면서 신뢰도 높은 poly(A) site를 찾고, cell type 사이 usage 차이의 false-positive rate를 경험적으로 통제할 수 있는가?

## 3. 데이터와 방법

Poly(A/T) soft clip을 가진 read를 모아 distinct molecule evidence로 site를 순위화하고, adenosine-rich genomic sequence에 의한 internal priming 후보를 제거한다. 사람 PBMC, mouse testis 등 2개 species의 4개 공개 library에서 PolyASite atlas와 shuffled control을 비교하고, donor가 다른 PacBio Kinnex long-read 자료로 site를 교차 확인했다. Differential test는 label shuffle로 여섯 설정의 오류율을 점검했으며, 12명 lung-cancer cohort에서 cell-type switch의 환자 간 재현성을 평가했다.

## 4. 핵심 결과

호출 site의 71–83%가 curated atlas site 100 bp 이내에 있었고 shuffled control보다 30배 이상 높았다. 사람 호출의 76.5%는 독립 long-read 자료가 지지했다. 오류율을 통제한 한 설정에서는 12명 환자에 걸쳐 15,942개 cell-type switch가 재현됐으며, 10회의 shuffled-label 분석에서는 재현 switch가 없었다. 높은 precision의 대가로 recall은 낮았다.

## 5. 한계

여섯 differential-test 설정 중 하나만 false-positive rate를 통제했다. 깊게 분석한 사람 자료는 사실상 한 donor이고, 두 번째 PBMC library의 donor 독립성은 확정되지 않았다. Long-read truth도 donor-matched가 아니어서 위치는 지지하지만 개인별 usage는 검증하지 못한다. Frozen analysis commit에 이후 수정된 PAS–gene assignment 결함이 포함되어 있고 현재 preprint다.

## 6. 재현 또는 활용 포인트

- Tool release와 논문 분석에 사용한 frozen commit을 구분해 기록한다.
- 분석 코드·사전등록·truth-set 생성 과정은 [companion repository](https://github.com/BMGLab/Project_PeakATail)에 공개되어 있다.
- Software archive는 [Zenodo concept DOI 10.5281/zenodo.22697820](https://doi.org/10.5281/zenodo.22697820)에서 확인할 수 있다.
- Precision·recall뿐 아니라 label-shuffle false-positive rate와 환자 간 replication을 함께 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney-biopsy scRNA-seq에서 immune, endothelial, tubular cell별 3′-UTR·poly(A) usage 변화를 찾으면 rejection-associated transcript regulation을 gene-level differential expression보다 세밀하게 볼 수 있다. 다만 renal cohort에서 donor·batch를 분리해 재현하고, 중요한 site는 matched long-read 또는 targeted assay로 확인해야 한다.

## 8. 관련 키워드

- scRNA-seq
- Alternative polyadenylation
- Poly(A)-site calling
- Internal priming
- Error calibration
- Isoform regulation

## 9. Bibliography

Tabat, Alireza A., Elmira B. Zendeh, and Yağız Kaymaz. “PeakATail: Precision-First Poly(A)-Site Calling and Calibrated Alternative Polyadenylation Analysis in Single-Cell RNA-seq.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.18.752791](https://doi.org/10.64898/2026.09.18.752791). Preprint; not peer reviewed.
