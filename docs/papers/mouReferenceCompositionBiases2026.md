---
type: paper
status: reference
rag_priority: high
updated: '2026-10-05'
tags:
- wiki/paper
---

# Reference Composition Biases Automated Cell Annotation and Obscures Biological Signals in Xenotransplantation Single-cell Atlases

## 기본 정보

- Citation key: `mouReferenceCompositionBiases2026`
- Item type: journal article
- Authors: Lisha Mou; Ying Lu; Zijing Wu; Qishan Zhang; Zuhui Pu
- DOI: 10.1111/xen.70171
- PMID: 42817914
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42817914/)
- Source/date: Xenotransplantation 33(5), 2026-09; PubMed indexed 2026-10-01

## 1. 한 줄 요약

돼지 kidney xenograft single-cell atlas에서 reference composition이 TranscriptFormer와 다른 annotation 방법을 collecting-duct label 쪽으로 붕괴시켜 distal tubule과 endothelial IFN signal을 가릴 수 있음을 보인다.

## 2. 왜 중요한가

다섯 dataset의 254,245 cell을 통합해 foundation model TranscriptFormer, Biomni와 전통 방법을 비교했다. Empirical reference composition을 쓰면 target-native TAL과 DCT cell의 약 97%가 collecting duct로 재할당됐고, 원래 보이던 endothelial interferon-stimulated program도 가려졌다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection annotation에서 가장 직접적인 경고다. Reference cell-type 비율을 바꾼 sensitivity analysis, target-native marker 검토, abstention과 compartment-level signal 보존을 함께 보고해 rare tubular state와 endothelial rejection program이 label transfer에 지워지지 않는지 확인해야 한다.

## 4. Bibliography

Mou, Lisha, Ying Lu, Zijing Wu, Qishan Zhang, and Zuhui Pu. "Reference Composition Biases Automated Cell Annotation and Obscures Biological Signals in Xenotransplantation Single-cell Atlases." _Xenotransplantation_ 33, no. 5 (2026). [https://doi.org/10.1111/xen.70171](https://doi.org/10.1111/xen.70171).
