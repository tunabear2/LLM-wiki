---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Protify: A Benchmarking Platform Revealing Task Dependence and Homology Leakage in Protein Language Model Evaluation

## 기본 정보

- Citation key: `rafailidisProtifyBenchmarkingPlatform2026`
- Item type: preprint
- Authors: N. Rafailidis; L. P. Hallee; T. Peleg; C. Horger; L. Haviland; J. P. Gleghorn
- Source: bioRxiv v1, posted 2026-11-05 (not peer reviewed)
- Original: [DOI: 10.64898/2026.11.04.764373](https://doi.org/10.64898/2026.11.04.764373); [code](https://github.com/Gleghorn-Lab/Protify)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

Protify는 protein language model의 zero-shot·supervised·transfer 평가를 통일하고, model 순위가 task와 homology-controlled split에 크게 의존함을 대규모 비교로 보인다.

## 2. 연구 질문

서로 다른 dataset·split·probe 설정 때문에 비교하기 어려운 protein LM을 재현 가능한 하나의 평가 인터페이스에서 공정하게 비교할 수 있는가?

## 3. 데이터와 방법

35개 pretrained model과 61개 curated dataset을 지원하는 low-code platform을 만들었다. ProteinGym에서 23개 model을 zero-shot 평가하고, enzyme classification·GO·PPI·localization 등 32개 supervised task에서 model·probe를 비교했다. Optimal-pH task에서는 일반 split과 homology-controlled split을 대조했다.

## 4. 핵심 결과

- ProteinGym에서 DPLM-3B가 평가한 self-supervised encoder 중 가장 높은 평균 Spearman correlation을 보였다.
- 32개 supervised task에서는 14개 model이 적어도 한 dataset에서 1위를 차지해 보편적 최강 model이 없었다.
- Optimal-pH의 pooled-embedding probe는 일반 split에서 전문 모델을 넘었지만 homology-controlled split에서는 모두 거의 0의 R²로 붕괴했고, full-residue transformer probe만 R² 0.248을 회복했다.

## 5. 한계

세 seed만 사용해 작은 순위 차이의 통계적 power가 제한된다. 지원 model·dataset이 빠르게 변하고, 모든 task의 label quality와 biological novelty를 같은 수준으로 보장하지 않는다. Protein 결과를 RNA·cell FM에 직접 일반화할 수 없다.

## 6. 재현 또는 활용 포인트

Model 이름뿐 아니라 pooling/probe, split 생성, homology threshold, seed, HPO budget을 결과와 함께 고정한다. Random split 성능과 cluster/family-held-out 성능을 나란히 보고 run-to-run variability보다 작은 순위 차이는 해석하지 않는다.

## 7. Transcriptomics·신장이식 연구와의 연결

Gene·cell foundation model benchmark에도 donor·cohort leakage와 probe 선택이 model 차이보다 클 수 있음을 보여준다. Kidney rejection task에서는 donor-held-out·center-held-out split과 단순 linear baseline을 고정한 뒤 embedding의 추가 가치를 평가해야 한다.

## 8. 관련 키워드

- protein language model
- benchmark platform
- homology leakage
- transfer learning

## 9. Bibliography

Rafailidis, N., et al. “Protify: A Benchmarking Platform Revealing Task Dependence and Homology Leakage in Protein Language Model Evaluation.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.04.764373](https://doi.org/10.64898/2026.11.04.764373).
