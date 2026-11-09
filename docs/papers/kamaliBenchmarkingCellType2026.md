---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Benchmarking of Cell Type Deconvolution Techniques for Microarray Data

## 기본 정보

- Citation key: `kamaliBenchmarkingCellType2026`
- Item type: journal article
- Authors: Zoha Kamali; Harold Snieder; Ahmad Vaez
- Source: iScience, online 2026-10-29; PubMed indexed 2026-11-07
- Original: [DOI: 10.1016/j.isci.2026.118079](https://doi.org/10.1016/j.isci.2026.118079); [PMID: 42997613](https://pubmed.ncbi.nlm.nih.gov/42997613/); [PMC: PMC13742846](https://pmc.ncbi.nlm.nih.gov/articles/PMC13742846/); [GEO: GSE22886](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE22886)
- 주 카테고리: `Microarray`
- 관련 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

FACS truth가 있는 microarray와 scRNA-seq reference에서 10개 deconvolution 방법과 전처리를 비교해 MuSiC, qprogwc, CIBERSORTx를 상위 방법으로 확인했다.

## 2. 연구 질문

RNA-seq 중심으로 개발된 최신 cell-type deconvolution 방법이 microarray intensity에서도 작동하며, probe 처리·quantile normalization·reference transformation이 성능에 얼마나 영향을 주는가?

## 3. 데이터와 방법

GSE22886의 FACS-separated blood/bone-marrow microarray 114개와 10x PBMC3k scRNA-seq reference를 사용했다. 10개 방법을 probe 선택, quantile normalization, reference log transformation 조건에서 비교하고 PBMC8k reference로 반복 검증했다. Known mixture를 가진 1,000개 pseudo-bulk도 만들었다.

## 4. 핵심 결과

- MuSiC, qprogwc, CIBERSORTx의 최대 Pearson r은 각각 0.74, 0.69, 0.67이었다.
- 전체 probe를 유지한 quantile-normalized microarray와 log-transformed scRNA reference 조합이 전반적으로 유리했다.
- Cell type별 성능 편차가 컸고 일부 가까운 lineage는 낮은 정확도를 보였다.

## 5. 한계

Ground truth가 있는 microarray가 하나뿐이고 혈액 세포에 한정된다. FACS-purified sample과 선형 혼합 pseudo-bulk는 실제 조직의 nonlinear intensity·batch·cell-state shift를 충분히 재현하지 못한다. Reference-free·tissue-specific 방법은 비교에서 제외되었다.

## 6. 재현 또는 활용 포인트

Probe-to-gene mapping, multi-probe 처리, quantile normalization, reference transformation을 고정하고 cell type별 r·RMSE를 보고한다. PBMC3k와 PBMC8k처럼 reference donor를 바꿔 순위 안정성을 확인하고 runtime·memory도 함께 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Legacy transplant microarray에서 kidney/immune scRNA atlas를 reference로 세포 조성을 복원하는 직접적 기준이다. Blood benchmark의 상위 method가 biopsy에서도 최선이라는 보장은 없으므로 histology·flow·spatial proportion이 있는 소규모 truth set으로 다시 검증해야 한다.

## 8. 관련 키워드

- microarray deconvolution
- scRNA-seq reference
- quantile normalization
- cell-type composition

## 9. Bibliography

Kamali, Zoha, Harold Snieder, and Ahmad Vaez. “Benchmarking of Cell Type Deconvolution Techniques for Microarray Data.” _iScience_, 2026. [https://doi.org/10.1016/j.isci.2026.118079](https://doi.org/10.1016/j.isci.2026.118079).
