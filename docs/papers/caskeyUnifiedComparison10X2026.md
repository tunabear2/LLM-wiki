---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# A Unified Comparison of 10X Genomics and Parse Biosciences scRNA-seq Technologies

## 기본 정보

- Citation key: `caskeyUnifiedComparison10X2026`
- Item type: preprint
- Authors: Miles Caskey; Ingleif B. Hallgrímsdóttir
- Source: bioRxiv v1, posted 2026-10-11 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.09.758116](https://doi.org/10.64898/2026.10.09.758116); [code](https://github.com/mcaskey6/10XvParse)
- 주 카테고리: `Transcriptomics / Platform`
- 관련 카테고리: `scRNA-seq`

## 1. 한 줄 요약

다섯 연구의 일곱 matched sample pair를 재분석한 결과 10X droplet과 Parse split-pool data는 nuclear/cytoplasmic RNA composition과 일부 bias가 달라 직접 교환 가능한 측정값이 아니었다.

## 2. 연구 질문

Priming chemistry의 영향과 platform 자체의 영향을 분리했을 때 10X Chromium과 Parse Evercode WT 사이에 어떤 일관된 compositional bias가 남는가?

## 3. 데이터와 방법

여러 tissue와 species를 포함한 공개 matched 10X–Parse sample pair 7개를 다섯 연구에서 수집했다. Parse read를 priming strategy별로 나눠 GC bias와 platform effect를 분리하고 gene count, nuclear/cytoplasmic-enriched transcript, cell composition을 비교했다. Droplet-specific assumption이 없는 contamination metric으로 background RNA도 평가했다.

## 4. 핵심 결과

- Parse 내부에서는 priming strategy에 따른 GC-content bias가 나타났다.
- Platform 차이는 priming effect보다 컸고 Parse에서 상대적인 nuclear RNA enrichment와 일관된 composition shift가 관찰됐다.
- Parse의 background RNA contamination은 10X와 비슷한 규모로, 현저히 낮다는 일반적 주장과 맞지 않았다.

## 5. 한계

공개된 일곱 matched pair와 사용된 chemistry/version에 한정된 재분석이다. Cell-type resolution보다 gene count와 composition 차이에 초점을 맞췄고 동일한 생물학적 표본이라도 wet-lab handling 차이를 완전히 분리할 수 없다.

## 6. 재현 또는 활용 포인트

Raw FASTQ에서 동일한 gene annotation과 QC threshold로 다시 처리하고 priming read를 분리한다. Platform을 단순 batch covariate로 지우기 전에 nuclear/cytoplasmic score, ambient RNA, cell-type composition과 donor-matched effect를 각각 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

10X와 Parse로 만든 kidney-biopsy atlas를 합칠 때 platform shift가 cell state나 rejection signal처럼 보일 위험을 직접 보여준다. Platform-balanced donor split과 within-platform replication을 우선해야 한다.

## 8. 관련 키워드

- 10X Genomics
- Parse Biosciences
- cross-platform benchmark
- nuclear RNA bias

## 9. Bibliography

Caskey, Miles, and Ingleif B. Hallgrímsdóttir. “A Unified Comparison of 10X Genomics and Parse Biosciences scRNA-seq Technologies.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.09.758116](https://doi.org/10.64898/2026.10.09.758116).
