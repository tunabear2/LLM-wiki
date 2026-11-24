---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# FULL-seq reveals isoform-specific regulatory architecture in single cells

## 기본 정보

- Citation key: `wangFULLSeqIsoformSpecific2026`
- Item type: preprint
- Authors: Ming Wang; Jiajia Qi; Francesco Monticolo; Xue Chen; Ailin Qiao; Liyuan Zou; Jing Shu
- Source: bioRxiv v1, posted 2026-11-18 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.17.767299](https://doi.org/10.64898/2026.11.17.767299)
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

FULL-seq은 같은 세포에서 chromatin accessibility와 최대 15-kb mRNA의 full-length transcript coverage를 함께 얻어 promoter–alternative first exon 조절 관계를 직접 연결하는 single-cell multiome platform이다.

## 2. 연구 질문

Gene-level RNA–ATAC multiome이 가리는 alternative promoter·first-exon 사용을 단일세포에서 직접 측정하고 기능적 phenotype과 연결할 수 있는가?

## 3. 데이터와 방법

동일 세포의 accessible chromatin과 full-length RNA를 공동 측정해 alternative first exon(AFE)별 promoter·TF program을 추론했다. Human cancer cell에서 metastasis-associated AFE를 찾고 독립 colorectal cancer cell-line 자료와 liver-metastasis patient cohort에서 재현한 뒤 CALB1 AFE를 CRISPRi로 억제해 migration 변화를 평가했다.

## 4. 핵심 결과

- RNA와 accessibility 양쪽에서 높은 sensitivity를 유지하며 최대 15-kb transcript의 exon-level coverage를 보고했다.
- 같은 gene의 서로 다른 AFE가 별도의 TF·regulatory architecture를 가지며 gene-level annotation이 이 관계를 가릴 수 있음을 보였다.
- Metastasis-associated CALB1 AFE는 독립자료에서 관찰됐고 CRISPRi 억제 시 colorectal-cancer cell migration이 감소했다.

## 5. 한계

Preprint의 제한된 cell system과 선택된 validation에 기반하며 다양한 조직·저품질 임상 specimen에서 throughput, doublet, isoform accuracy가 검증되지 않았다. AFE mapping은 reference annotation과 read coverage에 의존하고 long transcript의 완전성은 orthogonal long-read 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Cell당 gene·fragment·full-length transcript 수, TSS/AFE assignment, RNA–ATAC pairing rate와 doublet을 보고한다. Gene-level baseline과 isoform-aware model을 비교하고 candidate AFE는 targeted long-read, CAGE 또는 CRISPRi로 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection-associated gene의 총량이 같아도 immune·tubular cell에서 promoter·first-exon 사용이 달라질 수 있다. Fresh biopsy에서 적용 가능성과 RNA 품질을 확인한 뒤 isoform-aware regulatory link를 bulk/long-read 자료와 교차 검증할 수 있다.

## 8. 관련 키워드

- full-length scRNA-seq
- scATAC-seq
- alternative first exon
- single-cell multiome
- isoform regulation

## 9. Bibliography

Wang, Ming, et al. “FULL-seq Reveals Isoform-Specific Regulatory Architecture in Single Cells.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.17.767299](https://doi.org/10.64898/2026.11.17.767299).
