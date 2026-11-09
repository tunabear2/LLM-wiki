---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# A low-rank decoder bottleneck bounds reliability in foundation-model perturbation prediction

## 기본 정보

- Citation key: `zhangLowRankDecoder2026`
- Item type: preprint
- Authors: Zheyu Zhang; Yuanhao Huang; Fan Feng; Jie Liu
- arXiv: 2611.05849
- URL: [Link](https://arxiv.org/abs/2611.05849)
- Source/date: arXiv v1, submitted 2026-11-03

## 1. 한 줄 요약

STATE의 state-transition decoder는 낮은 rank의 attention bottleneck을 가지며, 예측 response와 가장 가까운 training response 사이의 거리가 perturbation별 신뢰도를 잘 나타낸다.

## 2. 왜 중요한가

SE-600M, scGPT, Tahoe-x1 encoder와 네 cell line에서 aggregate accuracy가 가리는 per-prediction reliability를 분석했다. Predicted nearest-neighbor distance는 관측 response 없이도 confidence score로 사용할 수 있고 encoder·cell line 사이에서 threshold transfer 가능성을 보였다.

## 3. 내 연구에 연결할 점

Rejection cytokine·drug perturbation의 후보 순위를 낼 때 평균 correlation만 보고하지 말고, renal cell state가 training response manifold에서 얼마나 떨어졌는지와 abstention threshold를 함께 제시해야 한다.

## 4. Bibliography

Zhang, Zheyu, Yuanhao Huang, Fan Feng, and Jie Liu. "A low-rank decoder bottleneck bounds reliability in foundation-model perturbation prediction." _arXiv_, 2026. [https://arxiv.org/abs/2611.05849](https://arxiv.org/abs/2611.05849).
