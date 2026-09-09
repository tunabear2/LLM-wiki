---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# Improving long-read somatic structural variant calling with pangenome and de novo personal genome assembly

## 기본 정보

- Citation key: qinImprovingLongReadSomatic2026
- Item type: journalArticle
- Authors: Qian Qin; Jakob M. Heinz; Heng Li
- Journal: Cancer Research Communications
- DOI: 10.1158/2767-9764.CRC-25-0769
- PMID: 42696744
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42696744/); [DOI](https://doi.org/10.1158/2767-9764.CRC-25-0769)
- Source/date: journal publication 2026-09-04; earlier preprint 2025-10-28
- 주 카테고리: DNA-seq / Variant Analysis

## 1. 한 줄 요약

minisv는 long-read somatic structural-variant call을 pangenome과 matched-normal de novo assembly에 다시 대조해 reference mismatch 유래 false positive를 줄이는 후처리 도구다.

## 2. 연구 질문

GRCh38 단일 reference에 정렬할 때 개인 germline 구조 차이가 somatic·mosaic SV처럼 보이는 문제를, population pangenome과 개인 assembly로 교차 확인해 완화할 수 있는가?

## 3. 데이터와 방법

기존 caller의 SV evidence를 pangenome 및 matched-normal de novo personal assembly 정렬과 비교하는 minisv를 제안했다. 5개 정상 sample과 6개 cancer cell-line tumor–normal pair에서 SAVANA, Severus, Sniffles2, nanomonsv의 call을 평가했다.

## 4. 핵심 결과

여러 caller에서 sensitivity 손실을 작게 유지하면서 germline–reference mismatch에서 생기는 거짓 somatic·mosaic SV를 크게 줄였다고 보고했다. Pangenome과 개인 assembly가 단일 linear reference의 오류를 상호 보완하며 caller-agnostic filtering 층으로 작동했다.

## 5. 한계

검증이 long-read와 cancer cell line 중심이다. Personal assembly에는 matched normal, 충분한 coverage와 추가 계산비용이 필요하고 pangenome의 ancestry representation에도 영향을 받는다. 실제 저순도 tumor나 임상 cohort에서의 일반화는 더 확인해야 한다.

## 6. 재현 또는 활용 포인트

- 코드: [qinqian/minisv.py](https://github.com/qinqian/minisv.py)
- Benchmark callset: [Zenodo 21852833](https://zenodo.org/records/21852833)
- 동일 sample에서 linear-reference-only, pangenome, personal-assembly filter를 분리해 sensitivity와 false positive를 비교한다.
- Reference·pangenome version, assembly quality와 caller version을 함께 고정해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

거부반응 transcriptomics와 직접 연결은 약하지만 이식 후 암·클론성 질환의 somatic SV 분석, 또는 donor–recipient genome 차이를 잘못 체세포 변이로 부르는 문제에 간접적으로 중요하다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- Long-read WGS
- Somatic structural variant
- Pangenome
- Personal assembly
- Benchmark

## 9. Bibliography

Qin, Qian, Jakob M. Heinz, and Heng Li. “Improving Long-read Somatic Structural Variant Calling with Pangenome and De Novo Personal Genome Assembly.” Cancer Research Communications 6 (2026). [https://doi.org/10.1158/2767-9764.CRC-25-0769](https://doi.org/10.1158/2767-9764.CRC-25-0769).
