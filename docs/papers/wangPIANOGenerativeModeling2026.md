---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# PIANO: Generative Gene-Expression Modeling and 100-Million-Cell Integration

## 기본 정보

- Citation key: `wangPIANOGenerativeModeling2026`
- Item type: journal article
- Authors: Ning Wang; Christopher Cardenas; Victor E. Nieto-Caballero; David Turner; Hannah Feinberg; Dan Yuan; Nathaniel Scott; Michael DeBerardine; Shu Dan; Lakme Caceres; Jessica Schembri; Wen-Jou Chang; Zizhen Yao; Changkyu Lee; Jonathan W. Pillow; Fenna M. Krienen
- Source: _Cell Reports Methods_, article 101661, published online 2026-11-12
- Original: [DOI 10.1016/j.crmeth.2026.101661](https://doi.org/10.1016/j.crmeth.2026.101661)
- PubMed: [PMID 43020064](https://pubmed.ncbi.nlm.nih.gov/43020064/)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

PIANO는 covariate가 gene expression에 미치는 영향을 생성모형으로 분리하면서 species·single-cell·spatial modality를 통합하고 1억 개 cancer cell까지 확장한 deep-learning framework다.

## 2. 연구 질문

강한 batch effect를 보정하면서 수천만~1억 cell로 확장하고, 단순 latent alignment를 넘어 covariate별 expression 변화를 생성적으로 모델링할 수 있는가?

## 3. 데이터와 방법

Probabilistic inference autoencoder network에 gene-expression generative model을 결합했다. Species 간, scRNA-seq와 spatial transcriptomics 간 통합을 평가하고, human Alzheimer brain의 공간 발현 진행 및 1억 개가 넘는 cancer cell의 drug perturbation을 모델링했다.

## 4. 핵심 결과

- 비교 방법보다 training이 10배 빠르다고 보고했다.
- Species 및 single-cell–spatial modality 간 integration에서 강건한 결과를 보였다.
- 1억 개가 넘는 cancer cell을 통합해 drug perturbation을 모델링하는 확장성을 시연했다.

## 5. 한계

초록은 세부 baseline, hardware, cell·donor split, biological-signal preservation 수치를 모두 제공하지 않는다. 대규모 integration에서 batch 제거와 disease·treatment state 보존을 donor-held-out 평가로 따로 확인해야 한다.

## 6. 재현 또는 활용 포인트

Count likelihood, covariate design, latent dimension, minibatch·distributed-training 설정과 hardware를 기록한다. Batch mixing score와 cell-type/state conservation, held-out donor reconstruction, runtime·memory를 함께 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

기관·platform·시점이 다른 대규모 kidney atlas와 spatial biopsy를 통합하고 injury·rejection covariate의 발현 효과를 분리하는 후보이다. Diagnosis·treatment 신호를 batch로 지우지 않는지 donor·center holdout으로 검증해야 한다.

## 8. 관련 키워드

- single-cell integration
- generative model
- multi-omics
- atlas-scale learning

## 9. Bibliography

Wang, Ning, et al. “PIANO enables generative modeling of gene expression and scales multi-omics integration to 100 million cells.” _Cell Reports Methods_, 2026, 101661. [https://doi.org/10.1016/j.crmeth.2026.101661](https://doi.org/10.1016/j.crmeth.2026.101661).
