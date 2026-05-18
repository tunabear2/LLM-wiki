# Geneformer

## 핵심 요약

Geneformer는 대규모 single-cell transcriptome corpus로 pretraining한 attention 기반 모델이다. Gene expression을 rank-based sequence로 변환하고, masked learning을 통해 gene network와 cellular context를 학습한다.

## 왜 중요한가?

Gene network 분석은 보통 많은 데이터가 필요하지만, 희귀 질환이나 특정 조직에서는 데이터가 제한적이다. Geneformer는 pretraining된 지식을 downstream task에 transfer해 제한된 데이터에서도 network biology prediction을 돕는 것을 목표로 한다.

## 입력 구조

- 각 cell에서 gene expression rank를 만든다.
- 많이 발현되는 gene이 sequence 앞쪽에 배치된다.
- Transformer가 gene token 사이의 context를 학습한다.

## 활용 task

- Disease state classification
- Gene dosage sensitivity prediction
- In silico gene deletion
- Candidate therapeutic target prioritization
- Cell state embedding analysis

## 주의점

- Rank-based input이므로 raw count 자체를 그대로 넣는 모델이 아니다.
- Gene vocabulary와 Ensembl ID 매핑을 정확히 맞춰야 한다.
- Attention weight를 causal network로 바로 해석하면 위험하다.

## 내 연구에 적용할 아이디어

Kidney transplant rejection에서 immune activation state를 Geneformer embedding으로 표현하고, rejection-associated gene perturbation 후보를 in silico로 탐색한다.

## 관련 자료

- [Transfer learning enables predictions in network biology](https://www.nature.com/articles/s41586-023-06139-9)
