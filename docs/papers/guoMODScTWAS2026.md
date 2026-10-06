---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# MOD-scTWAS: Leveraging gene co-expression for single-cell transcriptome-wide association studies

## 기본 정보

- Citation key: `guoMODScTWAS2026`
- Item type: preprint
- Authors: Hanmin Guo; Yao Lu; Lin Hou
- Source: bioRxiv v2 (posted 2026-09-30; not peer reviewed)
- DOI: [10.64898/2026.09.24.754034](https://doi.org/10.64898/2026.09.24.754034); [bioRxiv v2](https://www.biorxiv.org/content/10.64898/2026.09.24.754034v2)
- 주 카테고리: `GWAS`
- 교차 카테고리: `scRNA-seq`

## 1. 한 줄 요약

MOD-scTWAS는 cell-type별 coexpression module을 이용해 genetically regulated expression을 공동 추정하고, gene 간 correlation을 무시하는 scTWAS보다 예측력을 높인다.

## 2. 연구 질문

gene coexpression과 heteroscedastic/cross-gene structure를 이용하면 single-cell TWAS의 GReX 예측과 trait association power를 개선할 수 있는가?

## 3. 데이터와 방법

OneK1K 14 cell type에서 module 기반 GReX를 학습하고 기존 scTWAS와 mean R² 및 imputable cell-type/gene pair를 비교했다. UK Biobank quantitative hematology phenotype에 적용해 cell-type–gene association을 평가했다.

## 4. 핵심 결과

14개 cell type 모두에서 mean GReX R²가 개선되었고 imputable pair가 8,343개에서 8,695개로 늘었다. UKBB 분석은 방법별 유의한 cell-type/gene 조합을 추가로 회수해 immune trait 해석 가능성을 넓혔다.

## 5. 한계

stepwise와 joint estimation을 직접 비교하지 않았고, rare cell type과 bulk-derived BloodGen3 module 의존성이 남는다. 공개 코드와 frozen model artefact가 명확하지 않아 독립 재현성이 제한된다.

## 6. 재현 또는 활용 포인트

OneK1K reference, GWAS ancestry, LD panel, module version을 고정하고 conventional scTWAS·bulk TWAS와 동일한 multiple-testing 절차를 적용한다. cell-type-specific module이 tissue context에서 유지되는지 외부 single-cell cohort로 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 rejection GWAS를 immune·tubular cell type의 genetically regulated transcriptome과 연결하는 후보 방법이다. donor/recipient ancestry와 cell composition을 분리하고, eQTL prediction이 실제 biopsy expression과 맞는지 paired cohort에서 확인해야 한다.

## 8. 관련 키워드

- single-cell TWAS
- coexpression module
- genetically regulated expression
- GWAS–transcriptomics integration

## 9. Bibliography

Guo, Hanmin, Yao Lu, and Lin Hou. “MOD-scTWAS: Leveraging Gene Co-expression for Single-cell Transcriptome-wide Association Studies.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.24.754034](https://doi.org/10.64898/2026.09.24.754034).
