# Tokenizer

## 핵심 요약

Tokenizer는 원본 입력을 모델이 처리할 수 있는 token id sequence로 바꾸는 단계이다. LLM에서는 단어, subword, byte 단위 tokenization이 쓰이고, single-cell 모델에서는 gene이나 expression bin이 token 역할을 할 수 있다.

## 왜 중요한가?

모델은 문자열이나 gene symbol 자체를 이해하지 않고 정수 id와 embedding을 처리한다. Tokenizer가 입력을 어떻게 쪼개는지에 따라 vocabulary 크기, OOV 문제, sequence 길이, 희귀 단어/희귀 gene 처리 방식이 달라진다.

## 대표 방식

- Word-level: 단어 단위. 직관적이지만 vocabulary가 커지고 희귀 단어에 약하다.
- Character-level: 문자 단위. OOV는 줄지만 sequence가 길어진다.
- BPE(Byte Pair Encoding): 자주 등장하는 문자 조합을 반복적으로 합친다.
- WordPiece: BERT 계열에서 널리 쓰인 subword 방식.
- SentencePiece: 공백 처리까지 포함하는 언어 독립적 tokenization 방식.

## LLM 예시

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
encoded = tokenizer("Attention is all you need.", return_tensors="pt")

print(encoded["input_ids"])
print(tokenizer.convert_ids_to_tokens(encoded["input_ids"][0]))
```

## Bio AI에서의 대응

- Gene token: 각 gene을 하나의 token으로 본다.
- Expression value: count, normalized expression, rank, bin 등으로 표현한다.
- Cell sequence: 한 cell을 gene token sequence로 보고 model input으로 만든다.

## 체크 포인트

- Tokenizer vocabulary와 모델 weight는 함께 맞아야 한다.
- Special token(`[CLS]`, `[SEP]`, `[MASK]`, `<bos>`, `<eos>`)의 역할을 확인해야 한다.
- Bio model에서는 gene symbol mapping, duplicated gene, missing gene 처리가 중요하다.

## 관련 자료

- [Hugging Face Tokenizers](https://huggingface.co/docs/transformers/main/fast_tokenizers)
