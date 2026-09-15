---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# UCResponNet-X: cross-platform multi-dataset gene expression for predictive modeling of drug response in ulcerative colitis

## 기본 정보

- Citation key: topkaraogluUCResponNetXCrossPlatform2026
- Item type: journalArticle
- Authors: Mehmet Kutalmış Topkaraoğlu; İsmail Cantürk
- Journal: Computer Methods in Biomechanics and Biomedical Engineering
- DOI: 10.1080/10255842.2026.2729438
- PMID: 42717746
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42717746/); [DOI](https://doi.org/10.1080/10255842.2026.2729438)
- Source/date: electronically published and PubMed indexed 2026-09-10
- 주 카테고리: Microarray
- 교차 카테고리: Bulk RNA-seq; Transcriptomics / Platform

## 1. 한 줄 요약

UCResponNet-X는 세 microarray cohort에서 학습·검증한 infliximab-response model을 외부 RNA-seq cohort로 이전해 normalization 선택이 cross-platform 성능을 좌우함을 보인 framework다.

## 2. 연구 질문

Microarray와 RNA-seq 사이의 강한 platform effect에도 ulcerative-colitis biologic response classifier가 일반화될 수 있는가, 그리고 어떤 전처리 조합이 예측 신호를 가장 안정적으로 보존하는가?

## 3. 데이터와 방법

Infliximab response를 예측하기 위해 세 개의 독립 microarray cohort를 training·validation에 사용하고 별도의 RNA-seq dataset에서 platform transfer를 평가했다. Log2 transformation, quantile normalization, z-score standardization을 batch-effect correction 및 biologically informed feature selection과 조합하고, 여러 classification algorithm을 통일된 cross-validation protocol에서 비교했다.

## 4. 핵심 결과

Z-score standardization과 log2 transformation은 quantile normalization보다 platform 간 predictive signal을 더 잘 보존했다. 최고 평균 cross-validation AUROC는 0.824였고 외부 RNA-seq test AUROC는 0.821이었다. 저자들은 normalization strategy가 cross-platform transcriptomic prediction의 핵심 결정요인이며 legacy microarray를 재사용할 수 있다고 결론지었다.

## 5. 한계

초록에는 cohort별 표본 수, response 정의, class balance, 신뢰구간과 calibration 결과가 없다. 단일 질환·약제와 하나의 외부 RNA-seq dataset에 기반하므로 다른 질환, 약물 또는 기관으로의 일반화는 확인이 필요하다. 높은 AUROC만으로 고정 threshold의 임상 의사결정 성능이 보장되지는 않는다.

## 6. 재현 또는 활용 포인트

- 환자와 cohort가 train·validation·external test 사이에 겹치지 않도록 분할 단위를 확인한다.
- Normalization과 batch-correction parameter는 training data에서만 추정하고 외부 RNA-seq에 고정 적용해 leakage를 막는다.
- Log2, quantile, z-score 조건별 AUROC뿐 아니라 threshold 성능과 calibration을 함께 비교한다.
- 공통 gene mapping, biologically informed feature-selection 목록과 microarray probe-to-gene 집계 규칙을 고정한다.
- 초록에 cohort accession과 공개 코드가 없으므로 원문에서 데이터·구현 가용성을 별도 확인해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

여러 병원의 legacy rejection microarray를 RNA-seq 기반 graft-outcome 또는 치료반응 연구에 재사용할 때 직접 참고할 수 있다. 신장이식에 적용할 때는 UC에서 얻은 normalization 우위를 그대로 가정하지 말고, 기관·플랫폼을 완전히 분리한 external validation과 임상 threshold 평가를 다시 수행해야 한다.

## 8. 관련 키워드

- Microarray
- Bulk RNA-seq
- Transcriptomics / Platform
- Cross-platform transfer
- Batch correction
- Drug-response prediction
- External validation

## 9. Bibliography

Topkaraoğlu, Mehmet Kutalmış, and İsmail Cantürk. “UCResponNet-X: Cross-platform Multi-dataset Gene Expression for Predictive Modeling of Drug Response in Ulcerative Colitis.” Computer Methods in Biomechanics and Biomedical Engineering (2026): 1–17. [https://doi.org/10.1080/10255842.2026.2729438](https://doi.org/10.1080/10255842.2026.2729438).
