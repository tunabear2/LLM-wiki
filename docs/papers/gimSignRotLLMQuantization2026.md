---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# SignRot: LLM Quantization with Massive Outlier-Aware Sign-Adjusted Rotation

## 기본 정보

- Citation key: `gimSignRotLLMQuantization2026`
- Item type: preprint
- Authors: Jaehun Gim; Jaewoo Kim; Gyuwan Kim; Seo Yeon Park
- Source: arXiv v1, submitted 2026-11-12 (not peer reviewed)
- Original: [arXiv:2611.16502](https://arxiv.org/abs/2611.16502)
- Code: [HYU-ARK-Lab/SignRot](https://github.com/HYU-ARK-Lab/SignRot)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

SignRot은 massive activation outlier가 Hadamard 회전 뒤 양봉 분포를 만드는 문제를 부호 정렬과 비대칭 activation quantization으로 완화하는 경량 LLM 양자화 보정법이다.

## 2. 연구 질문

추론 시 추가 행렬곱 없이 기존 Hadamard 기반 post-training quantization의 massive-outlier 손실을 줄일 수 있는가?

## 3. 데이터와 방법

Calibration pass에서 massive-outlier channel을 찾고 해당 Hadamard row의 부호를 맞추는 sign vector를 구성한다. 이동한 activation 평균은 asymmetric zero-point로 흡수한다. QuaRot에 결합해 LLaMA3-70B를 WikiText2 perplexity와 zero-shot reasoning으로 평가했다.

## 4. 핵심 결과

- LLaMA3-70B에서 WikiText2 perplexity 5.88, 평균 zero-shot reasoning accuracy 72.73을 보고했다.
- 같은 설정의 SpinQuant보다 높은 결과를 보고했으며, calibration forward pass 1회와 element-wise sign flip만 추가한다.
- Online rotation에 별도 dense matrix multiplication을 넣지 않아 fast Walsh–Hadamard transform 경로를 유지한다.

## 5. 한계

초록에 제시된 정량 결과는 LLaMA3-70B 중심이며 다른 model family·bit width·hardware의 end-to-end latency와 energy 결과는 확인되지 않는다. Preprint 결과이므로 공개 코드로 정확도와 실제 serving 이득을 함께 재검증해야 한다.

## 6. 재현 또는 활용 포인트

Model·layer별 outlier threshold, weight/activation bit width, calibration corpus, symmetric/asymmetric quantizer를 고정한다. Perplexity와 downstream accuracy뿐 아니라 kernel latency, peak memory, throughput을 기존 QuaRot·SpinQuant와 같은 stack에서 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

논문·임상기록·omics metadata를 함께 다루는 로컬 LLM을 저정밀도로 운영할 때 비용 절감 후보이다. Rejection 관련 문서 QA에서는 희귀 임상용어와 수치 보존 여부를 FP16 기준과 별도로 확인해야 한다.

## 8. 관련 키워드

- post-training quantization
- activation outlier
- Hadamard rotation
- efficient inference

## 9. Bibliography

Gim, Jaehun, et al. “SignRot: LLM Quantization with Massive Outlier-Aware Sign-Adjusted Rotation.” _arXiv_, 2026. [https://arxiv.org/abs/2611.16502](https://arxiv.org/abs/2611.16502).
