# The Ensembl Variant Effect Predictor

## 기본 정보

- Citation key: `mclarenVEP2016`
- Item type: journalArticle
- Authors: William McLaren; Laurent Gil; Sarah E. Hunt; Harpreet Singh Riat; Graham R. S. Ritchie; Anja Thormann; Paul Flicek; Fiona Cunningham
- DOI: 10.1186/s13059-016-0974-4
- PMID: 27268795
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/27268795/)
- Source/date: Genome Biology, 2016

## 1. 한 줄 요약

Ensembl VEP는 VCF variant를 gene, transcript, protein consequence와 population/functional annotation으로 변환해 해석 가능하게 만드는 annotation framework다.

## 2. 왜 중요한가

Variant call은 그 자체로는 genomic coordinate일 뿐이다. VEP는 missense, synonymous, splice region, loss-of-function 같은 transcript consequence와 external database annotation을 붙여 biological interpretation의 출발점을 만든다.

## 3. 분석에서 위치

Variant calling/filtering 후 normalized VCF를 입력으로 넣고, Ensembl annotation version에 맞춰 consequence table 또는 annotated VCF를 만든다.

## 4. 주의점

- Transcript choice에 따라 consequence가 바뀌므로 canonical, MANE, Ensembl/RefSeq 기준을 명시해야 한다.
- Genome build와 annotation cache version이 VCF와 맞아야 한다.
- Pathogenicity prediction score는 evidence hierarchy의 일부일 뿐이며 clinical conclusion으로 바로 쓰면 안 된다.

## 5. Bibliography

McLaren, William, Laurent Gil, Sarah E. Hunt, Harpreet Singh Riat, Graham R. S. Ritchie, Anja Thormann, Paul Flicek, and Fiona Cunningham. "The Ensembl Variant Effect Predictor." _Genome Biology_, 2016. [https://doi.org/10.1186/s13059-016-0974-4](https://doi.org/10.1186/s13059-016-0974-4).
