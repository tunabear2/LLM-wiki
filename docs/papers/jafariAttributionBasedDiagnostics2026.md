---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Attribution-based diagnostics for single-cell foundation models

## 기본 정보

- Citation key: `jafariAttributionBasedDiagnostics2026`
- Item type: preprint
- Authors: Farnoush Rezaei Jafari; Tristan Lazard; Kenza Bouzid; Shruthi Bannur; Jeremiah Wander; Ashley Mae Conard; Stephanie Hyland; Lorin Crawford; Daniel Coelho de Castro
- arXiv: 2611.02335
- URL: [Link](https://arxiv.org/abs/2611.02335)
- Source/date: arXiv v2, revised 2026-11-03

## 1. 한 줄 요약

Cell2Sentence·scGPT annotation과 scGPT+STATE perturbation prediction에서 attribution은 정확도만으로 보이지 않는 marker 사용, context interaction과 shortcut을 진단한다.

## 2. 왜 중요한가

Attribution 결과는 model architecture, expression rank, biological reference, baseline과 null model 선택에 민감했다. 따라서 feature attribution을 곧바로 기전 증거로 해석하기보다, 통제된 reference와 prediction quality를 함께 보는 진단 도구로 사용해야 한다.

## 3. 내 연구에 연결할 점

Rejection annotation과 perturbation 예측에서 HLA·IFN·cytotoxicity marker가 실제 결정에 쓰이는지 확인하되, donor·batch·cell composition null과 renal-specific marker reference를 사전에 고정해야 한다.

## 4. Bibliography

Jafari, Farnoush Rezaei, Tristan Lazard, Kenza Bouzid, Shruthi Bannur, Jeremiah Wander, Ashley Mae Conard, Stephanie Hyland, Lorin Crawford, and Daniel Coelho de Castro. "Attribution-based diagnostics for single-cell foundation models." _arXiv_, 2026. [https://arxiv.org/abs/2611.02335](https://arxiv.org/abs/2611.02335).
