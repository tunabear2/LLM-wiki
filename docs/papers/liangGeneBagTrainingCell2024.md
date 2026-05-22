# GeneBag: training a cell foundation model for broad-spectrum cancer diagnosis and prognosis with bulk RNA-seq data

## 기본 정보

- Citation key: `liangGeneBagTrainingCell2024`
- Item type: preprint
- Authors: Yuhu Liang; Dan Li; Aguix Guohua Xu; Yan Shao; Kun Tang
- DOI: 10.1101/2024.06.27.601098
- URL: [Link](https://www.biorxiv.org/content/10.1101/2024.06.27.601098v1)

## Abstract


초록
광범위한 단일 세포 시퀀싱 데이터를 활용하여 세포 내 포괄적인 유전자-유전자 상호작용 네트워크를 캡슐화하기 위해 수많은 사전 학습 세포 기초 모델(CFM)이 구축되었습니다. 이 모델들은 세포 유형 주석, 교란 추론, 세포 상태 임베딩 등 다양한 세포 생물학 응용 분야에서 가능성을 보여주었습니다. 그러나 특히 암 진단 및 예후에서의 임상 유용성은 아직 미해결 과제입니다. 우리는 GeneBag 모델을 소개합니다. 이는 연속적인 발현 값과 전체 유전자 목록을 가진 '순서가 없는 유전자 가방'으로 세포를 표현하는 새로운 CFM입니다. 단일 세포 데이터로 사전 학습되고 대량 RNA-seq 데이터셋에서 미세 조정된 GeneBag은 암 진단 및 예후 시나리오에서 우수한 성능을 보여줍니다. 제로 샷 학습 환경에서 GeneBag은 암 및 비암 조직을 약 96.2%의 정확도로 분류할 수 있습니다. 미세 조정을 통해 40가지 암 유형과 해당 정상 생검을 전체 정확도 약 97.2%로 주석을 달 수 있습니다. 특히 방광암(93%)과 위암(90%)과 같은 까다로운 암 분류에 뛰어납니다. 더불어 GeneBag은 68.5%의 정확도와 5년 생존 예측(AUC)으로 약 80.4%의 암 병기 분류가 가능합니다. 이 연구는 RNA 기반 암 진단 및 예후에서 CFM의 잠재력을 처음으로 입증한 연구로, AI 보조 분자 진단의 유망한 길을 시사합니다.


## 1. 한 줄 요약

%% begin one-line-summary %%
GeneBag은 single-cell foundation model을 bulk RNA-seq 암 진단과 예후 예측으로 옮기기 위해, 세포/조직을 순서 없는 전체 유전자 bag과 연속 expression 값으로 표현하는 모델이다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
기존 single-cell foundation model은 주로 cell type annotation, perturbation prediction, cell state embedding처럼 single-cell 수준 task에서 성능을 보였다. 하지만 임상에서는 bulk RNA-seq가 더 널리 쓰이고, 암 진단/예후는 제한된 biomarker panel이나 암종별 end-to-end 모델에 의존하는 경우가 많았다.

이 논문이 겨냥한 한계는 두 가지다.

- Gene expression은 자연어처럼 고정된 단어 순서가 있는 sequence가 아니라, 유전자 ID와 연속 expression 값의 unordered set에 가깝다.
- 기존 암 RNA 모델은 특정 암종/작은 label set에 갇히기 쉬워, pan-cancer diagnosis와 prognosis로 일반화하기 어렵다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
GeneBag은 positional embedding 대신 gene ID embedding과 continuous expression embedding을 결합하고, 입력 유전자 순서를 계속 shuffle해 "순서 없는 gene bag" 관점을 강제한다. Longformer 기반 encoder로 약 1.8만 개 gene list를 한 번에 처리하고, masked expression prediction으로 single-cell RNA-seq에서 pretraining한다. 이후 GTEx bulk RNA-seq와 single-cell 데이터를 섞어 retraining하고, TCGA 기반 암/정상 분류, 암종 분류, 병기 예측, 생존 예측으로 fine-tuning한다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 sample마다 정렬된 gene ID sequence와 해당 gene의 expression value sequence다. 논문에서는 special token을 붙인 뒤 gene ID embedding과 expression value embedding을 더해 encoder 입력으로 사용한다.

주요 데이터는 다음과 같다.

- Single-cell pretraining: PanglaoDB 기반 약 130만 single-cell RNA-seq sequence
- Bulk retraining: GTEx bulk RNA-seq 19,081 samples + pretraining set에서 sampling한 100,000 cells
- Downstream fine-tuning: TCGA bulk RNA-seq 기반 normal/tumor, cancer type, stage, survival labels
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
GeneBag은 modified BERT/Longformer encoder 구조다.

1. Gene ID를 token embedding으로 변환한다.
2. Raw read count 기반 연속 expression 값을 sine/cosine 방식의 deterministic embedding으로 변환한다.
3. Gene embedding과 expression embedding을 더한다.
4. 유전자 순서를 shuffle해 fixed gene order에 대한 의존을 줄인다.
5. Longformer attention encoder가 full-length gene list를 처리한다.
6. Task에 따라 masked-expression decoder 또는 classifier/regression head를 붙인다.

논문 Methods 기준으로 encoder는 sequence length 17,932를 다루며, 6 attention heads와 6 encoder layers를 사용한다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
Pretraining은 masked expression prediction이다. Non-padding gene expression 값 중 일부를 masking하고, encoder output으로 원래 expression 값을 복원하며 MSE loss를 사용한다.

Fine-tuning objective는 task에 따라 달라진다.

- Cell type annotation, tumor recognition, tissue/cancer classification: CrossEntropy
- Tumor staging: stage를 continuous value로 보고 MSE regression
- Survival prediction: 1년, 3년, 5년 생존 여부 binary classification
%% end method-objective %%

### Output

%% begin method-output %%
모델 output은 task-specific head에 따라 달라진다.

- Single-cell cell type label
- Normal/tumor binary label
- Normal tissue, paracancerous tissue, tumor type label
- Cancer stage estimate
- 1-, 3-, 5-year survival probability
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
GeneBag의 전체 모델 구조를 보여준다. 각 sample은 gene ID와 expression value 쌍으로 표현되고, gene embedding과 expression embedding을 결합한 뒤 전체 유전자 sequence를 shuffle해서 Longformer encoder에 넣는다. Encoder output은 pretraining에서는 masked expression decoder로, fine-tuning에서는 task-specific decoder/classifier로 연결된다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
Zheng68K single-cell annotation 결과를 보여준다. Raw expression 기반 t-SNE와 confusion matrix를 통해 GeneBag이 single-cell annotation task에서 cell type 구조를 학습했는지 확인한다. 이후 Figure 3-5에서 bulk RNA-seq 기반 tissue/tumor classification, cancer subtype classification, staging/survival prediction으로 확장된다.
%% end figure-2 %%

## 6. 장점

%% begin strengths %%
- Full-length gene list와 continuous expression 값을 직접 다루기 때문에 binned expression이나 제한된 marker panel보다 정보 손실이 적다.
- Single-cell pretraining을 bulk RNA-seq 임상 task로 옮기는 구체적인 transfer 경로를 제시한다.
- Zero-shot tumor recognition에서 약 96.17% accuracy, tissue/tumor classification에서 약 97.23% accuracy, 40개 tumor type classification에서 약 93.62% accuracy를 보고했다.
- 병기 예측과 1/3/5년 생존 예측까지 포함해 diagnosis와 prognosis를 한 모델 계열에서 다룬다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- Preprint/초기 연구 성격이 강하므로 prospective cohort와 외부 병원 데이터 검증이 필요하다.
- Bone marrow의 zero-shot tumor recognition 성능이 낮았고, metastatic/recurrent tumor를 primary tumor와 구분하는 능력이 제한적이었다.
- Survival prediction 성능은 암종별 편차가 크며, KIRC/OV 등 일부 암종에서는 상대적으로 낮은 정확도를 보였다.
- 실제 임상 적용에는 RNA-seq protocol, batch effect, regulatory validation, treatment metadata와의 결합 문제가 남아 있다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서는 bulk biopsy RNA-seq를 "gene bag"으로 넣고 rejection phenotype을 예측하는 방향으로 응용할 수 있다. 특히 rejection grade를 cancer stage처럼 continuous/ordinal target으로 두거나, graft survival/rejection-free survival을 survival prediction task로 두는 설계가 자연스럽다.

Single-cell reference atlas로 pretraining 또는 adapter training을 하고, bulk biopsy transcriptome으로 retraining/fine-tuning하면 cell-level biology와 patient-level label 사이의 간극을 줄이는 실험을 만들 수 있다. GeneBag의 unordered full-gene representation은 gene ranking 기반 모델보다 biopsy bulk RNA-seq와 잘 맞을 수 있다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- GeneBag
- Cell foundation model
- Longformer
- Bulk RNA-seq
- Masked expression prediction
- Pan-cancer diagnosis
- Survival prediction
- Transfer learning
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%


아직 가져온 PDF highlight는 없습니다. 위 정리는 abstract, methods, results, figure captions를 기준으로 채웠다.

%% end annotations %%

## 11. Bibliography

Liang, Yuhu, Dan Li, Aguix Guohua Xu, Yan Shao와/과Kun Tang. “GeneBag: Training a Cell Foundation Model for Broad-Spectrum Cancer Diagnosis and Prognosis with Bulk RNA-Seq Data”. Preprint, bioRxiv, 2024년 7월 2일. [https://doi.org/10.1101/2024.06.27.601098](https://doi.org/10.1101/2024.06.27.601098).


%% Import Date: 2026-05-22T13:06:16.579+09:00 %%
