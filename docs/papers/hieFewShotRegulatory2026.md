---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# Few-Shot Regulatory Sequence Design with a Genomic Language Model

## 기본 정보

- Citation key: `hieFewShotRegulatory2026`
- Item type: bioRxiv preprint
- Authors: Brian Hie; Y. Allen Hao; Matthew Liu; Divya Nori; Gabriel Brixi; Tina Lau; Chandramohan A. Ramakrishnan; Daniel Chang; Ryan Park; William E. Allen
- Source: bioRxiv v1, posted 2026-10-30 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.28.762639](https://doi.org/10.64898/2026.10.28.762639)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

Evo 2에 수십 개의 기능 예시만 prompt로 주는 genomic in-context learning과 sequence-to-function reward 기반 RL을 결합해 세 human cell line과 mouse cortex에서 선택적인 enhancer를 실험 검증했다.

## 2. 연구 질문

추가 fine-tuning 없이 소수의 sequence–function 예시만으로 genomic language model을 새로운 regulatory DNA 설계 과제에 조건화할 수 있는가?

## 3. 데이터와 방법

Genome language model Evo 2에 수십 개의 regulatory sequence 예시를 prompt로 제공해 novel sequence를 생성했다. Genomic ICL의 induction-like mechanism을 분석하고, 실험에서 얻은 sequence-to-function model을 reward로 사용한 reinforcement learning으로 조건화를 강화했다. Human cell line 세 종류의 enhancer와 mouse cortex layer 5 extratelencephalic neuron enhancer를 실험 평가했다.

## 4. 핵심 결과

- Fine-tuning 없이 소수 예시만으로 novel하고 다양한 regulatory DNA를 생성했다.
- 세 human cell line에서 cell-type-specific expression을 유도하는 enhancer를 검증했다.
- Human regulatory data로 설계한 enhancer가 mouse cortex에서 기존 enhancer보다 강한 activity와 높은 layer-5-neuron specificity를 보였다.

## 5. 한계

검증 범위는 enhancer와 제한된 cell line·mouse brain context다. Reward model의 assay bias가 생성 결과에 전달될 수 있으며 human kidney, immune activation, off-target regulation과 장기 안전성은 평가하지 않았다.

## 6. 재현 또는 활용 포인트

Prompt example 수·구성, generation diversity, RL reward model과 wet-lab selection funnel을 함께 기록한다. 기존 enhancer, random sequence, ICL-only, ICL+RL을 같은 assay에서 비교해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Tubular·endothelial·immune cell state에 선택적인 reporter 또는 perturbation construct를 설계하는 방향을 제시한다. Rejection biopsy의 expression 예측이나 임상 outcome 모델로 직접 사용할 근거는 아니다.

## 8. 관련 키워드

- Bio AI
- genomic language model
- in-context learning
- enhancer design

## 9. Bibliography

Hie, Brian, et al. “Few-Shot Regulatory Sequence Design with a Genomic Language Model.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.28.762639](https://doi.org/10.64898/2026.10.28.762639).
