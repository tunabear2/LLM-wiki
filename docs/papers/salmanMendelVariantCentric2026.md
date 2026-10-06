---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# Mendel: a foundation model of human genetic variation

## 기본 정보

- Citation key: `salmanMendelVariantCentric2026`
- Item type: preprint
- Authors: A. Salman; H. Feng; P. Wei; R. Sun; L. Wu; W. Pan; C. Wu
- Source: bioRxiv (posted 2026-09-30; not peer reviewed)
- DOI: [10.64898/2026.09.28.755183](https://doi.org/10.64898/2026.09.28.755183); [bioRxiv v1](https://www.biorxiv.org/content/10.64898/2026.09.28.755183v1)
- 주 카테고리: `Bio AI`
- 교차 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

Mendel은 diploid variant event를 직접 토큰화한 1B StripedHyena2 모델로 regulatory variant 우선순위와 GTEx gene-expression 예측을 함께 학습한다.

## 2. 연구 질문

reference sequence 언어모델보다 variant 중심 표현이 causal regulatory variant와 개인별 cis-expression을 더 잘 설명할 수 있는가?

## 3. 데이터와 방법

IUPAC diploid variant token과 8,192 bp 문맥을 사용하고, known cohort variant loci를 대상으로 locus-contrastive batch와 variant event에서의 loss를 적용했다. GTEx 50 tissues gene expression 및 causal fine-mapping과 비교했다.

## 4. 핵심 결과

- SNV 분류 정확도는 0.984로 보고되었고, causal fine-mapping AUROC는 0.731이었다.
- GTEx 50개 조직에서 baseline 대비 cis-expression 예측이 개선되었으며, 45개 조직에서 더 많은 유전자가 FDR 기준을 통과했다.
- variant-centric 입력이 eQTL와 expression effect를 하나의 표현 공간에서 연결할 가능성을 보였다.

## 5. 한계

염색체별 모델과 알려진 cohort locus에 의존하여 unseen-locus 일반화가 시험되지 않았다. GTEx의 ancestry·tissue 구성 편향, rare heterozygote 회복 부족, 큰 계산비용과 제한적인 코드 공개도 재현성의 제약이다.

## 6. 재현 또는 활용 포인트

variant representation, reference build, ancestry와 allele frequency를 고정하고 held-out locus를 분리한다. 공개된 모델·코드 조건을 확인하기 전에는 수치 재현을 전제로 하지 않는다.

## 7. Transcriptomics·신장이식 연구와의 연결

donor·recipient variant와 biopsy RNA expression을 연결하는 eQTL/ASE prior로 사용할 수 있지만, HLA와 ancestry confounding을 별도 통제해야 한다. 신장이식 cohort에서는 genotype-to-expression 예측을 실제 genotype의 대체물로 해석하지 않고 외부 조직에서 검증한다.

## 8. 관련 키워드

- genomic foundation model
- variant-centric tokenization
- regulatory variant prioritization
- GTEx cis-expression

## 9. Bibliography

Salman, A., et al. “Mendel, a Foundation Model of Human Genetic Variation, Prioritizes Regulatory Variants and Improves Gene Expression Prediction.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.28.755183](https://doi.org/10.64898/2026.09.28.755183).
