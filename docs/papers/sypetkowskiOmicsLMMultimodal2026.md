---
type: paper
status: reference
rag_priority: high
updated: '2026-10-31'
tags:
- wiki/paper
---

# OmicsLM: A Multimodal Large Language Model for Multi-Sample Omics Reasoning

## 기본 정보

- Citation key: `sypetkowskiOmicsLMMultimodal2026`
- Item type: preprint
- Authors: M. Sypetkowski; Ł. Smoliński; R. Kinas; J. Krawczyk; B. Hofman; A. Możwiłło; M. Pikusa; T. Jetka; R. Powalski
- arXiv: 2605.06728
- URL: [Link](https://arxiv.org/abs/2605.06728)
- Source/date: arXiv revised v2, 2026-10-25

## 1. 한 줄 요약

OmicsLM은 bulk 또는 single-cell transcriptome을 compact continuous embedding으로 표현해 여러 sample과 자연어 instruction을 한 context에서 추론하는 9B multimodal language model이다.

## 2. 왜 중요한가

20B-token continued pretraining과 521만 conversation의 supervised fine-tuning을 거쳐 annotation, GEO-OmicsQA와 perturbation-response task를 평가한다. Text-only gene list보다 continuous omics representation이 낫다는 ablation으로 정량 expression을 language interface에 연결한다.

## 3. 내 연구에 연결할 점

여러 biopsy와 임상 설명을 함께 비교해 rejection trajectory를 질의하는 interface 후보지만, patient-level split, retrieval provenance, 숫자 fidelity와 unsupported biological explanation을 별도로 감사해야 한다.

## 4. Bibliography

Sypetkowski, M., Ł. Smoliński, R. Kinas, J. Krawczyk, B. Hofman, A. Możwiłło, M. Pikusa, T. Jetka, and R. Powalski. "OmicsLM: A Multimodal Large Language Model for Multi-Sample Omics Reasoning." _arXiv_, revised 2026. [https://arxiv.org/abs/2605.06728](https://arxiv.org/abs/2605.06728).
