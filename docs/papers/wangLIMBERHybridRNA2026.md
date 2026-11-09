---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# LIMBER: A Hybrid RNA Foundation Model for Predicting and Understanding RNA Structure and Function

## 기본 정보

- Citation key: `wangLIMBERHybridRNA2026`
- Item type: preprint
- Authors: Z. Wang; Y. Qiu; Y. He; I. Thompson; H. Wang; A. Porter; A. Li
- Source: bioRxiv v1, posted 2026-11-01 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.28.762670](https://doi.org/10.64898/2026.10.28.762670); [code](https://github.com/ziyaow1010/LIMBER); [weights](https://huggingface.co/Ziyao1010/LIMBER)
- 주 카테고리: `Bio AI`
- 관련 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

LIMBER는 bidirectional attention과 selective state-space layer를 교차 배치해 4,050만 ncRNA sequence에서 학습하고, RNA 구조·진화·기능 정보가 architecture와 scale에 따라 어떻게 형성되는지도 함께 평가한다.

## 2. 연구 질문

RNA의 장거리 염기 상호작용과 순차 문맥을 한 모델에서 포착하면서 구조·기능 task 전반에 transfer 가능한 표현을 학습할 수 있는가?

## 3. 데이터와 방법

RNAcentral의 약 4,050만 ncRNA sequence로 hybrid Mamba–BERT 계열을 pretrain했다. bpRNA, SPOT-RNA, Rivas, ArchiveII, Rfam, nRC, RNAGym, DeepIRES, 5′UTR MPRA, RNA–small-molecule benchmark를 이용해 secondary structure, 분류, mutation fitness, translation-related task와 ligand interaction을 zero-shot 또는 fine-tuning으로 평가했다. 순수 BERT·Mamba와 model/data/compute scaling도 비교했다.

## 4. 핵심 결과

- Secondary-structure prediction과 ncRNA classification에서 강한 성능을 보였고 translation·small-molecule task로도 transfer되었다.
- Task-agnostic probing은 구조·진화·기능 정보가 layer별로 다르게 조직됨을 보였다.
- Model capacity, training duration, dataset size의 scaling 효과가 biological capability마다 동일하지 않았다.

## 5. 한계

Pretraining이 ncRNA에 집중되어 mRNA 전체와 조직·질환 맥락을 직접 모델링한 것은 아니다. 일부 downstream 방법의 local window는 장거리 RNA interaction을 과소표현할 수 있다. 대부분 공개 benchmark와 preprint 결과이므로 family-held-out·실험 검증이 더 필요하다.

## 6. 재현 또는 활용 포인트

공개 checkpoint와 pure-BERT/Mamba size-matched model을 같은 family-aware split에서 비교한다. Random split과 homolog-held-out split을 분리하고, layer probing과 downstream fine-tuning의 seed·training budget을 고정한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Allograft biopsy의 isoform, UTR, lncRNA, RNA-structure variant를 기능적으로 우선순위화할 후보이다. Sample-level rejection 예측에는 sequence embedding만 쓰지 말고 expression abundance, cell composition, clinical covariate와의 순증분 가치를 별도 검증해야 한다.

## 8. 관련 키워드

- RNA foundation model
- Mamba–Transformer hybrid
- RNA structure
- scaling analysis

## 9. Bibliography

Wang, Z., et al. “LIMBER: A Hybrid RNA Foundation Model for Predicting and Understanding RNA Structure and Function.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.10.28.762670](https://doi.org/10.64898/2026.10.28.762670).
