# Single-cell LLM

## 핵심 요약

Single-cell LLM은 자연어 LLM의 tokenization, pretraining, transfer learning 아이디어를 single-cell omics 데이터에 적용하는 모델군이다. Gene, cell, perturbation, tissue context를 token 또는 embedding으로 표현해 downstream biological task에 활용한다.

## 자연어 LLM과의 대응

| NLP | Single-cell |
| --- | --- |
| Word/token | Gene, peak, protein, perturbation |
| Sentence/document | Cell, sample, patient |
| Corpus | Cell atlas, multi-omics atlas |
| Masked word prediction | Masked gene prediction |
| Text generation | Expression reconstruction, perturbation response prediction |

## 주요 task

- Cell type annotation
- Batch integration
- Perturbation prediction
- Drug response prediction
- Disease state classification
- Gene program discovery

## 중요한 설계 질문

- Gene order가 없는 데이터에서 sequence를 어떻게 정의할 것인가?
- Expression magnitude를 token에 어떻게 결합할 것인가?
- Batch/tissue/species 정보를 어떻게 condition으로 넣을 것인가?
- Cell-level output을 patient-level prediction으로 어떻게 aggregate할 것인가?

## 내 연구에 적용할 아이디어

Kidney transplant rejection에서는 single-cell LLM embedding을 immune cell subtype, rejection grade, clinical covariate와 함께 분석할 수 있다. 특히 patient-level label이 있을 때 cell-level representation을 어떻게 요약할지가 핵심이다.

## 관련 자료

- [Geneformer](https://www.nature.com/articles/s41586-023-06139-9)
- [scGPT](https://www.nature.com/articles/s41592-024-02201-0)

## 대표 Paper Notes

- [Geneformer](../papers/theodorisTransferLearningNetwork2023.md): rank-based gene token과 network biology transfer.
- [scGPT](../papers/cuiScGPTFoundation2024.md): generative pretrained transformer for single-cell multi-omics.
- [scFoundation](../papers/haoLargeScaleFoundation2024.md): large-scale single-cell transcriptomics foundation model.
- [scBERT](../papers/yangScBERTLargeScale2022.md): BERT식 pretraining을 cell type annotation에 적용한 초기 모델.
- [CellPLM](../papers/wenCellPLMPretraining2023.md): cell-cell relation을 반영하려는 cell language model.
- [UCE](../papers/rosenUniversalCellEmbeddings2023.md): tissue/species를 넘는 universal cell embedding.
- [Nicheformer](../papers/tejadaLapuertaNicheformer2025.md): single-cell과 spatial omics context를 함께 다루는 모델.
- [TranscriptFormer](../papers/pearceTranscriptFormer2025.md): cross-species generative cell atlas.

## 읽는 순서

1. [scBERT](../papers/yangScBERTLargeScale2022.md)로 "BERT idea가 scRNA-seq로 어떻게 옮겨졌는지"를 본다.
2. [Geneformer](../papers/theodorisTransferLearningNetwork2023.md), [scGPT](../papers/cuiScGPTFoundation2024.md), [scFoundation](../papers/haoLargeScaleFoundation2024.md)을 비교해 tokenization과 objective 차이를 잡는다.
3. [UCE](../papers/rosenUniversalCellEmbeddings2023.md), [Nicheformer](../papers/tejadaLapuertaNicheformer2025.md), [TranscriptFormer](../papers/pearceTranscriptFormer2025.md)로 cross-species/spatial 방향을 확장한다.
4. [Learnability benchmark](../papers/yanEvaluatingLearnabilitySingleCell2026.md)와 [causal circuit tracing](../papers/kendiukhovCausalCircuitTracing2026.md)으로 모델 한계를 같이 점검한다.
