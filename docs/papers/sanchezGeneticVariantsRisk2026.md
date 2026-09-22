---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# Genetic variants and renal-impairment risk in decompensated cirrhosis

## 기본 정보

- Citation key: `sanchezGeneticVariantsRisk2026`
- Item type: journalArticle
- Authors: Lukas Otero Sanchez et al.; CANONIC, PREDICT, ACLARA, ANRS CO12 CirVir, and CIRRAL study groups
- Journal: The Lancet Gastroenterology & Hepatology
- DOI: 10.1016/S2468-1253(26)00217-7
- PMID: 42759531
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42759531/); [DOI](https://doi.org/10.1016/S2468-1253(26)00217-7)
- Source/date: ahead of print 2026-09-18
- 주 카테고리: GWAS
- 교차 카테고리: scRNA-seq; Transcriptomics / Platform

## 1. 한 줄 요약

다인종 discovery와 독립 replication GWAS는 decompensated cirrhosis의 renal impairment와 연관된 SUSD1 locus를 찾고, single-cell·spatial transcriptomics로 plasmacytoid dendritic cell–type-I-interferon 축에 연결했다.

## 2. 연구 질문

Decompensated cirrhosis에서 renal impairment 감수성의 유전적 locus를 찾을 수 있으며, 그 효과가 compensated disease·일반 인구와 구별되고 관련 세포상태로 이어지는가?

## 3. 데이터와 방법

다섯 discovery cohort 3,220명에서 serum creatinine GWAS를 수행했으며 83%는 European, 17%는 admixed American ancestry였다. 네 독립 European cohort 1,728명에서 replication하고, compensated cirrhosis 3,139명과 UK Biobank 일반인 402,683명에서 context specificity를 평가했다. Liver, blood와 kidney의 single-cell·spatial transcriptomics로 locus 관련 세포를 매핑했다.

## 4. 핵심 결과

SUSD1 lead variant rs2099161은 trans-ancestry discovery에서 β=0.16, p=4.32×10^-10, 독립 replication에서 β=0.09, p=5.34×10^-3였고 결합 meta-analysis는 β=0.13, p=8.31×10^-11, I²=0%였다. CC genotype은 TT 대비 baseline kidney-failure odds ratio 1.60이었고 1주 incident failure와 terlipressin 필요 위험도 높았다. Transcriptomics는 plasmacytoid dendritic cell의 SUSD1 발현과 renal impairment에서의 type-I-interferon 증가를 지지했다.

## 5. 한계

Discovery의 83%와 replication 전부가 European ancestry여서 ‘multi-ancestry’ 표본의 균형은 제한적이다. Serum creatinine은 간질환에서 muscle mass와 hemodynamics의 영향을 받고, 관찰적 GWAS·expression mapping만으로 pDC–interferon의 인과성을 확정할 수 없다. Kidney finding은 cirrhosis context이며 transplantation에서 검증되지 않았다.

## 6. 재현 또는 활용 포인트

- Discovery·replication의 ancestry, imputation panel, QC와 covariate를 따로 기록한다.
- Lead variant effect allele과 serum-creatinine 방향을 모든 cohort에서 맞춘다.
- Compensated disease와 일반 인구를 negative-context comparator로 유지한다.
- Colocalization·cell abundance·interferon score를 독립 tissue cohort에서 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney function genetic signal을 blood·kidney cell state로 연결하는 설계가 donor/recipient GWAS–biopsy transcriptomics 통합의 좋은 예다. 신장이식에서는 calcineurin inhibitor, rejection, baseline eGFR와 donor genotype을 포함한 별도 model이 필요하다.

## 8. 관련 키워드

- GWAS
- Multi-ancestry
- Renal impairment
- SUSD1
- Single-cell transcriptomics
- Spatial transcriptomics

## 9. Bibliography

Sanchez, Lukas Otero, et al. “Genetic Variants and the Risk of Renal Impairment in Decompensated Cirrhosis: A Multi-Ancestry Genome-Wide Association Study.” The Lancet Gastroenterology & Hepatology (2026). [https://doi.org/10.1016/S2468-1253(26)00217-7](https://doi.org/10.1016/S2468-1253(26)00217-7).
