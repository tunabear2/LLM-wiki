---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# A Haplotype Reference Panel from 490,319 UK Biobank Genomes Improves Global Genotype Imputation

## 기본 정보

- Citation key: `wienbrandtHaplotypeReferencePanel2026`
- Item type: journal article
- Authors: Lars Wienbrandt; Christoph Prieß; Marcus Schmöhl; Volker Neff; Maria Gretsova; Guillermo Torres; Eike Matthias Wacker; Andre Franke; David Ellinghaus
- Source: Nature Genetics, online 2026-10-30
- Original: [DOI: 10.1038/s41588-026-02819-0](https://doi.org/10.1038/s41588-026-02819-0); [PMID: 42963394](https://pubmed.ncbi.nlm.nih.gov/42963394/)
- 주 카테고리: `GWAS`

## 1. 한 줄 요약

490,319 UK Biobank WGS로 만든 haplotype reference panel과 EagleImp/RAP workflow가 TOPMed r3보다 다수 population의 phasing·imputation을 개선하고 GWAS locus discovery와 fine-mapping resolution을 높였다.

## 2. 연구 질문

대규모 UK Biobank WGS panel이 기존 TOPMed reference보다 global population의 phasing·rare-variant imputation과 downstream GWAS를 개선하는가?

## 3. 데이터와 방법

UK Biobank 490,319명의 WGS로 reference panel을 만들고 EagleImp와 Research Analysis Platform의 EagleImp-RAP으로 phasing·imputation을 제공했다. 1000 Genomes superpopulation·subpopulation에서 TOPMed r3와 switch error, MAE, estimated squared correlation을 비교했다. Italy, Germany, Spain, Norway COVID-19 GWAS를 재imputation해 association과 fine-mapping 영향을 확인했다.

## 4. 핵심 결과

- AMR을 제외한 모든 superpopulation과 26개 중 25개 subpopulation에서 TOPMed보다 phasing switch error가 낮았다.
- MAF 0.01%까지 5개 중 4개 superpopulation의 MAE와 5개 모두의 estimated squared correlation이 개선되었고 East·South Asian에서 이득이 컸다.
- COVID-19 GWAS 재imputation은 genome-wide significant locus 발견과 fine-mapping resolution을 높였다.

## 5. 한계

AMR에서는 switch-error 우위가 없었고 population별 개선 폭이 달랐다. Panel 사용은 UK Biobank의 access·compute 환경에 의존하며, downstream 실증은 COVID-19 GWAS에 집중되었다.

## 6. 재현 또는 활용 포인트

Panel version, genome build, phasing tool, ancestry별 INFO/R²와 allele-frequency bin을 기록한다. TOPMed·1000 Genomes panel과 같은 sample·variant QC에서 비교하고 imputation 뒤 locus count뿐 아니라 fine-mapping credible set 변화를 본다.

## 7. Transcriptomics·신장이식 연구와의 연결

다양한 ancestry의 donor·recipient genotype을 보강해 eQTL·PRS·rejection GWAS를 biopsy expression과 연결하는 reference 후보이다. Cohort ancestry별 성능과 HLA/KIR 같은 복잡 locus는 별도 검증해야 한다.

## 8. 관련 키워드

- GWAS
- genotype imputation
- haplotype reference panel
- multi-ancestry genetics

## 9. Bibliography

Wienbrandt, Lars, et al. “A Haplotype Reference Panel Constructed from 490,319 UK Biobank Genomes Improves Genotype Imputation for Global Populations.” _Nature Genetics_, 2026. [https://doi.org/10.1038/s41588-026-02819-0](https://doi.org/10.1038/s41588-026-02819-0).
