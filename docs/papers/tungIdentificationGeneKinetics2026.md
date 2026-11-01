---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# Identification of Gene Kinetics Patterns Improves RNA Velocity and Cell Fate Prediction Using JuloVelo

## 기본 정보

- Citation key: `tungIdentificationGeneKinetics2026`
- Item type: bioRxiv preprint
- Authors: Kuo-Chen Tung; Yu-Hsiang Tu; Kai-Yuan Hsieh; Hsueh-Fen Juan; Hsuan-Cheng Huang
- Source: bioRxiv v1, posted 2026-10-27 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.24.761531](https://doi.org/10.64898/2026.10.24.761531); [code](https://github.com/jhlabtw/JuloVelo.jl)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

JuloVelo는 gene별 induction·repression kinetics pattern으로 neural RNA-velocity model을 초기화하고 multiome promoter accessibility를 보조 신호로 사용해 여덟 dataset에서 cell-fate 방향성과 계산 효율을 개선했다.

## 2. 연구 질문

모든 gene에 일정하거나 이진적인 kinetics를 가정하는 대신 gene별 dynamic pattern을 먼저 식별하면 RNA velocity와 cell-fate prediction을 안정화할 수 있는가?

## 3. 데이터와 방법

Gene을 Circle, Complete induction, Complete repression pattern으로 사전 분류하고 pattern-matched pretrained weight로 cell-specific kinetics network를 초기화했다. Multiome에서는 promoter chromatin accessibility로 kinetics 판정을 보조하고, transcription-factor modulation을 모사하는 in-silico perturbation을 추가했다. Erythrogenesis, neurogenesis, endocrinogenesis의 8개 dataset에서 constant-rate·cell-specific model과 비교했다.

## 4. 핵심 결과

- 비교 model보다 RNA-velocity 성능이 일관되게 높았고 hippocampal neurogenesis의 5개 lineage program을 복원했다.
- Promoter accessibility를 사용한 multiome 분석은 intrinsic·extrinsic velocity stability를 모두 높였다.
- CellDancer 대비 실행 시간을 약 70% 줄였다.

## 5. 한계

세 가지 kinetics pattern으로 복잡한 regulation을 이산화하며, snapshot에서 추정한 velocity가 실제 longitudinal lineage를 항상 보장하지 않는다. Preprint 단계이고 allograft inflammation·treatment transition은 검증하지 않았다.

## 6. 재현 또는 활용 포인트

Gene-pattern assignment, initialization seed, latent time, velocity consistency와 lineage direction을 분리해 평가한다. Ground-truth lineage 또는 time-course가 있는 dataset에서 pattern-free baseline과 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Activated immune·tubular cell이 injury에서 recovery 또는 rejection으로 이동하는 방향을 추정하는 후보지만, donor/timepoint가 적은 biopsy에서는 pseudotime과 임상 시간의 혼동을 별도 점검해야 한다.

## 8. 관련 키워드

- scRNA-seq
- RNA velocity
- trajectory inference
- single-cell multiome

## 9. Bibliography

Tung, Kuo-Chen, et al. “Identification of Gene Kinetics Patterns Improves RNA Velocity and Cell Fate Prediction Using JuloVelo.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.24.761531](https://doi.org/10.64898/2026.10.24.761531).
