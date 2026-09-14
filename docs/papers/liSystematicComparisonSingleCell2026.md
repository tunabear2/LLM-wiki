---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-14'
tags:
- wiki/paper
---

# A systematic comparison of single-cell perturbation response prediction models

## 기본 정보

- Citation key: `liSystematicComparisonSingleCell2026`
- Item type: journalArticle
- Authors: Lanxiang Li; Yue You; Yunlin Fu; Wenyu Liao; Xueying Fan; Shihong Lu; Ye Cao; Bo Li; Wenle Ren; Jiaming Kong; Shuangjia Zheng; Jizheng Chen; Xiaodong Liu; Luyi Tian
- DOI: 10.1126/sciadv.aed3414
- PMID: 42715312
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42715312/)
- Source/date: Science Advances, published/indexed 2026-09-09

## 1. 한 줄 요약

25개 dataset과 24개 metric에서 13개 single-cell perturbation prediction method를 비교해, fine-tuned foundation model도 variance와 synergy를 축소하며 어떤 모델도 cell-type transfer를 일관되게 해결하지 못함을 보였다.

## 2. 왜 중요한가

Unseen single-gene perturbation, combinatorial interaction, cross-cell-type transfer를 분리해 평가했다. 작은 효과에서는 control과 가까운 expression-level agreement가 높아 보였고, 큰 효과에서는 delta·DE metric이 더 분명한 신호를 포착했다. PerturbNet은 일부 task의 DE recovery에서 강했지만, 모델 순위는 effect size와 metric 관점에 크게 의존했다.

## 3. 내 연구에 연결할 점

Rejection biopsy에서 cytokine·면역억제제·유전자 perturbation response를 예측할 때 raw-expression, delta, DEG recovery를 함께 보고해야 한다. Donor와 cell type을 동시에 분리한 external test를 두고, 작은 효과를 control resemblance로 잘 맞춘 결과와 실제 rejection program 회복을 구분해야 한다.

## 4. Bibliography

Li, Lanxiang, Yue You, Yunlin Fu, Wenyu Liao, Xueying Fan, Shihong Lu, Ye Cao, et al. "A systematic comparison of single-cell perturbation response prediction models." _Science Advances_ 12, no. 37 (2026): eaed3414. [https://doi.org/10.1126/sciadv.aed3414](https://doi.org/10.1126/sciadv.aed3414).
