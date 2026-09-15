---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# Long-read based detection of large copy number variants with potential functional significance using the ContextSV structural variant caller

## 기본 정보

- Citation key: perdomoLongReadDetection2026
- Item type: journalArticle
- Authors: Jonathan Elliot Perdomo; Mian Umair Ahsan; Jasmine Akoto; James Bauer; Naiara Akizu; Kai Wang
- Journal: NAR Genomics and Bioinformatics
- DOI: 10.1093/nargab/lqag108
- PMID: 42719292
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42719292/); [DOI](https://doi.org/10.1093/nargab/lqag108)
- Source/date: electronically published 2026-09-09; PubMed indexed 2026-09-10
- 주 카테고리: DNA-seq / Variant Analysis

## 1. 한 줄 요약

ContextSV는 long-read 정렬 증거에 read coverage 기반 copy number와 SNV allele frequency를 결합해 기존 정렬 중심 caller가 놓칠 수 있는 대형 CNV와 inversion을 보완 검출하는 framework다.

## 2. 연구 질문

Long-read SV caller가 alignment evidence에 주로 의존하면서 놓치는 크고 복잡한 구조변이를, copy-number와 allele-frequency 문맥을 함께 모델링해 더 민감하게 찾을 수 있는가?

## 3. 데이터와 방법

ContextSV는 정렬 기반 SV evidence, sequencing coverage에서 추정한 copy number, SNV allele frequency를 통합한다. 별도의 machine-learning classifier인 ContextScore는 genomic-context feature로 각 SV의 confidence score를 산출한다. 저자들은 simulation과 real dataset에서 방법을 benchmark하고 KOLF2.1J reference stem-cell line에서 기존 방법이 검출하지 못한 후보를 추가로 평가했다.

## 4. 핵심 결과

ContextSV는 기존 long-read caller가 놓칠 수 있는 대형 CNV와 inversion의 검출을 개선했다고 보고했다. KOLF2.1J에서 찾아낸 여러 대형 SV는 실험적으로 검증됐으며, 저자들은 ContextSV를 기존 caller를 대체하기보다 임상적으로 관련될 수 있는 대형 SV의 sensitivity를 보완하는 도구로 제시했다.

## 5. 한계

초록에는 simulation·real benchmark의 표본 구성, 비교 caller, 변이 유형별 정량 성능과 실험 검증 절차가 제시되지 않는다. 주요 기여가 대형 CNV와 inversion에 집중되어 있어 SNV·small indel 또는 모든 SV 유형에 대한 우위를 의미하지 않는다. KOLF2.1J 이외의 독립 임상 cohort에서 일반화와 confidence-score calibration을 추가로 확인해야 한다.

## 6. 재현 또는 활용 포인트

- 동일한 long-read alignment와 기존 SV callset에 ContextSV를 추가해 alignment-only 결과와 직접 비교한다.
- 변이 크기와 유형별 sensitivity·precision을 분리하고, coverage와 SNV heterozygosity에 따른 성능 변화를 확인한다.
- Reference build, aligner, upstream caller, coverage 산출법과 ContextScore 설정을 함께 고정한다.
- 기존 caller와 불일치하는 대형 SV는 독립적인 실험 또는 orthogonal sequencing evidence로 확인한다.
- 코드: [WGLab/ContextSV](https://github.com/WGLab/ContextSV); [WGLab/ContextScore](https://github.com/WGLab/ContextScore)
- 재현 archive: [ContextSV Zenodo 21774707](https://doi.org/10.5281/zenodo.21774707); [ContextScore Zenodo 21815943](https://doi.org/10.5281/zenodo.21815943)

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 또는 transcriptomics를 직접 다루지는 않는다. 다만 donor·recipient WGS나 이식 후 종양 분석에서 놓치기 쉬운 대형 CNV·SV를 보완하고, 이후 gene dosage와 발현 변화의 연계를 검토하는 DNA–RNA 통합 분석에 활용할 수 있다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- Long-read sequencing
- Structural variant
- Copy number variant
- Variant calling
- Machine-learning confidence score

## 9. Bibliography

Perdomo, Jonathan Elliot, et al. “Long-read Based Detection of Large Copy Number Variants with Potential Functional Significance Using the ContextSV Structural Variant Caller.” NAR Genomics and Bioinformatics 8, no. 3 (2026): lqag108. [https://doi.org/10.1093/nargab/lqag108](https://doi.org/10.1093/nargab/lqag108).
