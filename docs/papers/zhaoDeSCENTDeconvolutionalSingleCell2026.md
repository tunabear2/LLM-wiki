---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# DeSCENT: Deconvolutional Single-Cell RNA-seq Enhances Transcriptome-based Cancer Survival Analysis

## 기본 정보

- Citation key: `zhaoDeSCENTDeconvolutionalSingleCell2026`
- Item type: journal article
- Authors: Yonghao Zhao; Zeyu You; Yu Shen; Jielei Chu; Xun Gong; Tianrui Li; Ziqiang Wang; Chuan Xu; Zhipeng Luo; Yazhou He
- Source: Bioinformatics, accepted 2026-11-03; PubMed indexed 2026-11-06
- Original: [DOI: 10.1093/bioinformatics/btag810](https://doi.org/10.1093/bioinformatics/btag810); [PMID: 42993079](https://pubmed.ncbi.nlm.nih.gov/42993079/); [code](https://github.com/YonghaoZhao722/DeSCENT); [Zenodo](https://doi.org/10.5281/zenodo.22073099)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`
- 관련 카테고리: `Bulk RNA-seq`, `scRNA-seq`

## 1. 한 줄 요약

DeSCENT는 scRNA-seq reference로 bulk RNA-seq를 cell-level profile로 분해하고 원래 bulk 표현과 결합해 여러 암의 survival prediction을 개선한다.

## 2. 연구 질문

생존 label이 풍부한 bulk cohort에 single-cell cellular representation을 복원해 tumor heterogeneity 정보를 더하면 transcriptome-only prognosis가 개선되는가?

## 3. 데이터와 방법

여덟 TCGA cancer cohort의 bulk RNA-seq를 reference-informed cellular profile로 deconvolution하고 bulk와 cell-level representation을 함께 사용했다. 서로 다른 세 survival model에서 bulk-only와 비교하고 별도 외부 cohort에서도 검증했다.

## 4. 핵심 결과

- 여덟 TCGA cohort에서 평균 C-index가 bulk-only보다 높았고 time-dependent AUC도 대체로 개선되었다.
- Integrated Brier score는 일관되게 좋아지지 않아 discrimination 개선이 calibration·prediction error 개선과 동일하지 않았다.
- 외부 검증에서도 세 baseline보다 평균 C-index가 높았지만 내부 평가보다 성능이 낮았다.

## 5. 한계

복원한 cell profile은 직접 측정한 single-cell data가 아니며 reference mismatch와 deconvolution error를 포함한다. Cancer cohort와 survival model별 편차가 평균값에 가려질 수 있고, 임상변수 위의 순증분 가치나 전향적 임상효용은 확립되지 않았다.

## 6. 재현 또는 활용 포인트

Reference 선택과 gene intersection을 fold 밖에서 고정하되 survival-informed selection은 fold 안에서 수행한다. Bulk-only, estimated cell fraction, cell-profile-only, 결합 model을 분리하고 C-index·time-AUC·IBS·calibration을 외부 cohort에서 함께 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney atlas로 bulk allograft biopsy를 분해한 뒤 원래 발현과 cell-state representation을 결합해 graft survival·rejection-free survival을 예측하는 직접적인 template이다. 정상 신장 reference가 rejection-specific state를 흡수하지 않는지 mismatch stress test가 필요하다.

## 8. 관련 키워드

- bulk RNA-seq deconvolution
- single-cell reference
- cancer survival
- external validation

## 9. Bibliography

Zhao, Yonghao, et al. “DeSCENT: Deconvolutional Single-Cell RNA-seq Enhances Transcriptome-based Cancer Survival Analysis.” _Bioinformatics_, 2026. [https://doi.org/10.1093/bioinformatics/btag810](https://doi.org/10.1093/bioinformatics/btag810).
