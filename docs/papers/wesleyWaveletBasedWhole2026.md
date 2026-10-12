---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# Wavelet-Based Whole-Genome-Doubling-Aware Single-Cell Copy-Number Calling

## 기본 정보

- Citation key: `wesleyWaveletBasedWhole2026`
- Item type: journal article
- Authors: Benjamin K. Wesley; Frank Wos; Soren Germer; Jade E. B. Carter; et al.
- Source: Nucleic Acids Research (published 2026-09-22; indexed 2026-10-10)
- Original: [DOI: 10.1093/nar/gkag960](https://doi.org/10.1093/nar/gkag960); [PMID: 42851130](https://pubmed.ncbi.nlm.nih.gov/42851130/); [PMC13650168](https://pmc.ncbi.nlm.nih.gov/articles/PMC13650168/)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

Songbird는 Tn5 fragment geometry, unbalanced Haar wavelet segmentation과 likelihood fitting을 결합해 저심도 single-cell WGS에서 whole-genome doubling과 absolute copy number를 추정한다.

## 2. 연구 질문

Read-depth ratio만으로 구별하기 어려운 WGD를 포함해 frozen tissue의 저심도 DLP+ scWGS에서 breakpoint와 실제 copy number를 정확히 부를 수 있는가?

## 3. 데이터와 방법

Properly paired fragment 좌표에서 unbalanced Haar wavelet으로 breakpoint를 찾고, fragment 인접부의 read-density geometry로 평균 ploidy를 추정한 뒤 likelihood ratio로 integer copy number를 맞춘다. Simulation, HEK293T/hTERT experimental ploidy ladder, 기존 DLP+와 식도선암 표본에서 HMMCopy·SCOPE·scAbsolute·ASCENT 등과 비교했다.

## 4. 핵심 결과

- Breakpoint recovery와 true copy-number 추정에서 비교 도구보다 우수했고 높은 copy-number event와 WGD를 분리했다.
- 0.1× 미만의 낮은 coverage까지 견고했으며 hg19, hg38, hs1 alignment를 지원했다.
- Tn5-based scWGS의 fragment artifact를 명시적으로 제거하고 ploidy ladder에서 absolute ploidy를 회복했다.

## 5. 한계

핵심 ploidy signal이 Tn5 fragment geometry에 기대므로 PCR·isothermal-amplification scWGS로 바로 일반화되지 않는다. Ground truth가 simulation·cell line·제한된 종양 표본 중심이고, 매우 복잡한 subclonal CNA와 임상 cohort에서 추가 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Library chemistry, duplicate filtering, coverage, genome build를 함께 기록한다. Breakpoint와 ploidy module을 따로 평가하고 bulk ASCAT 또는 orthogonal FISH와 비교한다. WGD 여부를 read-depth ratio만으로 판단하지 않는다.

## 7. Transcriptomics·신장이식 연구와의 연결

직접적인 이식 거부반응 도구는 아니지만 post-transplant malignancy나 clonal hematopoiesis의 CNA를 cell level에서 해석할 때 유용하다. RNA expression 변화와 연결하기 전에 assay-specific ploidy calibration이 필요하다.

## 8. 관련 키워드

- single-cell whole-genome sequencing
- copy-number variation
- whole-genome doubling
- unbalanced Haar wavelet

## 9. Bibliography

Wesley, Benjamin K., et al. “Wavelet-Based Whole Genome Doubling Aware Single-Cell Copy Number Calling.” Nucleic Acids Research, 2026. [https://doi.org/10.1093/nar/gkag960](https://doi.org/10.1093/nar/gkag960).
