---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# Deep-learning-driven Tumor Microenvironment Profiling Improves Immunotherapy Response Prediction

## 기본 정보

- Citation key: `wangDeepLearningDrivenTumor2026`
- Item type: bioRxiv preprint
- Authors: Ruo Han Wang; Brooks A. Benard; Ilayda Ilerten; Sabrina Zdravkovic; Reem Al-Humadi; Sahar Nasr; Brooke Howitt; Andrew J. Gentles
- Source: bioRxiv v1, posted 2026-10-13 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.06.757143](https://doi.org/10.64898/2026.10.06.757143); [EcoNet code](https://github.com/Gentles-lab/EcoNet); [test data](https://doi.org/10.5281/zenodo.22986445)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

EcoNet은 bulk transcriptome에서 추정한 tumor ecosystem과 조절·ligand–receptor network를 graph attention으로 통합해 pan-cancer 면역치료 반응을 예측하고 ccRCC cohort와 spatial data로 신호를 검증했다.

## 2. 연구 질문

독립 marker나 cell fraction 대신 TME의 cell-state 공존 구조와 방향성 신호망을 모델링하면 면역치료 반응 예측과 기전 해석이 개선되는가?

## 3. 데이터와 방법

2,532개 pan-cancer immunotherapy sample에서 EcoTyper cell state/ecotype과 scRNA 기반 ligand–receptor·조절 network를 만들고 graph attention embedding을 학습했다. 아홉 carcinoma의 공통 edge로 pan-cancer network를 구성한 뒤 ccRCC에 fine-tuning했다. 독립 ccRCC outcome cohort와 46개 ccRCC sample·약 45만 cell의 CosMx spatial transcriptomics로 검증했다.

## 4. 핵심 결과

- 기존 예측법보다 AUC 7.5–19.9%, marker signature보다 4.4–21.2% 높았다.
- High-attention gene은 독립 CRISPR T-cell-killing screen의 필수 gene에 enriched되었다.
- Fine-tuned score는 독립 ccRCC cohort의 outcome을 구분했고(P=0.024), interferon·antigen-presentation program은 spatial immune-enriched niche에 모였다.

## 5. 한계

아직 peer review 전이며 임상적 유용성을 평가한 전향 시험은 아니다. ccRCC spatial validation은 46개 sample이고, network는 deconvolution과 기존 interaction database의 추론에 의존한다. 새 CosMx data는 출판 시 GEO 공개 예정으로 즉시 완전 재현 가능한 상태는 아니다.

## 6. 재현 또는 활용 포인트

Code와 test data가 공개된다. Pan-cancer pretraining, cancer-specific fine-tuning, 완전 독립 outcome test를 분리하고 attention gene은 CRISPR·spatial localization 같은 orthogonal evidence로 확인하는 설계가 핵심이다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection biopsy에서도 T cell–myeloid–endothelial–tubular state의 공존과 방향성 cytokine network를 patient-level outcome으로 올리는 구조를 참고할 수 있다. 단, 암에서 정의한 ecotype과 edge를 이식 면역에 그대로 전이해서는 안 된다.

## 8. 관련 키워드

- Cancer Transcriptomics / Clinical Prediction
- tumor microenvironment
- immunotherapy response
- spatial transcriptomics

## 9. Bibliography

Wang, Ruo Han, et al. “Deep-learning-driven Tumor Microenvironment Profiling Improves Immunotherapy Response Prediction.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.06.757143](https://doi.org/10.64898/2026.10.06.757143).
