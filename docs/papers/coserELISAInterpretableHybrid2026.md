---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-24'
tags:
- wiki/paper
---

# ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics

## 기본 정보

- Citation key: `coserELISAInterpretableHybrid2026`
- Item type: preprint
- Authors: Omar Coser
- DOI: 10.48550/arXiv.2603.11872
- URL: [Link](https://arxiv.org/abs/2603.11872)
- Source/date: arXiv v3, revised 2026-07-31 (v1 2026-03-12)

## 1. 한 줄 요약

ELISA는 frozen scGPT expression embedding, BioBERT semantic retrieval, LLM 해석을 결합해 gene signature와 자연어 질의를 single-cell cell type·pathway·interaction 가설로 연결하는 agent framework다.

## 2. 왜 중요한가

질의를 gene marker scoring, semantic matching, reciprocal-rank fusion으로 routing하고, 원래 count matrix 없이 embedding 위에서 pathway activity, ligand–receptor, condition comparison, cell proportion 분석을 수행한다. 여섯 scRNA-seq dataset의 retrieval과 published-finding replication으로 평가해 single-cell foundation model representation을 자연어 기반 탐색 도구에 연결하는 설계를 보여준다. 다만 scGPT embedding과 LLM 해석이 만드는 가설은 expression-level 통계 검정이나 인과 검증을 대체하지 않는다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection에서 HLA, IFN, cytotoxicity, endothelial injury signature와 자연어 질의를 연결해 후보 cell state·pathway·ligand–receptor axis를 탐색하는 interface로 응용할 수 있다. 결과는 donor-level differential analysis, 원 count matrix 재검산, 외부 cohort와 spatial/perturbation evidence로 검증하고 retrieval corpus 및 prompt provenance를 기록해야 한다.

## 4. Bibliography

Coser, Omar. "ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2603.11872](https://doi.org/10.48550/arXiv.2603.11872).
