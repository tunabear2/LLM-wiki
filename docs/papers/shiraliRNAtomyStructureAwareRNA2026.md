---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# RNAtomy: A Structure-Aware RNA Foundation Model for Transferable Structural and Functional Representations

## 기본 정보

- Citation key: `shiraliRNAtomyStructureAwareRNA2026`
- Item type: preprint
- Authors: Azam Shirali; Ishaan Garg; Andrey Vasilyev; Pavitra Soni; Parshatd Govindasamy; Kalai Mathee; Prem Chapagain; Giri Narasimhan
- Source: bioRxiv v1, posted 2026-11-12 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.10.765792](https://doi.org/10.64898/2026.11.10.765792)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

RNAtomy는 RNA의 pairwise 3D geometry와 residue-level conformation을 함께 복원하도록 학습해 구조·기능 task로 전이하는 hybrid Mamba–Transformer foundation model이다.

## 2. 연구 질문

Sequence나 secondary structure 중심 RNA model을 넘어 3D geometry와 local conformation을 self-supervised pretraining에 통합하면 작은 학습 집합에서도 전이 가능한 RNA 표현을 얻을 수 있는가?

## 3. 데이터와 방법

Pairwise geometry와 residue descriptor를 joint masked reconstruction하고, Mamba block으로 global context를 전달하면서 shifted-window attention으로 pairwise map의 local interaction을 보완한다. Axis-aware FiLM으로 nucleotide conformation을 geometry map의 row·column 축에 주입했다. Nucleotide, nucleotide-pair, RNA 수준의 구조·기능 7개 task에서 기존 RNA foundation model과 task-specific method를 비교했다.

## 4. 핵심 결과

- Contact와 long-range base-pair prediction에서 비교 RNA foundation model 및 task-specific method보다 높은 성능을 보고했다.
- 구조 pretraining과 다른 interaction task에도 표현이 전이됐다.
- Translation 관련 예측과 regulatory-element identification에서도 우수한 결과를 보고했으며, 비교 foundation model보다 작은 pretraining set을 사용했다.

## 5. 한계

Preprint이며 초록에서 독립적인 wet-lab 검증이나 임상 cohort 검증은 제시되지 않았다. 평가가 구조·기능 예측 task 중심이므로 transcript abundance, 조직 상태, 질환 outcome으로의 전이는 별도 검증이 필요하다.

## 6. 재현 또는 활용 포인트

RNA 구조 source, train/test 구조 유사도, sequence-identity split, geometry descriptor와 masking ratio를 기록한다. Long-range contact와 functional task에서 homology leakage를 차단한 split으로 sequence-only·secondary-structure baseline과 비교해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

이식 후 염증에서 변하는 RNA 구조·translation·regulatory element 후보를 transcript abundance 외의 축으로 우선순위화할 수 있다. 다만 biopsy RNA-seq에 직접 적용하기보다 isoform·RBP·translation assay와 연결되는 후보 생성용으로 보는 것이 안전하다.

## 8. 관련 키워드

- RNA foundation model
- RNA 3D geometry
- Mamba–Transformer
- representation learning

## 9. Bibliography

Shirali, Ali, et al. “RNAtomy: A Structure-Aware RNA Foundation Model for Transferable Structural and Functional Representations.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.10.765792](https://doi.org/10.64898/2026.11.10.765792).
