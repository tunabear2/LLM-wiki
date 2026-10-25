---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# DNA Methylation Subtypes Inferred from Transcriptomes Guide Sunitinib and Immunotherapy Selection in Renal Cancer

## 기본 정보

- Citation key: `jeanneretDNAMethylationSubtypes2026`
- Item type: bioRxiv preprint
- Authors: F. Jeanneret; S. Schoch; P. Ballester; S. N. Symeonides; A. Laird; H. Axelson; D. Pflieger; C. Battail
- Source: bioRxiv v2, revised 2026-10-21 (not peer reviewed)
- Original: [DOI: 10.1101/2024.11.05.622095](https://doi.org/10.1101/2024.11.05.622095)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

Clear-cell renal-cell carcinoma의 DNA methylation subtype을 9개 gene-expression ratio로 복원해 sunitinib과 immune-checkpoint regimen의 서로 다른 progression-free-survival 패턴을 제시했다.

## 2. 연구 질문

CcRCC methylation heterogeneity를 transcriptome만으로 재현하고 metastatic therapy 선택과 연결할 수 있는가?

## 3. 데이터와 방법

727개 ccRCC tumor의 methylation meta-analysis로 네 기존 signature를 benchmark하고 hyper-methylated subtype을 정의했다. 589개 matched transcriptome으로 proliferation, endothelial tip-cell, DNMT3B/TET2 program을 분석하고 9개 gene ratio classifier를 만든 뒤 independent cohort와 네 treatment cohort에서 평가했다.

## 4. 핵심 결과

- Hyper-methylated subtype은 약 15%였고 overall survival이 짧았다.
- 9-ratio expression classifier는 독립 cohort에서 methylation subtype을 AUC-ROC 0.96으로 예측했다.
- 예측 hyper-methylated primary tumor는 atezolizumab+bevacizumab이 sunitinib보다 유리했고, hypo-methylated metastasis는 sunitinib 이득이 더 컸다.

## 5. 한계

치료 cohort의 retrospective 비교라 치료 배정과 primary/metastatic tissue 차이의 교란을 배제하지 못한다. 15% subtype의 사건 수와 cohort 간 assay 차이에 민감할 수 있으며 prospective biomarker-guided trial 검증이 없다.

## 6. 재현 또는 활용 포인트

Classifier의 9개 ratio, subtype threshold와 primary/metastasis를 고정해 cohort-held-out 재현을 한다. Treatment interaction은 prognostic main effect와 분리하고 clinical covariate를 포함한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney tissue의 latent epigenetic state를 compact expression ratio로 옮기는 설계는 rejection subtype에도 참고할 수 있다. 다만 renal cancer biology와 면역억제·allograft rejection은 다르므로 marker를 직접 전이하면 안 된다.

## 8. 관련 키워드

- Cancer Transcriptomics / Clinical Prediction
- Bulk RNA-seq
- renal cell carcinoma
- treatment response

## 9. Bibliography

Jeanneret, F., et al. “DNA Methylation Subtypes Inferred from Transcriptomes Guide Sunitinib and Immunotherapy Selection in Renal Cancer.” bioRxiv, v2, 2026. [https://doi.org/10.1101/2024.11.05.622095](https://doi.org/10.1101/2024.11.05.622095).
