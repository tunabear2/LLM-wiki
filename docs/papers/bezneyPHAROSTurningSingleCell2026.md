---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-14'
tags:
- wiki/paper
---

# PHAROS: turning single-cell perturbation models into target-directed drug-combination screens

## 기본 정보

- Citation key: `bezneyPHAROSTurningSingleCell2026`
- Item type: preprint
- Authors: Jon Bezney; Carlo Ruggeri; Federico Borra; Lei S. Qi; Francesca Buffa; Lars M. Steinmetz
- DOI: 10.64898/2026.09.08.749477
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.09.08.749477v1)
- Source/date: bioRxiv v1, posted 2026-09-10

## 1. 한 줄 요약

PHAROS는 pretrained STATE single-cell perturbation model의 one-drug prediction을 연결해 목표 cell state로 이동시키는 drug combination을 재학습 없이 탐색한다.

## 2. 왜 중요한가

두 independent combinatorial perturbation dataset에서 학습에 포함되거나 포함되지 않은 cell line의 exact 또는 mechanism-matched two-drug response를 회수했다. Ranking은 단일 약물 효과, 단순 additive effect, 공통 mechanism만으로 설명되지 않았고, 환자 종양 탐색에서는 FDA-approved regimen을 우선순위화하면서 입력이 model support 밖임을 명시했다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection state를 quiescent immune/endothelial/tubular target으로 전환하는 면역억제제 조합 후보를 생성하는 데 응용할 수 있다. 다만 transplant biopsy는 원 모델의 분포 밖일 가능성이 크므로 drug–drug toxicity, donor-level validation, 실제 combination perturbation과 immune/tissue-specific objective를 별도로 검증해야 한다.

## 4. Bibliography

Bezney, Jon, Carlo Ruggeri, Federico Borra, Lei S. Qi, Francesca Buffa, and Lars M. Steinmetz. "PHAROS: turning single-cell perturbation models into target-directed drug-combination screens." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.09.08.749477](https://doi.org/10.64898/2026.09.08.749477).
