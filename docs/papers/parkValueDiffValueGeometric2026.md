---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs

## 기본 정보

- Citation key: `parkValueDiffValueGeometric2026`
- Item type: preprint
- Authors: Junyoung Park; Jungwook Choi; Mingu Lee
- arXiv: 2609.23314
- DOI: 10.48550/arXiv.2609.23314
- URL: [arXiv](https://arxiv.org/abs/2609.23314); [DOI](https://doi.org/10.48550/arXiv.2609.23314)
- Source/date: arXiv v1, submitted 2026-09-20; not peer reviewed
- 주 카테고리: LLM / Transformer

## 1. 한 줄 요약

ValueDiff는 persistent attention sink가 약한 최신 LLM에서 key가 아니라 cache 평균으로부터의 value-vector 거리를 이용해, 고정 KV-cache 예산 안에서 덜 중요한 token을 제거한다.

## 2. 연구 질문

QK normalization, gated attention, learned sink 또는 logit softcapping 때문에 기존 sink 기반 eviction 신호가 약해진 모델에서도 query와 무관하게 안정적인 cache 중요도 점수를 만들 수 있는가?

## 3. 데이터와 방법

각 token의 value vector가 현재 cache의 value 평균에서 떨어진 L2 거리를 점수로 사용한다. 저자들은 미래 attention을 maximum-entropy로 가정하면 이 점수가 eviction으로 인한 output 교란을 최소화하는 기준으로도 유도된다고 설명한다. Prefill의 block boundary와 generation의 매 decoding step에서 eviction하며, RULER, LongBench, MATH-500과 sink-suppressed model 7종에서 고정 cache budget으로 비교했다.

## 4. 핵심 결과

RULER 2K-token budget에서 dense-cache 성능의 88–99%를 보존했고 7개 모델 중 6개에서 가장 높았다. LongBench 4K budget에서는 평균 dense-retention 92%로 가장 강한 기존 baseline의 83%를 앞섰다. MATH-500의 25% cache budget에서는 시험한 모든 sink-suppressed model에서 가장 강한 non-dense 방법이었고, gated-attention model에서는 기존 방법보다 최대 약 20점 높았다.

## 5. 한계

검증은 sink-suppressed architecture, 세 benchmark와 지정 budget에 집중된다. 이론은 미래 attention에 대한 maximum-entropy 가정에 의존하며, 실제 serving latency·memory fragmentation·batching 비용과 매우 긴 생성에서의 안정성은 별도 검증이 필요하다. 현재 결과는 v1 preprint다.

## 6. 재현 또는 활용 포인트

- Dense, 최근-token, sink 기반, key-geometry baseline과 동일 cache budget·eviction 주기로 비교한다.
- 모델별 attention-sink strength와 key/value dispersion을 먼저 측정한다.
- Accuracy retention뿐 아니라 peak memory, decode latency와 eviction overhead를 함께 기록한다.
- 긴 논문 RAG나 transcriptomics 보고서 생성에서는 evidence token이 선택적으로 탈락하는지 별도 점검한다.

## 7. Transcriptomics·신장이식 연구와의 연결

긴 임상 기록과 논문 근거를 함께 처리하는 RAG inference의 KV memory를 줄이는 후보지만 생물학 자료에서 검증된 방법은 아니다. 이식 근거 검색에서는 숫자·코호트·거부반응 판정 token의 보존율을 따로 평가해야 한다.

## 8. 관련 키워드

- LLM / Transformer
- KV cache eviction
- Value geometry
- Long-context inference
- Attention sink

## 9. Bibliography

Park, Junyoung, Jungwook Choi, and Mingu Lee. “ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs.” arXiv:2609.23314, version 1, 2026. [https://doi.org/10.48550/arXiv.2609.23314](https://doi.org/10.48550/arXiv.2609.23314). Preprint; not peer reviewed.
