---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# 방광암의 종양세포 MHC-II 프로그램과 면역관문억제제 성적

## 기본 정보

- Citation key: `bellmuntTumorCellMHCII2026`
- Item type: preprint
- Authors: Joaquim Bellmunt; Y. Xie; M. Gómez Muñoz; S. Kukreja; S. Walker; R. He; R. Li; X. Qiu; T. Zhang; P. Rodriguez; D. Garcia Gonzalez; I. Epstein; J. Parera; N. Juanpere; M. Lorenzo; O. Buisan; J. Senserrich; P. Servian; T. Silva; M. Brown; M. Cabrera; P. Cejas; H. W. Long
- Source: bioRxiv (posted 2026-09-22; not peer reviewed)
- DOI: [10.64898/2026.09.21.753036](https://doi.org/10.64898/2026.09.21.753036)
- Original: [bioRxiv v1](https://www.biorxiv.org/content/10.64898/2026.09.21.753036v1)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`
- 교차 카테고리: `Bulk RNA-seq`, `scRNA-seq`

## 1. 한 줄 요약

단일세포·크로마틴·조직 검증으로 정의한 방광암 종양세포 고유 MHC-II 프로그램이 초기 진행 위험과 pembrolizumab·atezolizumab 치료 성적을 층화했다.

## 2. 연구 질문

면역세포가 아닌 종양세포에서 발현되는 MHC-II 프로그램이 방광암 병기 전반의 면역 상태와 예후를 설명하고, TMB·PD-L1을 넘어 면역관문억제제 반응과 연관되는가?

## 3. 데이터와 방법

- single-nucleus/single-cell RNA-seq와 122개 검체의 HLA-DR 면역조직화학으로 MHC-II 신호의 악성 상피세포 기원을 확인했다.
- ATAC-seq, IFN-γ 자극 세포주·일차 종양 자료를 결합해 11유전자 종양세포 MHC-II 프로그램을 구성했다.
- NMIBC 434명, 수술 전 pembrolizumab PURE-01 82명, 전이성 atezolizumab IMvigor210 288명에서 진행, 병리학적 완전반응, 재발·전체생존과의 연관성을 평가했다.

## 4. 핵심 결과

- 약 3분의 1의 방광암에서 종양세포 MHC-II가 관찰됐다.
- luminal NMIBC에서 MHC-II-low 군의 진행 위험이 높았다(HR 3.31, 95% CI 1.37–7.99).
- PURE-01의 병리학적 완전반응률은 MHC-II-high 52%, low 24%였고(P=0.018), 재발 없는 생존도 차이가 났다(P=0.0054). TMB와 PD-L1을 함께 고려해도 연관성이 유지됐다.
- 방광 원발 전이암에서는 전체생존과 연관됐지만(HR 0.62, 95% CI 0.44–0.89), 상부요로 원발암에서는 재현되지 않았고 원발 부위 상호작용은 P=0.0018이었다.

## 5. 한계

- 두 면역관문억제제 코호트가 단일군이어서 예후 표지와 치료 선택용 예측 표지를 구분할 수 없다.
- 전이암 원발 부위 분석은 사후 분석이며, TCR·ex vivo 하위 분석의 표본 수가 작다.
- bulk 점수에는 전문 항원제시세포 신호가 섞일 수 있고, 절단값과 임상 측정법은 전향적으로 검증해야 한다.
- 동료평가 전 preprint이며, 저자들이 바이오마커 관련 특허 이해관계를 공개했다.

## 6. 재현 또는 활용 포인트

- 연구 생성 RNA/ATAC/single-cell 자료는 [GEO GSE334331](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE334331)에 공개됐다.
- 공개 분석 도구로 [VIPER](https://bitbucket.org/cfce/viper/src/master/)와 [CHIPS](https://github.com/liulab-dfci/CHIPS)를 사용했지만, 논문 전체를 한 번에 재현하는 전용 저장소는 제시되지 않았다.
- bulk 코호트에서 사용할 때는 single-cell 또는 공간 자료로 발현 세포 기원을 확인하고, TMB·PD-L1·병기 기준모델 대비 추가 가치를 평가해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

IFN-γ/JAK-STAT/MHC-II 축과 세포 기원 구분은 거부반응 생검에서 이식신 실질세포의 활성과 침윤 면역세포 신호를 분리하는 데 유용한 관점이다. 다만 암 치료용 점수와 절단값을 이식신에 직접 전용할 수는 없으며, 공간·single-cell 또는 조직염색 검증이 필요하다.

## 8. 관련 키워드

- bladder cancer
- tumor-cell MHC-II
- immune checkpoint blockade
- single-cell transcriptomics
- chromatin accessibility
- biomarker validation

## 9. Bibliography

Bellmunt J, Xie Y, Gómez Muñoz M, et al. A tumor-cell MHC-II program is associated with checkpoint-blockade outcomes across stages of bladder cancer. *bioRxiv*. Posted September 22, 2026. doi:[10.64898/2026.09.21.753036](https://doi.org/10.64898/2026.09.21.753036).
