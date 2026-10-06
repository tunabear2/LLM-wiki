---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-07'
tags:
- wiki/paper
---

# Cell-based polygenic risk scores predict clinical progression in Alzheimer’s disease

## 기본 정보

- Citation key: `sahelijoCellBasedPolygenicRisk2026`
- Item type: journalArticle
- Authors: Nathan Sahelijo; Priya Rajagopalan; Lu Qian; Rufuto Rahman; Daniel Goldstein; Sophia I. Thomopoulos; David A. Bennett; Lindsay A. Farrer; Thor D. Stein; Li Shen; Heng Huang; Kwangsik Nho; Andrew J. Saykin; Christos Davatzikos; Paul M. Thompson; Julia Tcw; Gyungah R. Jun; et al.
- Journal: Alzheimer’s & Dementia 22(10):e71895 (2026; indexed 2026-10-06)
- DOI: [10.1002/alz.71895](https://doi.org/10.1002/alz.71895); PMID: [42836738](https://pubmed.ncbi.nlm.nih.gov/42836738/)
- 주 카테고리: `GWAS`

## 1. 한 줄 요약

snRNA-seq coexpression network에서 만든 cell-based PRS를 ADNI·FHS 임상자료와 연결하고 PageRank로 후보 약물 표적을 우선순위화했다.

## 2. 연구 질문

세포 유형별 genetic risk가 임상 진행과 영상·amyloid 지표를 예측하며 network-based therapeutic target을 제안할 수 있는가?

## 3. 데이터와 방법

단일핵 transcriptome coexpression network에서 cell-specific gene set을 만들고 GWAS summary statistics로 PRS를 계산했다. ADNI와 Framingham Heart Study의 진행·영상 phenotype을 분석한 뒤 PageRank drug network와 hiPSC astrocyte 실험으로 후보를 점검했다.

## 4. 핵심 결과

cell-based PRS는 임상 진행 위험과 연관되었고 보고된 hazard ratio 범위는 1.25–2.02였다. imaging/amyloid signal과 연결되는 세포 네트워크 및 estradiol·levetiracetam 같은 후보를 제시했으며, 일부는 APOE/C4 관련 astrocyte readout에서 감소를 보였다.

## 5. 한계

AD-specific cohort와 prefrontal network, 제한적인 network sample, ancestry 편향 및 microglia representation 문제가 있다. PageRank/database 의존성과 in-vitro astrocyte 검증은 임상 효능을 입증하지 않는다.

## 6. 재현 또는 활용 포인트

GWAS ancestry와 cell-type reference를 일치시키고 PRS construction, network edge direction, drug database version을 고정한다. clinical-only, conventional PRS, cell-based PRS의 incremental value를 독립 cohort에서 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

직접적인 이식 논문은 아니지만, rejection GWAS를 cell-state network와 연결하고 예후·약물 후보를 우선화하는 분석 template를 제공한다. 신장에서는 tubular·endothelial·immune reference와 HLA/ancestry confounding을 새로 검증해야 한다.

## 8. 관련 키워드

- cell-based PRS
- snRNA-seq coexpression
- GWAS integration
- drug target prioritization

## 9. Bibliography

Sahelijo, Nathan, et al. “Cell-based Polygenic Risk Scores Predict Clinical Progression and Prioritize Network-based Therapeutic Targets in Alzheimer’s Disease.” *Alzheimer’s & Dementia*, 2026. [https://doi.org/10.1002/alz.71895](https://doi.org/10.1002/alz.71895).
