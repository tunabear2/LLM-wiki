---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# Multi-platform Benchmark of Sequencing-based Spatial Transcriptomics

## 기본 정보

- Citation key: `mortierNavigatingSpatialTranscriptomics2026`
- Item type: bioRxiv preprint
- Authors: Julien Mortier; Isabelle Scheyltjens; Elina Kuznecova; Kelly Lemeire; Fleur Parmentier; et al.
- Source: bioRxiv v1, posted 2026-10-16 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.15.759112](https://doi.org/10.64898/2026.10.15.759112); [analysis code](https://github.com/vibspatial/seq-spatial-transcriptomics-benchmark)
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

아홉 sequencing-based spatial transcriptomics assay를 tissue·보존법에 걸쳐 직접 비교하고, nominal spot size 대신 capture geometry·efficiency·spatial accuracy를 측정하는 표준 용어와 지표를 제안했다.

## 2. 연구 질문

서로 다른 chemistry와 array 구조를 가진 spatial platform의 실제 sampling resolution과 transcript recovery를 공정하게 비교해 assay 선택 기준을 만들 수 있는가?

## 3. 데이터와 방법

Mouse brain·liver·lung, human treatment-naïve NSCLC, rice root를 FF와 FFPE 조건에서 profiled했다. BMKMANU S1000/S3000, Curio Seeker, Nova-ST, Stereo-Seq, Visium/Visium HD의 FF·FFPE·3′ 구성을 포함한 아홉 assay를 1억 reads로 맞추고 capture area, functional/spatial coverage, local sampling geometry, UMI/gene recovery와 spatial accuracy를 비교했다.

## 4. 핵심 결과

- Capture area는 Curio Seeker 8.57 mm²에서 Stereo-Seq 약 100 mm²까지 크게 달랐다.
- Visium HD는 약 100% functional coverage였지만 다른 고밀도 assay도 2 µm spatial coverage 기준으로 약 91–100%에 도달해 단순 physical coverage만으로 resolution을 판단하기 어려웠다.
- Local gap, barcode decoding failure, transcript diffusion와 capture efficiency를 함께 보는 operational metric이 nominal capture-unit size보다 실제 분석 한계를 잘 설명했다.

## 5. 한계

각 tissue는 제한된 block과 replicate로 비교되어 biological variability와 장기 운영 안정성을 충분히 다루지 못한다. Non-human raw data와 human controlled-access data의 accession은 출판 시 제공 예정이었다. 여러 저자가 상용 assay를 제공하는 core facility에 속하고 vendor 할인 지원을 받았지만 vendor는 설계·분석에 관여하지 않았다고 밝혔다.

## 6. 재현 또는 활용 포인트

Analysis code와 1억-read subsampling 결과·Vitessce view가 제공된다. Assay를 고를 때 capture area, saturation, per-gene efficiency, spatial coverage/accuracy와 필요한 biological scale을 사전에 연결한다.

## 7. Transcriptomics·신장이식 연구와의 연결

작은 core biopsy에서 rejection lesion과 tubule–immune interface를 보려면 nominal 해상도보다 usable area, gap, FFPE compatibility와 transcript recovery가 중요하다. 같은 biopsy를 platform에 나눠 배치하는 within-tissue validation 설계의 기준이 된다.

## 8. 관련 키워드

- Transcriptomics / Platform
- spatial transcriptomics
- cross-platform benchmark
- spatial resolution

## 9. Bibliography

Mortier, Julien, et al. “Navigating the Rapidly Evolving Landscape of Sequencing-based Spatial Transcriptomics Technologies: A Comprehensive Multi-platform Benchmark.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.15.759112](https://doi.org/10.64898/2026.10.15.759112).
