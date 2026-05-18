# Single-cell Foundation Models

## 1. 한 줄 요약

Single-cell foundation model은 대규모 single-cell omics data로 pretraining한 모델을 cell type annotation, perturbation prediction, gene network analysis, disease modeling 등에 transfer하는 접근이다.

## 2. 배경

scRNA-seq 데이터는 빠르게 축적되고 있지만 dataset마다 batch, tissue, protocol, label 체계가 다르다. Foundation model은 많은 cell과 gene expression pattern을 미리 학습해 작은 downstream dataset에서도 더 나은 representation을 제공하려고 한다.

## 3. 핵심 아이디어

Cell을 하나의 문서처럼, gene을 token처럼 보고 Transformer류 모델을 적용한다. 모델은 masked gene prediction, generative reconstruction, contrastive learning 등으로 gene-gene, cell-cell, tissue context를 학습한다.

## 4. 대표 모델

| Model | 핵심 아이디어 | 활용 |
| --- | --- | --- |
| Geneformer | rank-based gene token sequence와 masked learning | network biology, perturbation, disease modeling |
| scGPT | generative pretrained transformer for single-cell multi-omics | annotation, batch correction, perturbation, multi-omics |
| scBERT/scFoundation 계열 | gene expression representation pretraining | cell annotation, transfer learning |

## 5. 주의점

- Gene vocabulary와 input preprocessing이 모델마다 다르다.
- Pretraining data와 내 dataset의 tissue/domain 차이가 성능에 영향을 준다.
- Attention이 곧 causal gene regulation이라는 뜻은 아니다.
- Downstream task에서는 baseline model과 external validation이 필요하다.

## 6. 내 연구에 적용할 아이디어

- Kidney transplant rejection dataset에서 patient/cell embedding을 추출한다.
- Rejection-related immune cell subtype annotation을 보조한다.
- Gene perturbation 또는 marker gene prioritization을 후보 생성 도구로 사용한다.
- 모델 embedding과 clinical covariate를 결합해 rejection prediction을 시도한다.

## 7. 관련 자료

- [Geneformer Nature paper](https://www.nature.com/articles/s41586-023-06139-9)
- [scGPT Nature Methods paper](https://www.nature.com/articles/s41592-024-02201-0)
