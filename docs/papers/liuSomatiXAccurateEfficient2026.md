---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# SomatiX: Accurate and Efficient Somatic SNV Detection from Matched Tumor-Normal Long-Read DNA Sequencing

## 기본 정보

- Citation key: `liuSomatiXAccurateEfficient2026`
- Item type: journal article
- Authors: Zelin Liu
- Source: Bioinformatics, online 2026-10-24; PubMed indexed 2026-10-26
- Original: [DOI: 10.1093/bioinformatics/btag792](https://doi.org/10.1093/bioinformatics/btag792); [PMID: 42928626](https://pubmed.ncbi.nlm.nih.gov/42928626/); [code](https://github.com/colinliuzelin/SomatiX); [Zenodo](https://doi.org/10.5281/zenodo.22062438)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

SomatiX는 allele-aware pileup을 쓰는 compact deep model로 matched tumor-normal ONT/PacBio long read에서 somatic SNV를 호출해 특히 ONT low-VAF 구간의 정확도와 runtime을 개선했다.

## 2. 연구 질문

Long-read error, tumor purity, tumor-in-normal contamination과 낮은 VAF 속에서도 matched tumor-normal somatic SNV를 정확하고 빠르게 검출할 수 있는가?

## 3. 데이터와 방법

Allele-aware pileup representation을 입력으로 한 deep-learning caller를 만들었다. 여러 cancer cell-line benchmark, sequencing context, VAF bin, minimum supporting-read threshold에서 DeepSomatic과 ClairS를 비교하고 held-out chromosome 1의 ONT·PacBio data를 평가했다.

## 4. 핵심 결과

- 대부분 ONT 조건에서 DeepSomatic과 ClairS보다 높은 F1을 보였고 PacBio에서도 경쟁 성능을 냈다.
- Supporting read ≥3, VAF ≥0.05에서 held-out chromosome 1 mean F1은 ONT 0.986, PacBio 0.988이었다.
- 평가 도구 중 가장 빠른 runtime과 강한 ONT low-VAF 성능을 보고했다.

## 5. 한계

핵심 수치는 cell-line과 held-out chromosome 1 benchmark에 기반하며 실제 low-purity clinical tumor의 전체 genome 검증은 아니다. Somatic SNV에 초점을 두고 indel·SV·CNV는 다루지 않는다.

## 6. 재현 또는 활용 포인트

Platform, coverage, tumor purity, contamination, VAF와 supporting-read bin별 precision·recall을 분리한다. Code와 trained model뿐 아니라 benchmark truth set과 inference threshold를 고정한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Post-transplant malignancy나 clonal hematopoiesis에서 long-read somatic SNV를 expression clone과 연결하는 후보가 된다. Donor·recipient germline 차이를 somatic signal로 오인하지 않도록 matched normal과 chimerism QC가 필수다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- somatic SNV
- long-read sequencing
- variant calling

## 9. Bibliography

Liu, Zelin. “SomatiX: Accurate and Efficient Somatic SNV Detection from Matched Tumor-Normal Long-Read DNA Sequencing.” _Bioinformatics_, 2026. [https://doi.org/10.1093/bioinformatics/btag792](https://doi.org/10.1093/bioinformatics/btag792).
