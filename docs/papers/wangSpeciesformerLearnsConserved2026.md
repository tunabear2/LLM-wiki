---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-28'
tags:
- wiki/paper
---

# Speciesformer learns conserved cellular states for cross-species generative virtual cell modeling

## 기본 정보

- Citation key: `wangSpeciesformerLearnsConserved2026`
- Item type: preprint
- Authors: Jiacheng Wang; Jiaqi Dong; Guowei Li; Chao Fang; Liwei Liu; Xin Gao
- DOI: 10.64898/2026.09.22.752128
- URL: [Link](https://doi.org/10.64898/2026.09.22.752128)
- Source/date: bioRxiv v1, posted 2026-09-23

## 1. 한 줄 요약

Speciesformer는 11개 species·154개 tissue의 1억 3,100만 cell을 evolution-informed gene space에 정렬해 cross-species representation, text-conditioned state generation과 unseen-context perturbation prediction을 통합한다.

## 2. 왜 중요한가

Species-specific gene을 공통 evolutionary space에 매핑하고, cell·gene representation과 transcriptome–text 양방향 생성 및 intervention-conditioned transition을 하나의 generative architecture로 연결한다. 다만 cross-species 평균 성능이 특정 tissue·rare state·unseen perturbation에서의 신뢰성을 보장하지 않으므로 species, tissue와 intervention을 동시에 분리한 평가가 필요하다.

## 3. 내 연구에 연결할 점

Mouse ischemia-reperfusion·alloimmune model에서 얻은 perturbation을 human kidney transplant state로 옮기는 후보지만, human biopsy를 최종 test로 남겨야 한다. HLA처럼 species correspondence가 약한 gene, immunosuppression, viral infection과 donor-specific context에서는 uncertainty와 abstention을 함께 검증해야 한다.

## 4. Bibliography

Wang, Jiacheng, Jiaqi Dong, Guowei Li, Chao Fang, Liwei Liu, and Xin Gao. "Speciesformer learns conserved cellular states for cross-species generative virtual cell modeling." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.09.22.752128](https://doi.org/10.64898/2026.09.22.752128).
