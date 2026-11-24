---
type: paper
status: reference
rag_priority: high
updated: '2026-11-24'
tags:
- wiki/paper
---

# scUNVEIL: Learning scRNA-seq Cell Embeddings Through Measurement Enrichment

## 기본 정보

- Citation key: `honzikScUNVEILLearning2026`
- Item type: preprint
- Authors: T. Honzik; L. Kuhajda; L. Houdova; D. Georgiev
- DOI: 10.64898/2026.11.17.767296
- URL: [Link](https://doi.org/10.64898/2026.11.17.767296)
- Source/date: bioRxiv v1, posted 2026-11-18

## 1. 한 줄 요약

scUNVEIL은 next-UMI prediction으로 저깊이 count에서 더 깊은 sequencing이 드러낼 transcriptome composition을 추정하고 그 hidden state를 cell embedding으로 사용한다.

## 2. 왜 중요한가

약 9,200만 human cell에 label 없이 pretraining했으며 gene-token attention 대신 residual MLP와 count vector를 사용한다. Fine-grained annotation의 linear evaluation에서 강한 zero-shot 성능과 transformer scFM 대비 1,000배가 넘는 inference 속도를 보고했다.

## 3. 내 연구에 연결할 점

저깊이 transplant scRNA-seq의 embedding과 expression enrichment에 유망하다. 그러나 UMI depth·chemistry·ambient RNA 차이를 biology로 복원할 수 있으므로 donor·protocol holdout과 원 count·downsampling control이 필수다.

## 4. Bibliography

Honzik, T., L. Kuhajda, L. Houdova, and D. Georgiev. "scUNVEIL: Learning scRNA-seq Cell Embeddings Through Measurement Enrichment." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.17.767296](https://doi.org/10.64898/2026.11.17.767296).
