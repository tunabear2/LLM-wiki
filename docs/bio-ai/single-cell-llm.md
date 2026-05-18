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
