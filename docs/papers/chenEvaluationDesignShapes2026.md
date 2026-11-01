---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# Evaluation Design Shapes Estimates of Cross-Donor Generalization in Single-Cell Classification

## 기본 정보

- Citation key: `chenEvaluationDesignShapes2026`
- Item type: bioRxiv preprint
- Authors: X. Chen; J. Li; A. Battle
- Source: bioRxiv v1, posted 2026-10-27 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.26.761949](https://doi.org/10.64898/2026.10.26.761949); [code](https://github.com/danielchen05/scRNA-cross-donor-generalization/); [Zenodo](https://doi.org/10.5281/zenodo.23669184)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

PBMC와 lung scRNA-seq에서 random cell split이 donor-held-out split보다 cell-type macro-F1을 일관되게 높여, unseen individual 일반화를 주장하려면 donor 단위 평가가 필요함을 보였다.

## 2. 연구 질문

같은 donor에서 나온 cell의 비독립성을 무시한 random cell split이 cross-donor cell-type classification 성능을 얼마나 낙관적으로 추정하는가?

## 3. 데이터와 방법

PBMC와 lung dataset에서 여러 expression representation을 사용해 random cell-level split과 donor-held-out evaluation의 macro-F1을 비교했다. Batch covariate adjustment와 donor-level mixed-effects model 뒤에도 gap이 남는지 확인했다. Kidney·pancreas·blood의 near-ceiling benchmark와 randomized-label floor control을 대조군으로 사용했다.

## 4. 핵심 결과

- PBMC와 lung에서 random cell split 성능이 donor-held-out보다 일관되게 높았다.
- 차이는 batch covariate 보정과 donor-level mixed-effects modeling 뒤에도 유지되었다.
- Near-ceiling benchmark와 randomized-label floor에서는 gap이 작아 bias 크기가 classification regime에 의존했다.

## 5. 한계

Cell-type classification과 공개 dataset에 집중했으며 phenotype prediction, perturbation, rare-state discovery를 직접 평가하지 않았다. 초록에는 dataset별 효과 크기가 제시되지 않아 실제 위험도는 cohort별 재평가가 필요하다.

## 6. 재현 또는 활용 포인트

Donor를 완전히 분리한 train/validation/test split을 만들고 random-cell 결과를 낙관적 대조군으로 함께 남긴다. Macro-F1과 rare-cell recall을 donor별 confidence interval로 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

여러 cell이 같은 biopsy·환자에서 나온 allograft scRNA-seq에서 cell-level split leakage를 막는 직접적인 평가 원칙이다. Rejection subtype·graft outcome은 cell이 아니라 donor 단위로 검증해야 한다.

## 8. 관련 키워드

- scRNA-seq
- cross-donor generalization
- evaluation leakage
- cell-type classification

## 9. Bibliography

Chen, X., J. Li, and A. Battle. “Evaluation Design Shapes Estimates of Cross-Donor Generalization in Single-Cell Classification of Cell-Type.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.26.761949](https://doi.org/10.64898/2026.10.26.761949).
