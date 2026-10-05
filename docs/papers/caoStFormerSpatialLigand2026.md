---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-05'
tags:
- wiki/paper
---

# stFormer integrates spatial ligand signaling into a foundation model for spatial transcriptomics

## 기본 정보

- Citation key: `caoStFormerSpatialLigand2026`
- Item type: journal article
- Authors: Shenghao Cao; Kaiyuan Yang; Jiabei Cheng; Jiachen Li; Hong-Bin Shen; Xiaoyong Pan; Ye Yuan
- DOI: 10.1016/j.crmeth.2026.101612
- PMID: 42815472
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42815472/)
- Source/date: Cell Reports Methods, e-published and PubMed indexed 2026-09-30

## 1. 한 줄 요약

stFormer는 spatial ligand gene을 cross-attention으로 통합하고 약 410만 Visium sample로 pretraining해, single-cell resolution과 whole-transcriptome coverage 사이를 잇는 spatial transcriptomics foundation model이다.

## 2. 왜 중요한가

Biased cross-attention으로 서로 다른 ST 기술을 통합하고 clustering, batch correction, cell-type prediction과 gene-function prediction에서 scFoundation을 비교 대상으로 평가한다. In silico perturbation으로 ligand–receptor response도 탐색하지만, public Visium corpus의 tissue coverage와 독립 platform 일반화가 실제 활용의 핵심이다.

## 3. 내 연구에 연결할 점

Rejection biopsy의 immune–endothelial–tubular ligand signaling과 lesion neighborhood를 표현하는 후보 모델이다. Kidney 외부 cohort, platform·center·donor holdout에서 expression-only·spatial baseline과 비교하고, ligand perturbation은 실제 renal data로 검증해야 한다.

## 4. Bibliography

Cao, Shenghao, et al. "stFormer Integrates Spatial Ligand Signaling into a Foundation Model for Spatial Transcriptomics." _Cell Reports Methods_ (2026): 101612. [https://doi.org/10.1016/j.crmeth.2026.101612](https://doi.org/10.1016/j.crmeth.2026.101612).
