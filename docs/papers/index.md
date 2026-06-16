# Paper Notes

Zotero와 Obsidian으로 가져온 논문 정리 문서를 모아두는 공간입니다.

## LLM / Transformer

- [Attention Is All You Need](vaswaniAttentionAllYou2023.md)
- [Transformer paper summary](transformer.md)
- [BERT](bert.md)
- [GPT](gpt.md)
- [GPT-2: unsupervised multitask learners](radfordLanguageModelsUnsupervised2019.md)
- [GPT-3: language models are few-shot learners](brownLanguageModelsFewShot2020.md)
- [T5: unified text-to-text transfer learning](raffelExploringLimitsTransfer2020.md)
- [RAG: retrieval-augmented generation](lewisRetrievalAugmentedGeneration2020.md)
- [Chinchilla: compute-optimal LLM training](hoffmannTrainingComputeOptimal2022.md)
- [InstructGPT / RLHF](ouyangTrainingLanguageModels2022.md)
- [LoRA: low-rank adaptation](huLoRALowRank2021.md)
- [LLaMA: open and efficient foundation language models](touvronLLaMAOpenEfficient2023.md)

## Bio AI

- [Single-cell Foundation Models](single-cell-foundation-models.md)
- [Geneformer](theodorisTransferLearningNetwork2023.md)
- [scGPT](cuiScGPTFoundation2024.md)
- [scFoundation](haoLargeScaleFoundation2024.md)
- [scBERT](yangScBERTLargeScale2022.md)
- [CellPLM](wenCellPLMPretraining2023.md)
- [UCE: universal cell embeddings](rosenUniversalCellEmbeddings2023.md)
- [Nicheformer](tejadaLapuertaNicheformer2025.md)
- [TranscriptFormer](pearceTranscriptFormer2025.md)
- [TxFM: masked gene-expression representation learning](kenyonDeanEffectiveBiologicalRepresentation2026.md)
- [SIGnature: single-cell foundation model gene importance](goldScoringGeneImportance2026.md)
- [Causal circuit tracing in single-cell foundation models](kendiukhovCausalCircuitTracing2026.md)
- [Bayesian HPO for scGPT fine-tuning](tayBayesianHyperparameterOptimization2026.md)
- [Learnability of single-cell LLMs](yanEvaluatingLearnabilitySingleCell2026.md)
- [GeneBag](liangGeneBagTrainingCell2024.md)
- [Path-GPTOmic](PathGPTOmicBalancedMultimodal.md)
- [HEIMDALL](haberHEIMDALLDisentanglingTokenizer2026.md)
- [USHER](pratapaUSHERGuidingFoundation2025.md)

## Cancer Transcriptomics / Clinical Prediction

- [EGSP: scFoundation embeddings for survival prediction](liuLeveragingSinglecellFoundation2026.md)
- [COIN: bulk-single-cell drug sensitivity inference](shangguanDrugSensitivityInference2025.md)

## Transcriptomics / Platform

- [RNA-Seq vs Microarray in Activated T Cells](zhaoComparisonRNASeqMicroarray2014.1.16..md)
- [Smart-seq2](picelliSmartSeq2Sensitive2013.md)
- [Drop-seq](macoskoDropSeq2015.md)
- [Seurat spatial reconstruction](satijaSpatialReconstruction2015.md)
- [Spatial transcriptomics](stahlSpatialTranscriptomics2016.md)
- [CITE-seq](stoeckiusCITESeq2017.md)
- [Scanpy](wolfSCANPY2018.md)
- [scVI](lopezDeepGenerativeSingleCell2018.md)
- [Harmony](korsunskyHarmony2019.md)

## 사용 흐름

1. Zotero에 논문과 PDF를 저장한다.
2. Obsidian에서 `Zotero Integration: LLM Wiki Paper Note`를 실행한다.
3. 생성된 `docs/papers/*.md` 문서를 읽고 직접 요약을 채운다.
4. `mkdocs serve`로 확인한다.
5. `git add .`, `git commit`, `git push`로 GitHub Pages에 반영한다.
