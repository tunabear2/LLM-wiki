---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# GPT

## 1. 한 줄 요약

GPT 계열은 Transformer decoder를 사용해 이전 token들로 다음 token을 예측하는 generative pretrained model이다.

## 2. 배경

기존 NLP 시스템은 task마다 별도 모델과 label이 필요한 경우가 많았다. GPT는 대규모 unlabeled text로 language modeling을 먼저 수행하고, downstream task에 맞게 fine-tuning하거나 prompting하는 방향을 보여주었다.

## 3. 핵심 아이디어

문장을 왼쪽에서 오른쪽으로 읽으며 다음 token을 예측한다. Decoder-only Transformer의 masked self-attention은 미래 token을 보지 못하게 막는다. 충분히 큰 모델과 데이터는 다양한 task를 언어 생성 문제로 흡수할 수 있다.

## 4. Method

### Input

이전 token sequence.

### Model Architecture

Transformer decoder stack. Masked self-attention을 사용한다.

### Training Objective

```math
max \sum_t log P(x_t | x_{<t})
```

### Output

다음 token probability distribution.

## 5. 장점

- 생성형 task에 자연스럽다.
- Prompting, instruction following, few-shot learning으로 확장되기 쉽다.
- RAG와 결합하면 외부 지식 기반 답변에 활용할 수 있다.

## 6. 한계

- 양방향 encoding이 필요한 classification task에서는 encoder 모델이 더 효율적일 수 있다.
- 모델 parameter에 저장된 지식은 업데이트가 어렵다.
- 근거 없는 답변을 생성할 수 있어 retrieval, citation, validation이 중요하다.

## 7. 내 연구에 적용할 아이디어

연구 노트, 논문 PDF, 분석 코드 설명을 RAG로 연결하면 GPT 계열 모델을 개인 연구 assistant처럼 쓸 수 있다. 단, 임상/생물학 해석에서는 반드시 출처와 원 데이터 확인이 필요하다.

## 8. 관련 자료

- [GPT-1 paper](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- [GPT-2 blog and paper](https://openai.com/index/better-language-models/)
