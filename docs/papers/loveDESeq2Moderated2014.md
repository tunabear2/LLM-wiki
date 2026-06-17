# DESeq2: moderated estimation of fold change and dispersion for RNA-seq data

## 기본 정보

- Citation key: `loveDESeq2Moderated2014`
- Item type: journalArticle
- Authors: Michael I. Love; Wolfgang Huber; Simon Anders
- DOI: 10.1186/s13059-014-0550-8
- PMID: 25516281
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/25516281/)
- Source/date: Genome Biology, 2014

## 1. 한 줄 요약

DESeq2는 RNA-seq count를 negative binomial GLM으로 모델링하고 dispersion과 log fold change를 shrinkage해 안정적인 differential expression 결과를 만든다.

## 2. 왜 중요한가

Bulk RNA-seq DEG 분석의 표준 baseline 중 하나다. 샘플 수가 작고 count variance가 큰 데이터에서 dispersion estimation과 LFC shrinkage가 해석 가능한 ranking을 만드는 데 중요하다.

## 3. 분석에서 위치

Gene-level raw count matrix와 sample metadata를 입력으로 받아 design formula에 따라 condition, batch, covariate 효과를 모델링한다. 결과는 DEG table, normalized count, variance-stabilized expression, MA plot 등으로 이어진다.

## 4. 주의점

- Input은 raw count여야 하며 TPM/FPKM/log-normalized matrix를 넣으면 안 된다.
- Batch, patient pairing, donor effect를 design에 넣지 않으면 rejection signal과 confounding이 섞일 수 있다.
- Gene filtering과 contrast 설정을 fold 안에서 일관되게 기록해야 한다.

## 5. Bibliography

Love, Michael I., Wolfgang Huber, and Simon Anders. "Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2." _Genome Biology_, 2014. [https://doi.org/10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8).
