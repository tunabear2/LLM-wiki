---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# The Genome In A Bottle HG002 assembly-based variant benchmark set

## 기본 정보

- Citation key: `olsonGIABHG002Benchmark2026`
- Item type: preprint
- Authors: Nathan D. Olson; Noah Dwarshuis; Nancy F. Hansen; et al.; Genome in a Bottle Consortium
- Source: bioRxiv (posted 2026-10-01; not peer reviewed)
- DOI: [10.64898/2026.09.23.752440](https://doi.org/10.64898/2026.09.23.752440); [benchmark FTP](https://ftp.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/AshkenazimTrio/HG002_NA24385_son/v5.0q/)
- Code: [DeFrABB](https://github.com/usnistgov/defrabb); [analysis](https://github.com/nate-d-olson/q100-variant-benchmark-paper)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

HG002 v5.0q는 phased diploid assembly와 DeFrABB 비교를 이용해 small variant와 structural variant를 GRCh37·GRCh38·CHM13에서 더 넓게 평가하는 GIAB benchmark다.

## 2. 연구 질문

assembly-based truth set이 반복·면역·복잡 구조 영역에서 short/long-read variant caller의 놓침과 false positive를 얼마나 더 포괄적으로 측정할 수 있는가?

## 3. 데이터와 방법

HG002 q100 phased assembly를 reference별 truth/benchmark로 만들고, callable region·small variant·SV를 기존 v4.2.1과 비교했다. 여러 sequencing technology와 variant-calling pipeline을 이용해 representation과 comparison 절차를 검증했다.

## 4. 핵심 결과

callable sequence가 약 200 Mbp 늘었고 small variant는 약 18%, SV는 약 3배 증가했다. 복잡한 immune/repetitive locus를 포함하며 FTP truth set, DeFrABB와 분석 코드가 공개되어 caller benchmark의 범위를 넓힌다.

## 5. 한계

매우 큰 구조·copy-number 차이와 assembly가 불확실한 영역은 여전히 제외된다. 단일 HG002 cell-line benchmark이므로 ancestry·tissue mosaicism·임상 sample에 대한 대표성을 보장하지 않는다.

## 6. 재현 또는 활용 포인트

reference build와 variant representation을 고정하고 v4.2.1과 v5.0q를 동시에 실행해 callable-region 변화가 성능 차이를 어떻게 만드는지 보고한다. caller별 precision/recall을 small variant와 SV로 분리한다.

## 7. Transcriptomics·신장이식 연구와의 연결

donor·recipient WGS caller와 HLA/SV QC의 기준 truth set으로 사용할 수 있다. RNA-seq expression outlier나 eQTL를 연결할 때 variant false positive를 줄이는 사전 benchmark로 유용하지만, 환자별 assembly와 ancestry 차이를 별도 검증해야 한다.

## 8. 관련 키워드

- Genome in a Bottle
- HG002
- assembly-based benchmark
- small and structural variants

## 9. Bibliography

Olson, Nathan D., et al. “The Genome In A Bottle HG002 Assembly-based Variant Benchmark Set Enables Comprehensive Benchmarking of Small and Structural Variants.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.23.752440](https://doi.org/10.64898/2026.09.23.752440).
