---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# Cause-excluded Effect Evaluation: a framework for the faithful assessment of genetic perturbation target identification

## 기본 정보

- Citation key: `huCauseExcludedEffect2026`
- Item type: preprint
- Authors: J. Hu; X. Qi; L. Tian; J. Yan; N. Liu; X. Li
- DOI: 10.64898/2026.10.03.752923
- URL: [Link](https://doi.org/10.64898/2026.10.03.752923)
- Source/date: bioRxiv v1, posted 2026-10-11

## 1. 한 줄 요약

Cause-excluded Effect Evaluation은 test perturbation cell의 학습 노출과 target gene 자체의 expression change를 제거해, genetic perturbation target identification의 training·evaluation leakage를 분리한다.

## 2. 왜 중요한가

16개 single-cell perturbation dataset에서 leakage를 제거하면 단순 structure-based method가 복잡한 deep model을 일관되게 앞섰다. Virtual-cell 또는 perturbation FM의 inverse-target 성능을 평가할 때 self-effect와 split artefact를 실제 predictive signal로 오인하지 않게 한다.

## 3. 내 연구에 연결할 점

Rejection state를 되돌릴 target을 찾을 때 perturbation target별 holdout을 적용하고 target gene self-effect를 score에서 제외해야 한다. Renal cell-type과 donor가 함께 unseen인 설정도 별도로 두는 것이 안전하다.

## 4. Bibliography

Hu, J., X. Qi, L. Tian, J. Yan, N. Liu, and X. Li. "Cause-excluded Effect Evaluation: a framework for the faithful assessment of genetic perturbation target identification." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.03.752923](https://doi.org/10.64898/2026.10.03.752923).
