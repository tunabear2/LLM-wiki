---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# GEMS: GWAS Effect Mechanisms via Sequence-to-Function

## 기본 정보

- Citation key: `xieGEMSGWASEffect2026`
- Item type: bioRxiv preprint
- Authors: Xiaoman Xie; Sheng Qian; Diana Chang; Tushar Bhangale; Mark I. McCarthy; Gokcen Eraslan; Kipper Fletez-Brant
- Source: bioRxiv v1, posted 2026-10-16 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.14.759213](https://doi.org/10.64898/2026.10.14.759213)
- 주 카테고리: `GWAS`

## 1. 한 줄 요약

GEMS는 Borzoi의 ATAC/RNA variant-effect prediction으로 fine-mapped GWAS variant를 분류하고 SHAP으로 variant별 관련 cell type을 연결해, aggregate enrichment를 개별 조절기전 수준으로 확장한다.

## 2. 연구 질문

비암호화 GWAS variant가 어느 cell type과 regulatory program에서 작동하는지 sequence-to-function model의 예측으로 복원할 수 있는가?

## 3. 데이터와 방법

Fine-mapped variant(PIP>0.1)를 positive, 같은 locus ±500 kb의 PIP<0.01 variant를 control로 두고 Borzoi의 cell-type별 ATAC-seq와 RNA-seq effect를 random forest feature로 사용했다. SHAP attribution과 permutation informativity score를 적용하고 asthma, LDL cholesterol, multiple sclerosis, type 2 diabetes에서 sLDSC 및 독립 cis-regulatory element와 비교했다.

## 4. 핵심 결과

- Fine-mapped variant의 median 58.7%는 ATAC, 65.9%는 RNA prediction으로 하나 이상의 cell type과 연결됐다.
- ATAC 기반 연결은 training atlas peak 밖 variant를 제외해도 독립 실험의 cis-regulatory element에 enriched되었다.
- Multiple sclerosis variant를 immune와 CNS module로 나누고 서로 다른 transcription-factor family를 연결했다.

## 5. 한계

유사한 regulatory program의 cell type을 잘 구분하지 못하고 Borzoi training tissue 범위에 제한된다. Borzoi RNA target 상당수가 bulk tissue여서 state resolution이 낮다. 충분한 fine-mapped variant가 필요한 well-powered GWAS에 적합하며, 다른 GWAS로 바꾸면 GEMS와 sLDSC 모두 성능이 낮아졌다. 원문에는 code/data availability가 명시되지 않았다.

## 6. 재현 또는 활용 포인트

GWAS별 positive/control 정의, locus leakage 방지, random seed에 따른 feature-importance 안정성과 permutation informativity를 기록한다. SHAP cell-type label은 독립 ATAC/eQTL/CRISPR 자료로 검증해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient GWAS hit을 immune, endothelial, tubular context와 biopsy expression으로 연결하는 후보 구조다. 이식 phenotype GWAS의 sample size와 fine-mapping power가 작으면 직접 학습보다 외부 trait prior를 쓰는 편이 현실적이다.

## 8. 관련 키워드

- GWAS
- fine-mapping
- variant-effect prediction
- cell-type interpretation

## 9. Bibliography

Xie, Xiaoman, et al. “GEMS (GWAS Effect Mechanisms via Sequence-to-Function): Unveiling Cell Type-specific Mechanisms for GWAS Variants.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.14.759213](https://doi.org/10.64898/2026.10.14.759213).
