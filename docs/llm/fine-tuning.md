---
type: concept
status: reference
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/concept
---

# Fine-tuning

## 핵심 요약

Fine-tuning은 이미 pretrained된 모델을 특정 task, domain, dataset에 맞게 추가 학습하는 과정이다. 처음부터 모델을 학습하는 것보다 적은 데이터와 계산량으로 좋은 성능을 얻을 수 있다.

## 왜 중요한가?

일반 LLM은 넓은 지식을 갖지만 특정 연구 문제, 병원 데이터, single-cell dataset의 label 체계에는 최적화되어 있지 않다. Fine-tuning은 모델을 내 데이터 분포와 목표 task에 맞추는 방법이다.

## 대표 방식

- Full fine-tuning: 모든 parameter를 업데이트한다.
- Linear probing: encoder는 고정하고 마지막 classifier만 학습한다.
- PEFT: LoRA, adapter 등 일부 작은 parameter만 학습한다.
- Instruction tuning: 입력 지시문과 원하는 답변 형식에 맞게 학습한다.

## 기본 절차

1. Pretrained model과 tokenizer를 선택한다.
2. Dataset을 task 형식에 맞게 정리한다.
3. Train/validation/test split을 만든다.
4. Loss와 metric을 정한다.
5. 학습 후 validation 성능과 overfitting을 확인한다.

## Hugging Face 예시

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
```

## 내 연구에 적용할 아이디어

- Rejection vs stable 상태를 예측하는 classifier head를 붙인다.
- scRNA-seq cell embedding을 patient-level feature로 aggregate한다.
- 데이터가 적을 때는 full fine-tuning보다 linear probing이나 LoRA를 먼저 시도한다.

## 관련 자료

- [Hugging Face fine-tuning guide](https://huggingface.co/docs/transformers/training)
