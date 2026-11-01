---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# Elucidating the Design Space of LM Data Attribution

## 기본 정보

- Citation key: `yuElucidatingDesignSpace2026`
- Item type: arXiv preprint
- Authors: Steven Yu; Sheng-Yu Wang; Kimia Hamidieh; Antonio Torralba; David Bau
- Source: arXiv v1, submitted 2026-10-29
- Original: [arXiv:2610.40655](https://arxiv.org/abs/2610.40655); [project](https://catt.baulab.info/)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

CATT는 완전히 가상인 사실을 학습시켜 정답 training evidence를 아는 통제 환경에서 LM data attribution을 진단하고, negative-log-odds gradient와 top-token 집계가 문서 전체 평균의 신호 희석을 크게 줄임을 보였다.

## 2. 연구 질문

Language model이 특정 사실을 생성하게 한 학습 문서를 정확히 찾는가를 dataset redundancy와 lexical distractor 같은 요인별로 분리해 평가할 수 있는가?

## 3. 데이터와 방법

가상의 지식으로 LM을 fine-tuning해 causal source document의 ground truth가 명확한 Controlled Attribution Benchmark for facT Tracing(CATT)를 만들었다. 문서 중복과 lexical distractor를 한 번에 하나씩 바꾸고 여러 attribution baseline을 비교했다. Gradient loss를 cross-entropy에서 negative log-odds로 바꾸고 문서 점수는 전체 token 평균 대신 상위 token만 집계했으며, FTRACE-TREX의 counterfactual retraining으로 외부 평가했다.

## 4. 핵심 결과

- 중복 문서와 distractor가 attribution 성능을 일관되게 낮췄다.
- Causal evidence는 일부 token에 국소화되어 있었고, negative-log-odds와 top-token 집계가 baseline 대비 ground-truth recall을 35–72 percentage point 높였다.
- FTRACE-TREX에서도 모든 평가 방법의 counterfactual retraining 성능이 개선되었고 최대 향상은 4.9배였다.

## 5. 한계

CATT의 핵심 ground truth는 합성 지식과 fact-tracing 설정에서 얻었다. 자연 문서의 중복·모순·시간 변화가 있는 대규모 biomedical corpus나 frontier-scale model에서 같은 개선 폭이 유지되는지는 별도 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Document redundancy와 lexical distractor를 따로 조절하고 token-level score distribution을 보존한다. Mean aggregation, top-token aggregation, cross-entropy gradient, negative-log-odds gradient를 같은 counterfactual retraining protocol로 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Biopsy 보고서·논문·임상 지침을 학습하거나 검색하는 LM이 어떤 문서의 어떤 문구에 의존했는지 감사하는 기준이 된다. 다만 합성 fact benchmark의 높은 recall을 임상 근거 추적 신뢰도로 직접 해석하면 안 된다.

## 8. 관련 키워드

- LLM / Transformer
- data attribution
- evaluation benchmark
- training-data tracing

## 9. Bibliography

Yu, Steven, et al. “Elucidating the Design Space of LM Data Attribution.” arXiv:2610.40655, 2026. [https://arxiv.org/abs/2610.40655](https://arxiv.org/abs/2610.40655).
