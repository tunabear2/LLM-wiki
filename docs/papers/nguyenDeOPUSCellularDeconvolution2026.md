---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# DeOPUS: power 변환과 shrinkage를 이용한 세포 조성 추정

## 기본 정보

- Citation key: `nguyenDeOPUSCellularDeconvolution2026`
- Item type: journalArticle
- Authors: Ha Nguyen; Khoi Nguyen; Phi Bya; Tarik Alafif; Tho T. Quan; Tin Nguyen
- Journal: *Briefings in Bioinformatics*. 2026;27(5):bbag524
- DOI: [10.1093/bib/bbag524](https://doi.org/10.1093/bib/bbag524)
- PMID: [42799697](https://pubmed.ncbi.nlm.nih.gov/42799697/)
- PMCID: [PMC13615545](https://pmc.ncbi.nlm.nih.gov/articles/PMC13615545/)
- 주 카테고리: `Bulk RNA-seq`
- 교차 카테고리: `Cancer Transcriptomics / Clinical Prediction`, `scRNA-seq`

## 1. 한 줄 요약

DeOPUS는 bulk와 single-cell reference의 동적 범위·이분산성·이상치 문제를 적응형 power 변환과 계층적 shrinkage로 완화해, 광범위한 조직의 세포 조성 추정 정확도를 높였다.

## 2. 연구 질문

reference 기반 bulk transcriptome deconvolution에서 유전자 발현의 극단적 동적 범위, 이분산성, 이상치가 만드는 오차를 데이터 적응형 변환과 shrinkage로 줄일 수 있는가?

## 3. 데이터와 방법

- 적응형 power 변환, 다단계 prior shrinkage, 순위 기반 quantile normalization을 결합한 hierarchical shrinkage transformation(HST) 뒤 선형 unmixing을 수행했다.
- DeconBenchmark/CELLxGENE로 만든 122개 사람 조직, 467명 donor, 1,241개 세포 유형의 pseudobulk 1,046개를 donor-pair holdout으로 평가했다.
- MuSiC, FARDEEP, AutoGeneS, AdRoit, CIBERSORT, Scaden, TAPE, DECODE와 비교하고, 실험적으로 세포 비율이 측정된 18개 실제 bulk 자료에서도 검증했다.

## 4. 핵심 결과

- pseudobulk에서 평균 Pearson 0.82, Spearman 0.77, MSE 0.007을 기록해 두 번째 방법의 0.75/0.68보다 높았다.
- 대부분의 조직·기관계에서 최상위였고, 세포 유형 수가 늘어나는 복잡한 혼합에서도 상대적 우위를 유지했다.
- 실제 자료 18개 모두에서 양의 상관을 보인 유일한 방법이었으며, 우세 세포 유형 추정에서도 가장 좋은 성능을 보였다.

## 5. 한계

- 완전하고 대표적인 reference와 선형 혼합 가정에 의존한다.
- reference에 없는 세포 유형, 큰 조성 변화, reference와 bulk 사이의 batch 차이는 여전히 오차를 만든다.
- 실제 암 조직에서 조성의 정답이 있는 검증은 제한적이고, 추정 불확실성을 직접 제공하지 않는다.
- chromatin이나 spatial 자료로의 직접 전이는 검증하지 않았다.

## 6. 재현 또는 활용 포인트

- 오픈소스 R 구현과 benchmark 코드는 [GitHub](https://github.com/tinnlab/DeOPUS)에 공개됐다.
- 실제 bulk 검증 자료와 산출물은 [Zenodo](https://doi.org/10.5281/zenodo.19050845)에서 제공된다.
- 재현 시 reference 구성과 유전자 scale을 동일하게 유지하고 donor 단위 holdout을 사용해야 한다. 전체 상관뿐 아니라 세포 유형별 오차와 unknown-content 민감도도 보고하는 것이 좋다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장 single-cell/single-nucleus reference로 이식신 bulk 생검의 면역·실질세포 비율을 추정하는 데 활용할 수 있다. 다만 활성화된 거부반응 세포 상태가 reference에 없을 수 있으므로 조직학, IHC, spatial 또는 single-cell 자료와 교차 검증해야 한다.

## 8. 관련 키워드

- cellular deconvolution
- bulk RNA-seq
- single-cell reference
- power transformation
- shrinkage
- benchmark

## 9. Bibliography

Nguyen H, Nguyen K, Bya P, Alafif T, Quan TT, Nguyen T. DeOPUS: cellular deconvolution via optimized power-transformed unmixing with shrinkage. *Briefings in Bioinformatics*. 2026;27(5):bbag524. doi:[10.1093/bib/bbag524](https://doi.org/10.1093/bib/bbag524).
