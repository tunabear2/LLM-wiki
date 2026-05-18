# BERT

## 1. 한 줄 요약

BERT는 Transformer encoder를 양방향으로 pretraining해서 문맥을 깊게 이해하는 representation을 학습한 모델이다.

## 2. 배경

GPT 계열의 left-to-right language model은 오른쪽 문맥을 직접 볼 수 없다. 반면 많은 자연어 이해 task는 문장의 양쪽 문맥이 모두 중요하다. BERT는 Masked Language Modeling으로 양방향 문맥 학습을 가능하게 했다.

## 3. 핵심 아이디어

입력 token 일부를 `[MASK]`로 가리고 원래 token을 맞히는 MLM을 사용한다. 문장 관계를 학습하기 위해 NSP(Next Sentence Prediction)를 함께 사용했다. Fine-tuning 시에는 task별 head만 붙이고 전체 모델을 end-to-end로 학습한다.

## 4. Method

### Input

`[CLS] sentence A [SEP] sentence B [SEP]` 형식의 token sequence.

### Model Architecture

Transformer encoder stack. 모든 token이 서로 양방향으로 attention한다.

### Training Objective

- Masked Language Modeling
- Next Sentence Prediction

### Output

- `[CLS]` embedding: classification task
- Token embedding: token classification, QA span prediction

## 5. 장점

- 문맥 양쪽을 모두 반영한다.
- 다양한 NLP task에 같은 architecture로 fine-tuning할 수 있다.
- Encoder representation 학습의 표준이 되었다.

## 6. 한계

- `[MASK]` token은 pretraining과 downstream 사이의 mismatch를 만든다.
- 생성형 task에는 decoder-only 모델보다 직접적이지 않다.
- NSP의 필요성은 이후 연구에서 재검토되었다.

## 7. 내 연구에 적용할 아이디어

Single-cell model에서 masked gene prediction을 쓰는 접근은 BERT의 MLM과 구조적으로 닮아 있다. 특정 gene을 mask하고 cell context에서 발현/존재를 예측하는 방식으로 gene-gene relationship을 학습할 수 있다.

## 8. 관련 자료

- [BERT paper](https://arxiv.org/abs/1810.04805)
