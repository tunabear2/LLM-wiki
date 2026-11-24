---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# Evaluating local assembly strategies for human long-read structural variant calling

## 기본 정보

- Citation key: `mirusEvaluatingLocalAssembly2026`
- Item type: preprint
- Authors: Tim Mirus; Richard Lüpken; Birte Kehr
- Source: bioRxiv v1, posted 2026-11-17 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.11.765824](https://doi.org/10.64898/2026.11.11.765824)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

Long-read SV caller의 전체 성능이 아니라 local assembly의 다섯 consensus 전략을 분리해 비교하고, read error·전처리·flank가 전략별 정밀도와 재현율을 어떻게 바꾸는지 보였다.

## 2. 연구 질문

HiFi·ONT structural-variant calling에서 local partial-order assembly 단계의 어떤 선택이 platform·read quality 변화에 견고한가?

## 3. 데이터와 방법

Popular SV caller와 유사한 다섯 consensus computation 전략을 구현해 simulation, GIAB, Human Pangenome Project와 ONT 공개자료에서 비교했다. Recent·older HiFi/ONT, error profile, spanning-read filtering, preprocessing, sequencing depth와 flank 길이를 바꾸고 breakpoint·sequence-level precision과 recall을 평가했다. 구현은 LR-Cons로 공개했다.

## 4. 핵심 결과

- Recent HiFi와 ONT에서는 대부분 전략이 높은 성능을 보였지만 older noisy ONT에서 k-mer·multiple-POA 전략의 성능이 크게 떨어졌다.
- abPOA와 RapidFuzz가 모든 설정에서 가장 안정적이었고 abPOA가 대체로 약간 높은 precision·recall을 보였다.
- 양쪽 reference flank에 anchor되는 spanning read와 더 긴 flank를 쓰는 전략이 real data에서 안정성을 높였다.

## 5. 한계

Caller의 local consensus 단계만 격리한 benchmark이므로 clustering, genotyping, filtering을 포함한 end-to-end 성능과 동일하지 않다. 공개 truth set의 breakpoint 불확실성과 특정 read chemistry·error profile에 민감하며 somatic low-VAF SV는 직접 평가하지 않았다.

## 6. 재현 또는 활용 포인트

Platform·basecaller·chemistry, read length·quality·coverage, spanning-read filter와 flank를 기록한다. Caller 비교 전 local assembly output의 sequence identity와 breakpoint tolerance를 분리하고 GIAB·pangenome truth 및 orthogonal validation을 함께 쓴다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient long-read WGS에서 SV와 expression outlier·ASE를 연결할 때 caller 이름만 비교하지 않고 assembly 단계의 platform 적합성을 점검하는 근거가 된다. Post-transplant malignancy의 low-VAF somatic SV에는 별도 검증이 필요하다.

## 8. 관련 키워드

- long-read sequencing
- structural variant
- local assembly
- partial-order alignment
- benchmarking

## 9. Bibliography

Mirus, Tim, Richard Lüpken, and Birte Kehr. “Evaluating Local Assembly Strategies for Human Long-Read Structural Variant Calling.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.11.765824](https://doi.org/10.64898/2026.11.11.765824).
