---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# Replicate libraries set the noise floor for cell-state claims in cross-sectional single-cell data

## 기본 정보

- Citation key: `razaReplicateLibrariesNoise2026`
- Item type: preprint
- Authors: Wasim Raza; Saba Mehmood; Carsten Enderlein; Fabrício Alves Barbosa Da Silva
- Source: bioRxiv v1, posted 2026-11-20 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.19.767931](https://doi.org/10.64898/2026.11.19.767931)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

조건당 하나의 library만 있는 cross-sectional scRNA-seq에서는 cell-level 검정이 library effect를 생물학적 state로 오인하므로, 조건 차이를 replicate-library 거리와 library-level permutation으로 평가해야 한다는 empirical audit다.

## 2. 연구 질문

Drug-tolerant cancer cell의 안정적 state 주장이 replicate library variation보다 충분히 큰가, 그리고 cell을 독립 표본으로 취급한 검정은 얼마나 오탐을 만드는가?

## 3. 데이터와 방법

GSE150949의 11개 10x library와 GSE149383 Drop-seq 자료를 분석하고 condition contrast와 same-condition replicate 거리의 비율을 정의했다. Simulated library effect에서 split-half, cell-level test, Harmony 후 test와 whole-library label을 바꾸는 exact permutation을 비교했다.

## 4. 핵심 결과

- True null simulation에서 single-library·split-half 검정은 99–100%를 기각했고, structured library effect에서 Harmony 후 cell-level test도 12–32% 오탐을 냈다.
- 조건당 4개 library에서는 library-level permutation이 모든 설정에서 false positive를 3–5%로 유지했다.
- 실제 10x 자료에서 same-condition replicate도 59–93% 정확도로 분리됐지만 주요 drug-time contrast는 replicate 거리의 4.5–51배였다.

## 5. 한계

새 실험 없이 두 공개 PC9 cell-line dataset을 재분석했으며, replicate biology와 technical effect를 분리하지 않는다. Library가 4개 미만이면 exact permutation power가 제한되고, 제안한 거리 비율의 일반 기준값은 조직·platform별 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Cell 수가 아니라 biological library를 실험 단위로 두고 조건당 최소 4개 replicate 또는 sample hashing을 고려한다. Condition effect를 replicate distance의 배수로 보고하며 donor/library-level permutation과 pseudobulk를 함께 실행한다.

## 7. Transcriptomics·신장이식 연구와의 연결

환자·biopsy가 적고 cell 수만 많은 rejection scRNA-seq에서 가장 중요한 설계 경고다. 환자당 하나의 library를 cell-level P-value로 검정하지 말고 donor/center 단위 replication, pseudobulk와 library noise floor로 rejection state를 확인해야 한다.

## 8. 관련 키워드

- biological replication
- library effect
- pseudoreplication
- single-cell statistics
- cancer cell state

## 9. Bibliography

Raza, Wasim, et al. “Replicate Libraries Set the Noise Floor for Cell-State Claims in Cross-Sectional Single-Cell Data: An Empirical Audit in Drug-Tolerant EGFR-Mutant PC9 Cells.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.19.767931](https://doi.org/10.64898/2026.11.19.767931).
