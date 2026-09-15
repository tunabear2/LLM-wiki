---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# Reconstructing signaling histories of single cells via perturbation screens and transfer learning

## 기본 정보

- Citation key: `hutchinsReconstructingSignalingHistories2026`
- Item type: journalArticle
- Authors: Nicholas T. Hutchins; Miram Meziane; Claire Lu; Maisam Mitalipova; David S. Fischer; Pulin Li
- Journal: Nature Methods
- DOI: 10.1038/s41592-026-03213-8
- PMID: 42711495
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42711495/); [DOI](https://doi.org/10.1038/s41592-026-03213-8)
- Source/date: published 2026-09-08; PubMed indexed 2026-09-09 13:24 KST
- 주 카테고리: scRNA-seq

## 1. 한 줄 요약

IRIS는 in-vitro signaling perturbation atlas에서 transferable response signature를 학습해, in-vivo single-cell transcriptome에서 현재 신호 활성뿐 아니라 과거의 signaling exposure까지 복원한다.

## 2. 연구 질문

세포가 현재 보이는 발현 상태만으로 직접 관측하기 어려운 signaling activity와 노출 이력을, 대규모 perturbation response를 이용해 세포 유형과 생물학적 맥락을 넘어 추정할 수 있는가?

## 3. 데이터와 방법

Human pluripotent stem cell에 다양한 signaling perturbation을 가해 고처리량 atlas를 만들고, transferable signaling response signature를 학습하는 neural-network model IRIS를 훈련했다. 이후 mouse embryo single-cell atlas에 적용해 세포별 signaling activity와 history를 추정하고, 서로 다른 developmental lineage에서 시간적·조합적 신호 사용 양상을 분석했다.

## 4. 핵심 결과

IRIS는 in-vivo cell type의 signaling activity와 history를 높은 정확도와 시간 해상도로 추정했다고 보고했다. Mouse embryo에서 combinatorial signaling code의 전반적 사용 양상을 찾고, 생물학적으로 의미 있는 heterogeneity와 여러 lineage의 과거 신호 노출을 복원했다. 서로 다른 세포 유형이 공유하는 보존된 signaling response signature를 이용할 수 있음을 보여줬다.

## 5. 한계

학습 atlas는 human pluripotent stem cell, 주요 적용 검증은 mouse embryo이므로 성인 인간 조직과 염증성 질환으로의 일반화는 추가 검증이 필요하다. 추정된 history는 직접 측정한 longitudinal lineage record가 아니라 transcriptomic signature 기반 inference다. 초록에는 donor·기관 간 holdout이나 신장이식 조직에서의 평가가 제시되지 않는다.

## 6. 재현 또는 활용 포인트

- Perturbation, dose와 sampling time을 명시한 reference atlas와 독립 in-vivo dataset을 분리한다.
- Held-out signal 조합과 cell type에서 현재 activity 및 history reconstruction을 각각 평가한다.
- 알려진 developmental 또는 experimental exposure와 추정 이력의 시간 순서를 대조한다.
- 새로운 조직에 적용할 때 expression depth, cell-state composition과 species shift를 통제한다.
- 코드: [Pulin-Li-Lab/IRIS-signaling-inference](https://github.com/Pulin-Li-Lab/IRIS-signaling-inference)

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection biopsy에서 IFN, TNF, TGF-β 등 현재 pathway score와 이전 cytokine exposure의 흔적을 분리하고, 면역·내피·세뇨관 세포가 거친 signaling history를 가설화하는 데 유용하다. 실제 활용에는 이식 전후 longitudinal sample, donor-level split과 독립 기관 cohort에서의 검증이 필요하다.

## 8. 관련 키워드

- scRNA-seq
- Perturbation atlas
- Transfer learning
- Signaling history
- Cell-state inference
- Developmental lineage

## 9. Bibliography

Hutchins, Nicholas T., Miram Meziane, Claire Lu, Maisam Mitalipova, David S. Fischer, and Pulin Li. “Reconstructing Signaling Histories of Single Cells via Perturbation Screens and Transfer Learning.” Nature Methods, 2026. [https://doi.org/10.1038/s41592-026-03213-8](https://doi.org/10.1038/s41592-026-03213-8).
