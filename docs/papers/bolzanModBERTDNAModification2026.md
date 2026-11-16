---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# ModBERT: a DNA modification and genetic variant-aware DNA large language model

## 기본 정보

- Citation key: `bolzanModBERTDNAModification2026`
- Item type: preprint
- Authors: Dante Bolzan; Ramana V. Davuluri; Shaun Mahony; Ferhat Ay
- Source: bioRxiv v1, posted 2026-11-13 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.12.766258](https://doi.org/10.64898/2026.11.12.766258)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

ModBERT는 allele frequency와 CpG methylation을 A/C/G/T/5mC 확률분포로 표현해 개인별 genetic·epigenetic sequence를 함께 읽는 DNA language model이다.

## 2. 연구 질문

Reference genome만 학습하는 DNA model에 population variant와 methylation을 함께 넣으면 개인별 chromatin·variant effect prediction을 개선할 수 있는가?

## 3. 데이터와 방법

1000 Genomes Long-Read Sequencing Consortium 242명의 allele frequency와 CpG methylation으로 five-letter probabilistic genome을 만들고 soft-target masked language modeling을 수행했다. 개인 fine-tuning에서는 genotype과 methylation을 같은 확률 표현에 넣었다. 11개 histone mark, 69개 transcription factor ChIP-seq, chromatin accessibility, caQTL effect로 평가했다.

## 4. 핵심 결과

- Methylation을 포함한 ModBERT가 ab initio model과 methylation 없는 ModBERT보다 functional-genomics peak classification에서 높았다.
- Held-out locus와 held-out individual을 동시에 분리한 chromatin-accessibility 평가에서 AUROC 0.88을 보고했다.
- Predicted variant effect는 likely causal caQTL과 Spearman 0.52로 일치했지만 LD로만 연관된 variant와는 일치하지 않았다.

## 5. 한계

Pretraining population은 242명이고 평가가 chromatin·binding task 중심이다. 개인별 expression, 임상 outcome, 다양한 ancestry의 외부 cohort 및 long-read chemistry 간 일반화는 초록에서 검증되지 않았다.

## 6. 재현 또는 활용 포인트

Genome build, variant phasing, methylation caller·probability calibration, locus/individual double holdout을 명시한다. Sequence-only, methylation-only, joint model을 같은 locus와 ancestry split에서 비교하고 causal caQTL과 LD proxy를 분리한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient phased genotype과 methylation으로 immune·tubular regulatory activity를 개인화하고 biopsy eQTL·ASE·expression outlier 후보를 정렬할 수 있다. 실제 rejection 예측에서는 genotype/methylation이 임상변수와 transcriptome 위에 주는 순증분 가치를 외부 cohort에서 평가해야 한다.

## 8. 관련 키워드

- DNA language model
- methylation
- personal genome
- variant effect prediction

## 9. Bibliography

Bolzan, Daniele, et al. “ModBERT: a DNA modification and genetic variant-aware DNA large language model.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.12.766258](https://doi.org/10.64898/2026.11.12.766258).
