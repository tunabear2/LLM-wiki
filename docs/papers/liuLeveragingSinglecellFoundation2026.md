# Leveraging single-cell foundation models for accurate survival outcome prediction

## 기본 정보

- Citation key: `liuLeveragingSinglecellFoundation2026`
- Item type: journalArticle
- Authors: Wei Liu; Qiang Wang; Lin Long; Wei Wang
- DOI: 10.1093/bioadv/vbag076
- URL: [Link](https://doi.org/10.1093/bioadv/vbag076)

## Abstract


Foundation models trained on large-scale single-cell transcriptomes can capture rich molecular representations of cellular states, yet their potential for cancer survival prediction from bulk RNA-seq data remains largely unexplored. We applied the single-cell foundation model scFoundation to derive patient-level embeddings across 25 cancer types from TCGA and systematically evaluated their prognostic value under both cancer-specific and pan-cancer settings. To leverage complementary information, we developed an Embedding–Gene–Survival Prediction (EGSP) model that integrates foundation model embeddings with gene expression and clinical variables. EGSP achieved a mean concordance index (C-index) of 0.724 across cancers and exceeded 0.8 in seven cancer types, consistently outperforming single-modality models and existing multi-omics survival approaches. Comparative analyses showed that embeddings derived from pretrained scFoundation weights exhibited lower redundancy with gene expression while retaining complementary prognostic signals relative to pan-cancer fine-tuned embeddings. Explainable AI analyses further revealed that prognostic embeddings capture interpretable biological programs related to tumor differentiation, immune activity, and tumor-intrinsic growth, enabling transparent survival prediction at both cohort and patient levels. Overall, single-cell foundation model embeddings provide biologically meaningful and partially non-redundant survival signals that substantially improve bulk RNA-seq–based prognostic modeling. https://github.com/weiliu123/EGSP.


## 1. 한 줄 요약

%% begin one-line-summary %%
EGSP는 bulk RNA-seq 암 환자에서 scFoundation embedding, 원 유전자 발현, 임상 변수를 결합해 TCGA 25개 암종의 overall survival risk를 더 정확하게 예측하려는 survival model이다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
Cancer survival prediction은 고차원 RNA-seq, 제한된 환자 수, censoring, 암종별 이질성 때문에 안정적인 모델링이 어렵다. 기존 모델은 raw gene expression과 clinical variable을 직접 쓰거나 multi-omics를 결합했지만, single-cell foundation model이 학습한 gene-gene interaction과 cell-state representation을 bulk survival prediction에 어떻게 활용할지는 충분히 검증되지 않았다.

선행 연구로 GeneFormer embedding을 TCGA survival과 연관시키거나, GeneBag처럼 생존을 5년 이진 분류로 바꾸는 시도가 있었지만, time-to-event survival modeling 관점에서는 아직 빈틈이 있었다. 이 논문은 scFoundation embedding이 raw expression과 중복되지 않는 prognostic signal을 제공하는지 체계적으로 확인한다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
각 암종의 training set에서 survival-associated gene을 먼저 고르고, top 512/1024/2048 gene만 scFoundation에 넣어 patient-level embedding을 만든다. EGSP는 pretrained scFoundation embedding, mean-centered gene expression, clinical variables(age, gender, pTNM)를 concatenation해 Cox loss로 risk score를 학습한다. 특히 pan-cancer fine-tuned embedding보다 원 pretrained embedding이 raw expression과 덜 중복되어 EGSP 성능을 더 끌어올렸다는 점이 핵심이다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 TCGA 25개 cancer type의 bulk RNA-seq count와 clinical survival 정보다.

- RNA-seq count: scFoundation이 다루는 19,264 gene에 맞춰 정렬
- Survival label: overall survival time과 event indicator
- Clinical variable: age, gender, 가능한 경우 pTNM stage
- Cohort: 중복/생존정보 결측/FFPE sample을 제외한 8,776 non-FFPE samples

각 cancer type 안에서 training set만 사용해 univariate Cox P-value 기준 top survival-associated genes를 선택한다. 이후 선택되지 않은 gene expression은 0으로 두고 scFoundation embedding을 만든다.
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
모델 흐름은 다음과 같다.

1. Cancer type별 training sample에서 각 gene의 univariate Cox P-value를 계산한다.
2. Top Ng genes(Ng = 512, 1024, 2048 비교; 최종적으로 1024 주로 사용)를 scFoundation 입력으로 사용한다.
3. scFoundation bulk-data pipeline으로 library-size normalization과 log(1 + x) transformation을 적용한다.
4. scFoundation에서 patient-level embedding을 추출한다. Embedding-only 모델에는 pool_type = all(3072 dim), integrative EGSP에는 feature dominance를 줄이기 위해 pool_type = max(768 dim)를 사용한다.
5. Embedding, mean-centered gene expression, clinical features를 concatenate한다.
6. Survival prediction head는 1024, 512, 256, 128 node의 4개 fully connected block으로 구성되고, 각 block은 FC, dropout 0.2, ReLU를 포함한다.
7. 마지막 layer는 환자별 scalar risk score를 출력한다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
학습 objective는 DeepSurv 계열의 Cox partial likelihood loss다. 모델은 생존 시간이 짧고 event가 발생한 환자에게 더 높은 risk score를 부여하도록 학습한다.

비교한 설정은 다음과 같다.

- Embed: scFoundation embedding만 사용
- Embed + Clin: embedding과 clinical variables 사용
- mRNA + Clin: gene expression과 clinical variables 사용
- Embed-pan / EGSP-pan: scFoundation 마지막 1-4개 encoder layer를 pan-cancer survival task로 fine-tuning한 embedding 사용
- EGSP: pretrained scFoundation embedding, gene expression, clinical variables를 결합
%% end method-objective %%

### Output

%% begin method-output %%
출력은 각 환자의 survival risk score다. 성능은 Harrell's C-index, Uno's C-index, integrated AUC(iAUC)로 평가한다.

주요 결과는 EGSP가 25개 cancer type 평균 C-index 0.724, iAUC 0.771을 달성했고, 7개 암종에서 C-index 0.8을 넘었다는 점이다. Embedding만 쓴 모델보다 raw expression과 clinical variable을 함께 결합했을 때 성능이 크게 좋아졌다.
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
scFoundation-based survival prediction architecture를 보여준다. Top survival-associated genes를 scFoundation에 넣어 embedding을 만들고, 이 embedding을 gene expression vector 및 clinical variables와 concat한 뒤 fully connected survival head에 넣어 Cox loss로 risk score를 학습하는 구조다. Ne, Ng, Nc는 각각 embedding, gene expression, clinical feature 차원을 뜻한다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
scFoundation embedding 자체가 prognostic signal을 담는지 평가한다. Embed-1024 t-SNE에서 cancer type별 clustering이 나타났고, 많은 embedding dimension이 Cox P-value 기준 survival-associated feature로 작동했다. Top 512/1024/2048 gene으로 만든 embedding을 Ridge-Cox/Lasso-Cox에 넣어 비교했을 때 raw expression 기반 Cox model과 비슷하거나 일부 cancer type에서는 더 robust한 성능을 보였다.
%% end figure-2 %%

## 6. 장점

%% begin strengths %%
- Bulk RNA-seq survival prediction에 single-cell foundation model embedding을 체계적으로 접목했다.
- Time-to-event survival modeling을 사용해 단순 5년 생존 이진분류보다 정보 손실이 적다.
- EGSP가 embedding, raw gene expression, clinical variables의 complementarity를 명확히 보여준다.
- Pretrained embedding과 pan-cancer fine-tuned embedding의 redundancy를 mutual information으로 비교해, 왜 pretrained embedding이 더 도움이 되는지 설명한다.
- SHAP과 pathway analysis로 Embed-638 같은 embedding feature가 tumor differentiation, immune activity, tumor-intrinsic growth program과 연결될 수 있음을 보여준다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- TCGA retrospective analysis이므로 외부 병원 cohort와 prospective validation이 필요하다.
- 평가가 C-index, Uno's C-index, iAUC 중심이라 실제 survival probability calibration과 decision curve utility는 부족하다.
- 입력 modality가 gene expression과 clinical data에 제한되어 WSI, methylation, CNV, treatment history 등은 포함하지 않았다.
- Small cancer cohort에서는 confidence interval이 넓고, clinical feature 의존도가 커져 apparent performance를 조심해서 해석해야 한다.
- scFoundation 하나만 주로 검증했기 때문에 Geneformer, scGPT, GenePT 등 다른 foundation embedding과의 조합은 후속 연구가 필요하다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서는 EGSP 구조를 rejection-free survival, graft survival, eGFR decline, chronic active rejection progression 같은 time-to-event outcome에 직접 옮길 수 있다. Biopsy bulk RNA-seq에서 rejection-associated gene을 training fold 안에서 고른 뒤 scFoundation/scGPT/Geneformer embedding을 만들고, raw expression 및 clinical variables(donor age, HLA mismatch, DSA, immunosuppression, time post-transplant)를 결합하는 설계가 자연스럽다.

중요한 실험 포인트는 embedding-only 모델이 아니라 "embedding + gene expression + clinical" 조합을 baseline과 비교하는 것이다. 또한 pan-cohort fine-tuning이 embedding을 label에 과적응시켜 raw expression과 중복되게 만드는지, transplant dataset에서도 mutual information과 SHAP으로 점검하면 좋다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- scFoundation
- EGSP
- Survival prediction
- Cox partial likelihood
- TCGA
- Bulk RNA-seq
- Foundation model embedding
- Non-redundant risk embedding
- SHAP
- Pan-cancer training
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%


아직 가져온 PDF highlight는 없습니다. 위 정리는 Bioinformatics Advances/Europe PMC 공개 본문과 abstract를 기준으로 채웠다.

%% end annotations %%

## 11. Bibliography

Liu, Wei, Qiang Wang, Lin Long와/과Wei Wang. “Leveraging single-cell foundation models for accurate survival outcome prediction”. _Bioinformatics Advances_ 6, 호 1 (2026): vbag076. [https://doi.org/10.1093/bioadv/vbag076](https://doi.org/10.1093/bioadv/vbag076).


%% Import Date: 2026-05-27T17:17:44.069+09:00 %%
