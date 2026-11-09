---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-09'
tags:
- wiki/paper
---

# CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention

## 기본 정보

- Citation key: `dabbahCISARetrofittingDense2026`
- Item type: preprint
- Authors: Mohammed Dabbah; Izhak Golan; Oren Tropp; Daniel Afrimi; Vladimir Anisimov; Tomer Asida; Nave Assaf; Ran El-Yaniv; Ido Galil; Yonatan Geifman; Omri Puny; Ido Shahaf; Akhiad Bercovich
- Source: arXiv v1, submitted 2026-11-02 (not peer reviewed)
- Original: [arXiv:2611.03200](https://arxiv.org/abs/2611.03200)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

CISA는 pretrained dense-attention 모델을 재학습하지 않고 KV cache를 고정 크기 chunk로 색인하고 query 간 선택을 공유해 million-token serving의 attention read와 처리시간을 줄인다.

## 2. 연구 질문

별도 full-length index cache나 sparse training 없이 long-context dense model에 실제 serving 이득이 나는 sparse attention을 붙일 수 있는가?

## 3. 데이터와 방법

Key summary로 fixed-size KV chunk를 선택하고 KV group당 하나의 indexing query를 사용한다. Prefill에서는 QShare가 인접 query의 선택을 재사용한다. NVIDIA Nemotron 3 Nano·Ultra와 Inkling-Small을 RULER, MRCR, LongBench v2, GraphWalks 및 1M-token serving workload에서 dense attention과 비교했다.

## 4. 핵심 결과

- Ultra의 1M-token one-layer BF16 실험에서 scoring·selection을 포함한 GPU work가 prefill 8.6배, decode 3.0배 빨랐다.
- Nano·Ultra의 RULER에서는 KV read를 8–16배 줄이면서 dense 대비 점수 차이가 최대 2.05 percentage point였다.
- B300 GPU 4장, 32 concurrent request, request당 4K output 조건에서 end-to-end throughput이 dense 대비 2.29배였고, 더 작은 budget은 2.61배까지 올랐지만 GraphWalks 점수 차이가 커졌다.

## 5. 한계

Calibration activation이 필요해 data-free 방법은 아니며 KV를 제거하지 않으므로 cache-capacity 압축도 아니다. 두 model family와 한 serving stack, 제한된 budget만 평가했고 긴 generation에서는 이득이 줄 수 있다. B300 중심 결과를 다른 GPU와 실제 transcriptomics agent workload에 그대로 일반화할 수 없다.

## 6. 재현 또는 활용 포인트

Context length, recent window, chunk size, selected-chunk budget, QShare group을 함께 기록하고 core-kernel speed와 end-to-end throughput을 분리한다. Dense 대비 task score 차이와 GPU memory·TTFT·TPOT를 같은 serving workload에서 측정해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

대규모 논문·임상기록·omics metadata를 함께 읽는 장문 RAG/agent를 운영할 때 비용을 줄일 후보이다. 다만 임상 정보 누락 위험이 있으므로 rejection 관련 long-context QA에서 dense attention과 답변 충실도를 먼저 비교해야 한다.

## 8. 관련 키워드

- sparse attention
- KV cache indexing
- long-context inference
- training-free retrofit

## 9. Bibliography

Dabbah, Mohammed, et al. “CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention.” _arXiv_, 2026. [https://arxiv.org/abs/2611.03200](https://arxiv.org/abs/2611.03200).
