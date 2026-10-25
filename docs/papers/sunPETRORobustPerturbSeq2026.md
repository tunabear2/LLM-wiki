---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# PETRO Enables Robust Estimation of On-Target Perturbation Effects in Perturb-seq

## 기본 정보

- Citation key: `sunPETRORobustPerturbSeq2026`
- Item type: bioRxiv preprint
- Authors: Z. Sun; H. Kang; S. Keles
- Source: bioRxiv v1, posted 2026-10-21 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.15.759256](https://doi.org/10.64898/2026.10.15.759256); [code](https://github.com/zsun263/PETRO)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

PETRO는 target당 guide 다수가 같은 on-target effect를 지지한다는 조건에서 guide별 arbitrary off-target effect를 허용해 Perturb-seq target-level effect를 robust하게 추정한다.

## 2. 연구 질문

효율적인 perturbation에서도 남는 guide-specific off-target effect가 pooled target estimate를 왜곡할 때 replicate-guide agreement로 on-target effect를 복원할 수 있는가?

## 3. 데이터와 방법

Outcome별 guide의 미지 소수가 invalid일 수 있는 majority-supported estimator를 만들고 common-effect와 proportional extension을 제시했다. CRISPRa·CRISPRi dataset, simulation, cortical Perturb-seq의 ZNF219·ARX·NR2E1 pathway 결과에서 pooling과 비교했다.

## 4. 핵심 결과

- Published guide filter 뒤에도 sequence-associated off-target bias가 남았고 한 CRISPRa dataset에서는 거의 두 배가 됐다.
- Off-target이 없을 때 pooling에 가까운 power를 유지했고, off-target이 있으면 cell 수가 늘어도 남는 pooling bias를 줄였다.
- ZNF219의 여러 pathway enrichment가 한 guide에 의존했지만 ARX·NR2E1의 concordant signal은 majority aggregation에서도 유지됐다.

## 5. 한계

절반 이상 guide가 invalid이거나 invalid guide끼리 같은 방향이면 실패할 수 있다. Small off-target effect와 sampling noise를 구분하기 어렵고 common/proportional on-target model이 모든 target–outcome 관계를 표현하지는 못한다.

## 6. 재현 또는 활용 포인트

Code가 공개된다. 최대 k개 invalid guide를 허용하려면 최소 2k+1 guide가 필요하므로 target당 홀수 guide 설계를 고려하고, guide-level estimate와 uncertainty를 보존한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection-associated TF·cytokine target을 Perturb-seq로 검증할 때 한 guide의 phenotype을 target effect로 오인하지 않게 한다. Guide consensus와 donor/cell-state별 heterogeneity를 함께 확인해야 한다.

## 8. 관련 키워드

- scRNA-seq
- Perturb-seq
- off-target effect
- robust estimation

## 9. Bibliography

Sun, Z., H. Kang, and S. Keles. “PETRO Enables Robust Estimation of On-Target Perturbation Effects in Perturb-seq.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.15.759256](https://doi.org/10.64898/2026.10.15.759256).
