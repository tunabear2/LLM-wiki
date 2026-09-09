---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# Prefix Sliding for efficient test-time scaling

## 기본 정보

- Citation key: muennighoffPrefixSlidingEfficient2026
- Item type: arXiv preprint
- Authors: Niklas Muennighoff; Zhengyang Wang; Zeyi Chen; Weijia Shi; Binyuan Hui; John Yang; Dapeng Jiang; Mika Senghaas; Fares Obeid; Johannes Hagemann; Sami Jaghouar; Ludwig Schmidt; Percy Liang; Jason Wei; Andrew Y. Ng; Luke Zettlemoyer; Yejin Choi; Mike Lewis
- arXiv: 2608.26070
- DOI: 10.48550/arXiv.2608.26070
- URL: [arXiv](https://arxiv.org/abs/2608.26070)
- Source/date: arXiv v1, 2026-08-26
- 주 카테고리: LLM / Transformer

## 1. 한 줄 요약

Prefix Sliding은 긴 추론 중 고정 instruction prefix와 최근 토큰 창만 attention에 남겨 KV-cache와 토큰당 계산량을 제한하는 test-time scaling 방법이다.

## 2. 연구 질문

중간 reasoning token 대부분의 영향력이 시간이 지나며 감소한다면, 핵심 지시와 현재 추론 문맥만 보존해 정확도를 유지하면서 장기 추론 비용을 줄일 수 있는가?

## 3. 데이터와 방법

고정 prefix와 최근 수천 토큰 window 사이의 토큰을 제거하는 attention 방식을 training-free 설정과 Prefix Sliding을 사용한 강화학습 설정에서 평가했다. Qwen3-1.7B를 중심으로 7B 부록 실험을 수행하고 AIME25, GPQA, MATH500 등에서 최대 64회 test-time sampling을 비교했으며 Hopper용 FlashAttention kernel과 공개 구현도 제시했다.

## 4. 핵심 결과

저자 보고 기준 training 없이 기존 모델을 최대 약 3배 빠르게 하면서 주요 reasoning benchmark 성능을 full attention과 비슷하게 유지했다. 강화학습을 결합하면 10만 토큰을 넘는 reasoning trace까지 확장할 수 있었고, 중간 토큰 요약이나 일반 sliding window보다 나은 결과를 보였다.

## 5. 한계

아직 peer review 전이며 주 실험 모델이 1.7B, 최대 검증이 7B 규모다. 과거 세부 정보가 다시 필요한 코드 문제에서는 16K 이상의 window가 필요했고 짧은 생성에서는 이득이 작다. 긴 tool output, multi-turn 지시, 사실 회수 정확도에 대한 검증도 제한적이다.

## 6. 재현 또는 활용 포인트

- 코드: [Muennighoff/prefix-sliding](https://github.com/Muennighoff/prefix-sliding)
- full attention, 같은 크기의 sliding window, 중간 요약을 동일 토큰 예산에서 비교해야 한다.
- 속도뿐 아니라 최대 메모리, 토큰당 지연, 장기 사실 회수 실패율을 함께 측정하는 것이 안전하다.

## 7. Transcriptomics·신장이식 연구와의 연결

긴 오믹스 문헌과 임상 기록을 읽는 RAG·분석 agent의 추론 비용을 낮출 후보지만, 생물학적 근거 문장과 환자별 시계열 정보가 중간 문맥에서 유실되지 않는지 별도 검증해야 한다.

## 8. 관련 키워드

- LLM / Transformer
- Test-time scaling
- Efficient attention
- KV-cache
- Long-horizon reasoning

## 9. Bibliography

Muennighoff, Niklas, et al. “Prefix Sliding for Efficient Test-Time Scaling.” arXiv:2608.26070, 2026. [https://doi.org/10.48550/arXiv.2608.26070](https://doi.org/10.48550/arXiv.2608.26070).
