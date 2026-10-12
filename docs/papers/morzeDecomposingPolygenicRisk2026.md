---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-12'
tags:
- wiki/paper
---

# Decomposing Polygenic Risk of Coronary Artery Disease into Distinct Biological Processes

## 기본 정보

- Citation key: `morzeDecomposingPolygenicRisk2026`
- Item type: preprint
- Authors: Jakub Morze; Katrina Smith; Maciej Kierczak; Göran Bergström; et al.
- Source: medRxiv v1, posted 2026-10-11 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.08.26365088](https://doi.org/10.64898/2026.10.08.26365088)
- 주 카테고리: `GWAS`

## 1. 한 줄 요약

Genome-wide significant CAD variant의 다형질 association matrix를 Bayesian NMF로 분해해 여덟 biological process별 polygenic risk score를 만들고 세 biobank에서 검증했다.

## 2. 연구 질문

하나의 전체 CAD PRS를 lipid, obesity, endothelial, coagulation과 remodeling처럼 개인별로 다른 생물학적 위험 축으로 분해할 수 있는가?

## 3. 데이터와 방법

주로 European ancestry인 일곱 CAD GWAS에서 526개 독립 genome-wide significant variant를 모으고 QC 뒤 78개 CAD-related phenotype association과 Bayesian NMF를 적용했다. 여덟 component별 pPRS를 UK Biobank 458,905명, SCAPIS 24,904명, Mass General Brigham Biobank 53,848명에서 clinical CAD, imaging, biomarker, proteomics, comorbidity와 연관시켰다.

## 4. 핵심 결과

- LDL-rich lipoprotein, triglyceride-rich lipoprotein, Lp(a), metabolically unhealthy normal weight, obesity, endothelial dysfunction, coagulation, cardiac remodeling의 여덟 component를 얻었다.
- 세 cohort에서 pPRS가 임상·subclinical CAD와 일관되게 연관됐고 서로 다른 biomarker·proteomic·comorbidity profile을 보였다.
- Conventional risk factor가 포착하지 못하는 process-specific profile을 분리했다.

## 5. 한계

Genome-wide significant variant만 써서 약한 polygenic component를 놓칠 수 있다. Discovery와 factor decomposition이 주로 European ancestry에 기반했고 다른 ancestry에는 별도 trait matrix가 필요할 수 있다. Risk-factor interaction은 관찰연구이며 제출본의 code availability가 아직 `[TBA]`다.

## 6. 재현 또는 활용 포인트

LD pruning reference, variant–trait matrix 구성, factor 수와 stability를 고정하고 cohort별 calibration을 보고한다. 전체 PRS와 pPRS를 함께 넣어 순증분 정보를 확인하고 ancestry-specific 재학습과 external validation을 분리한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient rejection GWAS가 충분히 커지면 면역, 내피, 응고, fibrosis 같은 process-specific score로 분해해 biopsy pathway score와 연결하는 template가 된다. 현재 CAD component를 이식 outcome에 그대로 옮길 근거는 없다.

## 8. 관련 키워드

- process-specific PRS
- Bayesian non-negative matrix factorization
- coronary artery disease
- multi-biobank validation

## 9. Bibliography

Morze, Jakub, et al. “Decomposing Polygenic Risk of Coronary Artery Disease into Distinct Biological Processes.” medRxiv, 2026. [https://doi.org/10.64898/2026.10.08.26365088](https://doi.org/10.64898/2026.10.08.26365088).
