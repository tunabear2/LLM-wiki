---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# Reconstructing donor genotypes from scRNA-seq for downstream eQTL and HLA–TCR analysis

## 기본 정보

- Citation key: `kockelberghScTAPASDonorGenotypes2026`
- Item type: preprint
- Authors: H. Kockelbergh; J. Astley; K. M. Kichula; Z. Zhang; E. S. Ng; COMBAT Consortium; et al.
- Source: bioRxiv (posted 2026-10-05; not peer reviewed)
- DOI: [10.64898/2026.09.30.755703](https://doi.org/10.64898/2026.09.30.755703); [code](https://github.com/yang-luo-lab/scTAPAS/tree/main)
- 주 카테고리: `DNA-seq / Variant Analysis`
- 교차 카테고리: `scRNA-seq`

## 1. 한 줄 요약

scTAPAS는 donor별 scRNA-seq에서 genotype을 복원해 별도 array 없이 cell type–eGene와 HLA–TCR association을 분석한다.

## 2. 연구 질문

single-cell transcriptome의 sparse allele evidence만으로 downstream eQTL과 HLA/TCR 분석에 충분한 donor genotype 정보를 회수할 수 있는가?

## 3. 데이터와 방법

COMBAT 10x 5′ PBMC 자료에서 cell barcode·UMI와 allele evidence를 donor 단위로 합치고 genotype likelihood를 추정했다. conventional array/imputation과 variant recovery 및 chromosome 6 HLA–TCR eQTL 분석을 비교했다.

## 4. 핵심 결과

array 대비 약 18%의 variant만 직접 회수했지만 cell type–eGene pair의 68.6%를 복원했다. HLA class II와 TCR Vα association을 downstream에서 확인했고, 공개 코드로 pipeline을 재실행할 수 있다.

## 5. 한계

검증은 5′ PBMC와 약 500 cell/donor 규모에 집중되며 3′ chemistry, 조직 biopsy, 희귀 변이와 다른 ancestry panel로의 일반화가 제한적이다. chr6 중심 결과이고 linear reference의 HLA bias와 genotype-identifiability 거버넌스가 남는다.

## 6. 재현 또는 활용 포인트

cell 수·coverage·donor origin을 고정하고 array/imputation truth와 calibration을 비교한다. HLA genotype과 TCR sequence의 재식별 위험, 동의 범위, low-confidence genotype filtering을 명시한다.

## 7. Transcriptomics·신장이식 연구와의 연결

donor/recipient array가 없는 신장이식 PBMC·biopsy scRNA-seq에서 HLA/eQTL와 rejection cell state를 연결하는 직접적인 설계 후보다. 이식 cohort에서는 genotype 회수를 임상 결정에 바로 사용하지 말고 독립 DNA assay와 HLA typing으로 확인한다.

## 8. 관련 키워드

- scRNA-seq genotyping
- eQTL
- HLA–TCR
- donor genotype

## 9. Bibliography

Kockelbergh, H., et al. “Reconstructing Donor Genotypes from scRNA-seq for Downstream eQTL and HLA–TCR Analysis.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.30.755703](https://doi.org/10.64898/2026.09.30.755703).
