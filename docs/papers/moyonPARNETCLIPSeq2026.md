---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# PARNET: a CLIP-seq-based foundation model for RNA sequence representation learning

## 기본 정보

- Citation key: moyonPARNETCLIPSeq2026
- Item type: bioRxiv preprint
- Authors: Lambert Moyon; Andreina Tirabassi; Artem Baranowskii; Charlotte Capitanchik; Klara Kuret Hodnik; Leo Wilkinson; Shubankar Londhe; Gabrijela Dumbovic; Julien Gagneur; Jernej Ule; Marc Horlacher; Annalisa Marsico
- DOI: 10.64898/2026.08.08.743506
- URL: [bioRxiv](https://doi.org/10.64898/2026.08.08.743506)
- Source/date: bioRxiv v1 posted 2026-08-13, indexed 2026-08-17
- 주 카테고리: Bio AI
- 교차 카테고리: Transcriptomics / Platform; DNA-seq / Variant Analysis

## 1. 한 줄 요약

PARNET은 다수의 eCLIP 실험을 염기 단위로 공동 학습해 RBP 결합과 RNA 서열 기능을 함께 표현하는 21M-parameter RNA foundation model이다.

## 2. 연구 질문

개별 RBP마다 별도 모델을 만드는 대신 다양한 CLIP-seq 신호를 공동 학습하면, 범용 RNA representation과 splice variant 해석 성능을 동시에 높일 수 있는가?

## 3. 데이터와 방법

ENCODE의 223개 eCLIP 실험과 150개 RNA-binding protein을 사용해 600-nt RNA 서열에서 염기별 결합 신호를 multi-task로 학습했다. Frozen embedding을 RNA 분류, 번역 효율, splicing·intron-retention 과제에 적용하고 단일 과제 RBPNet 및 더 큰 RNA sequence model들과 비교했다.

## 4. 핵심 결과

저자 보고 기준 RBPNet 대비 평균 Pearson correlation은 약 35%, Spearman correlation은 약 19% 향상됐다. Frozen representation도 여러 downstream 과제에서 대형 모델과 경쟁했으며 MutSpliceDB의 splice-altering variant 분류에서 AUPRC 0.801을 보고했다.

## 5. 한계

학습 자료가 약 150개 RBP와 K562·HepG2 두 세포주에 편중됐다. RNA 2차 구조와 변형을 직접 모델링하지 않으며, 긴 context와 모델 용량 차이도 성능 향상에 기여하므로 multi-task objective만의 효과로 단정할 수 없다. Preprint 결과이므로 독립 검증이 필요하다.

## 6. 재현 또는 활용 포인트

- 모델 코드: [marsico-lab/parnet](https://github.com/marsico-lab/parnet)
- 논문 분석 코드: [marsico-lab/parnet--paper](https://github.com/marsico-lab/parnet--paper)
- Renal·immune RBP에 대한 zero-shot 결과와 tissue-specific fine-tuning 결과를 나누어 평가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

거부반응 조직의 RBP program, intron retention, alternative splicing과 비암호 splice variant의 우선순위화에 활용할 수 있다. 다만 renal·immune context의 CLIP-seq가 부족하므로 발현 변화나 variant effect를 곧바로 기전으로 해석하면 안 된다.

## 8. 관련 키워드

- Bio AI
- RNA foundation model
- eCLIP / CLIP-seq
- RNA-binding protein
- Splicing
- Variant effect

## 9. Bibliography

Moyon, Lambert, et al. “PARNET: A CLIP-seq-based Foundation Model for RNA Sequence Representation Learning.” bioRxiv, 2026. [https://doi.org/10.64898/2026.08.08.743506](https://doi.org/10.64898/2026.08.08.743506).
