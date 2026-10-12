---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers

## 기본 정보

- Citation key: `chouOrthrosPhaseAware2026`
- Item type: preprint
- Authors: Yuhong Chou; Zehao Liu; Yuqi Pan; Qian Liu; Xianwei Chen; Zhongzhu Zhou; Jibin Wu
- Source: arXiv (submitted 2026-10-09; not peer reviewed)
- Original: [arXiv:2610.13735](https://arxiv.org/abs/2610.13735)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

Orthros는 prefill에는 linear attention, autoregressive decoding에는 full attention을 쓰는 하나의 phase-aware attention module로 긴 prompt 처리 비용을 줄인다.

## 2. 연구 질문

Full-attention layer를 섞지 않고도 linear attention의 긴 문맥 recall 저하를 보완하면서 실제 생성 workload의 비용을 낮출 수 있는가?

## 3. 데이터와 방법

입력 prompt를 한꺼번에 처리하는 prefill 단계와 token을 하나씩 생성하는 decode 단계를 분리한다. 같은 Orthros module이 prefill에서는 recurrent linear computation을, decode에서는 전체 prompt state에 접근하는 full-attention pattern을 사용한다. 여러 모델 크기의 from-scratch 학습과 기존 Transformer weight를 옮기는 data-efficient conversion을 비교하고, language modeling·in-context recall·128K needle-in-a-haystack·추론 속도를 평가했다.

## 4. 핵심 결과

- Transformer 대비 prefill을 최대 21.9배 가속하면서 end-to-end 추론 개선을 보고했다.
- 128K needle-in-a-haystack에서 거의 완전한 recall을 유지했고 실제 in-context recall에서도 Transformer 수준을 보였다.
- 기존 Transformer를 Orthros로 변환한 설정이 원 모델 성능을 회복하거나 일부 비교에서 넘어섰다.

## 5. 한계

Full attention을 decode 단계에 남기므로 출력이 매우 긴 workload에서는 이점이 줄 수 있다. 속도 주장은 hardware·kernel·prompt/output 길이 비율에 민감하며, 장기 생성과 다양한 공개 모델 계열에서 독립 재현이 필요하다.

## 6. 재현 또는 활용 포인트

같은 tokenizer·checkpoint·batch에서 prefill latency, decode latency, peak memory, end-to-end tokens/s를 분리한다. 짧은 출력/긴 prompt와 긴 출력 조건을 따로 보고, recall 평가와 perplexity를 함께 확인해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

긴 임상기록·논문·omics annotation을 함께 읽는 retrieval 또는 보고서 생성에 유용할 수 있다. 다만 신장이식 예측 정확도에 대한 근거는 없으므로 효율화 layer로만 보고 domain task 성능은 별도 검증해야 한다.

## 8. 관련 키워드

- phase-aware attention
- linear prefill
- full-attention decoding
- long-context inference

## 9. Bibliography

Chou, Yuhong, et al. “Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers.” arXiv, 2026. [https://arxiv.org/abs/2610.13735](https://arxiv.org/abs/2610.13735).
