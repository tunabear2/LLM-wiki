---
type: code-note
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/code-note
---

# Hugging Face

## 핵심 요약

Hugging Face는 pretrained model, tokenizer, dataset, training utility를 제공하는 생태계이다. LLM 실험을 빠르게 시작하고, 공개 모델을 fine-tuning하거나 inference에 사용하는 데 편리하다.

## 주요 라이브러리

- `transformers`: model, tokenizer, Trainer
- `datasets`: dataset loading과 preprocessing
- `tokenizers`: 빠른 tokenizer 구현
- `accelerate`: multi-GPU/distributed training 보조
- `peft`: LoRA 등 parameter-efficient fine-tuning

## Tokenizer와 Model 로드

```python
from transformers import AutoTokenizer, AutoModel

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

inputs = tokenizer("hello transformer", return_tensors="pt")
outputs = model(**inputs)
```

## Fine-tuning 흐름

1. Dataset 준비
2. Tokenizer 적용
3. Model class 선택
4. `TrainingArguments` 설정
5. `Trainer`로 학습
6. Evaluation과 model 저장

## 주의점

- Model과 tokenizer는 같은 checkpoint에서 불러온다.
- Sequence 길이 truncation/padding 전략을 명확히 정한다.
- Domain-specific data에서는 data leakage와 label imbalance를 확인한다.

## 관련 자료

- [Hugging Face Transformers training guide](https://huggingface.co/docs/transformers/training)
- [AutoTokenizer docs](https://huggingface.co/docs/transformers/v4.42.0/model_doc/auto)
