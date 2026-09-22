---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# dicast: machine-learning structural-variant detection from short reads

## 기본 정보

- Citation key: `alaviDicastMachineLearning2026`
- Item type: journalArticle
- Authors: Nico Alavi; M-Hossein Moeinzadeh; Jakob Hertzberg; Uirá Souto Melo; Lion Ward Al Raei; Paolo Infantino; Maryam Ghareghani; Marco Savarese; Stefan Mundlos; Martin Vingron
- Journal: Genome Biology
- DOI: 10.1186/s13059-026-04280-y
- PMID: 42754892
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42754892/); [DOI](https://doi.org/10.1186/s13059-026-04280-y); [code](https://github.com/burgshrimps/dicast)
- Source/date: published 2026-09-16; PubMed indexed 2026-09-18
- 주 카테고리: DNA-seq / Variant Analysis

## 1. 한 줄 요약

dicast는 여러 short-read SV caller의 call을 alignment·genomic-context feature로 XGBoost scoring해, 높은 precision을 유지하면서 consensus보다 더 많은 true·candidate pathogenic structural variant를 회수한다.

## 2. 연구 질문

대부분의 임상 workflow가 쓰는 short-read sequencing에서 caller consensus의 민감도 손실을 줄이면서도 structural-variant precision을 유지할 수 있는가?

## 3. 데이터와 방법

9개 sample과 5개 sequencing technology를 통합하고 수동 검수한 truth set을 구축했다. 8개 sample로 XGBoost scorer를 학습하고 한 sample holdout 및 독립 GIAB HG002에서 검증했다. Truth set에는 insertion 122,133개, deletion 104,099개, duplication 9,664개, inversion 335개가 포함됐다. 세 희귀질환 cohort에서도 diagnostic utility를 평가했다.

## 4. 핵심 결과

기존 short-read caller와 consensus보다 높은 precision 구간에서 더 많은 true positive를 회수했다. 세 희귀질환 cohort의 알려진 pathogenic SV를 모두 검출했고, consensus approach보다 candidate pathogenic deletion을 20% 더 찾았다. Code와 학습 model, manual-review viewer를 공개했다.

## 5. 한계

Multi-technology truth set도 기술 간 shared bias를 가질 수 있고 모든 call이 수동 검수된 것은 아니다. 현재 method는 deletion, insertion, duplication에 집중하며 inversion과 translocation은 지원하지 않는다. 더 다양한 ancestry, library protocol, coverage와 반복서열 영역에서의 검증이 필요하다.

## 6. 재현 또는 활용 포인트

- Reference build, caller version, candidate-union rule과 feature 계산을 고정한다.
- Sample-level holdout과 GIAB 같은 독립 truth set을 분리한다.
- SV type·size·repeat context별 precision–recall과 pathogenic-candidate burden을 보고한다.
- ML score cutoff는 validation data에서 잠근 뒤 clinical cohort에 적용한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor/recipient WGS에서 놓치기 쉬운 deletion·duplication을 찾고 expression outlier 또는 immune locus dosage와 연결하는 데 유용하다. 그러나 이식 outcome association에는 germline/somatic 구분, ancestry와 HLA/MHC 복잡성을 별도로 다뤄야 한다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- Structural variant
- Short-read sequencing
- XGBoost
- Diagnostic genomics

## 9. Bibliography

Alavi, Nico, et al. “dicast: A Machine Learning Method for Accurate Structural Variant Detection from Short-Read Sequencing Data.” Genome Biology (2026). [https://doi.org/10.1186/s13059-026-04280-y](https://doi.org/10.1186/s13059-026-04280-y).
