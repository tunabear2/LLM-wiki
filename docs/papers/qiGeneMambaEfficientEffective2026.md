---
type: paper
status: reference
rag_priority: high
updated: '2026-10-31'
tags:
- wiki/paper
---

# GeneMamba: Efficient and Effective Foundation Model on Single Cell Data

## 기본 정보

- Citation key: `qiGeneMambaEfficientEffective2026`
- Item type: conference paper
- Authors: C. Qi; H. Fang; S. Jiang; X. Song; T. Hu; Z. Wei
- DOI: 10.1109/IJCNN69854.2026.11728763
- PMID: 42903697
- URL: [Link](https://doi.org/10.1109/IJCNN69854.2026.11728763)
- Source/date: PubMed / IJCNN 2026, newly indexed 2026-10-22

## 1. 한 줄 요약

GeneMamba는 bidirectional state-space block과 pathway-aware contrastive objective로 약 3,000만 curated cell을 pretrain해 genome-scale gene sequence를 linear complexity로 처리한다.

## 2. 왜 중요한가

Transformer self-attention의 quadratic cost와 unidirectional SSM의 ordering bias를 함께 줄이면서 integration, annotation과 gene-rank reconstruction으로 transfer를 평가한다. 대규모 scFM에서 효율성과 biological prior를 함께 설계한 모델이다.

## 3. 내 연구에 연결할 점

대규모 kidney atlas에서 긴 gene vocabulary를 처리할 효율적 backbone 후보지만, pathway prior의 실제 이득을 ablation하고 donor·center 외부 cohort에서 scGPT, Geneformer와 raw-count baseline을 비교해야 한다.

## 4. Bibliography

Qi, C., H. Fang, S. Jiang, X. Song, T. Hu, and Z. Wei. "GeneMamba: Efficient and Effective Foundation Model on Single Cell Data." _Proceedings of the International Joint Conference on Neural Networks_, 2026. [https://doi.org/10.1109/IJCNN69854.2026.11728763](https://doi.org/10.1109/IJCNN69854.2026.11728763).
