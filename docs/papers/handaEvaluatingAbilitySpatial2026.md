---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-21'
tags:
- wiki/paper
---

# Evaluating the ability of spatial transcriptomics foundation models to learn multi-scale spatial variation

## 기본 정보

- Citation key: `handaEvaluatingAbilitySpatial2026`
- Item type: preprint
- Authors: Dhanav Handa; Cristina Martin-Linares; Genevieve Stein-O'Brien; Jonathan Ling; Uthsav Chitra
- DOI: 10.64898/2026.08.01.742217
- URL: [Link](https://doi.org/10.64898/2026.08.01.742217)
- Source/date: bioRxiv v1, posted 2026-08-06; newly indexed 2026-09-17

## 1. 한 줄 요약

SAFFRON은 sparse autoencoder로 spatial foundation model embedding을 해석한 결과 Novae만 global gradient에서 단순 baseline을 앞섰고, 어떤 모델도 local microenvironment pattern에서는 baseline을 일관되게 넘지 못했다고 보고한다.

## 2. 왜 중요한가

Spatial FM이 multi-scale structure를 학습한다는 주장을 global gradient와 local niche로 분리해 검증한다. Sparse feature의 해석 가능성뿐 아니라 non-foundation baseline 대비 실제 증분 성능을 요구한다는 점에서 spatial embedding 평가의 기준을 제시한다.

## 3. 내 연구에 연결할 점

Kidney rejection biopsy에서는 cortex–medulla 및 lesion-scale gradient와 immune–endothelial–tubular local niche를 따로 평가해야 한다. Banff lesion과 local inflammatory niche에서 Novae 등 FM이 spatial smoothing·expression baseline을 넘는지 external section과 center holdout으로 확인할 필요가 있다.

## 4. Bibliography

Handa, Dhanav, Cristina Martin-Linares, Genevieve Stein-O'Brien, Jonathan Ling, and Uthsav Chitra. "Evaluating the ability of spatial transcriptomics foundation models to learn multi-scale spatial variation." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.08.01.742217](https://doi.org/10.64898/2026.08.01.742217).
