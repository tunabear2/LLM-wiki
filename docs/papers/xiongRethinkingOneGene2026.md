---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Rethinking One Gene, One Token: Transcriptome-Aware Tokenization for Single-Cell Foundation Models

## 기본 정보

- Citation key: `xiongRethinkingOneGene2026`
- Item type: preprint
- Authors: Jiaqi Xiong; Jiaying Li; Yu Zheng; Xiang Zhou; Ziteng Wang; Xinting Hu; Jiaxin Qi
- arXiv: 2611.05410
- URL: [Link](https://arxiv.org/abs/2611.05410)
- Source/date: arXiv v1, submitted 2026-10-21; announced 2026-11

## 1. 한 줄 요약

scTAT은 cell마다 함께 발현되는 gene set과 개별 gene이 token 자리를 경쟁하게 해, 절반의 token budget으로 one-gene-one-token scFM과 비슷한 annotation 성능을 낸다.

## 2. 왜 중요한가

고정 gene grouping 대신 pretraining corpus에서 반복되는 gene set vocabulary와 cell-specific tokenizer를 결합하고, gene-level reconstruction은 유지한다. 동일 gene coverage에서 Transformer 연산량도 거의 절반으로 줄여 scFM의 입력 표현과 계산비용을 함께 다룬다.

## 3. 내 연구에 연결할 점

대규모 kidney-transplant atlas의 추론비용을 줄일 후보지만, 압축 뒤 HLA·IFN·cytotoxicity·endothelial injury program과 희귀 rejection state가 보존되는지 donor-level split으로 확인해야 한다.

## 4. Bibliography

Xiong, Jiaqi, Jiaying Li, Yu Zheng, Xiang Zhou, Ziteng Wang, Xinting Hu, and Jiaxin Qi. "Rethinking One Gene, One Token: Transcriptome-Aware Tokenization for Single-Cell Foundation Models." _arXiv_, 2026. [https://arxiv.org/abs/2611.05410](https://arxiv.org/abs/2611.05410).
