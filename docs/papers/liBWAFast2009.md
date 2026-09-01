---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# BWA: fast and accurate short read alignment with Burrows-Wheeler transform

## 기본 정보

- Citation key: `liBWAFast2009`
- Item type: journalArticle
- Authors: Heng Li; Richard Durbin
- DOI: 10.1093/bioinformatics/btp324
- PMID: 19451168
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/19451168/)
- Source/date: Bioinformatics, 2009

## 1. 한 줄 요약

BWA는 Burrows-Wheeler transform과 backward search를 사용해 short DNA reads를 reference genome에 빠르고 정확하게 align하는 도구다.

## 2. 왜 중요한가

WGS/WES short-read DNA-seq 분석에서 FASTQ를 BAM으로 바꾸는 기본 단계다. Variant calling 품질은 alignment 품질, mapping quality, duplicate/soft clipping 처리에 크게 의존한다.

## 3. 분석에서 위치

FASTQ QC 후 reference genome에 align하고, SAM/BAM output을 만든다. 이후 sorting, duplicate marking, base recalibration, variant calling으로 이어진다.

## 4. 주의점

- BWA-backtrack, BWA-SW, BWA-MEM은 read length와 목적이 다르다. 현대 short-read WGS/WES에서는 보통 BWA-MEM 또는 BWA-MEM2를 쓴다.
- Reference build와 decoy/alt contig 포함 여부가 variant call에 영향을 준다.
- RNA-seq splice-aware alignment에는 STAR/HISAT2 같은 별도 aligner가 필요하다.

## 5. Bibliography

Li, Heng, and Richard Durbin. "Fast and accurate short read alignment with Burrows-Wheeler transform." _Bioinformatics_, 2009. [https://doi.org/10.1093/bioinformatics/btp324](https://doi.org/10.1093/bioinformatics/btp324).
