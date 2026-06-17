# kallisto: near-optimal probabilistic RNA-seq quantification

## 기본 정보

- Citation key: `brayKallistoNearOptimal2016`
- Item type: journalArticle
- Authors: Nicolas L. Bray; Harold Pimentel; Pall Melsted; Lior Pachter
- DOI: 10.1038/nbt.3519
- PMID: 27043002
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/27043002/)
- Source/date: Nature Biotechnology, 2016

## 1. 한 줄 요약

kallisto는 read를 base-level alignment하지 않고 transcript compatibility를 빠르게 찾는 pseudoalignment로 transcript abundance를 추정한다.

## 2. 왜 중요한가

RNA-seq quantification을 "정렬 후 카운트"에서 "transcriptome compatibility 기반 빠른 추정"으로 바꾼 대표 방법이다. Bootstrap으로 quantification uncertainty를 제공해 transcript-level 분석과 sleuth 같은 downstream 모델에 연결된다.

## 3. 분석에서 위치

FASTQ를 transcriptome index에 pseudoalign하고 transcript abundance를 추정한다. Gene-level differential expression을 하려면 tximport 등으로 transcript-level estimate를 gene-level count/abundance로 요약한다.

## 4. 주의점

- Reference transcriptome annotation 품질에 민감하다.
- Genome alignment BAM이 필요한 junction QC, fusion, variant analysis에는 별도 aligner가 필요하다.
- Transcript-level uncertainty를 gene-level 분석에서 어떻게 요약하는지 기록해야 한다.

## 5. Bibliography

Bray, Nicolas L., Harold Pimentel, Pall Melsted, and Lior Pachter. "Near-optimal probabilistic RNA-seq quantification." _Nature Biotechnology_, 2016. [https://doi.org/10.1038/nbt.3519](https://doi.org/10.1038/nbt.3519).
