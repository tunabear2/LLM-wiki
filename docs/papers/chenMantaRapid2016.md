# Manta: rapid detection of structural variants and indels

## 기본 정보

- Citation key: `chenMantaRapid2016`
- Item type: journalArticle
- Authors: Xiaoyu Chen; Ole Schulz-Trieglaff; Richard Shaw; Bret Barnes; Felix Schlesinger; Morten Kallberg; Anthony J. Cox; Semyon Kruglyak; Christopher T. Saunders
- DOI: 10.1093/bioinformatics/btv710
- PMID: 26647377
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/26647377/)
- Source/date: Bioinformatics, 2016

## 1. 한 줄 요약

Manta는 paired-end read와 split-read evidence를 사용해 germline 및 somatic structural variant와 medium-sized indel을 빠르게 탐지하는 도구다.

## 2. 왜 중요한가

SNP/indel caller만으로는 deletion, duplication, inversion, translocation 같은 큰 genomic rearrangement를 충분히 잡기 어렵다. Manta는 short-read SV calling의 대표 baseline으로 WGS/WES 구조변이 분석의 사고방식을 알려준다.

## 3. 분석에서 위치

Alignment BAM과 reference genome을 입력으로 structural variant VCF를 만든다. Germline sample 또는 tumor-normal pair setting에 따라 calling mode가 달라진다.

## 4. 주의점

- SV calling은 coverage, insert size distribution, mapping artifact에 민감하다.
- Short-read만으로 반복서열/복잡한 rearrangement를 해석하는 데 한계가 있다.
- Clinical interpretation 전에는 read visualization, orthogonal validation, population SV frequency 확인이 필요하다.

## 5. Bibliography

Chen, Xiaoyu, Ole Schulz-Trieglaff, Richard Shaw, Bret Barnes, Felix Schlesinger, Morten Kallberg, Anthony J. Cox, Semyon Kruglyak, and Christopher T. Saunders. "Manta: rapid detection of structural variants and indels for germline and cancer sequencing applications." _Bioinformatics_, 2016. [https://doi.org/10.1093/bioinformatics/btv710](https://doi.org/10.1093/bioinformatics/btv710).
