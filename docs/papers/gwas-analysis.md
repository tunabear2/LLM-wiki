# GWAS Analysis Paper Notes

GWAS 분석 섹션은 genotype array 또는 sequencing-derived variants에서 genotype QC, population structure correction, imputation, association testing, meta-analysis, post-GWAS interpretation으로 이어지는 흐름을 공부하기 위한 공간이다. Transplant 연구에서는 recipient/donor genotype, HLA/KIR, immune response loci, expression QTL과 rejection phenotype을 연결할 수 있다.

## 핵심 질문

- Sample QC와 SNP QC는 어떤 artifact를 제거하는가?
- Population stratification, relatedness, batch effect를 association model에서 어떻게 통제하는가?
- Imputation은 왜 필요하고, reference panel과 ancestry mismatch가 결과에 어떤 영향을 주는가?
- GWAS summary statistics를 meta-analysis, heritability, gene-set/pathway analysis로 어떻게 확장하는가?
- GWAS hit을 transcriptomics, eQTL, cell-type-specific expression과 어떻게 연결할 수 있는가?

## 공부 순서

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [WTCCC GWAS](wtcccGWAS2007.md) | Large-scale case-control GWAS의 고전 예시 | Common disease GWAS design, multiple testing, replication 사고방식 |
| [PLINK](purcellPLINK2007.md) | Whole-genome association analysis toolset | Genotype QC, association testing, population structure workflow의 기본 도구 |
| [PCA stratification correction](pricePCA2006.md) | Principal components로 ancestry confounding 보정 | Donor/recipient ancestry, batch, cohort structure를 통제하는 기본 개념 |
| [IMPUTE2](howieIMPUTE22009.md) | Reference haplotype panel 기반 genotype imputation | Typed SNP를 더 촘촘한 variant set으로 확장해 fine mapping과 meta-analysis에 사용 |
| [METAL](willerMETAL2010.md) | GWAS summary statistics meta-analysis | 여러 cohort의 transplant phenotype GWAS를 합치는 기본 전략 |
| [LD Score regression](bulikSullivanLDSC2015.md) | Test statistic inflation에서 polygenicity와 confounding 분리 | GWAS signal 품질, heritability, genetic correlation 해석 |
| [MAGMA](deLeeuwMAGMA2015.md) | Gene/gene-set analysis of GWAS data | SNP-level result를 immune pathway, kidney cell type gene set과 연결 |

## 분석 체크리스트

- Sample call rate, heterozygosity, sex check, relatedness, ancestry outlier를 먼저 점검한다.
- SNP call rate, MAF, Hardy-Weinberg equilibrium, strand alignment, allele frequency mismatch를 확인한다.
- Association model에는 ancestry PCs, batch, sex, age 등 필요한 covariate를 명시한다.
- Imputed variant는 INFO/R2, dosage, allele alignment, reference panel version을 함께 기록한다.
- Post-GWAS 해석에서는 LD block, credible set, eQTL colocalization, cell-type-specific expression을 분리해서 본다.
