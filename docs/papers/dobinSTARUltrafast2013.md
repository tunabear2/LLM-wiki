---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# STAR: ultrafast universal RNA-seq aligner

## 기본 정보

- Citation key: `dobinSTARUltrafast2013`
- Item type: journalArticle
- Authors: Alexander Dobin; Carrie A. Davis; Felix Schlesinger; Jorg Drenkow; Chris Zaleski; Sonali Jha; Philippe Batut; Mark Chaisson; Thomas R. Gingeras
- DOI: 10.1093/bioinformatics/bts635
- PMID: 23104886
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/23104886/)
- Source/date: Bioinformatics, 2013

## 1. 한 줄 요약

STAR는 suffix array 기반 seed search와 stitching을 사용해 splice-aware RNA-seq alignment를 매우 빠르게 수행하는 aligner다.

## 2. 왜 중요한가

Bulk RNA-seq 분석에서 read를 genome에 정렬해 exon junction, fusion, allele-specific expression까지 볼 때 기본 도구로 많이 쓰인다. Transcript quantification만 할 때는 Salmon/kallisto가 충분할 수 있지만, BAM과 splice junction 자체를 분석해야 하면 STAR 같은 genome aligner가 필요하다.

## 3. 분석에서 위치

FASTQ QC 후 reference genome index에 read를 align하고, BAM과 splice junction table을 만든다. 이후 featureCounts/HTSeq로 gene-level count를 만들거나, variant calling, fusion detection, RSeQC 같은 QC에 연결할 수 있다.

## 4. 주의점

- Genome index 생성 시 GTF annotation과 overhang 길이를 실험 read length에 맞춰야 한다.
- Multimapping read, chimeric read, duplicate 처리 방식이 downstream count와 fusion call에 영향을 준다.
- Pseudobulk/scRNA-seq UMI 데이터에서는 cell barcode/UMI 처리 workflow와 분리해서 생각해야 한다.

## 5. Bibliography

Dobin, Alexander, Carrie A. Davis, Felix Schlesinger, Jorg Drenkow, Chris Zaleski, Sonali Jha, Philippe Batut, Mark Chaisson, and Thomas R. Gingeras. "STAR: ultrafast universal RNA-seq aligner." _Bioinformatics_, 2013. [https://doi.org/10.1093/bioinformatics/bts635](https://doi.org/10.1093/bioinformatics/bts635).
