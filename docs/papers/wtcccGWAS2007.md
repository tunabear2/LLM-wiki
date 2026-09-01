---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# WTCCC: genome-wide association study of 14,000 cases and 3,000 controls

## 기본 정보

- Citation key: `wtcccGWAS2007`
- Item type: journalArticle
- Authors: The Wellcome Trust Case Control Consortium
- DOI: 10.1038/nature05911
- PMID: 17554300
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/17554300/)
- Source/date: Nature, 2007

## 1. 한 줄 요약

WTCCC 2007은 7개 common disease의 대규모 case-control GWAS를 수행해 common variant association study의 표준적 설계와 분석 흐름을 보여준 landmark 논문이다.

## 2. 왜 중요한가

수천 명 규모의 genotype array data, shared controls, stringent QC, genome-wide significance, replication이라는 GWAS 기본 문법을 정립했다. 현대 biobank GWAS보다 작지만, 분석 개념을 배우기 좋은 출발점이다.

## 3. 분석에서 위치

Genotype QC 후 disease별 case-control association을 수행하고, Manhattan/QQ plot, replication, locus interpretation으로 이어지는 GWAS workflow의 전체 예시로 읽는다.

## 4. 주의점

- 2007년 array density와 reference panel은 현재 biobank/imputation workflow보다 낮은 해상도다.
- Shared controls는 효율적이지만 phenotype contamination과 population matching을 주의해야 한다.
- Association hit은 causal variant가 아니라 LD proxy일 수 있으므로 fine mapping과 functional follow-up이 필요하다.

## 5. Bibliography

The Wellcome Trust Case Control Consortium. "Genome-wide association study of 14,000 cases of seven common diseases and 3,000 shared controls." _Nature_, 2007. [https://doi.org/10.1038/nature05911](https://doi.org/10.1038/nature05911).
