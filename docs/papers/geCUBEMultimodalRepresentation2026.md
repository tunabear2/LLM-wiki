---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# CUBE: Multimodal Representation Learning Across Histomorphology, Spatial Protein, and Transcriptome Signals

## 기본 정보

- Citation key: `geCUBEMultimodalRepresentation2026`
- Item type: preprint
- Authors: Zhiyan Ge; Haoyang Cai
- DOI: 10.64898/2026.09.14.751379
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.14.751379v1); [DOI](https://doi.org/10.64898/2026.09.14.751379)
- Source/date: bioRxiv v1, posted 2026-09-20; not peer reviewed
- 주 카테고리: Bio AI
- 교차 카테고리: Cancer Transcriptomics / Clinical Prediction; Transcriptomics / Platform

## 1. 한 줄 요약

CUBE는 완전히 paired된 multimodal tissue data 없이도 H&E를 공통 bridge로 사용해 spatial protein phenotype과 transcriptome-associated signal을 하나의 attention-fused representation으로 연결한다.

## 2. 연구 질문

H&E–mIHC와 H&E–pseudo-spatial-transcriptomics처럼 서로 따로 paired된 자료를 이용해, 실제 spatial transcriptomics와 조직 면역구조로 전이되는 생물학적 표현을 학습할 수 있는가?

## 3. 데이터와 방법

Colorectal tissue에서 H&E–multiplex IHC 관계와 H&E–pseudo-ST 관계를 독립 encoder로 학습한 뒤 attention fusion한다. mIHC-derived concept로 biological grounding을 주고, 실제 Visium HD에서는 encoder를 고정한 decoder-only calibration을 수행했다. Protein reconstruction, immune–epithelial spatial score와 독립 ECM–receptor transcriptomic program으로 평가했다.

## 4. 핵심 결과

H&E에서 mIHC marker를 복원한 평균 Pearson correlation은 0.7256이었고 DAPI, CD3, panCK는 각각 0.7105, 0.5356, 0.9308이었다. Fusion representation은 936개 test patch의 immune–epithelial score를 Pearson 0.809, Spearman 0.857, R² 0.624로 예측했다. 외부 Visium HD의 17-gene ECM program은 111개 test patch에서 Pearson 0.539, Spearman 0.562였다.

## 5. 한계

Colorectal cancer 중심 proof-of-concept이며 mIHC marker가 DAPI, CD3, panCK로 제한된다. Transcriptomic branch는 pseudo-ST supervision에 의존하고 실제 Visium HD 외부검증은 한 section의 제한된 설정이다. Renal tissue, multi-center·scanner holdout과 clinical outcome은 검증되지 않았으며 v1 preprint다.

## 6. 재현 또는 활용 포인트

- H&E–mIHC와 H&E–ST pair를 환자 단위로 분리해 leakage를 막는다.
- Fusion 없이 각 branch 단독, frozen encoder와 end-to-end tuning을 비교한다.
- Marker reconstruction과 독립 gene-program transfer를 함께 평가한다.
- External tissue에서는 scanner, staining batch와 tissue region을 명시한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 biopsy H&E를 공통축으로 면역단백질 phenotype과 spatial transcriptomics를 연결하는 설계에 직접적이다. 적용 전에는 renal cortex/medulla, rejection subtype, donor·center·platform holdout과 실제 molecular rejection outcome으로 재검증해야 한다.

## 8. 관련 키워드

- Bio AI
- Multimodal representation learning
- Histopathology
- Spatial transcriptomics
- Multiplex immunohistochemistry

## 9. Bibliography

Ge, Zhiyan, and Haoyang Cai. “CUBE: Multimodal Representation Learning Reveals Biological Structure Across Histomorphology, Spatial Protein Phenotypes, and Transcriptome-Associated Signals.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.14.751379](https://doi.org/10.64898/2026.09.14.751379). Preprint; not peer reviewed.
