---
type: concept
status: reference
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/concept
---

# LLM Overview

## 핵심 개념

Large Language Model(LLM)은 대규모 텍스트로 학습한 언어 모델이다. 대부분의 현대 LLM은 Transformer 구조를 기반으로 하며, 주어진 문맥에서 다음 token을 예측하거나 빈 token을 복원하는 방식으로 언어의 통계적 패턴과 지식 표현을 학습한다.

## 왜 중요한가?

LLM은 단순 문장 생성 모델을 넘어, 요약, 질의응답, 코드 생성, 문서 검색, 데이터 해석, 생물학 문헌 분석 같은 다양한 작업의 공통 기반 모델로 쓰인다. Bioinformatics에서는 논문 검색, 유전자 기능 설명, single-cell annotation 보조, clinical note 해석 같은 작업에 연결될 수 있다.

## 기본 구성

1. Text를 tokenizer로 token id로 변환한다.
2. Token id를 embedding vector로 바꾼다.
3. Transformer layer가 token 간 관계를 attention으로 계산한다.
4. 마지막 hidden state로 다음 token 또는 task label을 예측한다.

## 핵심 용어

- Parameter: 모델이 학습하는 weight.
- Context window: 한 번에 입력할 수 있는 token 길이.
- Pretraining: 대규모 일반 데이터로 기본 언어 능력을 학습하는 단계.
- Fine-tuning: 특정 task나 domain에 맞게 추가 학습하는 단계.
- Inference: 학습된 모델로 답변을 생성하는 단계.

## 내 연구에 적용할 아이디어

- 논문 abstract와 figure legend를 구조화해서 빠르게 요약한다.
- Kidney transplant rejection 관련 gene signature를 설명하는 보조 도구로 사용한다.
- RAG를 붙여서 내 논문 PDF와 실험 노트 기반으로 답변하게 만든다.
- Single-cell foundation model의 embedding을 임상 phenotype prediction에 연결한다.

## 관련 자료

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [BERT](https://arxiv.org/abs/1810.04805)
- [GPT-1 paper](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
