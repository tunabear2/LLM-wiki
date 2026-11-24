---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# Domain-informed effector gene assignment exposes training-data dependence of drug target prioritisation from GWAS

## 기본 정보

- Citation key: `kohleickDomainInformedEffector2026`
- Item type: preprint
- Authors: Leonhard Kohleick; Kurt Herzog; Carl Beuchel; Martijn Zoodsma; Claudia Langenberg; Benjamin Wild; Maik Pietzner
- Source: bioRxiv v1, posted 2026-11-18 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.17.766419](https://doi.org/10.64898/2026.11.17.766419)
- 주 카테고리: `GWAS`

## 1. 한 줄 요약

DEFA는 GWAS effector-gene model을 서로 다른 biological-domain curation으로 각각 학습해, 정답 집합의 가정이 gene·drug-target 우선순위에 어떻게 전파되는지 숨기지 않고 보고한다.

## 2. 연구 질문

대규모 실험 ground truth가 없는 GWAS locus-to-gene 문제에서 하나의 curated positive set으로 학습한 성능이 다른 생물학적 domain으로 전이되는가?

## 3. 데이터와 방법

Trans-pQTL ligand–receptor/complex, metabolite allelic series 등 세 독립 evaluation set을 만들고 다섯 domain-informed model을 학습했다. 여섯 common disease의 lead variant를 annotation하고 distance weighting, effector assignment overlap과 340개 approved drug target 회수를 Open Targets L2G 등과 비교했다.

## 4. 핵심 결과

- 같은 방법의 AUPRC가 evaluation domain에 따라 0.91에서 0.46까지 떨어져 성능 전이가 제한됐다.
- 다섯 model의 effector-gene assignment overlap은 17.1–31.8%에 불과했고 차이는 주로 variant–gene distance 가중치에서 왔다.
- 모든 model의 합집합은 approved drug target 52.1%를 회수했지만 score 평균이나 joint training은 각각 38.8%, 36.5%에 그쳤다.

## 5. 한계

평가 집합도 완전한 실험 ground truth가 아니라 pQTL·metabolite·curation 가정을 가진 quasi-positive다. 여섯 질환과 common lead variant 중심이며 rare variant, ancestry별 LD, tissue-specific perturbation의 검증은 제한적이다. 분석 전체 자료는 final publication 시 공개 예정이라고 명시됐다.

## 6. 재현 또는 활용 포인트

Positive-set 출처, distance distribution과 disease knowledge overlap을 분리해 기록한다. 단일 통합 score보다 domain별 assignment와 disagreement를 보존하고 eQTL colocalization, chromatin contact, perturbation evidence로 후보를 교차 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection·graft-outcome GWAS를 biopsy expression과 연결할 때 eQTL, protein, druggability 중심 training set이 서로 다른 gene을 고를 수 있음을 경고한다. Immune·kidney cell-state evidence별 model을 유지하고 합의와 불일치를 후속 실험 우선순위로 활용할 수 있다.

## 8. 관련 키워드

- GWAS interpretation
- effector gene
- drug target prioritization
- benchmark leakage
- domain shift

## 9. Bibliography

Kohleick, Leonhard, et al. “Domain-Informed Effector Gene Assignment Exposes Training-Data Dependence of Drug Target Prioritisation from GWAS.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.17.766419](https://doi.org/10.64898/2026.11.17.766419).
