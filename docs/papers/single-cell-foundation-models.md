# Single-cell Foundation Models

## 1. 한 줄 요약

Single-cell foundation model은 대규모 single-cell omics data로 pretraining한 모델을 cell type annotation, perturbation prediction, gene network analysis, disease modeling 등에 transfer하는 접근이다.

## 2. 배경

scRNA-seq 데이터는 빠르게 축적되고 있지만 dataset마다 batch, tissue, protocol, label 체계가 다르다. Foundation model은 많은 cell과 gene expression pattern을 미리 학습해 작은 downstream dataset에서도 더 나은 representation을 제공하려고 한다.

## 3. 핵심 아이디어

Cell을 하나의 문서처럼, gene을 token처럼 보고 Transformer류 모델을 적용한다. 모델은 masked gene prediction, generative reconstruction, contrastive learning 등으로 gene-gene, cell-cell, tissue context를 학습한다.

## 4. 대표 모델

| Model | 핵심 아이디어 | 활용 |
| --- | --- | --- |
| Geneformer | rank-based gene token sequence와 masked learning | network biology, perturbation, disease modeling |
| scGPT | generative pretrained transformer for single-cell multi-omics | annotation, batch correction, perturbation, multi-omics |
| scBERT/scFoundation 계열 | gene expression representation pretraining | cell annotation, transfer learning |

## 5. 주의점

- Gene vocabulary와 input preprocessing이 모델마다 다르다.
- Pretraining data와 내 dataset의 tissue/domain 차이가 성능에 영향을 준다.
- Attention이 곧 causal gene regulation이라는 뜻은 아니다.
- Downstream task에서는 baseline model과 external validation이 필요하다.

## 6. 내 연구에 적용할 아이디어

- Kidney transplant rejection dataset에서 patient/cell embedding을 추출한다.
- Rejection-related immune cell subtype annotation을 보조한다.
- Gene perturbation 또는 marker gene prioritization을 후보 생성 도구로 사용한다.
- 모델 embedding과 clinical covariate를 결합해 rejection prediction을 시도한다.

## 7. 관련 자료

