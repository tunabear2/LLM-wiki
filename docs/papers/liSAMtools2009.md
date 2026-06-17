# The Sequence Alignment/Map format and SAMtools

## 기본 정보

- Citation key: `liSAMtools2009`
- Item type: journalArticle
- Authors: Heng Li; Bob Handsaker; Alec Wysoker; Tim Fennell; Jue Ruan; Nils Homer; Gabor Marth; Goncalo Abecasis; Richard Durbin; 1000 Genome Project Data Processing Subgroup
- DOI: 10.1093/bioinformatics/btp352
- PMID: 19505943
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/19505943/)
- Source/date: Bioinformatics, 2009

## 1. 한 줄 요약

SAM/BAM은 read alignment를 저장하는 표준 format이고, SAMtools는 이 format을 정렬, index, pileup, variant processing에 쓰는 기본 도구다.

## 2. 왜 중요한가

DNA-seq, RNA-seq, ATAC-seq 등 NGS 분석은 대부분 SAM/BAM/CRAM과 VCF를 중심으로 움직인다. Format을 이해하면 mapping quality, CIGAR, flag, read group, duplicate 같은 QC 정보를 직접 해석할 수 있다.

## 3. 분석에서 위치

Aligner output을 sort/index하고, region별 read extraction, coverage 확인, pileup 생성, format conversion에 사용한다. Variant calling 전후 QC와 debugging에 거의 항상 등장한다.

## 4. 주의점

- Read group 정보가 없거나 잘못되면 GATK 등 downstream tool에서 sample/library 구분이 깨질 수 있다.
- BAM coordinate sort와 index 여부를 tool별 요구사항에 맞춰 확인해야 한다.
- CIGAR와 flag 해석을 모르고 depth만 보면 soft clipping, supplementary alignment, duplicate artifact를 놓칠 수 있다.

## 5. Bibliography

Li, Heng, Bob Handsaker, Alec Wysoker, Tim Fennell, Jue Ruan, Nils Homer, Gabor Marth, Goncalo Abecasis, Richard Durbin, and the 1000 Genome Project Data Processing Subgroup. "The Sequence Alignment/Map format and SAMtools." _Bioinformatics_, 2009. [https://doi.org/10.1093/bioinformatics/btp352](https://doi.org/10.1093/bioinformatics/btp352).
