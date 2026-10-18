---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# Titan-Llama: Retrofitting Pre-trained LLMs with External Neural Memory Modules

## 기본 정보

- Citation key: `panTitanLlamaRetrofitting2026`
- Item type: arXiv preprint
- Authors: Sarah Pan; Ali Behrouz
- Source: arXiv v1, submitted 2026-10-13
- Original: [arXiv:2610.19210](https://arxiv.org/abs/2610.19210); [code](https://github.com/sarahpannn/titans-pytorch/tree/main)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

Titan-Llama는 기존 Llama attention layer 일부를 test-time에 갱신되는 고정 크기 neural memory로 바꿔, 최근 문맥은 정확히 유지하고 먼 문맥은 압축하는 post-training long-context 구조다.

## 2. 연구 질문

새 언어모델을 처음부터 학습하지 않고도 Transformer의 병렬 학습 이점을 유지하면서 long-context KV-cache 비용을 줄일 수 있는가?

## 3. 데이터와 방법

Llama-3.2-1B-Instruct에 blockwise attention mask와 neural memory module(NMM)을 삽입했다. 최근 token은 full-fidelity local attention으로 읽고 오래된 block은 inner objective를 이용해 NMM parameter에 recurrent하게 기록한다. QuALITY, LongHealth, RULER에서 문맥 기억·추론을 평가하고 NVIDIA A100 80GB에서 prefill, decode, peak/steady-state memory를 측정했다.

## 4. 핵심 결과

- Segmented-attention 대비 QuALITY 정확도는 23.87%에서 40.51%, LongHealth는 14.50%에서 40.75%로 상승했다.
- 평가한 중간 문맥 길이에서 prefill은 20% 이상, decode는 37% 빨라졌고 steady-state decode memory는 24% 줄었다.
- NMM만으로 뒤쪽 full-attention layer까지 모두 대체하면 RULER의 정확한 장거리 회수가 크게 약해져, local/full attention과 memory의 혼합이 중요했다.

## 5. 한계

실험은 1B Llama 한 backbone에 집중됐다. 짧은 문맥과 일부 hybrid 설정에서는 peak memory가 full attention보다 컸고, 최적 chunk size가 task별로 달랐다. RULER의 정확한 needle retrieval은 NMM이 full attention을 완전히 대체할 수준은 아니었다.

## 6. 재현 또는 활용 포인트

공개 구현에서 교체 layer 비율, 512–2,048 token chunk, inner-loop update 비용을 함께 기록한다. 평균 정확도뿐 아니라 exact retrieval, prefill/decode latency, peak와 steady-state memory를 분리해 측정해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

긴 이식 임상기록, 병리 판독, 논문 corpus를 한 context에서 다루는 RAG/agent memory 설계에 참고할 수 있다. 생물학 데이터나 임상 안전성을 직접 검증한 연구는 아니다.

## 8. 관련 키워드

- LLM / Transformer
- long-context inference
- neural memory
- test-time training

## 9. Bibliography

Pan, Sarah, and Ali Behrouz. “Titan-Llama: Retrofitting Pre-trained LLMs with External Neural Memory Modules.” arXiv:2610.19210, 2026. [https://arxiv.org/abs/2610.19210](https://arxiv.org/abs/2610.19210).
