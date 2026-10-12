---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing

## 기본 정보

- Citation key: `gargHowHighFloors2026`
- Item type: preprint
- Authors: Pranjal Garg
- DOI: 10.48550/arXiv.2610.08544
- URL: [Link](https://doi.org/10.48550/arXiv.2610.08544)
- Source/date: arXiv v1, submitted 2026-10-06

## 1. 한 줄 요약

Probe score를 단순 입력이 설명하는 floor와 전체 입력이 허용하는 ceiling 사이의 headroom으로 해석했을 때, scGPT가 biological variability를 일부만 추가로 encoding함을 보인다.

## 2. 왜 중요한가

높은 probe 성능을 곧바로 representation의 고유 정보로 해석하면 입력 자체의 예측력과 dataset별 ceiling을 놓칠 수 있다. 이 논문은 scFM embedding의 해석 가능성을 absolute score 대신 명시적 baseline과 recoverable headroom에 상대화하는 기준을 제공한다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection embedding에서 donor, batch, cell composition만으로 얻는 floor와 raw expression 기반 ceiling을 먼저 측정하고, scGPT embedding이 남은 headroom을 얼마나 회복하는지 patient-level split에서 평가해야 한다.

## 4. Bibliography

Garg, Pranjal. "How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2610.08544](https://doi.org/10.48550/arXiv.2610.08544).
