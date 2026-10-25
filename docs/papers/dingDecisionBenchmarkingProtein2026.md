---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# Decision Benchmarking Reveals When Protein Foundation Models Add Experimental Value

## 기본 정보

- Citation key: `dingDecisionBenchmarkingProtein2026`
- Item type: bioRxiv preprint
- Authors: W. Ding; C. Lu; Y. Li; H. Gong; Z. Wang
- Source: bioRxiv v1, posted 2026-10-20 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.13.758966](https://doi.org/10.64898/2026.10.13.758966)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

217개 ProteinGym assay에서 predictor 순위가 아니라 같은 실험비용으로 발견·우선순위 결정이 얼마나 좋아지는지를 평가해, protein FM의 이득이 measurement budget과 의사결정 목표에 따라 바뀜을 보였다.

## 2. 연구 질문

Zero-shot protein foundation model은 이미 일부 변이를 측정한 상황에서도 어떤 실험 의사결정에 실제 추가 가치를 주는가?

## 3. 데이터와 방법

ProteinGym의 217개 assay, 247만 variant와 95개 predictor를 사용했다. 20–100개 또는 더 많은 measurement budget에서 calibrated model prior, measured additivity, double-mutant measurement와 prediction-guided acquisition을 같은 비용으로 비교하고 evidence-based routing을 평가했다.

## 4. 핵심 결과

- Zero-shot accuracy는 calibration 뒤 discovery 성능 변이의 20% 미만만 설명했다.
- Calibrated prior는 20–100 measurement에서 budget-matched additivity보다 유리했지만, top-variant discovery는 50–100개, global ranking은 약 500개 측정 후 measured additivity가 앞섰다.
- Prediction-guided acquisition은 discovery를 개선했고 assay-level evidence routing은 random routing보다 나았다.

## 5. 한계

Retrospective ProteinGym substitution landscape에 한정되며 indel, de novo design과 실제 campaign 비용은 포함하지 않았다. 재현용 독립 code repository는 원문에서 확인되지 않았다.

## 6. 재현 또는 활용 포인트

AUROC나 correlation만 보고 model을 고르지 말고 측정 수, top-hit discovery, global ranking, 실험비용을 명시한 decision curve로 비교한다. Assay별 component coverage에 따라 전략을 다시 선택한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection biomarker나 표적 우선순위에서도 예측점수 자체보다 제한된 검증 실험으로 어떤 후보를 측정할지를 평가해야 한다. Protein variant 결과를 transcriptomic 후보선정에 직접 전이하는 근거는 아니다.

## 8. 관련 키워드

- Bio AI
- protein foundation model
- decision benchmarking
- active learning

## 9. Bibliography

Ding, W., et al. “Decision Benchmarking Reveals When Protein Foundation Models Add Experimental Value.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.13.758966](https://doi.org/10.64898/2026.10.13.758966).
