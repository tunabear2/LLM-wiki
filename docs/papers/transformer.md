---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Attention Is All You Need

## 1. 한 줄 요약

RNN이나 CNN 없이 attention만으로 sequence transduction을 수행하는 Transformer architecture를 제안한 논문이다.

## 2. 배경

기존 sequence-to-sequence 모델은 RNN/LSTM/GRU에 의존했기 때문에 긴 sequence 처리와 병렬화에 한계가 있었다. Attention은 이미 encoder-decoder 사이에서 중요하게 쓰였지만, 논문의 핵심은 recurrence 자체를 제거하고 attention을 중심 구조로 만든 것이다.

## 3. 핵심 아이디어

Self-attention으로 입력 token 사이의 관계를 직접 계산한다. Multi-head attention을 통해 서로 다른 representation subspace에서 여러 관계를 병렬로 본다. Positional encoding을 더해 recurrence 없이도 token 순서 정보를 제공한다.

## 4. Method

### Input

Token embedding에 positional encoding을 더한 sequence.

### Model Architecture

Encoder와 decoder는 attention block과 feed-forward network를 반복해서 쌓는다. Encoder는 self-attention을 사용하고, decoder는 masked self-attention과 encoder-decoder attention을 함께 사용한다.

### Training Objective

번역 task에서 target sentence의 다음 token을 예측하는 cross-entropy loss를 사용한다.

### Output

각 step에서 target vocabulary에 대한 probability distribution을 출력한다.

## 5. Figure 정리

### Figure 1

Transformer 전체 구조를 보여준다. 왼쪽은 encoder stack, 오른쪽은 decoder stack이다.

### Attention 수식

```math
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

## 6. 장점

- 병렬화가 쉽다.
- 긴 거리 token 관계를 직접 계산한다.
- 이후 BERT, GPT, single-cell foundation model의 기반이 되었다.

## 7. 한계

- Attention 계산량이 sequence 길이의 제곱에 비례한다.
- 위치 정보는 별도로 넣어야 한다.
- 매우 긴 sequence에서는 memory 부담이 크다.

## 8. 내 연구에 적용할 아이디어

Gene expression profile을 token sequence처럼 다루는 모델을 이해할 때 Transformer의 self-attention과 positional encoding 변형을 먼저 확인한다.

## 9. 관련 자료

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [내 Zotero 노트](vaswaniAttentionAllYou2023.md)
