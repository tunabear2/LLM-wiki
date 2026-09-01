---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# scRNA-seq Analysis Paper Notes

scRNA-seq 논문은 cell-level expression, cell-state representation, batch/platform integration, multimodal analysis, foundation model transfer를 중심으로 모아둔다. Kidney transplant biopsy에서는 cell type annotation 자체보다 rejection-associated cell state를 patient-level outcome과 어떻게 연결할지가 핵심이다.

## 핵심 질문

- Cell-level representation이 donor, protocol, tissue, disease-state batch effect를 넘어 재사용 가능한가?
- scRNA-seq foundation model embedding이 DEG, pathway score, pseudobulk baseline보다 어떤 정보를 더 주는가?
- Cell-level prediction을 patient-level rejection/prognosis로 올릴 때 어떤 pooling이 안정적인가?
- Bulk/microarray label을 scRNA-seq cell state로 전이할 때 cell type identity와 phenotype signal을 동시에 보존할 수 있는가?

## 공부 순서

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [Smart-seq2](picelliSmartSeq2Sensitive2013.md) | Full-length single-cell transcriptome profiling | Plate/full-length protocol과 droplet UMI data의 차이를 이해하는 배경 |
| [Drop-seq](macoskoDropSeq2015.md) | Droplet barcode 기반 high-throughput scRNA-seq | 10x류 biopsy atlas의 dropout, doublet, capture bias 해석 |
| [Scanpy](wolfSCANPY2018.md) | Python single-cell analysis toolkit | QC, normalization, clustering, marker detection, AnnData workflow |
| [scran deconvolution normalization](lunPoolingNormalizeSingleCell2016.md) | Pooling/deconvolution 기반 size factor estimation | Sparse single-cell count에서 library-size normalization의 한계 이해 |
| [Seurat anchor-based integration](stuartComprehensiveIntegration2019.md) | Cross-dataset/cross-modality anchor integration | 여러 scRNA-seq cohort를 합치거나 reference mapping할 때 기본 논문 |
| [scVI](lopezDeepGenerativeSingleCell2018.md) | Deep generative model for noisy single-cell counts | Batch correction, latent variable baseline, uncertainty-aware representation |
| [Harmony](korsunskyHarmony2019.md) | Fast embedding-level batch integration | Cross-donor/cross-cohort correction baseline |
| [Seurat WNN multimodal integration](haoIntegratedMultimodalSingleCell2021.md) | RNA, protein, chromatin 등 multimodal weighted-nearest neighbor | CITE-seq/spatial/scATAC를 biopsy state 해석에 연결하는 배경 |

## Foundation Model / Representation

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [Single-cell Foundation Models](single-cell-foundation-models.md) | scRNA-seq foundation model 전체 지도 | scGPT, Geneformer, scFoundation, CellPLM 계열을 비교하는 출발점 |
| [Geneformer](theodorisTransferLearningNetwork2023.md) | Rank-based gene token과 network biology transfer | Rejection marker gene prioritization, perturbation hypothesis 생성 후보 |
| [scGPT](cuiScGPTFoundation2024.md) | Generative pretrained transformer for single-cell multi-omics | Kidney biopsy scRNA-seq annotation, integration, rejection embedding baseline |
| [scFoundation](haoLargeScaleFoundation2024.md) | Large-scale single-cell transcriptomics foundation model | Bulk/pseudobulk biopsy embedding과 survival/rejection prediction 후보 |
| [scBERT](yangScBERTLargeScale2022.md) | BERT-style pretraining for cell type annotation | Early scRNA language model baseline |
| [CellPLM](wenCellPLMPretraining2023.md) | Cell-cell relation까지 고려하는 pretrained model | Patient/sample context를 반영하는 cell representation 아이디어 |
| [UCE](rosenUniversalCellEmbeddings2023.md) | Universal cell embeddings | Cross-species/cross-tissue embedding reference |
| [Nicheformer](tejadaLapuertaNicheformer2025.md) | Single-cell and spatial omics foundation model | Spatial biopsy와 scRNA-seq 연결 후보 |
| [TranscriptFormer](pearceTranscriptFormer2025.md) | Cross-species cell atlas generative model | Cell atlas-scale generalization 참고 |
| [SIGnature](goldScoringGeneImportance2026.md) | Single-cell foundation model attribution으로 gene importance scoring | Rejection-associated cell state에서 DEG를 넘어 context-specific gene 후보 탐색 |
| [Causal circuit tracing](kendiukhovCausalCircuitTracing2026.md) | scFM 내부 feature/circuit 해석과 한계 | scFM attribution 결과를 causal claim으로 과해석하지 않는 기준 |
| [Bayesian HPO for scGPT fine-tuning](tayBayesianHyperparameterOptimization2026.md) | scGPT fine-tuning hyperparameter optimization | Fold 내부 HPO와 external validation 분리 설계 |
| [Learnability of single-cell LLMs](yanEvaluatingLearnabilitySingleCell2026.md) | Task별 scFM learnability 평가 | Annotation, perturbation, prognosis task를 따로 baseline 비교해야 한다는 근거 |
| [HEIMDALL](haberHEIMDALLDisentanglingTokenizer2026.md) | Tokenizer design과 transfer robustness | Gene tokenization/normalization ablation 후보 |
| [USHER](pratapaUSHERGuidingFoundation2025.md) | OOD embedding drift correction | scRNA-seq, spatial, Xenium 등 platform drift 보정 아이디어 |

## Platform / Analysis Methods

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [Smart-seq2](picelliSmartSeq2Sensitive2013.md) | Full-length single-cell transcriptome profiling | Full-length protocol과 droplet UMI data 차이를 이해하는 배경 |
| [Drop-seq](macoskoDropSeq2015.md) | Droplet-based high-throughput scRNA-seq | 10x류 biopsy atlas의 dropout, doublet, capture bias 해석 |
| [Scanpy](wolfSCANPY2018.md) | Python single-cell analysis toolkit | QC, normalization, clustering, marker detection, scVI/scGPT 연동 |
| [scVI](lopezDeepGenerativeSingleCell2018.md) | Deep generative model for single-cell transcriptomics | Batch correction, latent variable baseline |
| [Harmony](korsunskyHarmony2019.md) | Single-cell batch integration | Cross-donor/cross-cohort embedding correction baseline |
| [CITE-seq](stoeckiusCITESeq2017.md) | Single-cell RNA + surface protein measurement | Transcriptome만으로 부족한 immune phenotype 보완 |
| [Seurat spatial reconstruction](satijaSpatialReconstruction2015.md) | Single-cell expression과 spatial pattern 연결 | scRNA-seq cell state를 tissue context로 해석하는 배경 |
| [Spatial transcriptomics](stahlSpatialTranscriptomics2016.md) | Tissue section gene expression mapping | Rejection lesion 위치와 cell state를 연결하는 후속 축 |

## 읽을 때 체크할 것

- Cell type annotation 성능과 patient-level phenotype prediction 성능을 분리해서 본다.
- Pretraining tissue, vocabulary, normalization, max sequence length가 내 kidney data와 맞는지 확인한다.
- Cell-level score를 patient-level score로 올릴 때 mean, median, p60/p75, MIL pooling을 비교한다.
- External scRNA-seq cohort에서는 common gene 재학습과 기존 checkpoint 재사용을 나누어 평가한다.
- Embedding이 biological state보다 protocol/platform을 먼저 분리하는지 domain classifier 또는 UMAP으로 점검한다.
