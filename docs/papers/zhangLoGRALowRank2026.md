---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-07'
tags:
- wiki/paper
---

# LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches

## 기본 정보

- Citation key: `zhangLoGRALowRank2026`
- Item type: preprint
- Authors: Shaokun Zhang; Yifan Zhang; Jian Hu; Yueying Li; Hao Zhang; Binfeng Xu; Jan Kautz; Yi Dong
- Source: arXiv (submitted 2026-10-05; not peer reviewed)
- Original: [arXiv:2610.06647](https://arxiv.org/abs/2610.06647); [Molt implementation](https://github.com/skzhang1/labs-molt/tree/logra/examples/scripts/logra)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

LoGRA는 RL post-training의 gradient를 low-rank sketch로 저장하고 predicted-KL step control을 결합해 업데이트 신호와 policy 동기화에 필요한 메모리를 줄인다.

## 2. 연구 질문

대규모 reasoning RL에서 dense Adam의 메모리 병목을 줄이면서 학습 안정성과 성능을 유지할 수 있는가?

## 3. 데이터와 방법

저랭크 gradient sketch를 모델 업데이트에 재사용하고, 각 update 전 policy 변화량을 예측해 step 크기를 조절하는 predicted-KL 제어를 적용했다. 1.5B·7B·27B 모델과 reasoning task에서 dense Adam 및 기존 RL 설정과 비교했다.

## 4. 핵심 결과

- 1.5B와 7B 설정에서 평균 학습 메모리가 각각 약 21.8%, 45.7% 줄면서 성능 저하가 없었다.
- 8-GPU 한 노드에서 27B 모델을 1,100 step 이상 안정적으로 학습했으며, dense Adam은 메모리 부족으로 실행되지 않았다.
- 공개 Molt 코드가 있어 gradient 압축과 KL 제어를 기존 post-training 파이프라인에 삽입할 수 있다.

## 5. 한계

검증은 주로 reasoning task와 제한된 Qwen 계열 설정에 머물렀다. 27B 결과는 dense baseline과 직접적인 정확도 비교가 불가능하고, wall-clock 속도·다양한 RL objective·장기 안정성은 더 검증해야 한다.

## 6. 재현 또는 활용 포인트

공개 예제의 rank, seed, rollout batch, predicted-KL threshold를 고정해 메모리뿐 아니라 update rate와 held-out 성능을 함께 기록한다. 작은 rank에서의 압축 오차와 optimizer state 저장량을 별도로 profiling한다.

## 7. Transcriptomics·신장이식 연구와의 연결

유전자·세포 표현 모델의 domain adaptation이나 임상 예측 fine-tuning을 제한된 GPU에서 수행할 때 적용 가능한 메모리 절감 패턴이다. 다만 작은 신장이식 cohort에서 RL을 쓸 근거가 자동으로 생기는 것은 아니며, supervised fine-tuning과 먼저 비교해야 한다.

## 8. 관련 키워드

- low-rank gradient sketch
- reinforcement learning post-training
- predicted KL control
- memory-efficient LLM training

## 9. Bibliography

Zhang, Shaokun, et al. “LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches.” arXiv, 2026. [https://arxiv.org/abs/2610.06647](https://arxiv.org/abs/2610.06647).
