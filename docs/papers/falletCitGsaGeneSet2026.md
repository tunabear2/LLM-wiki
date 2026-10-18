---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# cit_gsa: Gene Set Analysis for scRNA-seq with Covariate Adjustment

## 기본 정보

- Citation key: `falletCitGsaGeneSet2026`
- Item type: bioRxiv preprint / Bioinformatics application note
- Authors: Sara Fallet; Véronique Godot; Pierre Neuvial; Boris P. Hejblum
- Source: bioRxiv v1, posted 2026-10-14 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.13.758831](https://doi.org/10.64898/2026.10.13.758831); [CRAN citcdf](https://cran.r-project.org/package=citcdf); [reproduction archive](https://doi.org/10.5281/zenodo.23264404)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

cit_gsa는 gene-level DE 뒤 enrichment를 하는 2단계 절차 대신 조건부 분포 검정을 gene set 수준에서 한 번에 수행해, 다수 조건·연속변수와 covariate adjustment를 지원한다.

## 2. 연구 질문

scRNA-seq gene set differential analysis에서 평균 변화뿐 아니라 분포 형태 변화도 포착하면서 cell type 같은 공변량을 직접 보정할 수 있는가?

## 3. 데이터와 방법

Gene별 conditional CDF를 threshold별 logistic regression으로 추정하고 factor의 coefficient를 gene set 전체에서 score statistic으로 합쳤다. 1,000 genes, 200 cells, gene set 100개 gene의 평균 변화와 modality 변화 simulation을 500회 반복해 globaltest, GSEA, hypergeometric test와 비교했다. 실제 분석은 539 dendritic cells·17,691 genes에서 259 Blood Transcription Modules와 CD83 연관성을 DC subtype 보정 전후로 비교했다.

## 4. 핵심 결과

- 평균 변화에서는 self-contained 방법들이 유사했지만, 분포 modality가 바뀌는 시나리오에서 cit_gsa가 mean-regression 기반 globaltest보다 강했다.
- Gene correlation 0, 0.4, 0.8에서도 같은 방향을 보였다.
- Dendritic-cell 자료에서 subtype을 보정하면 marginal analysis의 일부 module 연관성이 사라지고 activation 관련 해석이 달라졌다.

## 5. 한계

Applications note 규모의 초기 연구이며 simulation과 한 public dataset에 집중했다. 수식은 cell을 iid observation으로 두므로 여러 환자의 phenotype을 비교할 때 donor 내 상관을 직접 모델링하지 않는다. 경쟁법과 null hypothesis가 달라 power만으로 우열을 단정하면 안 된다.

## 6. 재현 또는 활용 포인트

CRAN package와 모든 script/data가 Zenodo에 있다. Donor-level permutation, pseudobulk 또는 mixed-effect sensitivity analysis를 추가하고, self-contained와 competitive test의 질문 차이를 명시한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection 상태와 immune/tubular pathway의 연관성을 cell type, treatment, batch로 보정할 때 유용하다. 이식 biopsy에서는 cell 수가 아니라 환자가 추론 단위라는 점을 보완해야 한다.

## 8. 관련 키워드

- scRNA-seq
- gene set analysis
- covariate adjustment
- conditional independence

## 9. Bibliography

Fallet, Sara, et al. “cit_gsa: Gene Set Analysis for scRNA-seq with Covariate Adjustment.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.13.758831](https://doi.org/10.64898/2026.10.13.758831).
