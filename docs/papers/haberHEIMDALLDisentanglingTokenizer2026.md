---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# HEIMDALL: Disentangling tokenizer design for robust transfer in single-cell foundation models

## 기본 정보

- Citation key: `haberHEIMDALLDisentanglingTokenizer2026`
- Item type: preprint
- Authors: Ellie Haber; Shahul Alam; Nicholas Ho; Renming Liu; Evan Trop; Shaoheng Liang; Muyu Yang; Spencer Krieger; Jian Ma
- DOI: 10.1101/2025.11.09.687403
- URL: [Link](https://www.biorxiv.org/content/10.1101/2025.11.09.687403v3)

## Abstract


Foundation models for single-cell RNA-sequencing (scRNA-seq) data are emerging as powerful tools for single-cell analysis, yet their performance depends critically on how cells are tokenized into model inputs. Single-cell data lack a canonical tokenization scheme, and many design choices in current single-cell foundation models (scFMs) remain heuristic, entangled, and difficult to evaluate. Here, we introduce Heimdall, a unified framework for dissecting and redesigning tokenizers in scFMs. By decomposing existing tokenization strategies into individual design choices, Heimdall enables attribution of the components that underlie robust generalization, allowing more principled design of improved tokenizers. Combining Heimdall with a minimal transformer backbone, we find that tokenizer design is instrumental for generalization in challenging distribution-shift settings such as cross-tissue, cross-species, and cross-gene-panel cell type classification, as well as reverse perturbation prediction. We show that, while tokenizer choice has little effect in scenarios with matched train and test data, it becomes imperative under distribution shift. Rather than identifying a single globally optimal tokenizer, Heimdall reveals that robust transfer depends on a small number of tokenization design axes – especially gene identity, expression encoding, and ordering – that expose different biological priors to the model. In this sense, universal transferability in scFMs still depends on a non-universal tokenizer interface. Together, these findings establish tokenization as a critical design axis in scFMs and provide design principles and reusable infrastructure for more robust scFMs.


## 1. 한 줄 요약

%% begin one-line-summary %%
HEIMDALL은 single-cell foundation model에서 세포를 어떤 token sequence로 바꿀지라는 문제를 모듈로 분해하고, tokenizer 선택이 tissue/species/gene-panel shift와 perturbation task에서 얼마나 중요한지 비교하는 프레임워크다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
scGPT, Geneformer, scFoundation, scBERT, UCE 같은 scFM은 모두 scRNA-seq profile을 transformer 입력으로 바꾸지만, gene identity, expression value, gene order, token selection을 어떻게 설계하는지는 모델마다 다르고 상당히 휴리스틱하다. 기존 benchmark는 model size, pretraining corpus, objective, context length가 함께 달라져 tokenizer 자체가 downstream 성능에 미치는 영향을 분리하기 어려웠다.

이 논문은 "single-cell에는 자연어처럼 정해진 tokenization 문법이 없다"는 문제에서 출발한다. 특히 matched train/test 환경에서는 tokenizer 차이가 작아 보일 수 있지만, 실제 활용에서는 tissue shift, species shift, spatial gene panel shift처럼 입력 분포가 달라지는 상황이 흔하다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
HEIMDALL은 tokenizer를 gene identity encoder(FG), expression encoder(FE), cell constructor(FC)로 나누고, FC를 다시 ORDER, SEQUENCE, REDUCE로 분해한다. 같은 transformer backbone과 같은 training 조건에서 scGPT/Geneformer/scFoundation/scBERT/UCE tokenizer를 재구현해 비교하고, 개별 module을 바꿔가며 어떤 설계가 transfer 성능을 만드는지 ablation한다. 결론은 단일 universal tokenizer가 있다기보다, gene identity, expression encoding, ordering이 task별 biological prior를 다르게 주입한다는 것이다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 cell별 gene expression vector와 gene set이다. HEIMDALL은 이 고차원 expression vector를 sequence model이 받을 수 있는 "cell sentence"로 변환한다.

평가에 사용한 task는 다음과 같다.

- Cross-tissue cell type classification: scTab/CELLxGENE subset에서 colon/small intestine으로 학습하고 brain cell type을 예측
- Cross-species classification: human cell로 학습하고 mouse cell type을 예측, orthology mapping 여부를 비교
- Spatial transcriptomics gene-panel shift: 서로 다른 spatial transcriptomics gene panel 사이에서 cell type classification
- Reverse perturbation prediction: Norman single/double gene knockout dataset에서 control-perturbed pair를 보고 perturbation identity를 예측
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
HEIMDALL은 특정 pretrained scFM 자체를 새로 제안하기보다, tokenizer를 공정하게 비교하기 위한 modular interface를 제안한다.

1. FG(gene identity encoder): gene ID를 embedding으로 바꾼다. 예시는 Gene2vec, ESM2, GenePT, HyenaDNA, random embedding 등이다.
2. FE(expression encoder): expression value를 token feature로 바꾼다. 예시는 integer/quantile binning, continuous encoding, no-op 등이다.
3. FC(cell constructor): gene embedding과 expression embedding을 cell-level token sequence로 조립한다.
4. ORDER: gene token 순서를 정한다. 예시는 expression sorting, chromosome sorting, random order 등이다.
5. SEQUENCE: context length 안에 어떤 gene token을 넣을지 정한다. 예시는 truncation, weighted sampling 등이다.
6. REDUCE: FG와 FE를 더하거나 결합해 최종 token representation을 만든다.
7. 동일한 transformer encoder 또는 비교 가능한 sequence model에 tokenizer output을 넣고 downstream head로 평가한다.

논문은 tokenizer 효과를 분리하기 위해 대부분의 실험에서 대규모 pretraining 없이 scratch training을 사용한다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
주요 downstream objective는 task에 따라 달라진다.

- Cell type classification: [CLS] embedding 기반 multi-class cross-entropy
- Reverse perturbation prediction: paired-cell representation으로 perturbation class를 예측하는 classification loss
- 일부 비교 실험: masked language modeling(MLM) pretraining 후 fine-tuning

핵심은 objective 자체보다, 동일 objective와 backbone을 고정한 상태에서 tokenizer module만 바꿔 성능 차이를 attribution하는 것이다.
%% end method-objective %%

### Output

%% begin method-output %%
출력은 평가 task별 label 또는 score다.

- Cell type label
- Species/tissue/gene-panel shift 상황에서의 cell type prediction
- Perturbation identity 또는 top-k perturbation 후보
- Module ablation별 MCC, hit-rate, UMAP/confusion matrix 등 비교 결과
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
HEIMDALL의 tokenizer abstraction을 보여준다. Single-cell expression profile에서 gene identity와 expression value를 받아 FG, FE, FC 모듈을 거쳐 cell sentence를 만들고, 이를 transformer에 입력하는 흐름이다. Figure 1B는 Gene2vec/ESM2/GenePT 같은 FG, binning/continuous encoding 같은 FE, expression sorting/random/chromosome sorting과 sampling/truncation 같은 FC 구성요소 예시를 보여준다. Figure 1C는 이 구조로 기존 tokenizer 비교, module ablation, 새 tokenizer 조합을 할 수 있음을 정리한다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
Cross-tissue generalization benchmark를 보여준다. Colon/small intestine cell로 학습하고 brain cell을 평가했을 때 tokenizer 간 MCC 차이는 크지 않았고, Geneformer-tok이 약간 높았지만 raw expression linear baseline과 비슷한 수준이었다. Context length는 2,048 token 근처까지 도움이 되고 이후 plateau가 나타났으며, Geneformer-tok ablation에서는 expression-based ORDER가 cross-tissue 성능에 중요한 요소로 나타났다.
%% end figure-2 %%

## 6. 장점

%% begin strengths %%
- Tokenizer를 FG, FE, FC/ORDER/SEQUENCE/REDUCE로 분해해 scFM 설계 차이를 공정하게 비교할 수 있게 했다.
- "큰 pretrained model끼리 비교"가 아니라 같은 backbone/조건에서 tokenizer만 바꾸는 실험이라 원인 분석력이 좋다.
- Tissue, species, gene-panel, perturbation처럼 실제 single-cell 전이에서 자주 만나는 distribution shift를 나눠 평가했다.
- 결론이 실용적이다. IID 환경에서는 tokenizer 차이가 작지만, OOD transfer에서는 gene identity, expression encoding, ordering이 중요하다는 설계 원칙을 준다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- Scratch training 중심 실험이므로, 대규모 pretraining을 충분히 한 실제 scFM의 최종 성능을 그대로 대변한다고 보기는 어렵다.
- Benchmark task가 cell type classification과 reverse perturbation에 집중되어 있어, batch integration, trajectory, regulatory network inference 등에는 추가 검증이 필요하다.
- Tokenizer 외에도 data curation, model scale, training objective, context length가 실제 scFM 성능에 큰 영향을 줄 수 있다.
- "최적 tokenizer" 하나를 제시하기보다는 task별 trade-off를 보여주는 논문이라, 내 데이터에 바로 적용하려면 별도 ablation이 필요하다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection 연구에서는 scRNA-seq reference atlas와 bulk biopsy RNA-seq 사이에 tissue/protocol/gene-panel shift가 존재할 가능성이 크다. HEIMDALL식 ablation을 이용하면 gene ID embedding, expression binning, expression sorting/ranking 중 어떤 tokenization이 rejection phenotype transfer에 중요한지 분리해 볼 수 있다.

특히 biopsy bulk RNA-seq를 single-cell foundation model 입력으로 바꿀 때, Geneformer식 rank tokenization과 scFoundation/scGPT식 expression encoding을 같은 downstream classifier에서 비교하는 실험이 좋다. Rejection subtype, Banff grade, graft survival task에서 tokenizer가 성능과 calibration에 미치는 영향을 먼저 확인하면 이후 모델 선택 근거가 훨씬 강해진다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- HEIMDALL
- Single-cell foundation model
- Tokenizer
- Gene identity encoder
- Expression encoder
- Cell sentence
- Distribution shift
- Cross-tissue transfer
- Cross-species transfer
- Gene-panel shift
- Reverse perturbation prediction
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%


아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv/Europe PMC 공개 본문과 abstract를 기준으로 채웠다.

%% end annotations %%

## 11. Bibliography

Haber, Ellie, Shahul Alam, Nicholas Ho, 기타. “HEIMDALL: Disentangling Tokenizer Design for Robust Transfer in Single-Cell Foundation Models”. Preprint, bioRxiv, 2026년 4월 12일. [https://doi.org/10.1101/2025.11.09.687403](https://doi.org/10.1101/2025.11.09.687403).


%% Import Date: 2026-05-27T13:33:36.024+09:00 %%
