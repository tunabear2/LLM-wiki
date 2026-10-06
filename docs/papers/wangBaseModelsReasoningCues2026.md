---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-07'
tags:
- wiki/paper
---

# Base Models Can Reason By Taking a Cue From Training Data

## 기본 정보

- Citation key: `wangBaseModelsReasoningCues2026`
- Item type: preprint
- Authors: Sophie L. Wang; Amil Dravid; Rulin Shao; Kevin Farhat; Sewon Min; Alexei A. Efros
- Source: arXiv (submitted 2026-10-05; not peer reviewed)
- Original: [arXiv:2610.06851](https://arxiv.org/abs/2610.06851); [code](https://github.com/sophicle/cues)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

학습 데이터와 연결된 응답 시작 토큰(cue)을 고정하면 base model도 RL 모델에 가까운 수학·코딩 추론과 서로 다른 안전 행동을 보일 수 있음을 인과적 데이터 개입으로 분석했다.

## 2. 연구 질문

RL이 만든 추론 향상의 일부가 가중치 전체의 능력보다 응답 시작 cue의 확률과 데이터 연관성에 있는가?

## 3. 데이터와 방법

Olmo-3-7B와 Qwen3-14B 등 base/RL 모델에서 시작 토큰을 고정해 MATH-500·코딩 성능을 비교하고, hidden-state와 학습 문서 유형의 상관을 측정했다. 학습 데이터의 cue를 바꾸거나 제거하는 causal intervention과 안전 거부/순응 사례를 함께 사용했다.

## 4. 핵심 결과

- Olmo-3-7B의 `.\n\nOkay` cue는 MATH-500 pass@1을 42%에서 78%로, Qwen3-14B의 `Alright,`는 72%에서 87%로 높였다.
- RL은 유효 cue의 확률을 올렸고, cue 고정만으로 base–RL 성능 차이의 상당 부분을 회복했다.
- `chicken` 같은 임의 단어도 학습 데이터 개입으로 추론 cue가 될 수 있었으며, cue에 따라 안전 거부·순응 행동도 달라졌다.

## 5. 한계

효과는 모델과 cue에 의존하며 모든 base model에서 유효하지 않았다. 실험은 특정 수학·코딩 benchmark와 제한된 모델군에 집중되어 실제 장기 추론·배포 안전성으로 일반화할 수 없다.

## 6. 재현 또는 활용 포인트

공개 코드로 모델별 cue 탐색, seed·prompt 고정, cue를 찾는 데이터 개입과 단순 prompt engineering을 분리해 재현할 수 있다. 성능 상승을 reasoning capability 자체의 증가로 해석하지 말고 cue 민감도와 refusal calibration을 별도 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

직접적인 omics 논문은 아니지만, transcriptomics LLM이 특정 gene-token 순서나 문맥 cue에 과도하게 의존하는지 점검하는 실험 설계를 제공한다. 이식 예후 모델에서는 cue 고정 성능을 임상 외부 검증 성능과 혼동하지 않는 것이 중요하다.

## 8. 관련 키워드

- base model reasoning
- training-data cue
- causal data intervention
- safety behavior

## 9. Bibliography

Wang, Sophie L., et al. “Base Models Can Reason By Taking a Cue From Training Data.” arXiv, 2026. [https://arxiv.org/abs/2610.06851](https://arxiv.org/abs/2610.06851).
