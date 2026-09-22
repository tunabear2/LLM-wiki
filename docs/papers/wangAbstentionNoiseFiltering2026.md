---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention

## 기본 정보

- Citation key: `wangAbstentionNoiseFiltering2026`
- Item type: preprint
- Author: Richard Zhe Wang
- arXiv: 2609.22005
- DOI: 10.48550/arXiv.2609.22005
- URL: [arXiv](https://arxiv.org/abs/2609.22005); [DOI](https://doi.org/10.48550/arXiv.2609.22005)
- Source/date: arXiv v1, submitted 2026-09-18; not peer reviewed
- 주 카테고리: LLM / Transformer

## 1. 한 줄 요약

Softmax attention의 value gating 이득을 head가 아무것도 출력하지 않는 abstention과 residual-stream 간섭을 억제하는 noise filtering으로 분해해, 두 기능을 함께 넣을 때 가장 안정적으로 개선됨을 보였다.

## 2. 연구 질문

Attention value gate가 성능을 높이는 이유는 확률합 1 제약을 피하는 abstention 때문인가, superposed feature의 간섭을 제거하는 filtering 때문인가, 또는 두 효과가 scale에 따라 달라지는가?

## 3. 데이터와 방법

Per-head learned sink logit으로 abstention을, value별 gate로 noise filtering을 구현하고 10M, 50M, 124M, 350M parameter의 matched language model을 학습했다. Baseline, abstention-only, filtering-only, 두 기능 결합 모델을 validation loss로 비교하고, value pathway에 통제된 인공 interference를 주입해 gate가 어떤 잡음을 제거하는지 시험했다.

## 4. 핵심 결과

Abstention의 이득은 model scale이 커질수록 감소한 반면 filtering 이득은 증가했다. 10M에서는 gating 이득의 대부분을 abstention이 설명했고 350M에서는 filtering이 대부분을 설명했다. 두 primitive를 함께 구현한 모델이 모든 scale에서 가장 좋았으며 추가 parameter는 미미하고 KV cache와 호환됐다.

## 5. 한계

가장 큰 모델이 350M으로 현재 대규모 LLM보다 작고, 350M 결과는 seed 하나뿐이다. 두 gate 형태 모두 특정 interference 방향에 blind spot이 있었으며 downstream reasoning·retrieval task나 실제 serving 성능은 보고되지 않았다. 현재 v1 preprint다.

## 6. 재현 또는 활용 포인트

- Parameter 수와 training token을 맞춘 네 ablation을 같은 seed에서 비교한다.
- Validation loss와 함께 head별 abstention rate, gate sparsity와 injected-noise response를 기록한다.
- 작은 model은 여러 seed, 큰 model도 가능한 범위에서 반복해 scale trend의 불확실성을 제시한다.
- KV-cache 호환성뿐 아니라 fused-kernel 구현 시 latency를 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

희소하고 잡음이 큰 gene-token attention에서 불필요한 context를 거부하고 feature interference를 줄이는 설계 가설로 쓸 수 있다. 다만 omics에서의 이득은 전혀 검증되지 않았으므로 gene masking, pathway recovery와 patient-level prediction을 각각 ablation해야 한다.

## 8. 관련 키워드

- LLM / Transformer
- Softmax attention
- Value gating
- Abstention
- Noise filtering

## 9. Bibliography

Wang, Richard Zhe. “Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention.” arXiv:2609.22005, version 1, 2026. [https://doi.org/10.48550/arXiv.2609.22005](https://doi.org/10.48550/arXiv.2609.22005). Preprint; not peer reviewed.
