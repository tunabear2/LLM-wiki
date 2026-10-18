---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# A Phenome-wide Structural Variant Map from 467,152 UK Biobank Genomes

## 기본 정보

- Citation key: `atanurPhenomeWideStructural2026`
- Item type: journal article
- Authors: Santosh S. Atanur; Fengyuan Hu; Haiyi Lou; Xiaoyin Li; Xueqing Zoe Zou; et al.
- Source: Cell, online 2026-10-15
- Original: [DOI: 10.1016/j.cell.2026.09.035](https://doi.org/10.1016/j.cell.2026.09.035); [PubMed PMID: 42880286](https://pubmed.ncbi.nlm.nih.gov/42880286/)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

UK Biobank 467,152명 WGS에서 160만 SV를 18,263개 임상·정량·단백질 phenotype과 연관 분석해, 기존 CNV 연구가 보지 못한 광범위한 SV–phenotype 지도를 만들었다.

## 2. 연구 질문

Population-scale WGS에서 다양한 structural variant가 질환, quantitative trait와 plasma protein에 기여하는 범위를 얼마나 확장해 볼 수 있는가?

## 3. 데이터와 방법

467,152 UK Biobank genome의 160만 SV에 대해 13,322 binary trait, 2,018 quantitative trait, 2,923 plasma protein의 PheWAS와 protein-QTL analysis를 수행했다. SV type·위치와 functional genomic region overlap을 함께 해석했다.

## 4. 핵심 결과

- SV의 82.25%는 기존 copy-number variant 연구의 검출 범위 밖이었다.
- 3,467개 SV가 1,690개 protein과 연결됐고, 전체적으로 28,184개 health-outcome association을 검출했다.
- 기존 GWAS locus에서 연관된 SV의 32.21%가 functional genomic region과 겹쳤으며 rare SV의 큰 phenotype effect도 확인했다.

## 5. 한계

대규모 연관 지도이지 개별 SV의 인과기전을 직접 입증한 연구는 아니다. UK Biobank의 phenotype 정의와 cohort 구성, 사용한 SV callset에 결과가 의존하며 독립 population에서의 replication이 필요하다. 저자들은 연구 당시 AstraZeneca 직원·계약자였고 주식 또는 옵션을 보유할 수 있다고 밝혔다.

## 6. 재현 또는 활용 포인트

UK Biobank controlled-access WGS와 phenotype이 필요하다. SV type, allele frequency, callability와 relatedness/population structure를 통제하고, 기존 CNV/SNV signal과 조건부 분석한 뒤 expression·protein QTL로 좁히는 순서가 적절하다.

## 7. Transcriptomics·신장이식 연구와의 연결

신기능, 면역, 약물반응과 연관된 SV를 donor·recipient 후보로 우선순위화하고 biopsy eQTL/expression outlier와 교차할 수 있다. Association catalog 자체를 이식 outcome의 인과 근거로 사용해서는 안 된다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- GWAS
- structural variation
- phenome-wide association

## 9. Bibliography

Atanur, Santosh S., et al. “A Phenome-wide Structural Variant Map from 467,152 UK Biobank Genomes.” Cell, 2026. [https://doi.org/10.1016/j.cell.2026.09.035](https://doi.org/10.1016/j.cell.2026.09.035).
