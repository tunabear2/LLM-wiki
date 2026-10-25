---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# corrdeconv Corrects Deconvolution's Misreading of Disease Cell States as Abundance

## 기본 정보

- Citation key: `jiangCorrdeconvCorrectsDeconvolution2026`
- Item type: bioRxiv preprint
- Authors: H. Jiang; F. Gao; P. Liu; Y. Wu; Y. Jie; Y. Li; Y. Jiang
- Source: bioRxiv v1, posted 2026-10-24 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.19.760015](https://doi.org/10.64898/2026.10.19.760015); [code and derived data](https://doi.org/10.5281/zenodo.23354822)
- 주 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

corrdeconv는 disease-state expression shift가 bulk·methylation·spatial deconvolution의 cell proportion으로 오인되는 문제를 실제 cell count와 downstream gene-list 오류로 평가·교정한다.

## 2. 연구 질문

Per-sample correlation이 높은 deconvolution 결과도 disease-induced cell-state 변화 때문에 잘못된 abundance effect를 만들 수 있는가, 그리고 count evidence로 이를 줄일 수 있는가?

## 3. 데이터와 방법

26개 disease의 8,465명·specimen에서 same-person cell count와 inferred proportion을 대조하고 28개 방법을 평가했다. Proportion error 대신 count-refuted disease effect와 gene-list error로 correction을 선택하는 corrdeconv를 만들고 published analysis와 R4RA trial subgroup 결정을 replay했다.

## 4. 핵심 결과

- Blood disease effect 2,660개 중 1,119개(42%)가 실제 count와 반대였고, 그중 96%는 per-sample correlation 또는 cross-method agreement 기준을 통과했다.
- DREAM primary-metric rank와 refutation rank의 상관은 0.10이었다.
- Target-cohort count 없이도 DREAM winner보다 refuted effect를 46% 줄였고, count가 있을 때 replay된 20개 잘못된 결정을 모두 교정했다.

## 5. 한계

우열은 저자가 정의한 count-refuted effect와 gene-list error에 기반하고, count assay 자체의 sampling·compartment 차이도 남는다. 모든 tissue와 새 disease cohort에서 prospective하게 검증된 것은 아니며 preprint의 강한 성능 주장은 독립 재현이 필요하다.

## 6. 재현 또는 활용 포인트

MIT-licensed package와 derived data가 Zenodo에 공개된다. Reconstruction correlation뿐 아니라 paired histology/flow count, disease-effect direction, downstream DEG/pathway 변경을 함께 평가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Allograft biopsy에서 activated tubular/immune state를 cell 수 증가로 오해할 위험을 직접 다룬다. Deconvolution proportion은 matched histology, flow cytometry 또는 spatial count로 교차검증한 뒤 rejection association에 사용해야 한다.

## 8. 관련 키워드

- Bulk RNA-seq
- deconvolution
- cell-state confounding
- benchmark

## 9. Bibliography

Jiang, H., et al. “corrdeconv Corrects Deconvolution's Misreading of Disease Cell States as Abundance, Overturning Benchmarks and Outperforming Every Published Deconvolution Method.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.19.760015](https://doi.org/10.64898/2026.10.19.760015).
