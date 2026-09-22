---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# Regulatory-prior-guided attention for unpaired single-cell RNA–ATAC integration

## 기본 정보

- Citation key: `chengRegulatoryPriorGuidedAttention2026`
- Item type: journalArticle
- Authors: Zhenglong Cheng; Jiao Zhang; Shixiong Zhang
- Journal: Bioinformatics
- DOI: 10.1093/bioinformatics/btag696
- PMID: 42758136
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42758136/); [DOI](https://doi.org/10.1093/bioinformatics/btag696); [code](https://github.com/zlCreator/scHPGT)
- Source/date: electronically published 2026-09-18
- 주 카테고리: scRNA-seq
- 교차 카테고리: Bio AI

## 1. 한 줄 요약

scHPGT는 regulatory-link prior로 RNA–ATAC cross-attention을 제한해 unpaired modality를 맞추면서도 partial-overlap 또는 condition-shift에서 고유한 cell state를 과도하게 합치지 않는다.

## 2. 연구 질문

Feature space와 sparsity가 다른 unpaired scRNA-seq·scATAC-seq를 통합할 때, 단순 distribution matching이 condition-specific state를 지우는 문제를 regulatory prior로 줄일 수 있는가?

## 3. 데이터와 방법

Modality-specific encoder, gene–peak regulatory link로 제한한 cross-modal Transformer와 domain-adversarial objective를 결합한다. PBMC3k, mouse spleen, CITE-seq/ASAP-seq PBMC와 PBMC10k에서 clustering, label transfer, modality alignment와 biological-structure preservation을 평가했다. Partial-overlap·condition-shift 실험과 attention-derived regulatory-link 해석도 수행했다.

## 4. 핵심 결과

시험한 benchmark에서 clustering agreement, label transfer와 biological structure preservation을 개선하면서 modality alignment를 유지했다. Partial overlap과 condition shift에서는 공유 population을 정렬하되 unmatched·condition-specific state를 부적절한 대응군으로 강제하지 않았다. Attention-derived link는 marker gene regulatory region과 cell-type-specific transcription-factor program을 회수했다.

## 5. 한계

평가는 주로 PBMC와 mouse spleen에 집중되고 질환·임상 outcome 검증은 없다. 결과가 regulatory prior의 coverage와 오류에 얼마나 민감한지, donor·protocol confounding이 강한 tissue에서 동일한지는 추가 검증이 필요하다. Attention link를 causal regulation으로 해석할 수는 없다.

## 6. 재현 또는 활용 포인트

- Regulatory-link source, genome build와 peak-to-gene mapping rule을 고정한다.
- Shared와 unmatched population을 분리한 simulation·real-data 평가를 포함한다.
- Modality mixing뿐 아니라 cell-state 보존, label transfer와 regulatory recovery를 함께 본다.
- Prior-free Transformer와 adversarial-only ablation으로 각 요소의 기여를 분리한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney allograft의 scRNA–scATAC 통합에서 rejection-specific immune·tubular state가 batch correction으로 사라지는 것을 막는 후보 방법이다. Donor와 rejection label이 confounded되지 않은 외부 cohort에서 state 보존과 patient-level outcome을 확인해야 한다.

## 8. 관련 키워드

- scRNA-seq
- scATAC-seq
- Multi-omics integration
- Regulatory prior
- Cross-modal Transformer

## 9. Bibliography

Cheng, Zhenglong, Jiao Zhang, and Shixiong Zhang. “Regulatory-Prior-Guided Attention Preserves Biological Structure during Unpaired Single-Cell RNA–ATAC Integration.” Bioinformatics (2026). [https://doi.org/10.1093/bioinformatics/btag696](https://doi.org/10.1093/bioinformatics/btag696).
