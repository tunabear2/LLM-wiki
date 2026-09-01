---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Attention Is All You Need

## 기본 정보

- Citation key: `vaswaniAttentionAllYou2023`
- Item type: preprint
- Authors: Ashish Vaswani; Noam Shazeer; Niki Parmar; Jakob Uszkoreit; Llion Jones; Aidan N. Gomez; Lukasz Kaiser; Illia Polosukhin
- DOI: 10.48550/arXiv.1706.03762
- URL: [Link](http://arxiv.org/abs/1706.03762)

## Abstract


The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.


## 1. 한 줄 요약

%% begin one-line-summary %%
RNN/CNN 기반 sequence-to-sequence 모델의 순차 계산 병목을 없애기 위해, attention만으로 encoder-decoder 구조를 구성한 Transformer를 제안한 논문이다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
이전의 기계번역 모델은 주로 RNN, LSTM, GRU 또는 CNN 기반 encoder-decoder 구조를 사용했다. RNN 계열은 token을 순서대로 처리해야 하므로 학습 병렬화가 어렵고, 긴 sequence에서 멀리 떨어진 token 사이의 의존성을 학습하기 어렵다. CNN 계열은 RNN보다 병렬화가 쉽지만, 먼 위치 사이의 정보를 연결하려면 여러 layer를 쌓아야 한다. 이 논문은 이러한 순차 처리와 긴 path length 문제를 self-attention으로 해결하려고 했다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
Transformer는 recurrence와 convolution을 제거하고 self-attention으로 모든 token 사이의 관계를 직접 계산한다. Multi-head attention은 여러 representation subspace에서 서로 다른 관계를 동시에 보게 해준다. Positional encoding을 token embedding에 더해 순서 정보를 제공함으로써, 순차 구조 없이도 sequence 정보를 처리한다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 source sentence와 target sentence를 subword token으로 변환한 sequence이다. WMT 2014 English-German에서는 약 4.5M sentence pair를 사용했고, shared source-target vocabulary 약 37,000개의 byte-pair encoding token을 사용했다. English-French에서는 약 36M sentence pair와 32,000개 word-piece vocabulary를 사용했다.
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
Transformer는 encoder stack과 decoder stack으로 구성된다.

- Encoder: 동일한 layer를 6개 쌓는다. 각 layer는 multi-head self-attention sub-layer와 position-wise feed-forward network sub-layer를 가진다.
- Decoder: 동일한 layer를 6개 쌓는다. 각 layer는 masked multi-head self-attention, encoder-decoder attention, position-wise feed-forward network를 가진다.
- Residual connection과 layer normalization을 각 sub-layer 주변에 적용한다.
- Base model은 `d_model = 512`, attention head 8개, feed-forward hidden dimension `d_ff = 2048`을 사용한다.
- Big model은 `d_model = 1024`, attention head 16개, `d_ff = 4096`을 사용한다.

핵심 attention 수식:

```math
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

Multi-head attention은 Q, K, V를 여러 head로 projection한 뒤 각 head에서 attention을 계산하고, 그 결과를 concat해서 다시 projection한다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
목표는 machine translation에서 이전 target token들과 source sentence가 주어졌을 때 다음 target token을 예측하는 것이다. Decoder는 autoregressive하게 target token을 생성하며, training에서는 cross-entropy 기반 next-token prediction objective를 사용한다. Optimizer는 Adam을 사용했고, learning rate는 warmup 후 inverse square root schedule로 감소시켰다. Regularization으로 residual dropout과 label smoothing을 사용했다.
%% end method-objective %%

### Output

%% begin method-output %%
각 decoding step에서 target vocabulary 전체에 대한 probability distribution을 출력하고, 그중 다음 token을 선택해 번역 문장을 생성한다. 논문에서는 beam search와 length penalty를 사용해 최종 번역 결과를 만들었다.
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
Transformer의 전체 encoder-decoder architecture를 보여준다. 왼쪽 encoder는 self-attention과 feed-forward network를 반복하고, 오른쪽 decoder는 masked self-attention, encoder-decoder attention, feed-forward network를 반복한다. 이 그림에서 가장 중요한 포인트는 RNN recurrence가 전혀 없고 attention block이 중심 연산이라는 점이다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
왼쪽은 scaled dot-product attention을 보여준다. Q와 K의 dot product를 `sqrt(d_k)`로 나누고 softmax를 적용한 뒤 V의 weighted sum을 계산한다. 오른쪽은 multi-head attention을 보여준다. 여러 attention head가 병렬로 서로 다른 관계를 학습하고, 결과를 concat한 뒤 최종 projection한다.
%% end figure-2 %%

## 6. 장점

%% begin strengths %%
- RNN의 순차 계산 병목을 제거해 학습 병렬화가 훨씬 쉽다.
- Self-attention은 sequence 내 임의의 두 token을 짧은 path로 연결하므로 long-range dependency 학습에 유리하다.
- Multi-head attention을 통해 서로 다른 유형의 syntactic/semantic 관계를 동시에 포착할 수 있다.
- WMT 2014 English-German에서 Transformer big이 BLEU 28.4, English-French에서 BLEU 41.8을 달성했다.
- 이후 BERT, GPT, T5, Vision Transformer, single-cell foundation model 등 많은 모델의 기본 구조가 되었다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- Self-attention의 계산량과 memory 사용량은 sequence length에 대해 `O(n^2)`로 증가한다.
- 순서 정보가 모델 구조에 내재되어 있지 않아 positional encoding이 필요하다.
- 매우 긴 sequence, image/audio/video 같은 큰 입력에는 local attention, sparse attention 등 추가 설계가 필요하다.
- Attention weight가 해석 가능성을 줄 수는 있지만, 그것이 곧 causal explanation을 의미하지는 않는다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
- Single-cell foundation model에서 gene을 token으로 보고 self-attention으로 gene-gene relationship을 학습하는 구조를 이해하는 기본 논문으로 사용한다.
- Kidney transplant rejection scRNA-seq에서 cell state를 Transformer embedding으로 표현하고, rejection/stable label을 예측하는 downstream classifier를 붙일 수 있다.
- Geneformer나 scGPT의 architecture를 읽을 때 `Q, K, V`, multi-head attention, positional/value encoding이 expression data에서 어떻게 변형되는지 비교한다.
- Patient-level prediction에서는 cell-level token/embedding을 어떻게 aggregate할지 별도로 설계해야 한다.
- Attention map을 marker gene 후보 탐색에 참고할 수 있지만, causal gene regulation으로 직접 해석하지 않도록 주의한다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- Transformer
- Self-attention
- Multi-head attention
- Positional encoding
- Sequence-to-sequence
- Machine translation
- Foundation model
- Single-cell foundation model
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%


아직 가져온 PDF highlight가 없습니다. Zotero PDF reader에서 highlight를 만든 뒤 다시 import한다.

%% end annotations %%

## 11. Bibliography

Vaswani, Ashish, Noam Shazeer, Niki Parmar, 기타. “Attention Is All You Need”. arXiv:1706.03762. Preprint, arXiv, 2023년 8월 2일. [https://doi.org/10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762).


%% Import Date: 2026-05-18T12:36:54.283+09:00 %%
