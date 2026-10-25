---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# Characterizing and Mitigating Protocol-Dependent Gene Expression Bias in 3′ and 5′ Single-Cell RNA Sequencing

## 기본 정보

- Citation key: `shydlouskayaCharacterizingProtocolBias2026`
- Item type: journal article
- Authors: Valeryia Shydlouskaya; S. M. Mansour Haeryfar; Tallulah S. Andrews
- Source: Frontiers in Bioinformatics 6:1931243, published 2026-10-08; PubMed indexed 2026-10-25
- Original: [DOI: 10.3389/fbinf.2026.1931243](https://doi.org/10.3389/fbinf.2026.1931243); [PMID: 42923213](https://pubmed.ncbi.nlm.nih.gov/42923213/); [code](https://github.com/Val554/10X_3prime_vs_5prime)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

Matched 10X 3′/5′ scRNA-seq에서 protocol bias는 소수의 재현성 있는 gene에 집중되며, 무조건적 batch correction보다 해당 gene의 표적 처리와 gene-level distortion 점검이 안전할 수 있음을 보였다.

## 2. 연구 질문

10X 3′와 5′ chemistry 사이 expression bias는 transcriptome 전반에 퍼지는가, 그리고 어떤 normalization·batch correction이 cross-protocol 비교를 보존하는가?

## 3. 데이터와 방법

여섯 dataset·36명의 matched 3′/5′ sample을 같은 subject 안에서 비교해 867개 recurrent protocol-biased gene을 정의했다. Kidney·skin·liver를 포함한 별도 7개 matched sample로 검증하고 11개 normalization/correction 방법을 alignment, gene-level concordance와 differential-expression distortion으로 비교했다.

## 4. 핵심 결과

- 867개 gene이 protocol 차이를 불균형하게 설명했고 제거 후 held-out comparison에서도 3′/5′ mixing과 cosine similarity가 개선됐다.
- FastMNN 등은 cell population이 잘 맞을 때 statistical alignment를 높였지만, 불완전한 cell-type overlap에서는 gene signal을 왜곡하고 false DE를 늘릴 수 있었다.
- Bias가 제한된 gene set에 집중되어 aggressive global correction 없이 대부분 gene을 비교할 가능성을 제시했다.

## 5. 한계

10X 3′/5′, 주로 면역조직과 intra-subject 비교에 집중했다. Brain·reproductive tissue가 부족하고 multi-subject group comparison의 타당성을 확립하지 못했으며 probe-based 또는 더 이질적인 platform으로 일반화되지 않을 수 있다.

## 6. 재현 또는 활용 포인트

Code와 biased-gene list가 공개된다. Correction 전후 UMAP mixing뿐 아니라 gene-level fold change, false DE와 unmatched cell-type 보존을 함께 검사한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney validation sample이 포함되어 3′ atlas와 5′ immune-repertoire biopsy를 통합할 때 직접 참고할 수 있다. Rejection-specific cell type의 비율 차이를 batch로 지우지 않도록 protocol-biased gene 제거와 pseudobulk sensitivity analysis를 우선 비교한다.

## 8. 관련 키워드

- scRNA-seq
- Transcriptomics / Platform
- 10X 3′/5′ chemistry
- batch correction

## 9. Bibliography

Shydlouskaya, Valeryia, S. M. Mansour Haeryfar, and Tallulah S. Andrews. “Characterizing and Mitigating Protocol-Dependent Gene Expression Bias in 3′ and 5′ Single-Cell RNA Sequencing.” Frontiers in Bioinformatics 6 (2026): 1931243. [https://doi.org/10.3389/fbinf.2026.1931243](https://doi.org/10.3389/fbinf.2026.1931243).
