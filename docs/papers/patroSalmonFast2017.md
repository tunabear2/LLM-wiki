# Salmon: fast and bias-aware quantification of transcript expression

## 기본 정보

- Citation key: `patroSalmonFast2017`
- Item type: journalArticle
- Authors: Rob Patro; Geet Duggal; Michael I. Love; Rafael A. Irizarry; Carl Kingsford
- DOI: 10.1038/nmeth.4197
- PMID: 28263959
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/28263959/)
- Source/date: Nature Methods, 2017

## 1. 한 줄 요약

Salmon은 lightweight mapping과 bias-aware inference를 결합해 RNA-seq transcript abundance를 빠르고 정확하게 추정하는 도구다.

## 2. 왜 중요한가

현대 bulk RNA-seq pipeline에서 Salmon + tximport + DESeq2/edgeR/limma 조합은 정렬 기반 workflow의 실용적 대안이다. GC bias, positional bias 등 technical bias를 모델링해 transcript quantification의 안정성을 높이는 관점이 중요하다.

## 3. 분석에서 위치

FASTQ에서 transcript-level abundance를 만든 뒤, tximport로 gene-level count-like matrix를 생성하고 DESeq2/edgeR/voom에 연결한다. 빠른 cohort 재분석이나 여러 reference annotation 비교에 유용하다.

## 4. 주의점

- Alignment-free 결과는 reference transcriptome annotation과 decoy sequence 설정에 영향을 받는다.
- Downstream DE에는 TPM을 직접 넣지 말고 count-like estimate와 length correction 방식을 명시해야 한다.
- STAR 같은 genome aligner와 결과 차이를 QC 단계에서 비교하면 platform artifact를 더 잘 볼 수 있다.

## 5. Bibliography

Patro, Rob, Geet Duggal, Michael I. Love, Rafael A. Irizarry, and Carl Kingsford. "Salmon provides fast and bias-aware quantification of transcript expression." _Nature Methods_, 2017. [https://doi.org/10.1038/nmeth.4197](https://doi.org/10.1038/nmeth.4197).
