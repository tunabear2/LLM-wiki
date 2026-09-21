---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-21'
tags:
- wiki/paper
---

# Towards a knowledge-enhanced single-cell foundation model

## 기본 정보

- Citation key: `zhangTowardsKnowledgeEnhanced2026`
- Item type: preprint
- Authors: Hanqing Zhang; Jie Bao; Mei Ma; Shuai Liu; Jiaying Ma; Jiaguan Liu; Jiaxiao Li; Zhenbo Li; Wenwen Gong; Zhijun Ca
- DOI: 10.48550/arXiv.2609.14970
- URL: [Link](https://arxiv.org/abs/2609.14970)
- Source/date: arXiv v1, 2026-09-14

## 1. 한 줄 요약

scKITE는 cell-level text annotation과 gene-regulatory supervision을 auxiliary decoder로 pretraining에만 결합해, 17만 9,067개 cell로도 더 큰 single-cell foundation model을 여러 downstream task에서 앞섰다고 보고한다.

## 2. 왜 중요한가

Single-cell FM의 성능 향상을 단순한 corpus 확대가 아니라 biological knowledge 축으로 설명한다. Auxiliary decoder를 추론 시 제거하므로 downstream encoder 비용을 늘리지 않지만, 비교 결과가 annotation·regulatory prior의 품질과 pretraining corpus overlap에 얼마나 의존하는지는 별도 검증이 필요하다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection에서는 Banff lesion, immune/endothelial/tubular cell-state annotation과 kidney GRN을 보조 supervision으로 넣는 소규모 domain adaptation을 시험할 수 있다. Donor·center holdout과 text-label ablation을 두어 실제 generalization과 label leakage를 구분해야 한다.

## 4. Bibliography

Zhang, Hanqing, Jie Bao, Mei Ma, Shuai Liu, Jiaying Ma, Jiaguan Liu, Jiaxiao Li, Zhenbo Li, Wenwen Gong, and Zhijun Ca. "Towards a knowledge-enhanced single-cell foundation model." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2609.14970](https://doi.org/10.48550/arXiv.2609.14970).
