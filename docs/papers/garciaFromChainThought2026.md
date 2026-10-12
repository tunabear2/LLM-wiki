---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# From Chain-of-Thought to Loops: Non-Autoregressive Latent Reasoning via Looped Transformers

## 기본 정보

- Citation key: `garciaFromChainThought2026`
- Item type: preprint
- Authors: Gerard Grau García; Arnau Padrés Masdemont; Niccolò Grillo; Jordi Ros-Giralt; Arash Behboodi; Victor Conchello Vendrell
- Source: arXiv (submitted 2026-10-08; not peer reviewed)
- Original: [arXiv:2610.11472](https://arxiv.org/abs/2610.11472)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

LLoCoT는 reasoning token을 순차 생성하는 대신 고정된 latent workspace를 shared Transformer로 반복 갱신해 reasoning latency를 병렬화한다.

## 2. 연구 질문

명시적 chain-of-thought의 정확도를 유지하면서 reasoning 단계의 직렬 token 생성 병목을 줄일 수 있는가?

## 3. 데이터와 방법

학습 중 explicit CoT의 continuous representation을 target으로 만들고, 64개 latent slot을 두 번 반복 갱신한 뒤 probabilistic head가 latent token을 병렬 표본화해 autoregressive answer decoder를 조건화한다. 1.7B backbone에서 HumanEval과 MBPP를 base model, answer-only SFT, explicit reasoning SFT, NF-CoT와 비교했다.

## 4. 핵심 결과

- 두 code-generation benchmark 평균에서 비교 방법 중 가장 높은 성능을 보였고 explicit reasoning SFT와 비슷한 정확도였다.
- reasoning SFT 대비 첫 answer token까지 약 36배, reasoning 단계 latency는 약 42배 줄었다.
- 전체 throughput은 9.2% 증가했다.

## 5. 한계

검증이 1.7B 모델과 code-generation 두 task에 한정됐다. Reasoning SFT보다 peak memory와 이론 FLOPs가 더 크며, 이득은 계산량 감소보다 병렬화에서 온다. Workspace 크기와 반복 횟수도 입력 난도와 무관하게 고정된다.

## 6. 재현 또는 활용 포인트

Accuracy뿐 아니라 time-to-first-token, reasoning latency, peak memory, FLOPs를 같은 hardware에서 함께 측정한다. CoT target 생성 방식과 latent slot 수·반복 횟수 ablation을 고정하고 비-code reasoning으로 외삽하지 않는다.

## 7. Transcriptomics·신장이식 연구와의 연결

복잡한 임상·omics 추론 agent의 응답 지연을 줄일 후보지만 생물학적 reasoning 정확도는 검증되지 않았다. 근거 추적이 필요한 이식 연구에서는 latent reasoning을 사용하더라도 최종 근거 문장과 데이터 provenance를 별도로 남겨야 한다.

## 8. 관련 키워드

- latent reasoning
- looped Transformer
- non-autoregressive chain-of-thought
- reasoning latency

## 9. Bibliography

García, Gerard Grau, et al. “From Chain-of-Thought to Loops: Non-Autoregressive Latent Reasoning via Looped Transformers.” arXiv, 2026. [https://arxiv.org/abs/2610.11472](https://arxiv.org/abs/2610.11472).
