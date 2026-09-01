---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# MIAME: minimum information about a microarray experiment

## 기본 정보

- Citation key: `brazmaMIAME2001`
- Item type: journalArticle
- Authors: Alvis Brazma; Pascal Hingamp; John Quackenbush; Gavin Sherlock; Paul Spellman; Chris Stoeckert; John Aach; Wilhelm Ansorge; Catherine A. Ball; Helen C. Causton; et al.
- DOI: 10.1038/ng1201-365
- PMID: 11726920
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/11726920/)
- Source/date: Nature Genetics, 2001

## 1. 한 줄 요약

MIAME는 microarray experiment를 해석하고 재현하기 위해 필요한 raw data, processed data, sample annotation, array annotation, protocol, experimental design의 최소 정보를 정의한 표준이다.

## 2. 왜 중요한가

Microarray는 platform, probe annotation, hybridization protocol, normalization 방식이 결과 해석에 큰 영향을 준다. MIAME는 public repository에 deposit된 expression data를 재분석할 때 metadata를 어떻게 확인해야 하는지 기준을 제공한다.

## 3. 분석에서 위치

GEO/ArrayExpress에서 dataset을 고를 때 sample annotation, raw file, platform annotation, protocol, processed matrix가 충분한지 확인하는 체크리스트로 쓴다.

## 4. 주의점

- MIAME-compliant라고 해서 phenotype label이 분석 목적에 충분히 깨끗하다는 뜻은 아니다.
- 오래된 microarray dataset은 probe annotation이 낡았을 수 있어 최신 gene annotation으로 재매핑이 필요하다.
- Clinical metadata 누락, batch/date 누락, treatment history 누락은 downstream model의 confounding이 될 수 있다.

## 5. Bibliography

Brazma, Alvis, Pascal Hingamp, John Quackenbush, Gavin Sherlock, Paul Spellman, Chris Stoeckert, John Aach, Wilhelm Ansorge, Catherine A. Ball, Helen C. Causton, et al. "Minimum information about a microarray experiment (MIAME)-toward standards for microarray data." _Nature Genetics_, 2001. [https://doi.org/10.1038/ng1201-365](https://doi.org/10.1038/ng1201-365).
