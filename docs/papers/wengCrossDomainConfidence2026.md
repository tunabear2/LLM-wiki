---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-14'
tags:
- wiki/paper
---

# Cross-domain confidence reliability and remappability of frozen single-cell representations

## 기본 정보

- Citation key: `wengCrossDomainConfidence2026`
- Item type: preprint
- Authors: Guangzheng Weng; Danfei Zhu; Yufei Zhao; Patrick C. Martin; Hyobin Kim; Junghyun Jung; Gi-Hoon Nam; Kyoung Jae Won
- DOI: 10.64898/2026.08.31.748446
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.08.31.748446v1)
- Source/date: bioRxiv v1, posted 2026-09-04; indexed in the 2026-09-08 watch window

## 1. 한 줄 요약

Frozen single-cell foundation model의 cell-type classifier에서 maximum softmax probability는 cross-domain confidence를 제대로 나타내지 못하며, 소량의 target-domain label을 이용한 재보정이 필요하다.

## 2. 왜 중요한가

Source와 target 사이의 confidence gap을 rank-ordering error와 systemic probability drift로 분해해, raw probability cutoff만으로 자동 판정을 수락하는 방식이 기술·생물학적 shift에서 안전하지 않음을 보였다. Target-specific recalibration은 신뢰도를 높이지만 manual review 대상으로 보내는 cell 수를 늘리는 trade-off가 있다.

## 3. 내 연구에 연결할 점

Kidney transplant biopsy의 rejection cell-state annotation에서는 외부 atlas에서 얻은 scFM classifier의 확률을 그대로 쓰지 말고, center·protocol·disease state를 대표하는 소규모 local label로 calibration해야 한다. 희귀 immune/endothelial state는 abstention과 전문가 검토율까지 함께 보고하는 것이 적절하다.

## 4. Bibliography

Weng, Guangzheng, Danfei Zhu, Yufei Zhao, Patrick C. Martin, Hyobin Kim, Junghyun Jung, Gi-Hoon Nam, and Kyoung Jae Won. "Cross-domain confidence reliability and remappability of frozen single-cell representations." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.08.31.748446](https://doi.org/10.64898/2026.08.31.748446).
