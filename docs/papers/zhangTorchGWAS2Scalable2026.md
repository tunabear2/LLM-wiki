---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# TorchGWAS2: cost-effective phenome- and genome-wide association testing in related samples

## 기본 정보

- Citation key: `zhangTorchGWAS2Scalable2026`
- Item type: preprint
- Authors: Mengyu Zhang; Ziqian Xie; Samaneh Salehi Nasab; Nannan Wang; Xingzhong Zhao; et al.; Han Chen
- DOI: 10.64898/2026.09.10.26362744
- PMID: 42780060
- URL: [medRxiv](https://www.medrxiv.org/content/10.64898/2026.09.10.26362744v1); [PubMed](https://pubmed.ncbi.nlm.nih.gov/42780060/); [DOI](https://doi.org/10.64898/2026.09.10.26362744); [code](https://github.com/hanchenlab/TorchGWAS2/tree/support-to-bed-format)
- Source/date: medRxiv v1, posted 2026-09-16; PMC released 2026-09-22 and PubMed indexed 2026-09-24; not peer reviewed
- 주 카테고리: GWAS

## 1. 한 줄 요약

TorchGWAS2는 related sample과 반복·longitudinal phenotype을 위한 linear mixed model score test를 결정론적 variance correction과 GPU로 가속해 대규모 PheWAS·GWAS 비용을 줄인다.

## 2. 연구 질문

수천 개 imaging·omics phenotype을 related individual에서 검사할 때, 무작위 variant subsampling 없이 type-I error와 power를 유지하면서 LMM 연산을 phenotype·variant·sample 수에 선형으로 확장할 수 있는가?

## 3. 데이터와 방법

Variant별 score-test variance를 결정론적 correction factor로 보정해 randomized sampling과 반복 I/O를 없애고 GPU tensor 연산으로 구현했다. Unrelated·related individual, cross-sectional·longitudinal design, missing phenotype을 지원한다. UK Biobank 64,703명의 양안 retinal image-derived endophenotype 128개와 TOPMed 16,352명의 circulating metabolite 1,023개에 적용하고 기존 LMM 도구와 calibration, power와 실행시간을 비교했다.

## 4. 핵심 결과

Simulation에서 type-I error를 통제하면서 큰 효과 variant의 residual variance를 갱신해 일부 조건에서 fastGWA보다 높은 power를 보였다. 양안을 별도 반복 측정으로 모델링해 single-eye 분석에서 놓친 세 유의 영역을 찾았다. TOPMed metabolomics 분석에서는 약 100배의 속도 향상을 보였고, 저자들은 월 단위 작업을 시간 단위로 줄일 수 있다고 보고했다.

## 5. 한계

Missing phenotype 처리는 available-case이며 missing completely at random 가정에 의존한다. 실증은 retinal imaging과 metabolomics 두 영역에 집중되고 UK Biobank·TOPMed individual-level data는 통제 접근이라 완전한 독립 재현 장벽이 있다. GPU 환경과 genotype I/O 구성에 따라 실제 비용 이득이 달라질 수 있으며 현재 preprint다.

## 6. 재현 또는 활용 포인트

- Code: [hanchenlab/TorchGWAS2](https://github.com/hanchenlab/TorchGWAS2/tree/support-to-bed-format)
- Relatedness, 반복 측정과 between/within-subject variance 구조를 분석 전 명시한다.
- 기존 도구와 genomic inflation, type-I error, effect·SE concordance 및 runtime·cloud cost를 함께 비교한다.
- UK Biobank와 TOPMed는 승인된 controlled-access 절차가 필요하다.

## 7. Transcriptomics·신장이식 연구와의 연결

대규모 이식 cohort에서 longitudinal renal function, rejection score, pathology image와 transcriptomic module을 다수 phenotype으로 검사할 때 계산 병목을 줄일 수 있다. 다만 작은 biopsy cohort에서는 계산 속도보다 power, ancestry, center effect와 phenotype missingness가 더 큰 제한이므로 별도 설계가 필요하다.

## 8. 관련 키워드

- GWAS
- Phenome-wide association
- Linear mixed model
- Related samples
- Longitudinal phenotype
- GPU acceleration
- Omics genetics

## 9. Bibliography

Zhang, Mengyu, Ziqian Xie, Samaneh Salehi Nasab, et al. “TorchGWAS2: Cost-Effective Phenome- and Genome-Wide Association Testing in Related Samples.” medRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.10.26362744](https://doi.org/10.64898/2026.09.10.26362744). Preprint; not peer reviewed.
