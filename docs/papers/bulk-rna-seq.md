---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Bulk RNA-seq Analysis Paper Notes

Bulk RNA-seq 논문은 sample/patient-level expression을 임상 phenotype, survival, drug response, platform transfer와 연결하는 관점에서 모아둔다. 분석 기본기는 read alignment/quantification, normalization, differential expression, pathway interpretation, patient-level modeling 순서로 공부한다.

## 핵심 질문

- Bulk RNA-seq의 tissue-level mixture signal을 foundation model embedding이 raw expression보다 더 잘 요약하는가?
- scRNA-seq로 pretraining한 모델이 bulk RNA-seq downstream task로 transfer될 때 어떤 조건에서 유리하거나 무너지는가?
- Bulk, pseudobulk, microarray 사이의 scale, dynamic range, zero/low-expression 차이를 어떤 전처리로 흡수할 수 있는가?
- Kidney transplant rejection/prognosis에서는 raw gene-space, pretrained embedding, clinical covariate를 어떻게 결합해야 external validation에서 버티는가?

## 공부 순서

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [STAR: ultrafast universal RNA-seq aligner](dobinSTARUltrafast2013.md) | Splice-aware RNA-seq read alignment | BAM 기반 QC, junction/fusion, allele-specific expression까지 확장할 때 기본 aligner |
| [kallisto: near-optimal probabilistic RNA-seq quantification](brayKallistoNearOptimal2016.md) | Pseudoalignment 기반 transcript quantification | 빠른 transcript/gene abundance 추정과 bootstrap uncertainty 이해 |
| [Salmon: fast and bias-aware transcript quantification](patroSalmonFast2017.md) | Bias-aware lightweight transcript quantification | alignment-free quantification, tximport 기반 gene-level DE workflow 후보 |
| [TMM normalization](robinsonScalingNormalization2010.md) | RNA composition bias 보정 | Bulk/pseudobulk count 비교에서 library size만으로 부족한 이유를 이해하는 핵심 |
| [DESeq2](loveDESeq2Moderated2014.md) | Negative binomial GLM, dispersion/LFC shrinkage | 소표본 rejection cohort에서 안정적인 DEG 분석 baseline |
| [voom-limma](lawVoomPrecision2014.md) | Mean-variance trend와 precision weights | 복잡한 design matrix, batch/covariate 포함 DE 분석 baseline |

## 임상/모델링 확장

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [TxFM: Effective Biological Representation Learning by Masking Gene Expression](kenyonDeanEffectiveBiologicalRepresentation2026.md) | RNA-seq count에 맞춘 masked autoencoder와 curated corpus | Bulk/pseudobulk rejection task에서 raw expression 대비 pretrained embedding의 추가 가치를 비교하는 후보 |
| [GeneBag](liangGeneBagTrainingCell2024.md) | Single-cell pretraining 후 GTEx/TCGA bulk RNA-seq 임상 task로 확장 | Bulk biopsy RNA-seq를 unordered gene bag으로 넣어 rejection grade, survival, prognosis target을 예측하는 설계 참고 |
| [EGSP: scFoundation embeddings for survival prediction](liuLeveragingSinglecellFoundation2026.md) | TCGA bulk RNA-seq에서 scFoundation embedding, gene expression, clinical variables를 결합한 survival model | Graft survival, rejection-free survival, eGFR decline 예측에서 embedding+gene+clinical 구조를 이식 가능 |
| [COIN: bulk-single-cell drug sensitivity inference](shangguanDrugSensitivityInference2025.md) | Labeled bulk RNA-seq와 unlabeled scRNA-seq를 contrastive learning으로 연결 | Bulk rejection label을 scRNA-seq cell state score로 전이하는 bridge model 아이디어 |
| [RNA-Seq vs Microarray in Activated T Cells](zhaoComparisonRNASeqMicroarray2014.1.16..md) | RNA-seq와 microarray의 dynamic range, low-expression, isoform 차이 | Microarray/bulk RNA-seq/scRNA-seq transfer에서 platform shift를 해석하는 기본 근거 |

## 관련 Article / Report Scraps

- [Benchmarking Gene Expression Foundation Models on Bulk RNA-Seq Data](../articles/2026-05-27-bulk-rnaseq-foundation-model-benchmark.md): TCGA bulk RNA-seq task에서 single-cell foundation model과 bulk-specific model을 비교한 conference abstract 정리.

## 읽을 때 체크할 것

- 입력 단위가 sample, patient, pseudobulk, cell 중 무엇인지 구분한다.
- Count, TPM/FPKM, RMA, log1p CPM, rank token, quantile binning처럼 preprocessing이 model input과 맞는지 확인한다.
- Fold 안에서 gene selection, survival-associated gene selection, HPO가 끝나는지 확인한다.
- Bulk-to-scRNA, scRNA-to-bulk 방향을 분리해서 해석한다.
- External cohort 성능이 raw expression baseline, linear model, clinical-only model보다 실제로 나은지 본다.
