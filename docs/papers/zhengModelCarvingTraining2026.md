---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# Model Carving: Training Transformers That Optimize Their Own Topology

## 기본 정보

- Citation key: `zhengModelCarvingTraining2026`
- Item type: preprint
- Authors: Kaden Zheng; Pratyusha Sharma
- Source: arXiv v1, posted 2026-11-20
- Original: [arXiv:2611.27962](https://arxiv.org/abs/2611.27962)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

Model Carving은 attention·MLP sublayer마다 학습 가능한 scalar gate를 두어 가중치와 Transformer topology를 한 번에 학습하고, 불필요한 sublayer를 제거한 비균일 모델을 얻는다.

## 2. 연구 질문

고정된 균일 Transformer를 사후 pruning·distillation하는 대신 학습 중 loss가 직접 sublayer 구성을 선택하면 같은 계산 예산에서 더 작고 빠른 모델을 얻을 수 있는가?

## 3. 데이터와 방법

각 attention·MLP sublayer에 learnable gate를 붙이고 sparsity pressure로 gate가 꺼진 구성요소를 제거한다. Standard Transformer 140M–2.7B와 looped Transformer 140M–1.3B를 사전학습해 dense training, pruning, distillation과 동일 크기·동일 학습 compute 조건에서 validation loss, few-shot task, generation, FLOPs와 decode speed를 비교했다.

## 4. 핵심 결과

- Carved model은 같은 학습 compute에서 최대 1.7배 더 많은 compute를 쓴 dense model보다 낮은 validation loss를 보고했다.
- Size-matched pruning·distillation baseline보다 좋은 성능을 보였고, 이 차이는 모델 규모가 커질수록 증가했다.
- 제거된 sublayer가 실제로 실행되지 않아 token당 FLOPs를 최대 34% 줄이고 decode를 최대 1.6배 가속했다.

## 5. 한계

평가는 저자가 선택한 사전학습 규모와 topology regularization에 한정되며, 대규모 instruction tuning·RL 이후에도 같은 구조가 최적인지는 확인되지 않았다. Gate threshold와 sparsity schedule이 학습 안정성 및 architecture search 비용에 미치는 영향도 배포 환경별 재검증이 필요하다.

## 6. 재현 또는 활용 포인트

초기 topology, gate regularizer, 제거 threshold와 제거 시점을 고정하고 dense·magnitude pruning·distillation을 같은 token·FLOP 예산에서 비교한다. Parameter 수만 아니라 실제 kernel 호출, latency, peak memory와 downstream calibration을 함께 측정해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

작은 임상·오믹스 모델을 edge 또는 제한된 GPU에서 운영할 때 사후 압축 대신 학습 중 필요한 block만 남기는 설계 후보가 된다. 단, 작은 transplant cohort에서는 topology 선택 자체가 cohort artifact에 과적합하지 않도록 center holdout이 필요하다.

## 8. 관련 키워드

- neural architecture search
- Transformer pruning
- adaptive topology
- efficient inference

## 9. Bibliography

Zheng, Kaden, and Pratyusha Sharma. “Model Carving: Training Transformers That Optimize Their Own Topology.” _arXiv_, 2026. [https://arxiv.org/abs/2611.27962](https://arxiv.org/abs/2611.27962).
