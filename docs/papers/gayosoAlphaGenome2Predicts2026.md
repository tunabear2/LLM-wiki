---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# AlphaGenome 2 predicts regulatory activity and variant effects across cell states

## 기본 정보

- Citation key: `gayosoAlphaGenome2Predicts2026`
- Item type: preprint
- Authors: Adam Gayoso et al.
- Source: bioRxiv v1, posted 2026-11-17 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.11.765857](https://doi.org/10.64898/2026.11.11.765857)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

AlphaGenome 2는 1-Mb DNA와 tissue·cell type·cell state 조건을 함께 입력해 단일세포 atlas에 맞춘 regulatory activity, enhancer–gene link와 variant effect를 예측하는 sequence-to-function foundation model이다.

## 2. 연구 질문

Donor 수가 적은 single-cell atlas에서도 sequence model을 세포 상태로 조건화하면 가까운 cell state의 조절 차이와 비암호화 변이 효과를 fine-tuning 없이 구분할 수 있는가?

## 3. 데이터와 방법

Human·mouse organism-wide single-cell atlas와 ENCODE·GTEx·4D Nucleome·FANTOM5 등 bulk functional genomics를 함께 학습했다. Condition embedding을 sequence network 전반에 주입하며, 새 scRNA-seq dataset에서는 gene expression으로 condition을 추론한다. Single-cell eQTL, enhancer–gene linking, chromatin·expression imputation, fine-mapped GWAS variant에서 AlphaGenome 1 및 dataset-specific model과 비교했다.

## 4. 핵심 결과

- Causal single-cell eQTL을 90% precision에서 찾는 recall이 fine-tuned AlphaGenome 1보다 약 2배 높았다고 보고했다.
- Enhancer–gene linking과 cell-state-specific regulatory prediction에서 specialized baseline을 넘어섰다.
- 640개 human condition의 enhancer–gene atlas와 510개 condition에서 약 700만 common·trait-associated variant score를 만들었다.

## 5. 한계

높은 precision에서는 fine-mapped eQTL과 GWAS causal variant의 일부만 회수했다. Accessible chromatin 밖, 매우 먼 element, post-transcriptional mechanism의 효과를 과소평가하며 disease·stimulated·transient state가 학습자료에 부족하다. Condition embedding은 관찰자료의 상관 구조를 반영하므로 perturbation이나 동적 전이를 인과적으로 예측한다고 볼 수 없다.

## 6. 재현 또는 활용 포인트

Reference build, condition ontology, 학습 atlas와 target cohort 중복, fine-mapping 기준을 기록한다. API score는 eQTL colocalization, allele-specific expression, chromatin accessibility와 교차 검증하고 cell state별 precision–recall을 따로 본다. 현재 model은 비상업 연구용 API이며 임상 진단용으로 검증되지 않았다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection GWAS·donor/recipient variant를 immune, endothelial, tubular cell state별 enhancer–gene link와 연결하는 강력한 prior가 될 수 있다. 그러나 rejection·면역억제 자극 상태가 학습 atlas에 부족하므로 biopsy scRNA/ATAC, eQTL·ASE로 반드시 후속 검증해야 한다.

## 8. 관련 키워드

- genomic foundation model
- variant effect prediction
- enhancer–gene linking
- single-cell atlas
- GWAS interpretation

## 9. Bibliography

Gayoso, Adam, et al. “AlphaGenome 2 Predicts Regulatory Activity and Variant Effects across Cell States.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.11.765857](https://doi.org/10.64898/2026.11.11.765857).