- [Geneformer Nature paper](https://www.nature.com/articles/s41586-023-06139-9)
- [scGPT Nature Methods paper](https://www.nature.com/articles/s41592-024-02201-0)

## 8. 최근 추가 논문

| Paper | Source/date | DOI/URL | 한 줄 요약 | 관련성 |
| --- | --- | --- | --- | --- |
| [TxFM: Effective Biological Representation Learning by Masking Gene Expression](kenyonDeanEffectiveBiologicalRepresentation2026.md) | arXiv, 2026-05-29 | [10.48550/arXiv.2605.31562](https://doi.org/10.48550/arXiv.2605.31562) | RNA-seq count에 맞춘 masked autoencoder와 curated corpus로 transcriptomics representation을 학습한다. | Kidney transplant rejection bulk/pseudobulk RNA-seq에서 raw expression 대비 pretrained embedding의 추가 가치를 비교하는 후보 모델이다. |
| [SIGnature: Scoring gene importance by interpreting single-cell foundation models](goldScoringGeneImportance2026.md) | PubMed / Nature Biotechnology, 2026-05-27 | [10.1038/s41587-026-03112-5](https://doi.org/10.1038/s41587-026-03112-5) | Single-cell foundation model attribution으로 gene importance를 계산해 atlas-scale disease signature를 검색한다. | Rejection-associated immune cell state에서 DEG를 넘어 context-specific regulatory gene 후보를 찾는 데 유용하다. |
| [Causal circuit tracing reveals distinct computational architectures in single-cell foundation models](kendiukhovCausalCircuitTracing2026.md) | PubMed / Bioinformatics, 2026-06 watch window | [10.1093/bioinformatics/btag379](https://doi.org/10.1093/bioinformatics/btag379) / [PMID:42296381](https://pubmed.ncbi.nlm.nih.gov/42296381/) | Geneformer와 scGPT 내부 SAE feature circuit을 ablation으로 추적해 coherence와 causal encoding의 한계를 평가한다. | Rejection marker를 scFM 해석으로 뽑을 때 causal claim을 피하고 perturbation/external cohort 검증을 붙여야 한다는 기준을 준다. |
| [Bayesian Hyperparameter Optimization Improves scGPT Fine-Tuning for Single-Cell Multi-Omics Integration](tayBayesianHyperparameterOptimization2026.md) | PubMed / Bioinformatics, 2026-06 watch window | [10.1093/bioinformatics/btag374](https://doi.org/10.1093/bioinformatics/btag374) / [PMID:42286785](https://pubmed.ncbi.nlm.nih.gov/42286785/) | scGPT fine-tuning hyperparameter를 Bayesian optimization으로 찾으면 multi-omics integration 성능과 재현성을 높일 수 있다. | Kidney transplant scRNA/spatial/bulk integration에서 fold 내부 HPO와 external validation을 분리하는 실험 설계에 직접 참고된다. |
| [Evaluating the learnability of single-cell large language models on multiple tasks](yanEvaluatingLearnabilitySingleCell2026.md) | PubMed / BMC Genomics, 2026-06 watch window | [10.1186/s12864-026-12975-6](https://doi.org/10.1186/s12864-026-12975-6) / [PMID:42249309](https://pubmed.ncbi.nlm.nih.gov/42249309/) | Geneformer/scGPT의 장점이 task별로 다르며, perturbation prediction에서는 scaling만으로 충분하지 않을 수 있음을 보인다. | Rejection annotation, prognosis, perturbation 후보 생성 task마다 raw expression과 단순 baseline을 별도 비교해야 한다는 근거다. |
| [Single-Cell Cross-Modal Transfer by Adversarial Fine-Tuning of Foundation Models](boydSingleCellCrossModal2026.md) | arXiv, 2026-06-04 | [10.48550/arXiv.2606.07676](https://doi.org/10.48550/arXiv.2606.07676) | Single-cell foundation model을 adversarial fine-tuning해 unpaired ST와 scRNA-seq 사이의 cross-modal translation을 수행한다. | Paired spatial biopsy가 부족한 kidney transplant cohort에서 immune cell state와 tissue neighborhood를 연결하는 후보 접근이다. |
| [Integrating gene regulatory priors into Transformer attention with scTransformer for interpretable scRNA-seq analysis](miliaScTransformerRegulatoryPriors2026.md) | arXiv, 2026-06-08 | [10.48550/arXiv.2606.09558](https://doi.org/10.48550/arXiv.2606.09558) | Gene regulatory prior로 Transformer attention을 제약해 single-cell representation의 해석성과 cell type 분리를 개선하려 한다. | Rejection regulatory program 해석에서 attention 기반 설명을 prior-constrained model과 비교하는 기준이 된다. |
| [Finetuning masking challenges narrow-task evaluation of cell foundation models](shakeelFinetuningMaskingCellFM2026.md) | bioRxiv, 2026-06-06 | [10.64898/2026.06.04.730272](https://doi.org/10.64898/2026.06.04.730272) | Fine-tuning이 pretraining data scale 차이를 가려 좁은 task benchmark로는 scFM representation quality를 평가하기 어렵다고 주장한다. | Rejection prediction에서는 fine-tuned accuracy만 보지 말고 frozen embedding, linear probe, cross-center transfer를 같이 평가해야 한다. |
| [Stack: In-Context Learning of Single-Cell Biology](dongStackInContextSingleCell2026.md) | bioRxiv revised v2, 2026-06-08 | [10.64898/2026.01.09.698608](https://doi.org/10.64898/2026.01.09.698608) | Context cell 예시를 사용해 fine-tuning 없이 perturbation, donor effect, disease condition을 예측하려는 in-context single-cell foundation model이다. | Donor-specific rejection response, cytokine stimulation, steroid response를 patient context에 맞춰 예측하는 실험 설계에 맞다. |
| [HoloCell: A Generative Foundation Model for Holistic Cellular Modeling](jiangHoloCellGenerativeFoundation2026.md) | bioRxiv, 2026-06-11 | [10.64898/2026.06.07.730684](https://doi.org/10.64898/2026.06.07.730684) | Epigenome, transcriptome, proteome을 함께 다루는 대규모 multimodal generative single-cell foundation model이다. | Modality가 부분적으로만 있는 transplant multi-omics cohort에서 missing-modality-aware integration 후보가 된다. |
| [Cellfm-datasets: A Unified Data Infrastructure for Single-Cell and Spatial Transcriptomics Foundation Model Pretraining](zhangCellfmDatasets2026.md) | bioRxiv, 2026-06-14 | [10.64898/2026.06.11.731508](https://doi.org/10.64898/2026.06.11.731508) | H5AD cohort를 sparse memmap과 Hugging Face dataset interface로 바꿔 sc/spatial transcriptomics FM pretraining IO를 안정화한다. | Multi-center kidney transplant H5AD/spatial corpus를 만들 때 metadata, spatial block, distributed sampling 설계에 참고된다. |
| [Elucidating the Design Space of Generative Models for Single-Cell Perturbation Prediction](bhattacharyaDesignSpacePerturbation2026.md) | bioRxiv, 2026-06-18 | [10.64898/2026.06.15.732063](https://doi.org/10.64898/2026.06.15.732063) | ExpressionVAE는 unordered expression을 discrete latent code로 압축해 perturbation-conditioned generative prediction을 수행한다. | Steroid/cytokine response나 anti-rejection therapy signature simulation에서 scFM 기반 perturbation baseline으로 비교할 수 있다. |
| [Benchmarking gene expression reconstruction from single-cell latent representations](fuBenchmarkingGeneExpressionReconstruction2026.md) | bioRxiv, 2026-06-18 | [10.64898/2026.06.15.731445](https://doi.org/10.64898/2026.06.15.731445) | ReconEval은 single-cell latent representation과 foundation model embedding에서 gene expression을 얼마나 충실히 복원하는지 평가한다. | Predicted rejection cell state를 gene/pathway 수준으로 해석하기 전 marker와 IFN/endothelial program 보존성을 점검하는 데 필요하다. |
| [CellTosg2Sequence: A Unified Text-Omics-Signaling-Graph Large Language Model for Single-Cell Analysis](chenCellTosg2SequenceUnified2026.md) | bioRxiv, 2026-06-22 | [10.64898/2026.06.16.732397](https://doi.org/10.64898/2026.06.16.732397) | Biomedical text prior와 signaling graph token을 cell sentence에 붙여 cell type annotation과 해석을 수행한다. | Banff lesion, alloimmune pathway, IFN/TNF signaling prior를 rejection cell annotation에 넣는 설계 후보가 된다. |
| [OmniCell: Unified Foundation Modeling of Single-Cell and Spatial Transcriptomics for Cellular and Molecular Insights](pangOmniCellUnified2026.md) | bioRxiv revised v3, 2026-06-23 | [10.64898/2025.12.29.696804](https://doi.org/10.64898/2025.12.29.696804) | scRNA-seq와 spatial transcriptomics를 함께 학습해 expression program을 tissue context와 연결한다. | Rejection immune infiltrate를 tubulitis, glomerulitis, peritubular capillaritis 같은 spatial lesion context와 함께 해석하는 데 맞다. |
| [Systematic benchmarking of zero-shot utility and robustness in single-cell transcriptomic foundation models](liuSystematicBenchmarkingZeroShot2026.md) | bioRxiv, 2026-06-23 | [10.64898/2026.06.18.733285](https://doi.org/10.64898/2026.06.18.733285) | 20개 representation과 1,607개 dataset을 비교해 zero-shot scFM utility와 robustness가 task별로 엇갈림을 보인다. | Cross-center rejection prediction에서 HVG/PCA, pathway score, scFM embedding을 함께 비교해야 한다는 benchmark 근거다. |
| [CellOS: Learning a World Model of Cellular State through Joint Embedding Prediction](zhouCellOSWorldModel2026.md) | bioRxiv revised v2, 2026-06-25 | [10.64898/2026.06.18.733163](https://doi.org/10.64898/2026.06.18.733163) | Expression view와 perception view를 joint embedding prediction으로 정렬하는 12B 규모 cellular world model이다. | Annotation, integration, perturbation response를 함께 다루는 rejection workflow 후보지만 compute와 validation 비용을 먼저 따져야 한다. |
| [VCBench: A Multi-Dimensional Benchmark for Single-Cell Foundation Models](weidenerVCBenchMultiDimensional2026.md) | bioRxiv, 2026-06-23 | [10.64898/2026.06.18.733146](https://doi.org/10.64898/2026.06.18.733146) | Virtual cell capability를 7개 dimension으로 나눠 scFM과 단순 baseline을 비교하고 contamination reporting을 요구한다. | Rejection 연구에서 perturbation, modality integration, temporal progression claim을 분리 평가하는 체크리스트가 된다. |
| [Glitch genes: embedding geometry predicts functional fragility in single-cell foundation models](whalleyGlitchGenesEmbedding2026.md) | bioRxiv, 2026-06-27 | [10.64898/2026.06.22.733850](https://doi.org/10.64898/2026.06.22.733850) | Geneformer/scGPT/scFoundation embedding geometry로 outlier gene을 찾아 perturbation 해석 취약성을 점검한다. | IFN, HLA, cytotoxicity, endothelial marker를 scFM attribution으로 해석하기 전 embedding audit을 붙이는 근거다. |
| [PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction](wuPerturbCellRLVerifierGuided2026.md) | arXiv, 2026-06-26 | [10.48550/arXiv.2606.27752](https://doi.org/10.48550/arXiv.2606.27752) | Pretrained single-cell transcriptomic generator를 verifier reward 기반 RL로 post-training해 perturbation response의 DEG/pathway 일관성을 높인다. | Rejection perturbation simulation에서 IFN, cytotoxicity, endothelial activation 같은 pathway-specific verifier를 설계하는 기준이 된다. |
| [Partial-label metric ceilings for evaluating gene regulatory networks inferred from single-cell foundation models](kendiukhovPartialLabelMetric2026.md) | PubMed / BioSystems, 2026-06-30 | [10.1016/j.biosystems.2026.105864](https://doi.org/10.1016/j.biosystems.2026.105864) / [PMID:42379339](https://pubmed.ncbi.nlm.nih.gov/42379339/) | Incomplete curated GRN reference의 observed F1/AUPR ceiling을 계산해 scGPT-derived regulatory edge 평가를 보정한다. | Rejection regulatory network benchmark에서 literature bias와 partial label coverage를 분리해 보고해야 한다는 기준이다. |
| [Causal intervention validation of gene regulatory signals in scGPT](kendiukhovCausalInterventionValidation2026.md) | PubMed / Journal of Biomedical Informatics, 2026-07-03 | [10.1016/j.jbi.2026.105080](https://doi.org/10.1016/j.jbi.2026.105080) / [PMID:42398561](https://pubmed.ncbi.nlm.nih.gov/42398561/) | scGPT gene token intervention은 일부 tissue의 curated TF-target reference와 맞지만 CRISPR perturbation transfer는 AUROC가 거의 random이다. | Kidney rejection marker/TF edge를 scGPT로 뽑을 때 model-internal hypothesis와 biological causality를 분리해야 한다. |
| [Tabular Foundation Models Are Competitive Cellular Perturbation Predictors Across Biological Scales](pallaTabularFoundationModels2026.md) | bioRxiv revised v2, 2026-07-02 | [10.64898/2026.06.28.735106](https://doi.org/10.64898/2026.06.28.735106) | TabICL/TabPFN 같은 tabular FM이 scGPT, STACK 등 specialized single-cell perturbation model과 경쟁하거나 더 나을 수 있음을 보인다. | Rejection perturbation/therapy response 예측에서 scFM만 쓰지 말고 tabular FM, CatBoost, linear/pathway baseline을 함께 비교해야 한다. |
| [Raw-count embeddings improve single-cell foundation models](schledeRawCountEmbeddings2026.md) | bioRxiv, 2026-07-03 | [10.64898/2026.06.29.735389](https://doi.org/10.64898/2026.06.29.735389) | Gene Intelligence는 log1p raw count를 직접 token embedding에 넣어 rank/normalization 없이도 큰 scFM과 경쟁한다. | Kidney transplant scRNA-seq에서 normalization/tokenization choice가 HLA/IFN/endothelial marker 보존성에 미치는 영향을 따로 검증해야 한다. |
| [Task-adapted biological foundation models uncover perturbation-centric representations](parejaLorenteTaskAdaptedBiological2026.md) | bioRxiv, 2026-07-05 | [10.64898/2026.06.30.735584](https://doi.org/10.64898/2026.06.30.735584) | scGPT를 LINCS L1000 perturbation identity objective로 fine-tuning해 perturbation-centric embedding과 MOA/target 관계 회수를 개선한다. | IFN/TNF, ischemia-reperfusion, immunosuppression response 같은 rejection-relevant perturbation objective 설계에 참고된다. |
| [scVision: A vision foundation model for single-cell biology via spatial gene cartography](yesilogluScVision2026.md) | arXiv, 2026-07-15 | [10.48550/arXiv.2607.14163](https://doi.org/10.48550/arXiv.2607.14163) | Cell transcriptome을 gene co-expression layout 위의 이미지로 렌더링해 vision transformer가 expression magnitude와 gene 관계를 함께 학습한다. | Rejection scRNA-seq에서 token-based scFM과 vision-style embedding이 HLA/IFN/endothelial program을 얼마나 보존하는지 비교할 후보 모델이다. |
| [Foundation model reveals the shared organization of transcription and topologically associating domains](liangFoundationModelReveals2026.md) | PubMed / Cell Systems, 2026-07 watch window | [10.1016/j.cels.2026.101675](https://doi.org/10.1016/j.cels.2026.101675) / [PMID:42468531](https://pubmed.ncbi.nlm.nih.gov/42468531/) | 33M transcriptome foundation model의 contextual similarity로 TAD 내부 co-regulation 구조를 분석한다. | Rejection DEG와 pathway를 TAD/chromatin context와 함께 해석할 때 가설 생성용 transcriptome representation으로 참고된다. |
| [What topological and geometric structure do biological foundation models learn? Evidence from 141 hypotheses](kendiukhovTopologicalGeometric2026.md) | PubMed / PLOS ONE, 2026-07 watch window | [10.1371/journal.pone.0344826](https://doi.org/10.1371/journal.pone.0344826) / [PMID:42467671](https://pubmed.ncbi.nlm.nih.gov/42467671/) | scGPT/Geneformer embedding의 topology, manifold geometry, cross-model alignment를 null control과 함께 대규모로 검정한다. | Rejection marker나 regulatory edge를 scFM embedding geometry로 제안할 때 tissue-specific null control과 external validation을 요구하는 근거다. |

## 9. Paper watch 기록

- [2026-06-08 single-cell FM paper watch](../reports/single-cell-fm-paper-watch-2026-06-08.md): 첫 실행 기록, 추가 논문, 중복/false positive 제외 기준, MkDocs 검증 상태를 정리했다.
