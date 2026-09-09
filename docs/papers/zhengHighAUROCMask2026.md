---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# High AUROC can mask decision failure in sepsis transcriptomic classifiers

## 기본 정보

- Citation key: zhengHighAUROCMask2026
- Item type: journalArticle
- Authors: Hongwei Zheng; Wenbiao Chen
- Journal: PLOS ONE
- DOI: 10.1371/journal.pone.0357585
- PMID: 42691061
- URL: [Open article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0357585); [PubMed](https://pubmed.ncbi.nlm.nih.gov/42691061/)
- Source/date: published 2026-09-03
- 주 카테고리: Microarray
- 교차 카테고리: Bulk RNA-seq; Transcriptomics / Platform

## 1. 한 줄 요약

외부 transcriptomic cohort에서 높은 AUROC가 고정 threshold의 의사결정 성공을 보장하지 않으며 sample-wise rank 변환이 가장 안정적인 inductive 전처리였음을 보인 benchmark다.

## 2. 연구 질문

Platform·cohort shift가 있을 때 분류 순위는 유지돼도 score scale이 이동해 임계값 의사결정이 무너질 수 있는가, 그리고 calibration보다 전처리 선택이 더 중요한가?

## 3. 데이터와 방법

GSE65682·GSE95233 microarray, GSE154918 RNA-seq, GSE28750 inflammatory-stress cohort를 사용했다. 동일한 L2 logistic regression에 네 가지 전처리를 적용하고 AUROC, fixed-threshold balanced accuracy, calibration과 외부-cohort adaptation을 비교했다.

## 4. 핵심 결과

Standard·robust scaling은 AUROC가 거의 1이어도 외부 balanced accuracy가 약 0.50까지 떨어질 수 있었다. Strict-inductive sample-rank normalization은 대체로 0.95–1.00의 balanced accuracy를 유지했다. 외부 비라벨 분포를 쓰는 robust adaptation도 강했지만 이는 고정 single-sample transfer가 아니라 transductive adaptation이다.

## 5. 한계

Inflammatory-stress 검증군은 21명으로 작고 processed matrix만 사용했다. 모델군도 logistic regression에 제한되며 clinical covariate, 치료 영향과 subgroup fairness를 충분히 평가하지 않았다. 특정 sepsis signature의 결과를 다른 질환에 그대로 일반화할 수 없다.

## 6. 재현 또는 활용 포인트

- GEO: GSE65682, GSE95233, GSE154918, GSE28750
- 코드: [Zhenghongwei11/High-AUROC-sepsis-decision-failure](https://github.com/Zhenghongwei11/High-AUROC-sepsis-decision-failure)
- 재현 archive: [Zenodo 21850714](https://doi.org/10.5281/zenodo.21850714)
- AUROC와 함께 frozen threshold의 balanced accuracy, calibration, sample 단위 적용 가능성을 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

서로 다른 병원·microarray·RNA-seq 플랫폼으로 이동하는 rejection classifier에서 특히 직접적이다. 외부 cohort 전체 분포를 미리 쓰지 않는 진짜 single-biopsy inference와 cohort adaptation을 구분해 평가해야 한다.

## 8. 관련 키워드

- Microarray
- Bulk RNA-seq
- Cross-platform transfer
- External validation
- Calibration
- Decision threshold

## 9. Bibliography

Zheng, Hongwei, and Wenbiao Chen. “High AUROC Can Mask Decision Failure in Sepsis Transcriptomic Classifiers: Preprocessing Stability Outweighs Post Hoc Calibration across Cohorts.” PLOS ONE 21, no. 9 (2026): e0357585. [https://doi.org/10.1371/journal.pone.0357585](https://doi.org/10.1371/journal.pone.0357585).
