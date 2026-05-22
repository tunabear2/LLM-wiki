# Path-GPTOmic: A Balanced Multi-modal Learning Framework for Survival Outcome Prediction

## 기본 정보

- Citation key: `PathGPTOmicBalancedMultimodal`
- Item type: arXiv preprint
- Authors: Hongxiao Wang; Yang Yang; Zhuo Zhao; Pengfei Gu; Nishchal Sapkota; Danny Z. Chen
- DOI: 10.48550/arXiv.2403.11375
- URL: [Link](https://arxiv.org/abs/2403.11375)

## Abstract


Path-GPTOmic은 암 생존 예측을 위해 병리 이미지와 genomics 데이터를 함께 쓰는 multimodal framework다. 기존 pathology-genomics 모델은 gene-gene interaction 같은 생물학적 지식을 충분히 활용하지 못하고, 한 modality가 loss optimization을 지배해 다른 modality가 덜 학습되는 문제가 있었다. 이 논문은 single-cell RNA-seq로 학습된 scGPT embedding space를 bulk RNA-seq에 맞게 smoothing하고, Cox partial likelihood loss에 맞춘 gradient modulation으로 pathology branch와 genomics branch의 학습 불균형을 줄인다. TCGA-GBMLGG와 TCGA-KIRC에서 기존 baseline보다 높은 C-index를 보고했다.


## 1. 한 줄 요약

%% begin one-line-summary %%
Path-GPTOmic은 H&E pathology image와 bulk RNA-seq/CNV/mutation genomics를 결합해 암 생존 위험을 예측하면서, scGPT의 single-cell 지식을 bulk RNA-seq에 맞게 조정하고 modality imbalance를 줄이는 방법이다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
암 생존 예측에서는 pathology image가 morphology와 microenvironment를, genomics가 gene expression과 molecular state를 제공한다. 기존 multimodal 모델은 두 정보를 fusion하지만, bulk RNA-seq branch가 충분한 external biological knowledge를 활용하지 못하거나, 성능이 강한 modality가 전체 loss를 지배해 다른 modality가 under-optimized되는 문제가 있다.

특히 survival prediction에서는 classification loss와 달리 Cox partial likelihood loss를 쓰기 때문에, multimodal imbalance를 어떻게 조절할지에 대한 설계가 덜 정리되어 있었다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
첫째, single-cell foundation model인 scGPT 뒤에 MLP-A를 붙이고 mixup 기반 smoothing으로 bulk RNA-seq가 더 자연스럽게 놓이는 embedding space를 만든다. 둘째, CNV/mutation/RNA-seq로 만든 genomics feature와 pathology image feature를 합쳐 Cox survival model을 학습한다. 셋째, genomics branch와 image branch의 contribution을 추적해 gradient를 동적으로 조절함으로써 한 modality가 다른 modality의 학습을 억누르지 않게 한다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 환자 단위 paired multimodal data다.

- H&E-stained pathology images
- Genomics features: mutation, copy number variation, bulk RNA-seq
- Survival time과 censoring/event label

실험은 TCGA-GBMLGG 1,505 samples와 TCGA-KIRC 1,251 samples를 사용했고, 15-fold cross-validation으로 평가했다.
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
Path-GPTOmic은 두 단계로 구성된다.

1. scGPT bulk adaptation
   - scGPT parameter는 freeze한다.
   - 두 single-cell RNA-seq sample을 mixup해 pseudo-bulk expression을 만든다.
   - scGPT 뒤에 3-layer MLP-A를 붙여 smooth/interpolatable embedding space를 학습한다.

2. Multimodal survival model
   - CNV와 mutation은 SNN으로 처리한다.
   - Bulk RNA-seq는 frozen scGPT + MLP-A로 embedding한다.
   - CNV/mutation/RNA embedding을 concat한 뒤 MLP-B로 genomics feature를 만든다.
   - Pathology image는 T2T-ViT image encoder로 feature를 만든다.
   - Genomics feature와 image feature를 concat하고 linear hazard head로 log hazard ratio를 예측한다.
   - Training 중 modality contribution discrepancy를 계산해 gradient를 조절한다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
MLP-A smoothing 단계에서는 mixup된 single-cell expression이 평균적인 cell type target으로 수렴하도록 학습해 bulk-like RNA embedding을 안정화한다. Survival model 단계에서는 Cox partial log-likelihood를 cost function으로 사용한다.

핵심은 Cox loss에서 한 modality가 이미 잘 맞으면 global loss가 작아져 다른 modality의 gradient가 약해질 수 있다는 점이다. 논문은 modality별 contribution discrepancy ratio를 계산하고, under-optimized branch가 더 충분히 학습되도록 gradient modulation을 적용한다.
%% end method-objective %%

### Output

%% begin method-output %%
최종 output은 환자별 log hazard ratio 또는 survival risk score다. 성능 평가는 survival prediction에서 흔히 쓰는 C-index로 수행한다.
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
Path-GPTOmic pipeline 전체를 보여준다. 위쪽은 scGPT 뒤 MLP-A를 학습해 bulk RNA-seq embedding space를 조절하는 단계이고, 아래쪽은 genomics branch와 pathology image branch를 결합해 Cox survival prediction을 수행하는 단계다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
논문은 Figure 1 중심의 방법 논문이고, 주요 결과는 Table 1-3에 제시된다. Path-GPTOmic은 TCGA-GBMLGG에서 C-index 0.848 ± 0.014, TCGA-KIRC에서 0.754 ± 0.030을 달성해 Pathomic Fusion, PathOmics 등 baseline보다 높았다. Ablation에서는 scGPT smoothing과 gradient modulation을 함께 썼을 때 가장 좋은 성능을 보였다.
%% end figure-2 %%

## 6. 장점

%% begin strengths %%
- scGPT를 그대로 bulk RNA-seq에 적용하지 않고, mixup smoothing으로 embedding space를 조절했다.
- Pathology image와 genomics branch의 학습 불균형을 Cox survival loss 관점에서 다뤘다.
- 기존 pathology-genomics fusion baseline과 비교해 GBMLGG, KIRC 모두에서 C-index 향상을 보였다.
- Kidney transplant처럼 pathology image와 transcriptomics가 동시에 존재하는 문제에 구조적으로 잘 맞는다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- 실험이 TCGA-GBMLGG와 TCGA-KIRC 두 dataset에 제한되어 있어 cancer type과 institution 일반화는 추가 검증이 필요하다.
- Bulk RNA-seq를 위해 scGPT embedding을 smoothing하지만, single-cell model에서 bulk sample로 넘어가는 biological assumption이 완전히 검증된 것은 아니다.
- Pathology encoder와 genomics branch의 preprocessing 선택에 성능이 의존할 수 있다.
- 실제 임상 survival prediction에는 treatment, stage, clinical covariate, batch/site effect를 더 체계적으로 통제해야 한다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection 연구에서는 biopsy pathology image와 bulk/single-cell transcriptomics를 함께 넣어 rejection risk, graft survival, 또는 treatment response를 예측하는 multimodal model로 확장할 수 있다.

중요한 포인트는 modality imbalance다. Transcriptomics branch가 강하면 pathology branch가 덜 학습될 수 있고, 반대로 image feature가 강하면 molecular signal이 묻힐 수 있다. Path-GPTOmic의 gradient modulation 아이디어는 pathology, RNA-seq, clinical covariate를 함께 쓰는 rejection model에서 각 branch가 실제로 학습되고 있는지 점검하는 기준이 될 수 있다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- Path-GPTOmic
- scGPT
- Multimodal learning
- Pathology-genomics fusion
- Bulk RNA-seq
- Cox partial likelihood
- Gradient modulation
- Survival prediction
- TCGA
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%


아직 가져온 PDF highlight는 없습니다. 위 정리는 arXiv abstract, method, results를 기준으로 채웠다.

%% end annotations %%

## 11. Bibliography

Wang, Hongxiao, Yang Yang, Zhuo Zhao, Pengfei Gu, Nishchal Sapkota, and Danny Z. Chen. “Path-GPTOmic: A Balanced Multi-modal Learning Framework for Survival Outcome Prediction”. arXiv, 2024. [https://doi.org/10.48550/arXiv.2403.11375](https://doi.org/10.48550/arXiv.2403.11375).


%% Import Date: 2026-05-22T13:06:16.582+09:00 %%
