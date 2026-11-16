---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# ProClust: Statistical Significance of Clusters in Single-Cell Transcriptomics

## 기본 정보

- Citation key: `qianProClustStatisticalSignificance2026`
- Item type: preprint
- Authors: Haina Qian; Haoze Wu; Yifan Dai; Guanao Yan; Yufeng Liu
- Source: bioRxiv v1, posted 2026-11-10 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.08.764985](https://doi.org/10.64898/2026.11.08.764985)
- Code: [Anonym027/ProClust](https://github.com/Anonym027/ProClust)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

ProClust는 log-concave single-cluster null과 projection 기반 p-value로 초기 overclustering을 검정하고 근거가 부족한 cluster를 병합한다.

## 2. 연구 질문

최종 cluster 수를 미리 정하지 않고 scRNA-seq의 과분할을 통계적으로 검정해 지지되는 세포 이질성만 남길 수 있는가?

## 3. 데이터와 방법

하나의 cluster를 log-concave distribution으로 정의하고 여러 projection에서 clustering uncertainty와 p-value를 계산한다. Null을 기각할 증거가 부족한 cluster pair를 병합한다. Parametric simulation, PBMC-based semi-synthetic data, Human Lung Cell Atlas, Tabula Muris, Hydra에서 평가했다.

## 4. 핵심 결과

- Single-population null simulation에서 거짓 subdivision을 피했다.
- True population 수가 달라지는 simulation에서 underlying structure를 일관되게 복원했다.
- 세 실제 atlas에서 reference annotation과 대체로 일치하면서 지지되는 substructure는 보존하고 근거가 부족한 group은 병합했다.

## 5. 한계

Single-cluster null의 log-concavity 가정이 복잡한 trajectory나 continuous state에 맞지 않을 수 있다. 실제 atlas annotation은 완전한 ground truth가 아니며 donor·batch 구조에서 p-value calibration을 별도로 확인해야 한다.

## 6. 재현 또는 활용 포인트

Initial clustering algorithm·resolution, projection 수, multiple-testing correction, minimum cluster size를 기록한다. Donor-aware null simulation과 label permutation에서 type-I error를 확인하고 known marker·orthogonal assay와 함께 해석한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Allograft biopsy에서 작은 rejection-associated cluster를 발견할 때 overclustering artifact와 실제 rare state를 구분하는 보조 검정이 될 수 있다. Donor imbalance와 injury continuum을 반영한 simulation에서 먼저 calibration해야 한다.

## 8. 관련 키워드

- clustering significance
- overclustering
- scRNA-seq
- statistical testing

## 9. Bibliography

Qian, Hong, et al. “ProClust provides reliable statistical significance of clusters for single-cell transcriptomic data.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.08.764985](https://doi.org/10.64898/2026.11.08.764985).
