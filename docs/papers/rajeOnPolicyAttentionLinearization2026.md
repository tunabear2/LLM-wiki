---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# On-Policy Attention Linearization

## 기본 정보

- Citation key: `rajeOnPolicyAttentionLinearization2026`
- Item type: preprint
- Authors: Arian Raje; Anupam Nayak; Anthony Fei; Akaash Parthasarathy; Mohamed Abdelfattah; Gauri Joshi
- arXiv: 2609.31947
- DOI: 10.48550/arXiv.2609.31947
- URL: [arXiv](https://arxiv.org/abs/2609.31947); [DOI](https://doi.org/10.48550/arXiv.2609.31947)
- Source/date: arXiv v1, submitted 2026-09-25; not peer reviewed
- 주 카테고리: LLM / Transformer

## 1. 한 줄 요약

OPAL은 full-attention 언어 모델의 75% attention layer를 linear attention으로 바꾼 뒤, 학생 모델이 생성한 장기 trajectory에서 교사 신호를 받는 on-policy distillation으로 retrieval과 reasoning 손실을 회복한다.

## 2. 연구 질문

Full-attention Transformer를 효율적인 hybrid attention 모델로 사후 변환할 때, fixed corpus를 이용한 off-policy distillation에서 누적되는 recurrent-state 오류를 줄이면서 장문 검색과 추론 능력을 보존할 수 있는가?

## 3. 데이터와 방법

Qwen3-4B와 MiMo-7B-RL-0530의 36개 layer 중 27개를 Gated DeltaNet으로 교체하고 9개 full-attention layer를 유지했다. 학습은 100M-token hidden-state alignment, 600M-token 4K-context 및 300M-token 32K-context off-policy distillation, 2B-token on-policy distillation으로 구성된다. 마지막 단계에서는 학생 rollout 길이를 512에서 32K token까지 늘리고 frozen teacher의 token-level 분포를 따라가게 한다. FineWeb-Edu, CodeParrot-Clean, OpenWebMath와 수학·instruction·합성 retrieval prompt를 사용했으며, commonsense 6종, 4K–32K needle retrieval, GSM 계열, MATH-500과 AIME에서 평가했다.

## 4. 핵심 결과

두 hybrid model은 needle-in-a-haystack 평가에서 full-attention teacher의 성능을 사실상 모두 회복했다. 평균 수학 추론 성능은 Qwen 기반 모델이 teacher의 83.4%, MiMo 기반 모델이 93.4%를 유지했고, 절대 평균은 각각 67.6%와 72.2%였다. 128K context에서는 cache와 recurrent-state memory가 full attention보다 약 4배 작았고, 높은 동시성 조건의 serving throughput은 약 2배 높았다. 별도의 SFT나 RLVR 없이 모델당 약 3B training token을 사용했다.

## 5. 한계

검증 대상은 4B와 7B급 두 모델이며, 장문 평가는 합성 retrieval과 수학 reasoning에 집중된다. Commonsense benchmark 유지율은 Qwen 86.9%, MiMo 93.7%로 장문 능력 회복과 일반 성능 사이의 trade-off가 남았다. arXiv v1 본문에는 코드나 변환 checkpoint 공개 링크가 없어 결과를 즉시 재현하기 어렵다.

## 6. 재현 또는 활용 포인트

- 공개 Qwen3-4B와 MiMo-7B-RL-0530 teacher를 기준으로 동일한 9:27 full-attention/Gated-DeltaNet 구성을 비교한다.
- Off-policy control과 student-generated on-policy trajectory를 같은 token budget으로 비교한다.
- Retrieval·reasoning 점수와 함께 KV/state memory, latency, throughput과 commonsense 성능 저하를 보고한다.
- 논문은 3–4대 NVIDIA H100 또는 H200을 사용했고, 학습 dataset의 평가 문항 13-gram overlap을 제거했다.

## 7. Transcriptomics·신장이식 연구와의 연결

직접적인 생의학 검증은 없지만, 긴 유전자 token sequence나 다수의 임상 기록·논문을 함께 처리하는 transcriptomics RAG의 memory 비용을 줄이는 architecture-conversion 후보가 될 수 있다. 적용 전에는 거부반응 판정, cohort 수치와 marker gene 같은 핵심 evidence가 긴 context에서 보존되는지 별도로 평가해야 한다.

## 8. 관련 키워드

- LLM / Transformer
- Linear attention
- Hybrid attention
- On-policy distillation
- Long-context reasoning
- Efficient inference

## 9. Bibliography

Raje, Arian, Anupam Nayak, Anthony Fei, Akaash Parthasarathy, Mohamed Abdelfattah, and Gauri Joshi. “On-Policy Attention Linearization.” arXiv:2609.31947, version 1, 2026. [https://doi.org/10.48550/arXiv.2609.31947](https://doi.org/10.48550/arXiv.2609.31947). Preprint; not peer reviewed.
