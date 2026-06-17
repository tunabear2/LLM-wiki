# DNA-seq / Variant Analysis Paper Notes

DNA 분석 섹션은 WGS/WES/targeted sequencing에서 FASTQ를 variant interpretation으로 바꾸는 기본 흐름을 공부하기 위한 공간이다. 우선 short-read DNA-seq variant analysis를 중심으로 두고, 나중에 methylation, ATAC-seq, long-read, HLA typing은 별도 섹션으로 확장한다.

## 핵심 질문

- Read alignment, duplicate marking, base quality recalibration 같은 전처리가 variant call 품질에 어떤 영향을 주는가?
- SNP/indel, structural variant, copy-number alteration는 각각 어떤 evidence를 쓰는가?
- Germline variant와 somatic variant, single-sample calling과 joint calling은 어떻게 다른가?
- Variant annotation에서 transcript choice, population frequency, predicted consequence를 어떻게 해석해야 하는가?
- Transplant 연구에서는 donor/recipient genotype, HLA/KIR, eQTL, rejection-associated variant를 expression 분석과 어떻게 연결할 수 있는가?

## 공부 순서

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [BWA](liBWAFast2009.md) | Burrows-Wheeler transform 기반 short-read alignment | WGS/WES read를 reference genome에 붙이는 출발점 |
| [SAMtools / SAM-BAM format](liSAMtools2009.md) | Alignment format과 BAM/VCF 처리 도구 | BAM/CRAM/VCF가 무엇을 담는지 이해하는 기본 문법 |
| [GATK Best Practices](vanDerAuweraGATKBestPractices2013.md) | FastQ-to-variant-call germline workflow | QC, duplicate marking, recalibration, variant filtering의 표준 흐름 |
| [FreeBayes](garrisonFreeBayes2012.md) | Haplotype-based small variant calling | GATK 외 Bayesian/haplotype variant caller 비교 후보 |
| [Manta](chenMantaRapid2016.md) | Structural variant와 medium-sized indel detection | Paired-end/split-read evidence로 deletion, duplication, inversion 등을 찾는 방법 |
| [Ensembl VEP](mclarenVEP2016.md) | Variant consequence annotation | VCF를 gene/transcript/protein-level consequence로 해석하는 기본 도구 |

## 분석 체크리스트

- Reference genome build, annotation version, contig naming이 모든 단계에서 일치하는지 확인한다.
- Mapping quality, coverage, duplication rate, insert size, contamination, sex check 같은 sample-level QC를 먼저 본다.
- Germline 분석에서는 joint calling과 population frequency filtering을, somatic 분석에서는 matched normal과 tumor purity를 구분한다.
- Variant annotation은 transcript choice에 따라 consequence가 바뀔 수 있으므로 canonical transcript와 MANE/Ensembl/RefSeq 기준을 기록한다.
- RNA-seq와 결합할 때는 expression outlier, allele-specific expression, eQTL, donor/recipient genotype mismatch를 별도 가설로 둔다.
