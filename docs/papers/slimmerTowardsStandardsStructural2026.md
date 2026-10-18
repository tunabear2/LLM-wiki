---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# Towards Standards for Analysing Structural Variants from Short-read WGS

## 기본 정보

- Citation key: `slimmerTowardsStandardsStructural2026`
- Item type: bioRxiv preprint
- Authors: James C. Slimmer; Johanna L. Jones; William R. Reay; Kathryn P. Burdon; Nicholas B. Blackburn
- Source: bioRxiv v1, posted 2026-10-14 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.13.758836](https://doi.org/10.64898/2026.10.13.758836); [prioritySV code](https://github.com/jcslimmer/prioritySV); [benchmark archive](https://doi.org/10.5281/zenodo.21126342)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

30× short-read WGS의 16개 SV caller와 ensemble을 base-pair exact truth set으로 비교해, 기존 ensemble이 constituent caller보다 exact breakpoint·size 정확도를 크게 악화시킬 수 있음을 보였다.

## 2. 연구 질문

Short-read deletion, insertion, duplication을 연구 간 비교와 annotation에 쓸 만큼 정확히 표현하려면 caller와 ensemble merging을 어떻게 평가해야 하는가?

## 3. 데이터와 방법

HG002 T2T-Q100과 Platinum Pedigree truth set, 1KGP-ONT·CoLoRS long-read database를 사용했다. 30× Illumina WGS에서 16개 individual tool과 GATK-SV, MOPline, Parliament2 등을 breakpoint와 size의 여러 threshold로 비교했다. Benchmark별 우수 caller를 우선하는 intra-sample merging proof-of-concept를 만들었다.

## 4. 핵심 결과

- 16개 tool 중 deletion·insertion·duplication을 모두 안정적으로 exact-match 출력한 것은 다섯 개뿐이었다.
- 일부 ensemble은 가장 좋은 constituent tool보다 perfect-match accuracy가 최대 98% 낮았다.
- Priority merging은 HG002 deletion과 insertion에서 최고 F1을 냈고, common exact-match SV는 두 long-read database와 높은 일치를 보였다.

## 5. 한계

Recall 우선 merging은 false positive를 늘릴 수 있다. 일부 caller가 genotype을 내지 않아 genotyping accuracy를 평가하지 않았고, inversion과 copy-number state도 benchmark 범위 밖이었다. Truth set과 sample 수가 제한되고 short read는 큰 insertion에 본질적 제약이 있다.

## 6. 재현 또는 활용 포인트

Raw/processed VCF와 script가 공개된다. VCF representation을 표준화한 뒤 permissive overlap과 exact breakpoint/size를 모두 보고하고, caller별 장점을 반영한 merging과 orthogonal long-read validation을 분리한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient SV나 post-transplant clonal event를 expression outlier와 연결하기 전에 breakpoint·size와 genotype 신뢰도를 점검하는 기준이다. HLA/KIR처럼 homologous한 영역에는 별도 long-read/targeted 검증이 필요하다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- structural variant
- short-read WGS
- benchmark

## 9. Bibliography

Slimmer, James C., et al. “Towards Standards for Analysing Structural Variants from Short-read Whole Genome Sequencing Data.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.13.758836](https://doi.org/10.64898/2026.10.13.758836).
