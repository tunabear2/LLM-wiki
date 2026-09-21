---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-21'
tags:
- wiki/paper
---

# scGPA: an LLM-assisted workflow for directional virtual gene perturbation analysis from single-cell transcriptomes

## 기본 정보

- Citation key: `tangScGPALLMAssistedWorkflow2026`
- Item type: journalArticle
- Authors: Haijun Tang; Hening Li; Qinghao Zhao; Xiang Zhou; Lei Peng; Yangjie Cai; Rongzhen Lin; Yufeng Li; Yiyi Yuan; Wenyu Feng; Yun Liu; Zezheng Liu; Qingchu Li
- DOI: 10.1186/s12864-026-13270-0
- PMID: 42754836
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42754836/)
- Source/date: BMC Genomics, published 2026-08-25; indexed 2026-09-17

## 1. 한 줄 요약

scGPA는 subsampled GRN, signed dose-aware propagation과 LLM 해석을 결합해 다섯 Perturb-seq dataset에서 directional prediction 정확도 23.0%를 보고하며 GEARS 20.7%, scGPT 15.1%와 비교했다.

## 2. 왜 중요한가

Single-cell perturbation 결과를 전체 expression reconstruction보다 방향성 있는 downstream gene, confidence와 evidence summary로 제공한다. qRT-PCR validation을 포함하지만 전체 실험 gene 기준 directional concordance는 37.0%였으므로, headline 성능과 실제 검증 범위를 구분해 해석해야 한다.

## 3. 내 연구에 연결할 점

Rejection-associated target의 knockdown·overexpression 후보를 방향성 있게 우선순위화하는 baseline으로 쓸 수 있다. Donor/cell-type holdout, scGPT와 단순 signed-GRN baseline, effect-size별 calibration 및 renal cell perturbation 실험을 함께 설계해야 한다.

## 4. Bibliography

Tang, Haijun, Hening Li, Qinghao Zhao, Xiang Zhou, Lei Peng, Yangjie Cai, Rongzhen Lin, et al. "scGPA: an LLM-assisted workflow for directional virtual gene perturbation analysis from single-cell transcriptomes." _BMC Genomics_ 27 (2026). [https://doi.org/10.1186/s12864-026-13270-0](https://doi.org/10.1186/s12864-026-13270-0).
