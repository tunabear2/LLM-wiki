---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-28'
tags:
- wiki/paper
---

# The Unreasonable Effectiveness of Cell Types in Describing Neuronal Physiological Features

## 기본 정보

- Citation key: `sharmaUnreasonableEffectivenessCell2026`
- Item type: preprint
- Authors: Harshil Sharma; Xiao-Ping Liu; Thomas Chartrand; Brian Kalmbach; Ed Lein; Stefan Mihalas; Zhixin Lu
- DOI: 10.64898/2026.08.27.744753
- PMID: 42779632
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42779632/)
- Source/date: bioRxiv v2, posted 2026-09-16; PubMed indexed 2026-09-24

## 1. 한 줄 요약

Human neuron Patch-seq 495개에서 전기생리 feature를 예측할 때 전통적 cell-type representation이 scGPT embedding 단독보다 대체로 강했고, 두 표현을 결합했을 때 최고 성능을 보였다.

## 2. 왜 중요한가

Foundation embedding, cell type, ion-channel gene과 highly variable gene representation을 같은 paired transcriptomic–electrophysiology task에서 비교한다. 수백 sample 규모에서는 일반 목적 pretrained embedding이 discrete biological label을 자동으로 대체하지 않으며, architecture와 initialization에 따른 변동도 커 단순 baseline과 joint model이 필요함을 보여준다.

## 3. 내 연구에 연결할 점

Kidney rejection outcome이나 lesion 예측에서도 scGPT embedding을 cell-type composition, curated pathway와 임상 covariate의 대체물로 가정하면 안 된다. Donor-level split에서 각 표현의 단독·결합 이득과 initialization variance를 함께 보고해야 한다.

## 4. Bibliography

Sharma, Harshil, Xiao-Ping Liu, Thomas Chartrand, Brian Kalmbach, Ed Lein, Stefan Mihalas, and Zhixin Lu. "The Unreasonable Effectiveness of Cell Types in Describing Neuronal Physiological Features." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.08.27.744753](https://doi.org/10.64898/2026.08.27.744753).
