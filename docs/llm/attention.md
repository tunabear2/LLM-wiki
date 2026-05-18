# Attention Mechanism

## 핵심 요약

Attention은 입력 token들 사이의 관계를 계산해서, 어떤 token이 다른 token을 얼마나 참고해야 하는지 학습하는 방법이다.

## 직관적 설명

문장을 읽을 때 모든 단어를 똑같이 보는 것이 아니라, 현재 단어를 이해하는 데 중요한 단어에 더 집중한다. Transformer에서는 이 집중 정도를 attention score로 계산한다.

## Q, K, V

각 token embedding은 세 가지 벡터로 변환된다.

- Query: 내가 찾고 싶은 정보
- Key: 내가 가진 정보의 주소
- Value: 실제 전달할 정보

## Scaled Dot-Product Attention

```math
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```
