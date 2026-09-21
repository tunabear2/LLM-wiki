---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-21'
tags:
- wiki/paper
---

# scE2TM improves single-cell embedding interpretability and reveals cellular perturbation signatures

## 기본 정보

- Citation key: `chenScE2TMImprovesSingleCell2026`
- Item type: journalArticle
- Authors: Hegang Chen; Yuyin Lu; Yifan Zhao; Zhiming Dai; Fu Lee Wang; Qing Li; Yanghui Rao; Yue Li
- DOI: 10.1038/s41467-026-76825-5
- PMID: 42744811
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42744811/)
- Source/date: Nature Communications, published 2026-08-17; indexed 2026-09-15

## 1. 한 줄 요약

scE2TM은 scGPT cell embedding을 cross-view distillation으로 topic model에 전달하고 embedding-clustering regularization으로 topic collapse를 줄여, 20개 dataset에서 clustering과 pathway-level interpretability를 함께 개선한다.

## 2. 왜 중요한가

Foundation embedding을 그대로 zero-shot 사용하기보다 task-specific interpretable model의 external knowledge로 활용한다. Ablation에서 scGPT view 제거 시 clustering이 하락했지만 tissue mismatch, domain shift와 alternative FM은 평가하지 않아, knowledge transfer 효과의 범위는 아직 제한적이다.

## 3. 내 연구에 연결할 점

Rejection biopsy에서 scGPT embedding을 IFN, cytotoxicity, endothelial injury, fibrosis topic으로 압축해 donor-level signature를 만들 수 있다. Topic 다양성과 pathway coherence를 함께 보고, 외부 center·disease-state shift 및 raw-expression topic model 대비 증분 가치를 검증해야 한다.

## 4. Bibliography

Chen, Hegang, Yuyin Lu, Yifan Zhao, Zhiming Dai, Fu Lee Wang, Qing Li, Yanghui Rao, and Yue Li. "scE2TM improves single-cell embedding interpretability and reveals cellular perturbation signatures." _Nature Communications_, 2026. [https://doi.org/10.1038/s41467-026-76825-5](https://doi.org/10.1038/s41467-026-76825-5).
