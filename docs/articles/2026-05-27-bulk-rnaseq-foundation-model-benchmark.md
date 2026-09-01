---
type: article
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/article
---

# Benchmarking Gene Expression Foundation Models on Bulk RNA-Seq Data

저장일: 2026-05-27

## 기본 정보

- Type: conference abstract / poster abstract
- Source: Cancer Research, AACR Annual Meeting 2026 abstract 5478
- Title: Abstract 5478: Benchmarking gene expression foundation models on bulk RNA-Seq data
- Authors: Jong Hyun Kim; Sunwoo Yu; Soonyoung Lee; Tae Hyun Hwang; Jongseong Jang; Janghyeon Lee
- Published: 2026-04-03 online; AACR Annual Meeting 2026, 2026-04-17 to 2026-04-22
- DOI: [10.1158/1538-7445.AM2026-5478](https://doi.org/10.1158/1538-7445.AM2026-5478)
- URL: [AACR Journals](https://aacrjournals.org/cancerres/article/86/7_Supplement/5478/778323/Abstract-5478-Benchmarking-gene-expression)
- Local source: downloaded PDF, not committed to repo
- Topic: bulk RNA-seq, single-cell foundation model transfer, TCGA benchmark

## 한 줄 요약

Single-cell RNA foundation model을 bulk RNA-seq에 그대로 적용할 수 있는지 TCGA downstream task로 비교한 conference abstract이다. CellFM과 scFoundation은 bulk task에서도 비교적 잘 일반화했고, scBERT/scLong은 제한적이었으며, 핵심은 model size보다 pretraining이 gene-gene biological relationship을 얼마나 잘 포착했는지에 있다고 해석한다.

## 배경

최근 scRNA foundation model은 cell type 전반의 gene-gene relationship을 학습한다는 장점 때문에 bulk RNA-seq에도 적용되고 있다. 하지만 single-cell data는 sparse하고 cell-level representation을 학습하는 반면, bulk RNA-seq는 tissue-level mixture와 평균화된 expression을 담는다.

따라서 중요한 질문은 다음과 같다.

- scRNA 기반 foundation model이 bulk RNA-seq tissue data로 정말 transfer되는가?
- bulk RNA-seq로 학습된 모델, 예: BulkFormer, 과 비교했을 때 어떤 모델이 강한가?
- 성능 차이가 모델 크기 때문인지, pretraining objective와 biological prior 때문인지 구분할 수 있는가?

## Method

데이터와 평가:

- Dataset: TCGA bulk RNA-seq
- 비교 모델:
  - Single-cell models: `CellFM`, `GeneFormer`, `scBERT`, `scFoundation`, `scGPT`, `scLong`
  - Bulk model: `BulkFormer`
- Embedding extraction:
  - 각 모델의 published procedure를 따른다.
  - 명시되지 않은 경우 valid gene token에 대해 average pooling을 적용한다.
  - expression input은 각 모델의 original preprocessing에 맞춰 normalization한다.
- Evaluation:
  - fixed embedding 위에 linear probe를 학습한다.
  - Hyperparameter tuning 후 best configuration으로 final evaluation한다.
  - 10 random data splits 평균으로 결과를 낸다.

Downstream task:

| Task | Metric |
| --- | --- |
| Gene mutation classification | AUROC |
| Survival prediction | C-index |

## 주요 결과

### Pan-cancer mutation prediction

6개 biomarker gene mutation prediction task에서의 AUROC:

| Model | AUROC |
| --- | ---: |
| CellFM | 0.870 ± 0.053 |
| scFoundation | 0.858 ± 0.056 |
| BulkFormer | 0.827 ± 0.058 |
| GeneFormer | 0.822 ± 0.060 |
| scGPT | 0.673 ± 0.077 |
| scBERT | 0.614 ± 0.054 |
| scLong | 0.597 ± 0.053 |

해석:

- CellFM과 scFoundation이 가장 좋은 성능을 보였다.
- BulkFormer는 bulk-specific model임에도 mutation classification에서는 CellFM/scFoundation보다 낮고 GeneFormer와 비슷한 수준이다.
- scGPT는 이 abstract의 mutation prediction benchmark에서는 중간 이하 성능으로 보인다.
- scBERT와 scLong은 bulk RNA-seq transferability가 제한적이었다.

### Subtype-specific mutation tasks

BRCA, COAD, LUAD, RCC의 subtype-specific mutation task에서도 비슷한 추세가 보고되었다.

- CellFM과 scFoundation이 top performance를 유지
- BulkFormer가 그 다음 그룹
- scBERT와 scLong은 제한적 generalization

### Survival prediction

14개 cancer type survival prediction의 C-index:

| Model | C-index |
| --- | ---: |
| BulkFormer | 0.839 ± 0.086 |
| scFoundation | 0.672 ± 0.081 |
| CellFM | 0.665 ± 0.078 |
| scBERT | 0.599 ± 0.054 |
| scLong | 0.589 ± 0.052 |

주의: abstract 문장에는 scFoundation/CellFM이 best overall이고 BulkFormer와 comparable하다고 되어 있지만, 제시된 수치만 보면 BulkFormer가 훨씬 높다. 따라서 survival result는 원문 poster 또는 full result table을 다시 확인해야 한다.

## 내 연구와 연결

장기 이식 예후 예측에서 bulk RNA-seq/microarray training data와 scRNA-seq test data를 함께 쓰는 상황과 직접 연결된다.

- scRNA model이라고 해서 bulk RNA-seq로 자동 generalize되는 것은 아니다.
- 모델별 pretraining 방식, gene tokenization, pooling strategy가 bulk transfer 성능에 큰 영향을 줄 수 있다.
- scGPT는 내 rejection pipeline에서 kidney-specific pretrained embedding으로 유용했지만, 이 TCGA benchmark에서는 mutation task 성능이 낮게 나온다. 따라서 scGPT 하나만 고정하지 말고 CellFM, scFoundation, GeneFormer, BulkFormer 계열도 후보로 비교할 가치가 있다.
- Fixed embedding + linear probe만으로 평가했기 때문에, adapter fine-tuning이나 domain-specific head를 붙이면 결과가 달라질 수 있다.
- Tissue-level bulk task에서는 gene-gene interaction뿐 아니라 tumor purity, cell composition, pathway-level signal이 중요하므로 pathway aggregation head와 patient-level calibration이 필요하다.

## 실험 아이디어

1. 현재 scGPT rejection pipeline에 같은 평가 프레임으로 CellFM/scFoundation embedding을 추가한다.
2. `CLS`, mean pooling, attention pooling, pathway pooling을 모델별로 고정해 pooling effect를 분리한다.
3. Bulk/microarray training -> scRNA-seq test뿐 아니라, scRNA-seq pseudobulk -> bulk/microarray test 방향도 비교한다.
4. Gene mutation classification처럼 label이 gene-specific인 task와 rejection/survival처럼 pathway/cell-composition dependent task를 분리해서 해석한다.
5. Fixed encoder + linear probe, adapter head, last-n fine-tuning을 같은 split에서 비교한다.

## 주의할 점 / 한계

- Conference abstract라 full method와 full table이 제한적이다.
- TCGA oncology benchmark이므로 kidney transplant rejection이나 graft prognosis로 바로 일반화하면 안 된다.
- 모델별 preprocessing이 다르므로 성능 차이가 tokenizer/preprocessing 차이인지 model representation 차이인지 추가 ablation이 필요하다.
- Linear probe benchmark는 representation quality를 보기에 좋지만, task-specific fine-tuning 성능과는 다를 수 있다.
- Survival prediction 수치와 textual interpretation 사이에 불일치가 있어 원문 poster 확인이 필요하다.

## 관련 문서

- [Transplant Prognosis Model Notes](../reports/transplant-prognosis-model-notes.md)
- [scGPT Rejection End-to-End v3/v4](../code/logs/2026-05-26-scgpt-rejection-end2end-v3-v4.md)
- [Single-cell Foundation Models](../papers/single-cell-foundation-models.md)
- [RNA-Seq vs Microarray in Activated T Cells](../papers/zhaoComparisonRNASeqMicroarray2014.1.16..md)
