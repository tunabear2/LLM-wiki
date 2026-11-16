---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# bronko: Ultrafast Alignment-Free Detection of Viral Genome Variation

## 기본 정보

- Citation key: `doughtyBronkoAlignmentFree2026`
- Item type: journal article
- Authors: Ryan D. Doughty; Michael J. Tisza; Todd J. Treangen
- Source: _Genome Research_, published 2026-11-10
- Original: [DOI 10.1101/gr.282104.126](https://doi.org/10.1101/gr.282104.126)
- PubMed: [PMID 43009286](https://pubmed.ncbi.nlm.nih.gov/43009286/)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

bronko는 locality-sensitive bucket, k-mer pseudo-pileup, mutation-dense region assembly, streaming noise test를 결합해 viral read에서 alignment 없이 minor variant를 탐지한다.

## 2. 연구 질문

대규모 viral sequencing에서 full alignment 비용을 피하면서 SNP·indel과 intrahost minor variant의 정밀도를 유지할 수 있는가?

## 3. 데이터와 방법

Reference 대비 SNP 후보를 찾는 locality-sensitive bucketing, k-mer count 기반 pseudo-mapping, mutation-dense region과 indel용 greedy de novo assembly, sliding-window outlier noise model을 결합했다. Simulated amplicon, whole-genome alignment 비교, chronic SARS-CoV-2 longitudinal data에서 평가했다.

## 4. 핵심 결과

- Simulated amplicon에서 기존 도구보다 높은 precision과 비슷한 recall을 보였고 실행시간은 10~1,000배 빨랐다.
- Sequencing read에서 만든 alignment의 SNP content가 whole-genome alignment와 거의 같으면서 더 빠르게 실행됐다.
- 만성 SARS-CoV-2 종단 자료에서 intrahost diversification과 adaptive mutation pattern을 재현했다.

## 5. 한계

Viral genome과 amplicon 중심 검증이므로 human diploid genome, repeat-rich region, germline·somatic calling으로 직접 일반화할 수 없다. Complex structural variant와 host contamination 조건은 별도 검증이 필요하다.

## 6. 재현 또는 활용 포인트

k-mer length, bucket·noise threshold, reference set, depth와 minor-allele-frequency range를 고정한다. Truth set에서 precision–recall을 depth별로 보고하고 standard aligner+caller와 CPU time·memory를 같은 hardware에서 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

면역억제 환자의 바이러스 재활성화와 intrahost evolution을 biopsy·혈액 transcriptome과 연결할 때 빠른 viral-variant screening에 활용할 수 있다. Donor·recipient germline 분석용 caller의 대체재는 아니다.

## 8. 관련 키워드

- alignment-free variant detection
- viral genomics
- k-mer pseudo-mapping
- minor variants

## 9. Bibliography

Doughty, Ryan D., Michael J. Tisza, and Todd J. Treangen. “Ultrafast alignment-free detection of viral genome variation with bronko.” _Genome Research_, 2026. [https://doi.org/10.1101/gr.282104.126](https://doi.org/10.1101/gr.282104.126).
