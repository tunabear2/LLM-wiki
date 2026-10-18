---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# Constructed Negatives Shape the Evaluation of Sequence-Based Protein–Protein Interaction Models

## 기본 정보

- Citation key: `durandConstructedNegativesShape2026`
- Item type: bioRxiv preprint
- Authors: Enzo Durand; Sergei Grudinin; Béatrice Durand; Élodie Laine
- Source: bioRxiv v1, posted 2026-10-15 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.08.757593](https://doi.org/10.64898/2026.10.08.757593); [code and evaluation data](https://github.com/hanzopgp/PPIShiftSubmission)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

PPI 예측에서 관측되지 않은 protein pair를 음성으로 만드는 방식만 바꿔도 AUPRC와 모델 순위가 크게 달라져, protein language model benchmark의 음성 구성 자체가 핵심 실험변수임을 보였다.

## 2. 연구 질문

실험적으로 확인된 non-interaction이 드문 상황에서 constructed negative의 선택이 sequence/pLM 기반 PPI 모델 비교를 얼마나 왜곡하는가?

## 3. 데이터와 방법

Positive, protein-disjoint split, class balance와 model selection을 고정하고 여섯 음성 구성과 네 sequence model을 factorial하게 비교했다. 세 모델은 pLM representation을 사용했다. Y2H assay non-detection, IntAct curated negative, BioGRID·STRING positive 등 외부 source와 partner-shuffling shortcut control을 사용하고 세 seed로 학습 변동을 측정했다.

## 4. 핵심 결과

- Test negative 구성만 바꿔 AUPRC가 최대 0.26 이동했고 최고 모델도 달라졌다.
- pLM 공간에서 true partner와 매칭한 음성에서는 pLM 기반 모델들이 거의 chance 수준으로 떨어졌다.
- Constructed training negative는 외부 평가 120개 비교 중 108개에서 uniform sampling보다 나빴고, 손실은 AUROC 0.23까지였다.

## 5. 한계

512-residue 공통 subset은 원래 Gold training positive의 16.3%만 보존했다. 네 모델과 ESM-2 계열 한 pLM family만 평가했으며, 어떤 음성도 실제 non-interaction을 증명하지 못한다. 외부 source에는 sequence/pair overlap이 있어 엄격한 OOD 검증으로 해석할 수 없다.

## 6. 재현 또는 활용 포인트

Pipeline, 음성 생성법, seed·checkpoint hash와 figure-level 결과가 공개된다. 음성 구성을 독립 변수로 두고 representation-matched negative, pair-shuffle, assay/curated external data를 함께 보고하는 설계가 재사용 가능하다.

## 7. Transcriptomics·신장이식 연구와의 연결

Ligand–receptor, donor–recipient interaction, drug-response pair model에서 무작위 non-pair를 진짜 음성처럼 쓰는 위험을 직접 경고한다. 이식 transcriptomics의 interaction benchmark도 hard negative와 assay-supported negative를 분리해야 한다.

## 8. 관련 키워드

- Bio AI
- protein language model
- protein–protein interaction
- benchmark design

## 9. Bibliography

Durand, Enzo, et al. “Constructed Negatives Shape the Evaluation of Sequence-Based Protein–Protein Interaction Models.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.08.757593](https://doi.org/10.64898/2026.10.08.757593).
