---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-09'
tags:
- wiki/paper
---

# European LD Proxies Lose Tagging for 43% of GWAS Leads in the African Panel: SwiftLD

## 기본 정보

- Citation key: `christensenEuropeanLDProxies2026`
- Item type: preprint
- Authors: Joe Christensen
- Source: bioRxiv v1, posted 2026-11-05 (not peer reviewed)
- Original: [DOI: 10.64898/2026.11.04.760946](https://doi.org/10.64898/2026.11.04.760946); [code and reproduction](https://github.com/joe-b-christensen/swiftld)
- 주 카테고리: `GWAS`
- 관련 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

SwiftLD는 vcftools의 pairwise LD 출력을 byte-identical하게 재현하면서 크게 가속하고, European proxy SNP의 African-panel tagging 손실을 chromosome 22에서 정량화한다.

## 2. 연구 질문

기존 vcftools pipeline의 출력 호환성을 깨지 않고 LD 계산을 가속하며, ancestry가 바뀔 때 GWAS lead proxy가 얼마나 보존되는지 빠르게 평가할 수 있는가?

## 3. 데이터와 방법

vcftools 0.1.17의 `--hap-r2`와 `--geno-r2` 및 18개 option 조합을 호환 대상으로 구현했다. 1000 Genomes chromosome 22의 503–2,504명, 0.25–1 Mb region에서 vcftools·PLINK 2와 비교했고 세 장비에서 167,749개 differential test를 수행했다. GWAS lead의 European best proxy를 ancestry panel별로 재평가했다.

## 4. 핵심 결과

- AVX-512 2-thread 조건에서 vcftools보다 기하평균 826배, PLINK 2보다 end-to-end 7.6배 빨랐다.
- 세 장비의 167,749개 test에서 vcftools와 다른 byte가 없었다.
- European lead proxy가 r² ≥ 0.8을 유지한 비율은 African panel 57.4%, 다른 non-European panel 85.6–92.7%, European split-half 98.1%였다.

## 5. 한계

속도 headline은 2-thread SwiftLD와 single-thread vcftools의 짧은 chromosome 22 region 비교이며 thread scaling과 BGZF 경로는 충분히 평가되지 않았다. Byte identity를 위해 vcftools의 알려진 출력 결함도 복제한다. Proxy-tagging 분석은 causal-effect transfer나 PRS accuracy를 측정한 것이 아니다.

## 6. 재현 또는 활용 포인트

CPU instruction set, thread, compression format, region size, sample 수와 window를 기록한다. Byte-level regression test 뒤 r² tolerance와 downstream pruning/fine-mapping 결과도 별도로 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient ancestry가 다양한 cohort에서 eQTL/TWAS·fine-mapping용 LD를 빠르게 만들 수 있다. European proxy를 그대로 쓰면 African ancestry의 regulatory variant–expression 연결을 놓칠 수 있으므로 ancestry-matched LD와 imputation QC가 필요하다.

## 8. 관련 키워드

- linkage disequilibrium
- vcftools compatibility
- multi-ancestry GWAS
- SwiftLD

## 9. Bibliography

Christensen, Joe. “European LD Proxies Lose Tagging for 43% of GWAS Leads in the African Panel: a Chromosome 22 Analysis with SwiftLD, an 826-Fold Faster, Byte-Identical vcftools LD.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.04.760946](https://doi.org/10.64898/2026.11.04.760946).
