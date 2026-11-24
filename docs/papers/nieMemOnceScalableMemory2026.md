---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# MemOnce: A Scalable Memory Architecture for Large Language Models

## 기본 정보

- Citation key: `nieMemOnceScalableMemory2026`
- Item type: preprint
- Authors: Chang Nie; Chaoyou Fu; Songlin Liu; Yiqing Hu; Caifeng Shan
- Source: arXiv v1, posted 2026-11-20
- Original: [arXiv:2611.27973](https://arxiv.org/abs/2611.27973)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

MemOnce는 최종층 hidden state의 일부만 영구 memory로 저장하고 질의별 sparse retrieval 뒤 각 층의 KV cache를 복원해, 장기 대화의 세부 기억과 메모리·지연 효율을 함께 노린 언어모델 구조다.

## 2. 연구 질문

전체 token·layer의 KV cache를 유지하지 않고도 100만 token 규모의 지속적 상호작용에서 필요한 과거 정보를 다시 불러올 수 있는가?

## 3. 데이터와 방법

Memory encoder-decoder가 최종층 상태를 압축해 저장하고, memory sparse attention이 현재 질의와 관련된 segment를 한 번 선택해 여러 층에서 공유한다. 선택된 표현은 on-demand KV cache로 복원된다. FineWeb-Edu 사전학습, Qwen3.5-4B 적응, WikiText·LAMBADA와 8개 zero-shot task, MemBench·LoCoMo·LongMemEval·PersonaMem, MMLU·GSM8K·GPQA에서 Transformer, linear attention, KV-sharing, native-memory model과 비교했다.

## 4. 핵심 결과

- Qwen3.5-4B의 1M context에서 저장 memory state를 1,313배, prefill latency를 6.9배 줄이고 throughput을 3.5배 높였다고 보고했다.
- 4K–1M token memory benchmark와 일반 능력 평가에서 고정 크기 linear state보다 세부 회상과 효율의 균형이 좋았다.
- 저장 단계와 query-aware routing을 분리해 같은 memory representation을 retrieval·reranking에도 전이했다.

## 5. 한계

Preprint이며 주요 효율 수치는 저자 구현과 선택된 hardware·benchmark에 의존한다. 압축률과 sparse routing budget에 따라 장기 정보가 누락될 수 있고, 1M-context 결과가 다양한 실제 agent workload나 임상 문서 RAG에서 그대로 유지되는지는 독립 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Compression ratio, segment 길이, retrieval budget, KV decoding 비용을 각각 기록하고 동일한 GPU·batch·context에서 full-attention, sliding-window, retrieval-memory baseline과 비교한다. 정확도뿐 아니라 cache 크기, prefill/decode latency, 누락된 근거의 위치별 recall을 함께 본다.

## 7. Transcriptomics·신장이식 연구와의 연결

장기간 누적되는 biopsy, 병리, 약물, 감염 기록을 질의 시점에 선택적으로 복원하는 임상 RAG memory 후보가 될 수 있다. 다만 환자별 longitudinal evidence를 압축할 때 희귀 rejection event가 사라지지 않는지 별도의 recall audit가 필요하다.

## 8. 관련 키워드

- long-context memory
- KV-cache compression
- sparse attention
- continual interaction

## 9. Bibliography

Nie, Chang, et al. “MemOnce: A Scalable Memory Architecture for Large Language Models.” _arXiv_, 2026. [https://arxiv.org/abs/2611.27973](https://arxiv.org/abs/2611.27973).
