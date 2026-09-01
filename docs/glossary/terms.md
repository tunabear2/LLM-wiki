---
type: glossary
status: reference
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/glossary
---

# Glossary

## LLM

Large Language Model. 대규모 텍스트로 학습된 언어 모델.

## Token

모델이 처리하는 입력 단위. 단어, subword, byte, gene 등이 될 수 있다.

## Embedding

Token, gene, cell 같은 discrete object를 dense vector로 표현한 것.

## Attention

각 token이 다른 token을 얼마나 참고할지 계산하는 mechanism.

## Query, Key, Value

Attention 계산에 쓰이는 세 벡터. Query는 찾는 정보, Key는 비교 대상의 주소, Value는 전달되는 내용으로 이해할 수 있다.

## Transformer

Self-attention과 feed-forward network를 반복해 sequence representation을 학습하는 architecture.

## Encoder

입력 sequence 전체를 읽어 representation을 만드는 구조.

## Decoder

이전 token을 보고 다음 token을 생성하는 구조.

## Pretraining

대규모 일반 데이터로 모델의 기본 representation을 학습하는 단계.

## Fine-tuning

Pretrained model을 특정 task나 domain에 맞게 추가 학습하는 단계.

## RAG

Retrieval-Augmented Generation. 외부 문서를 검색해 context로 넣고 답변을 생성하는 방식.

## scRNA-seq

Single-cell RNA sequencing. 개별 cell 수준에서 gene expression을 측정하는 기술.

## AnnData

Single-cell 분석에서 자주 쓰이는 Python 데이터 구조. `X`, `obs`, `var`, `obsm` 등을 포함한다.

## HVG

Highly Variable Gene. cell 간 변동성이 커서 downstream 분석에 중요한 gene subset.

## Batch Effect

생물학적 차이가 아니라 실험 조건, 날짜, 장비, protocol 차이에서 생기는 변동.

## Cell Type Annotation

Cluster나 cell에 biological cell type label을 붙이는 과정.

## Foundation Model

대규모 데이터로 pretraining한 뒤 여러 downstream task로 transfer할 수 있는 모델.

## Perturbation Prediction

Gene knockout, drug treatment, disease condition 같은 perturbation이 cell state에 미치는 변화를 예측하는 task.
