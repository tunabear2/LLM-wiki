---
type: concept
status: reference
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/concept
---

# Transformer

## 핵심 요약

Transformer는 sequence를 순차적으로 읽는 RNN 대신, self-attention으로 모든 token 사이의 관계를 한 번에 계산하는 neural network architecture이다. LLM, BERT, GPT, 많은 single-cell foundation model의 기본 뼈대가 된다.

## 왜 중요한가?

Transformer는 긴 문맥에서 어떤 token이 어떤 token을 참고해야 하는지 학습할 수 있고, 병렬 연산이 쉬워 대규모 학습에 적합하다. 이 특성 때문에 NLP뿐 아니라 protein sequence, gene expression, multi-omics 데이터에도 확장된다.

## 구조

Transformer layer는 보통 다음 블록으로 구성된다.

1. Multi-head self-attention
2. Residual connection
3. Layer normalization
4. Feed-forward network
5. Residual connection
6. Layer normalization

## Encoder와 Decoder

- Encoder: 입력 전체를 양방향으로 읽어 representation을 만든다. BERT 계열에 많이 쓰인다.
- Decoder: 이전 token만 보고 다음 token을 생성한다. GPT 계열에 많이 쓰인다.
- Encoder-decoder: 입력 sequence를 encoding한 뒤 output sequence를 생성한다. 번역, 요약에 쓰인다.

## 핵심 수식

```math
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

## 내 연구에 적용할 아이디어

Single-cell expression matrix를 sequence처럼 다루면 gene token 사이의 관계를 attention으로 학습할 수 있다. 다만 gene expression은 자연어와 달리 순서가 고정된 문장이 아니므로, tokenization과 positional encoding을 어떻게 설계하는지가 중요하다.

## 관련 자료

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
