---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# Learning stochastic dynamics and cell-fate landscapes from single-cell snapshots via optimal transport

## 기본 정보

- Citation key: `liuLearningStochasticDynamics2026`
- Item type: journalArticle
- Authors: Juntan Liu; Peijie Zhou; Qing Nie; Chunhe Li
- Journal: Science Advances
- DOI: 10.1126/sciadv.aeb4205
- PMID: 42715336
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42715336/); [DOI](https://doi.org/10.1126/sciadv.aeb4205)
- Source/date: online published 2026-09-09; PubMed indexed 2026-09-09 23:04 KST
- 주 카테고리: scRNA-seq

## 1. 한 줄 요약

DiffusionOT는 여러 시점의 single-cell snapshot을 optimal transport와 neural ODE로 연결해 stochastic cell-state dynamics, trajectory와 fate landscape를 함께 추정한다.

## 2. 연구 질문

세포를 직접 추적하지 않은 여러 시점의 transcriptomic snapshot만으로, 평균적인 이동뿐 아니라 gene-expression stochasticity와 population growth를 포함한 cell-fate dynamics를 복원할 수 있는가?

## 3. 데이터와 방법

Stochastic differential equation을 ordinary differential equation으로 변환하고, optimal transport와 neural network를 이용해 고차원 landscape model 및 데이터의 stochastic force를 비지도 학습했다. Stochastic trajectory analysis로 lineage를 추적하고 gene perturbation module로 in-silico knockout과 overexpression을 수행한다. Simulation과 spatial Stereo-seq를 포함한 실제 4개 dataset에서 평가했다.

## 4. 핵심 결과

저자들은 DiffusionOT가 state-transition velocity, cellular trajectory, population growth, gene regulatory network와 cell-fate landscape를 정확하고 효율적으로 추정했다고 보고했다. 여러 시점의 snapshot에서 stochastic force를 학습함으로써 deterministic trajectory만으로 설명하기 어려운 상태 전이와 분기 구조를 함께 다뤘다.

## 5. 한계

추정 결과는 여러 시점의 sampling 설계와 stochastic dynamics 및 optimal-transport 가정에 의존하며, 실제 동일 세포의 lineage를 직접 관측한 것은 아니다. 초록에는 donor·기관 간 generalization과 ground-truth lineage가 있는 실험에서의 검증 범위가 구체적으로 제시되지 않는다. In-silico knockout·overexpression 결과도 실험적 perturbation 검증이 필요하다.

## 6. 재현 또는 활용 포인트

- Time point별 biological replicate와 cell 수를 균형 있게 두고, 시간 정보 없이 학습한 baseline과 비교한다.
- Velocity, fate probability, growth와 GRN 성능을 각각 독립적인 ground truth 또는 perturbation 자료로 평가한다.
- Sampling interval, OT regularization과 stochastic-force model에 대한 sensitivity analysis를 수행한다.
- Donor를 가로질러 cell을 섞기보다 donor-level holdout에서 trajectory transfer를 검증한다.
- 코드: [liujuntan/DiffusionOT](https://github.com/liujuntan/DiffusionOT); 재현 archive: [Zenodo 18251638](https://zenodo.org/records/18251638)

## 7. Transcriptomics·신장이식 연구와의 연결

이식 전후 또는 acute-to-chronic rejection의 serial biopsy에서 immune activation, endothelial injury와 tubular repair가 어떤 확률적 경로로 전이하는지 모델링할 후보이다. Gene perturbation module로 rejection program의 조절 인자를 우선순위화할 수 있지만, 실제 cytokine·약물 perturbation과 독립 이식 cohort에서 반드시 검증해야 한다.

## 8. 관련 키워드

- scRNA-seq
- Optimal transport
- Neural ODE
- Stochastic dynamics
- Cell-fate landscape
- Trajectory inference
- In-silico perturbation

## 9. Bibliography

Liu, Juntan, Peijie Zhou, Qing Nie, and Chunhe Li. “Learning Stochastic Dynamics and Cell-Fate Landscapes from Single-Cell Snapshots via Optimal Transport.” Science Advances, 2026. [https://doi.org/10.1126/sciadv.aeb4205](https://doi.org/10.1126/sciadv.aeb4205).
