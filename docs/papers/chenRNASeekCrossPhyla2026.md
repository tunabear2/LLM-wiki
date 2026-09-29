---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# RNASeek: A Cross-Phyla Generative Foundation Model for Multipurpose RNA Modeling and Reinforcement Learning-Based Design

## 기본 정보

- Citation key: `chenRNASeekCrossPhyla2026`
- Item type: bioRxiv preprint
- Authors: Shiyuan Chen; Neil R. Fernandes; Wei Vivian Li; Lili Wang; Zhenyu Jia; Joy S. Xiang
- DOI: 10.64898/2026.09.24.754173
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.24.754173v1); [DOI](https://doi.org/10.64898/2026.09.24.754173)
- Source/date: bioRxiv v1, posted 2026-09-28; not peer reviewed
- 주 카테고리: Bio AI
- 교차 카테고리: LLM / Transformer

## 1. 한 줄 요약

RNASeek는 cross-phyla transcript sequence와 자연어를 학습한 1.6B autoregressive RNA foundation model에서 기능 예측과 GRPO 기반 ribozyme·3′ UTR 설계를 하나의 backbone으로 연결한다.

## 2. 연구 질문

다양한 종의 RNA sequence, 구조 표기와 자연어 task instruction을 함께 사전학습하면, 같은 generative backbone으로 RNA 기능을 예측하고 원하는 기능과 sequence constraint를 만족하는 새로운 RNA를 설계할 수 있는가?

## 3. 데이터와 방법

DeepSeek 1.2B/Qwen2.5 계열의 28-layer decoder-only architecture를 약 1.6B parameter로 구성했다. Tokenizer는 nucleotide, RNAfold dot-bracket 구조, UTR·intron markup과 약 12,000개 자연어 token을 함께 처리한다. 100종이 넘는 동물·식물·균류·바이러스의 약 1.5×10^11 mRNA nucleotide와 약 20억 PubMed abstract token을 32,768-token context로 사전학습했다. 이후 ribozyme self-cleavage와 viral 3′ UTR stability dataset에 regression head를 fine-tune하고, 그 predictor를 reward model로 사용해 GRPO로 sequence를 생성했다. Ribozyme은 51,804/5,756 train/validation sequence, stability task는 similarity filtering 후 18,815/2,935 sequence를 사용했으며, 생성 3′ UTR 네 개를 reporter assay로 검증했다.

## 4. 핵심 결과

Ribozyme activity prediction의 validation Pearson correlation은 0.628로 비교한 19개 foundation model 중 상위권이었지만 RiNALMo 계열보다는 낮았다. Viral 3′ UTR stability는 Spearman correlation 0.342로 UTR-BERT-4mer와 같고 RiNALMo-micro 0.348 및 UTR-BERT-6mer 0.358보다 낮았다. 네 RNASeek 3′ UTR 모두 negative control보다 약 2.8–7.5배 높은 reporter activity를 보였고, RNASeek527은 negative control과 시험한 GEMORNA sequence 및 training-library 상위 후보보다 유의하게 높았다. 생성 ribozyme은 시험한 조건에서 wild-type 수준의 activity를 보였다.

## 5. 한계

아직 peer review 전이며 3′ UTR wet-lab 검증 후보가 네 개로 작다. Ribozyme 학습 자료는 고정 backbone의 두 loop만 무작위화한 library라 construction·cloning bias가 남을 수 있다. Viral 3′ UTR은 하나의 luciferase reporter context에서만 검증됐고, 모델 입력에는 cell type이나 transcriptomic state가 없다. 학습된 reward model의 오차와 편향이 GRPO 설계 품질의 상한이 된다.

## 6. 재현 또는 활용 포인트

- 학습·평가·생성 코드와 model weight: [JoyXiangLab/rnaseek-full](https://huggingface.co/JoyXiangLab/rnaseek-full)
- Pretraining은 8대 NVIDIA A100 80GB와 DeepSpeed ZeRO-3, FSDP, FlashAttention-2를 사용했다.
- Sequence similarity를 통제한 split, 단순 LSTM 및 RNA/DNA foundation model baseline, shuffled sequence를 함께 비교한다.
- 생성 결과는 reward score에 그치지 않고 독립적인 reporter 또는 cleavage assay로 검증해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

RNASeek는 expression matrix가 아니라 RNA sequence와 구조를 모델링하므로 신장이식 예후 예측에 바로 적용되는 모델은 아니다. 다만 rejection-associated transcript의 UTR, splicing과 RNA stability 가설을 만들거나 regulatory RNA 후보를 설계하는 후속 연구에 활용할 수 있으며, 이 경우 신장·면역 cell state와 면역억제 환경을 반영한 별도 reward model과 실험 검증이 필요하다.

## 8. 관련 키워드

- Bio AI
- RNA foundation model
- Autoregressive Transformer
- Cross-phyla pretraining
- RNA sequence design
- Reinforcement learning
- GRPO

## 9. Bibliography

Chen, Shiyuan, Neil R. Fernandes, Wei Vivian Li, Lili Wang, Zhenyu Jia, and Joy S. Xiang. “RNASeek: A Cross-Phyla Generative Foundation Model for Multipurpose RNA Modeling and Reinforcement Learning-Based Design.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.24.754173](https://doi.org/10.64898/2026.09.24.754173). Preprint; not peer reviewed.
