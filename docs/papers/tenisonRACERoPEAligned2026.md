---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# RACE: RoPE-Aligned Attention Compression Based on Query-Key Activation Energies

## 기본 정보

- Citation key: `tenisonRACERoPEAligned2026`
- Item type: arXiv preprint
- Authors: Irene Tenison; Abdulrahman Alabdulkareem; Daniel Karl I. Weidele; Nima Dehmamy; Dan Gutfreund
- Source: arXiv v1, submitted 2026-10-20
- Original: [arXiv:2610.28385](https://arxiv.org/abs/2610.28385)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

RACE는 RoPE의 회전 좌표쌍을 query·key activation energy로 선별해 projection weight에 접어 넣음으로써, runtime 복원이나 전용 kernel 없이 KV-cache 폭과 attention 연산을 함께 줄인다.

## 2. 연구 질문

Pretrained RoPE attention을 품질 저하와 복원 overhead를 억제하면서 native low-dimensional attention으로 바꿀 수 있는가?

## 3. 데이터와 방법

Query와 key를 같은 저차원 공간으로 줄이는 문제를 approximate matrix multiplication으로 정식화하고, RoPE와 교환 가능한 coordinate selection은 완전한 rotary pair를 보존해야 함을 보였다. Calibration forward pass의 joint Q/K energy로 pair를 고르고 value에는 calibrated low-rank subspace를 적용한 뒤 projection weight에 folding했다. 세 model family에서 language modeling, 15개 zero-shot task, LongBench와 64K–256K system benchmark를 평가했다.

## 4. 핵심 결과

- Structured pruning보다 정확했고 reconstruction-based compression과 경쟁하면서도 runtime reconstruction을 없앴다.
- KV-cache 50% 보존·256K context에서 원본 대비 inference FLOPs 47.8%, allocated GPU memory 28.1%, TTFT 43.2%를 줄이고 throughput을 1.79배 높였다.
- Token eviction/compaction과 KV quantization을 함께 적용할 수 있었다.

## 5. 한계

50%처럼 공격적인 압축에서는 짧은 KL-distillation recovery가 품질 회복에 중요했다. System 결과는 단일 NVIDIA H100과 평가한 세 model family에 한정되고, 이식 가능한 code repository는 원문에 명시되지 않았다.

## 6. 재현 또는 활용 포인트

Calibration corpus, Q/K pair energy, retained rotary pair와 recovery 유무를 기록한다. 같은 cache 비율뿐 아니라 TTFT, throughput, 실제 allocated memory와 perplexity·long-context score를 함께 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

긴 임상 기록과 biopsy 지식을 함께 읽는 local RAG/LLM의 cache 비용을 낮추는 후보지만, biomedical corpus에서 중요한 희귀 근거가 압축으로 사라지지 않는지 별도 검증해야 한다.

## 8. 관련 키워드

- LLM / Transformer
- KV-cache compression
- RoPE
- efficient inference

## 9. Bibliography

Tenison, Irene, et al. “RACE: RoPE-Aligned Attention Compression Based on Query-Key Activation Energies.” arXiv:2610.28385, 2026. [https://arxiv.org/abs/2610.28385](https://arxiv.org/abs/2610.28385).
