---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# EXPRESSO: 암종 간 종양 전사체 기반 치료 반응 예측

## 기본 정보

- Citation key: `palMachineLearningFramework2026`
- Item type: journalArticle
- Authors: Lipika Ray Pal; E. M. Gertz; N. Ulhas Nair; S. Mukherjee; S. Patiyal; T. Cantore; E. M. Campagnolo; T.-G. Chang; S. R. Dhruba; Y. Kim; E. D. Shulman; P. S. Rajagopal; D.-T. Hoang; S. Hannenhalli; A. A. Schäffer; E. Ruppin
- Journal: *Cancer Research* (online 2026-09-24)
- DOI: [10.1158/0008-5472.CAN-25-5220](https://doi.org/10.1158/0008-5472.CAN-25-5220)
- PMID: [42782170](https://pubmed.ncbi.nlm.nih.gov/42782170/)
- Related preprint DOI alias: [10.1101/2025.10.24.684491](https://doi.org/10.1101/2025.10.24.684491) ([bioRxiv v3](https://www.biorxiv.org/content/10.1101/2025.10.24.684491v3))
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`
- 교차 카테고리: `Bulk RNA-seq`, `Microarray`

## 1. 한 줄 요약

EXPRESSO는 암종·플랫폼이 다른 다기관 종양 전사체를 표적·바이오마커 사전지식과 결합해, 여섯 치료군의 반응을 독립 코호트까지 예측한 범암종 기계학습 프레임워크다.

## 2. 연구 질문

치료 전 bulk 종양 전사체만으로 서로 다른 암종, 치료, RNA-seq·microarray 플랫폼을 넘어 치료 반응을 일반화해 예측할 수 있는가? 알려진 약물 표적과 맥락별 바이오마커를 모델에 반영하면 기존 전사체 서명이나 일반 기계학습보다 나은가?

## 3. 데이터와 방법

- 9개 암종, 6개 일차 치료군(anti-PD-1/PD-L1, trastuzumab, bevacizumab, BRAF inhibitor, paclitaxel, FAC/FEC)의 91개 코호트, 5,675명을 통합했다.
- RNA-seq와 microarray를 함께 쓰기 위해 표본 내 유전자 순위 정규화를 적용했다.
- 약물별 LASSO logistic regression을 기본으로, `EXPRESSO-T`는 알려진 표적 유전자를 penalty-free로 두고 `EXPRESSO-B`는 nested leave-one-cohort-out 교차검증 안에서 맥락별 바이오마커를 추가했다.
- 20개 공개 전사체 서명과 다른 기계학습법을 비교하고, 학습에 쓰지 않은 22개 독립·전향 코호트 및 면역관문억제제 무진행생존 자료에서 검증했다.

## 4. 핵심 결과

- 치료군별 평균 ROC-AUC는 0.62–0.73, 반응 odds ratio 중앙값은 2.4–4.6이었다.
- EXPRESSO는 비교한 20개 전사체 서명과 대안 기계학습법보다 전반적으로 높은 성능을 보였고, 독립 코호트에서도 교차검증 결과가 재현됐다.
- 면역관문억제제 모델은 반응뿐 아니라 무진행생존도 층화했다.
- 일부 치료에서는 코호트가 늘어도 성능이 포화돼, bulk 전사체만으로 얻을 수 있는 예측력의 한계도 드러났다.

## 5. 한계

- RNA-seq와 microarray의 기술적 이질성이 크며, 저자들이 시험한 batch correction은 성능을 개선하지 못했다.
- PD-1과 PD-L1 치료를 묶었고 병용요법 코호트도 주된 약물 중심으로 모델링해 치료별 차이를 완전히 분리하지 못한다.
- 이진 반응 예측은 대체 치료 사이의 인과적 선택 모델이 아니며, 중간 수준의 판별력에 대해 보정, 임상적 순효용, 실제 전향 배치 검증이 더 필요하다.

## 6. 재현 또는 활용 포인트

- [GitHub](https://github.com/ruppinlab/EXPRESSO)에 분석·추론 코드, nested 교차검증, 환경 잠금 파일이 공개돼 있다.
- 입력 자료와 재현 산출물은 [Zenodo](https://doi.org/10.5281/zenodo.21878615)에서 제공된다.
- 재사용할 때는 코호트 단위 외부 검증을 유지하고, 독립 시험 코호트의 메타데이터가 특징 선택이나 전처리에 유입되지 않도록 해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

다기관 신장이식 생검 전사체로 거부반응 치료 반응이나 예후를 예측할 때 적용 가능한 설계다. 다만 센터 단위 holdout과 nested 특징 선택을 유지하고, 조직학·DSA·크레아티닌 같은 임상 기준모델 및 치료요법별 보정·의사결정 효용을 함께 평가해야 한다.

## 8. 관련 키워드

- treatment response prediction
- bulk transcriptomics
- pan-cancer
- LASSO
- cross-cohort validation
- RNA-seq / microarray integration

## 9. Bibliography

Pal LR, Gertz EM, Nair NU, et al. A Machine Learning Framework Enables Supervised Treatment Response Prediction from Tumor Transcriptomics across Cancer Types. *Cancer Research*. Published online September 24, 2026. doi:[10.1158/0008-5472.CAN-25-5220](https://doi.org/10.1158/0008-5472.CAN-25-5220). Related preprint: doi:[10.1101/2025.10.24.684491](https://doi.org/10.1101/2025.10.24.684491).
