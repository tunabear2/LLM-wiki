---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-10'
tags:
- wiki/paper
---

# Scaling an Autoregressive Transformer for Single-Cell Generation

## 기본 정보

- Citation key: `sharipovScalingAutoregressiveTransformer2026`
- Item type: preprint
- Authors: Aleksandr Sharipov; Yusif Mukhtarov; Igor Molybog
- DOI: 10.48550/arXiv.2608.02961
- URL: [Link](https://arxiv.org/abs/2608.02961)
- Source/date: arXiv v1, 2026-08-03

## 1. 한 줄 요약

Quantized VAE tokenizer와 causal Transformer로 single-cell gene-expression vector를 생성하고, model size와 training data에 따른 pretraining loss의 two-exponent scaling law와 compute-optimal frontier를 추정한다.

## 2. 왜 중요한가

Single-cell foundation model의 규모를 키울 때 parameter와 data를 어떤 비율로 배분해야 하는지를 생성 품질과 loss 관점에서 정량화한다. Held-out cell type의 expression distribution을 조건부 생성으로 비교하며, downstream perturbation response prediction으로의 fine-tuning 가능성도 제시한다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection용 모델을 처음부터 크게 pretrain하기보다 공개 atlas와 제한된 biopsy cohort에서 compute-optimal 규모를 먼저 추정해야 한다. 생성 cell이 HLA, IFN, cytotoxicity, endothelial injury program과 donor-level variation을 보존하는지 외부 cohort에서 검증하는 기준으로 활용할 수 있다.

## 4. Bibliography

Sharipov, Aleksandr, Yusif Mukhtarov, and Igor Molybog. "Scaling an Autoregressive Transformer for Single-Cell Generation." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2608.02961](https://doi.org/10.48550/arXiv.2608.02961).
