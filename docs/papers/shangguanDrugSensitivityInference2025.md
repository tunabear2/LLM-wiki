# Drug Sensitivity Inference Through Foundation Model–Driven Contrastive Integration of Bulk and Single-Cell Omics

## 기본 정보

- Citation key: `shangguanDrugSensitivityInference2025`
- Item type: conferencePaper
- Authors: Ningyuan Shangguan; Yuansong Zeng; Wenbing Li; Yuedong Yang
- DOI: 10.1109/BIBM66473.2025.11356510
- URL: [Link](https://ieeexplore.ieee.org/document/11356510/metrics)

## Abstract


Tumor heterogeneity hinders drug response prediction: bulk RNA-seq obscures cell-level resistance, while scRNA-seq lacks annotated drug response data. Existing methods transferring knowledge from bulk to single-cell often underuse pretrained models and ignore inter-cell relationships, limiting heterogeneity modeling. We propose COIN (Contrastive Learning-driven Omics Integration Network), integrating labeled bulk RNA-seq with unlabeled scRNA-seq for single-cell drug sensitivity prediction. COIN leverages CellFM, a foundation model pretrained on 100 M cells, and uses a shared feature extractor with contrastive learning to align shared patterns and capture micro-heterogeneity, while an auxiliary reconstruction loss ensures robust representations. Trained solely on bulk data, COIN predicts single-cell sensitivity and outperforms existing methods, with 9% average AUC and 7% AUPR improvements. COIN effectively overcomes the limitations of bulk data for heterogeneity modeling and eliminates the need for costly single-cell drug screening annotations, advancing personalized cancer therapy.


## 1. 한 줄 요약

%% begin one-line-summary %%
COIN은 labeled bulk RNA-seq drug response와 unlabeled scRNA-seq를 CellFM 기반 contrastive learning으로 통합해, single-cell 수준의 drug sensitivity를 annotation 없이 예측하려는 모델이다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
Drug response prediction에서 bulk RNA-seq는 환자/세포주 수준의 약물 반응 label을 얻기 쉽지만, 여러 subclone과 cell state가 섞여 있어 single-cell heterogeneity를 가린다. 반대로 scRNA-seq는 tumor heterogeneity를 잘 보여주지만, 각 cell에 drug response label을 붙이는 실험은 비용이 크고 데이터가 부족하다.

기존 bulk-to-single transfer 방법은 bulk label을 single-cell로 옮기려 하지만, pretrained single-cell foundation model의 표현력을 충분히 활용하지 않거나 cell-cell relationship과 micro-heterogeneity를 약하게 다루는 한계가 있었다. COIN은 bulk label만으로 single-cell drug sensitivity를 추론하는 bridge model을 목표로 한다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
COIN은 CellFM이 만든 single-cell transcriptomic representation을 활용하고, labeled bulk RNA-seq와 unlabeled scRNA-seq를 shared feature extractor로 같은 latent space에 보낸다. Contrastive learning으로 bulk와 single-cell의 shared drug-response pattern을 맞추고, auxiliary reconstruction loss로 representation이 과도하게 붕괴하지 않도록 한다. 학습은 bulk drug response label만으로 수행하지만, inference는 single-cell sensitivity prediction으로 확장된다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 source domain의 labeled bulk RNA-seq와 target domain의 unlabeled scRNA-seq다.

- Labeled bulk RNA-seq: GDSC에서 가져온 1,074 cancer cell lines와 226 drugs의 drug sensitivity data. Drug response는 IC50/AUC로 측정하고, drug별 IC50 평균을 threshold로 sensitive(1)/resistant(0)를 이진화한다.
- Bulk expression: GDSC baseline RNA-seq expression profile(RMA-normalized).
- Unlabeled scRNA-seq: GEO에서 수집한 scRNA-seq data. Drug response labels는 training에는 쓰지 않고 evaluation에 사용한다. SCANPY로 QC하며, detected genes가 200개 미만인 cell, mitochondrial gene expression이 5%를 넘는 cell, 3개 미만 cell에서만 detected된 gene을 필터링한다.
- Feature selection: source/target shared genes 전체를 쓰는 `all` 전략과 2,128 protein-protein interaction genes를 쓰는 `ppi` 전략을 비교한다.

모델은 CellFM embedding을 original expression profile과 concatenate해 biological prior와 denoising 효과를 함께 사용한다.
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
COIN은 5개 module로 구성된다.

1. CellFM information fusion: input expression matrix `X`와 CellFM embedding `X_emb`를 concatenate해 `X_fused = X || X_emb`를 만든다.
2. Shared feature extractor: 같은 encoder `F`가 bulk `X_fused_s`와 single-cell `X_fused_t`를 latent representation `Z_s`, `Z_t`로 보낸다.
3. Decoder reconstruction: binomial noise를 넣은 입력을 decoder `D`가 원 fused feature로 복원한다.
4. Contrastive learning: source-to-target, target-to-source 양방향 symmetric triplet formulation을 사용한다. 각 anchor에 대해 nearest opposite-domain sample을 positive, farthest sample을 negative로 두고 margin loss를 계산한다.
5. Drug response predictor: source-domain latent representation 위에 dropout을 포함한 5-layer MLP를 붙이고, sigmoid로 drug sensitivity probability를 출력한다.

논문 제목의 "foundation model-driven contrastive integration"은 CellFM representation, shared encoder, contrastive domain alignment, reconstruction을 함께 쓰는 구조를 가리킨다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
학습 objective는 세 요소로 볼 수 있다.

- `L_BCE`: labeled bulk RNA-seq의 sensitive/resistant label을 예측하는 binary cross-entropy
- `L_CL`: bulk와 scRNA-seq latent representation을 양방향 triplet loss로 alignment하는 contrastive loss
- `L_MSE`: noisy input에서 fused expression/CellFM feature를 복원하는 reconstruction loss

전체 loss는 `L = L_MSE + L_CL + L_BCE`다. 중요한 점은 drug predictor를 source bulk label로 학습하고, single-cell drug screening annotation 없이 target scRNA-seq cell의 sensitivity를 추론한다는 것이다.
%% end method-objective %%

### Output

%% begin method-output %%
출력은 cell별 drug sensitivity probability 또는 sensitive/resistant prediction이다. 성능은 mean AUC와 mean AUPR로 평가한다.

주요 결과는 `all` feature 전략에서 pre-treatment 평균 AUC/AUPR 0.906/0.910, post-treatment 평균 AUC/AUPR 0.655/0.695를 달성했다는 점이다. Pre-treatment에서는 SCAD 대비 평균 AUC 9%, AUPR 7% 높았고, post-treatment에서는 SCAD 대비 평균 AUC 12.7%, AUPR 7.4% 높았다.
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
COIN framework overview다. CellFM-enhanced bulk RNA-seq와 unlabeled scRNA-seq를 shared feature extractor에 넣고, contrastive learning으로 bulk-single-cell 관계를 align/disentangle하며, decoder reconstruction으로 feature robustness를 유지한 뒤 drug sensitivity를 예측하는 전체 흐름을 보여준다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
Afatinib과 PLX4720 scRNA-seq representation의 UMAP visualization이다. COIN representation은 drug-sensitive cell과 drug-insensitive cell을 비교 방법보다 더 분리해 보여주며, bulk와 single-cell RNA-seq의 shared/local feature를 contrastive learning과 reconstruction loss로 통합하면 cell-level drug response pattern을 잡을 수 있다는 점을 시각적으로 뒷받침한다.
%% end figure-2 %%

### Table 1-3

%% begin table-summary %%
Table 1은 pre-treatment drug sensitivity prediction 결과다. `all` feature strategy에서 COIN은 Afatinib 0.901/0.901, AR-42 0.974/0.976, Gefitinib 0.981/0.981 등 높은 AUC/AUPR을 보였고, 평균 0.906/0.910으로 XGBoost, SVM, Random Forest, scDEAL, SCAD를 앞섰다.

Table 2는 post-treatment 결과다. `all` strategy에서 COIN은 평균 AUC/AUPR 0.655/0.695를 보였고, PLX4720(A375)에서는 0.825/0.880으로 가장 높았다. 다만 PLX4720(451Lu)처럼 drug/cell-line setting에 따라 COIN이 항상 최고는 아니며, post-treatment 평균 성능은 pre-treatment보다 낮다.

Table 3 ablation은 모든 구성요소가 필요함을 보여준다. Pre-treatment 기준 full COIN은 0.906/0.910인데, `L_MSE` 제거 시 0.822/0.868, `L_CL` 제거 시 0.714/0.736, CellFM 제거 시 0.875/0.898로 떨어진다. 특히 contrastive loss 제거의 성능 하락이 커서 bulk-single-cell alignment가 핵심임을 시사한다.
%% end table-summary %%

## 6. 장점

%% begin strengths %%
- Single-cell drug response annotation이 없어도 bulk label을 활용해 cell-level sensitivity를 추론하는 문제 설정이 실용적이다.
- CellFM 같은 large-scale single-cell foundation model을 drug response transfer에 직접 활용한다.
- Symmetric triplet contrastive learning과 reconstruction을 함께 써서 bulk-scRNA alignment와 representation 보존을 동시에 겨냥한다.
- Tumor heterogeneity 때문에 bulk response가 평균화되는 문제를 single-cell inference로 풀려는 방향이 명확하다.
- Pre-treatment와 post-treatment scenario를 나눠 평가했고, `all` gene strategy와 `ppi` strategy를 비교해 global gene expression의 중요성을 보여준다.
- Ablation에서 `L_CL`, `L_MSE`, CellFM fusion의 기여를 분리해 검증했다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- 4-page conference paper라 dataset split, GEO accession별 세부 sample composition, hyperparameter, statistical uncertainty가 비교적 압축적으로 제시되어 있다.
- Bulk response label을 single-cell label로 전이할 때, 실제 cell-level sensitivity ground truth가 부족하면 평가가 간접적일 수 있다.
- Drug response를 drug별 mean IC50 기준으로 이진화하므로 dose-response curve와 continuous sensitivity 정보를 일부 잃는다.
- Bulk와 single-cell 데이터의 tissue/cancer type/drug coverage가 다르면 contrastive alignment가 batch 또는 lineage signal을 학습할 위험이 있다.
- CellFM representation에 의존하므로, CellFM pretraining coverage 밖의 rare state나 protocol에서는 성능 저하가 가능하다.
- Drug dose, exposure time, viability assay 차이 같은 pharmacological metadata를 얼마나 잘 정규화했는지 확인이 필요하다.
- Post-treatment 평균 성능은 pre-treatment보다 낮고, 일부 drug/cell-line setting에서는 classical 또는 기존 transfer method가 더 나은 항목도 있어 clinical robustness는 추가 검증이 필요하다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Transplant rejection 연구로 옮기면, "labeled bulk biopsy + unlabeled single-cell/spatial biopsy"를 contrastive integration하는 구조로 바꿀 수 있다. Bulk biopsy에는 rejection label, Banff score, graft outcome이 있고, scRNA-seq/spatial data에는 cell-level immune state가 있으므로 COIN식 framework가 bulk label을 cell state 수준으로 전이하는 데 유용할 수 있다.

예를 들어 bulk RNA-seq에서 rejection/non-rejection 또는 steroid response label을 학습하고, unlabeled scRNA-seq biopsy cell에 "rejection-associated sensitivity/state score"를 부여하는 실험을 만들 수 있다. Reconstruction loss를 유지하면 cell type identity를 잃지 않고, contrastive loss는 bulk phenotype과 single-cell heterogeneity를 연결하는 역할을 할 수 있다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- COIN
- CellFM
- Drug sensitivity prediction
- Bulk RNA-seq
- scRNA-seq
- Contrastive learning
- Reconstruction loss
- Bulk-to-single-cell transfer
- Tumor heterogeneity
- Single-cell drug response
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%


아직 가져온 PDF highlight는 없습니다. 위 정리는 사용자가 제공한 `Drug_Sensitivity_Inference_Through_Foundation_ModelDriven_Contrastive_Integration_of_Bulk_and_Single-Cell_Omics.pdf` 원문을 기준으로 보강했다.

%% end annotations %%

## 11. Bibliography

Shangguan, Ningyuan, Yuansong Zeng, Wenbing Li와/과Yuedong Yang. “Drug Sensitivity Inference Through Foundation Model–Driven Contrastive Integration of Bulk and Single-Cell Omics”. _2025 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)_, 2025년 12월, 1809–12. [https://doi.org/10.1109/BIBM66473.2025.11356510](https://doi.org/10.1109/BIBM66473.2025.11356510).


%% Import Date: 2026-05-27T17:17:44.078+09:00 %%
