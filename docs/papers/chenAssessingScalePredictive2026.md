---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-03'
tags:
- wiki/paper
---

# Assessing scale and predictive diversity in models for single-cell transcriptomics based on Geneformer

## 기본 정보

- Citation key: `chenAssessingScalePredictive2026`
- Item type: journalArticle
- Authors: Junfan Chen; Fabian Schmidt; Ricardo Henao
- DOI: 10.1371/journal.pcbi.1013701
- PMID: 42531328
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42531328/)
- Source/date: PubMed / PLOS Computational Biology, indexed 2026-07-30

## 1. 한 줄 요약

GFCAB는 Geneformer 계열의 rank-ordered gene modeling에 누적 할당과 유사도 정규화를 넣어 반복 예측을 줄이고 희귀·질병 관련 유전자 회수와 cross-dataset 일반화를 개선한다.

## 2. 왜 중요한가

대규모 pretraining data가 항상 더 좋은 single-cell representation을 만들지는 않는다는 결과를 제시한다. 더 작은 corpus로 학습한 모델도 큰 모델과 비슷하거나 더 잘 일반화했으며, 데이터 규모보다 입력 구조에 맞는 objective와 예측 다양성이 중요할 수 있음을 보여준다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection scRNA-seq에서 Geneformer를 사용할 때 atlas 규모만 비교하지 말고 donor·center를 분리한 cross-dataset 평가를 해야 한다. HLA, IFN, endothelial injury처럼 빈도는 낮지만 임상적으로 중요한 gene을 얼마나 보존하는지와 PCA/HVG baseline 대비 이득을 함께 측정하는 근거가 된다.

## 4. Bibliography

Chen, Junfan, Fabian Schmidt, and Ricardo Henao. "Assessing scale and predictive diversity in models for single-cell transcriptomics based on Geneformer." _PLOS Computational Biology_, 2026. [https://doi.org/10.1371/journal.pcbi.1013701](https://doi.org/10.1371/journal.pcbi.1013701).
