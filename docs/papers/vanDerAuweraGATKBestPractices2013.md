# From FastQ data to high-confidence variant calls: the GATK Best Practices pipeline

## 기본 정보

- Citation key: `vanDerAuweraGATKBestPractices2013`
- Item type: journalArticle
- Authors: Geraldine A. Van der Auwera; Mauricio O. Carneiro; Christopher Hartl; Ryan Poplin; Guillermo del Angel; Ami Levy-Moonshine; Tadeusz Jordan; Khalid Shakir; David Roazen; Joel Thibault; et al.
- DOI: 10.1002/0471250953.bi1110s43
- PMID: 25431634
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/25431634/)
- Source/date: Current Protocols in Bioinformatics, 2013

## 1. 한 줄 요약

이 논문은 BWA와 GATK를 사용해 FASTQ에서 high-confidence germline SNP/indel call까지 가는 Best Practices workflow를 정리한다.

## 2. 왜 중요한가

Germline WGS/WES variant calling의 표준 교과서 역할을 한다. Alignment, sorting, duplicate marking, base quality score recalibration, variant calling, filtering 같은 단계가 왜 필요한지 한 흐름으로 이해할 수 있다.

## 3. 분석에서 위치

FASTQ QC와 BWA alignment 후 GATK preprocessing을 거쳐 HaplotypeCaller, joint genotyping, VQSR 또는 hard filtering으로 variant callset을 만든다.

## 4. 주의점

- GATK version 변화에 따라 세부 command는 바뀌므로 최신 공식 문서와 함께 봐야 한다.
- Single sample calling과 cohort joint calling은 민감도와 genotype consistency가 다르다.
- Somatic cancer variant calling, RNA-seq variant calling, mitochondrial variant calling은 별도 Best Practices가 필요하다.

## 5. Bibliography

Van der Auwera, Geraldine A., Mauricio O. Carneiro, Christopher Hartl, Ryan Poplin, Guillermo del Angel, Ami Levy-Moonshine, Tadeusz Jordan, Khalid Shakir, David Roazen, Joel Thibault, et al. "From FastQ data to high-confidence variant calls: the Genome Analysis Toolkit best practices pipeline." _Current Protocols in Bioinformatics_, 2013. [https://doi.org/10.1002/0471250953.bi1110s43](https://doi.org/10.1002/0471250953.bi1110s43).
