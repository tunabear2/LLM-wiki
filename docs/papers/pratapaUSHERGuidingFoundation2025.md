---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# USHER: Guiding Foundation Model Representations through Distribution Shifts

## 기본 정보

- Citation key: `pratapaUSHERGuidingFoundation2025`
- Item type: preprint
- Authors: Aditya Pratapa; Purushothama Rao Tata; Rohit Singh
- DOI: 10.1101/2025.11.20.689462
- URL: [Link](https://www.biorxiv.org/content/10.1101/2025.11.20.689462v2)

## Abstract


초록
특정 생물학적 데이터 방식에 사전 학습된 기초 모델은 새로운 분석에서 나온 유통 외(OOD) 데이터를 접할 때 체계적인 표상 편향을 보입니다. 임베딩 드리프트는 세포 상태나 조직 형태의 진정한 생물학적 변이보다는 주로 계측 및 프로토콜 관련 인공물에서 발생합니다. 이러한 드리프트는 기존 배치 효과와 구별되며, 샘플 크기가 부족한 경우가 많아 재학습으로 해결할 수 없고, 기존 임베딩을 수정하면 안정적인 표현에 의존하는 하위 도구가 깨집니다. 우리는 OOD 임베딩을 기초 모델의 참조 공간으로 반환하는 간단한 변환을 학습할 수 있는 적응형 프레임워크인 USHER를 소개합니다. USHER는 기대 최대화 스타일 절차를 통해 임베딩 변환을 가능하게 합니다. 유통 내 기준 샘플이 주어진 후, USHER는 먼저 연결되지 않은 OOD(출처)와 참조(타겟) 임베딩을 정렬하면서도 국소 구조를 보존하는 융합 그로모프-바서스타인 결합을 추정합니다. 최적 수송 결합을 하위 작업에 더 유용하게 만들기 위해, 우리는 높은 신뢰도 대응관계만 유지하도록 엔트로피 필터링 개념을 도입합니다. 두 번째 단계에서는 USHER가 OOD 데이터에 대한 모델의 표현 공간을 신뢰성 있게 복원하는 저복잡도 변환을 학습합니다. 우리는 이 학습된 변환이 유사한 실험 조건에서 다른 OOD 데이터로 일반화됨을 입증합니다. 우리는 USHER를 적용해 Xenium 전사체 개수에 대해 scGPT를 실행할 때 나타나는 플랫폼 특이적 편향을 수정했습니다: USHER는 Xenium 임베딩을 원래의 scRNA-seq 표현 공간으로 매핑하여 세포 유형 군집화와 교차 플랫폼 통합을 개선했습니다. H&E 이미지로 훈련된 조직병리학 기초 모델은 데이터 획득 아티팩트로 인해 MALDI 대사물 프로파일 조직 이미지에서 실패합니다. USHER는 이를 교정하여 세포 유형 분류와 단백질 풍부도 추정을 가능하게 합니다. USHER는 빠르게 변화하는 실험 환경 속에서 생물학적 기초 모델을 전반적으로 적용할 수 있는 일반화 가능한 프레임워크를 제공합니다.


## 1. 한 줄 요약

%% begin one-line-summary %%
USHER는 OOD assay에서 나온 foundation model embedding을 모델 재학습 없이 reference embedding space로 되돌리기 위해, optimal transport 기반 대응관계와 저복잡도 변환을 학습하는 post-hoc alignment framework다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
Biological foundation model은 특정 modality나 protocol에서 pretraining되기 때문에, 새로운 assay나 platform에서 나온 데이터를 넣으면 embedding이 생물학적 차이보다 장비/프로토콜 artifact를 반영해 shift될 수 있다. 이런 drift는 일반적인 batch effect와 비슷해 보이지만, foundation model의 downstream tool이 이미 reference embedding geometry에 의존한다는 점에서 문제가 더 크다.

재학습이나 fine-tuning은 OOD sample 수가 부족하면 어렵고, 기존 embedding space 자체를 바꾸면 이미 구축된 classifier, imputation model, search/index tool과 호환성이 깨질 수 있다. USHER는 model을 고정한 채 OOD embedding만 reference space로 이동시키는 문제로 재정의한다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
USHER는 unpaired OOD(source) embedding과 reference(target) embedding 사이에서 Fused Gromov-Wasserstein coupling을 추정해 구조를 보존하는 대응관계를 찾는다. Entropic filtering으로 신뢰도 높은 correspondence만 남긴 뒤, OOD embedding을 reference space로 보내는 단순한 변환을 학습한다. 이 방식은 scGPT로 만든 Xenium spatial transcript count embedding과 histopathology foundation model의 MALDI tissue image embedding drift를 보정하는 데 사용된다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 이미 계산된 foundation model embedding이다.

- Source `Xs`: 새로운 assay/platform에서 나온 OOD embedding
- Target `Xt`: foundation model이 잘 작동하는 reference in-distribution embedding
- Pairing: source와 target이 one-to-one matched sample일 필요는 없다.
- Auxiliary signal: transcriptomics에서는 shared genes 기반 logistic-regression cell-type probability, spatial image에서는 affine-aligned coordinate distance를 cross-domain auxiliary cost로 사용한다.

주요 실험 데이터는 두 축이다.

- scGPT + Xenium: IPF lung dataset. Xenium section은 38,280 cells와 343 genes, scRNA-seq reference는 matched tissue의 atlas이며 marginal cell-type distribution을 맞추기 위해 26,323 reference cells를 사용했다.
- H-optimus-1 + post-MALDI H&E: lung adenocarcinoma near-serial sections. Post-PCF H&E를 in-distribution reference로, post-MALDI H&E를 artifact가 있는 OOD source로 두고 14 x 14 pixel patch별 1,536-dimensional embedding을 사용했다.
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
USHER는 foundation model 내부를 바꾸지 않는 post-hoc transformation pipeline이다.

1. Frozen foundation model로 source `Xs`와 target `Xt` embedding을 계산한다.
2. Target-domain statistics로 양쪽 embedding을 standardization한다.
3. E-step에서 Fused Gromov-Wasserstein(FGW) optimal transport로 soft correspondence matrix `P`를 추정한다.
4. FGW의 cross-domain cost는 `M = gamma * M_aux + (1 - gamma) * M_feat`로 두고, structure cost는 kNN graph geodesic distance(k = 30)를 사용한다.
5. Entropic filtering으로 high-entropy/low-confidence row를 제거하고, Hungarian assignment로 sparse one-to-one correspondence를 만든다.
6. M-step에서 1개 linear layer 또는 shallow one-hidden-layer MLP `f_theta`를 학습해 OOD embedding을 matched target 쪽으로 이동시킨다.
7. M-step loss는 matched pair distance와 transformed source/target feature-wise variance 차이를 함께 줄인다.
8. E-step과 M-step을 반복한 뒤, 학습된 `f_theta`를 같은 protocol의 held-out OOD sample에 재사용한다.

논문 실험에서는 FGW trade-off `alpha`, auxiliary weight `gamma`, fitting loss weight `lambda`를 조정하며, scGPT/Xenium 주 실험에서는 `alpha = 0.3`, `lambda = 0.9`, 초기 auxiliary warm-start 이후 `gamma = 0.4`를 사용했다. Entropic regularization은 0.05, M-step은 Adam learning rate 1e-3, EM은 대략 20-25 iterations를 기본 설정으로 사용한다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
Pretraining objective가 아니라 alignment objective다. E-step에서는 source와 target 사이의 feature distance, auxiliary similarity, within-domain local geometry 보존을 함께 고려하는 FGW optimal transport problem을 푼다. M-step에서는 filtered correspondence를 기준으로 source embedding이 matched target embedding에 가까워지도록 하면서, transformed source의 분산 구조가 target과 비슷하게 유지되도록 학습한다.

핵심 제약은 "foundation model은 수정하지 않고 embedding만 이동"하는 것이다. 따라서 downstream classifier나 imputation tool이 기대하는 reference geometry를 유지하는 것이 목표다.
%% end method-objective %%

### Output

%% begin method-output %%
출력은 reference space에 정렬된 corrected OOD embedding과 재사용 가능한 transform `f_theta`다. 이 embedding은 이후 cell type clustering, cross-platform integration, unassayed gene imputation, histology cluster recovery, protein abundance prediction 같은 downstream task에 사용된다.
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
USHER의 전체 workflow를 보여준다. OOD assay/protocol에서는 foundation model embedding이 reference space에서 drift되고, USHER는 embedding space 위에서만 low-complexity transform을 학습해 OOD representation을 기존 reference space로 되돌린다. 알고리즘은 FGW optimal transport로 correspondence를 추정하는 E-step과, simple neural transform을 fitting하는 M-step을 반복한다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
Xenium transcript count를 scGPT에 넣었을 때 생기는 OOD embedding drift와 USHER 보정 결과를 보여준다. 원래 scRNA-seq와 Xenium scGPT embedding은 각각 내부 cell type 구조를 어느 정도 담지만, joint UMAP에서는 modality별로 분리된다. Harmony, Scanorama, ComBat, sysVI, Tangram 같은 비교 방법은 separation을 줄여도 충분한 integration을 만들지 못한 반면, USHER는 Xenium embedding을 scRNA-seq manifold로 정렬하면서 biological clustering을 유지했다.

주요 수치로 USHER는 BRAS 0.84, NMI 0.67, graph connectivity 0.86, KBET 0.36을 보고했다. Linear-only variant인 USHER-L도 BRAS 0.82로 비슷하게 작동했고, learned weight matrix가 sparse/near-diagonal이라 OOD drift가 완전한 re-embedding보다 축별 recalibration에 가까움을 시사한다.
%% end figure-2 %%

### Figure 3

%% begin figure-3 %%
Figure 3은 학습된 USHER transform이 같은 Xenium protocol의 held-out sections에도 재사용될 수 있음을 보여준다. 별도 retraining 없이 4개 추가 Xenium section을 scRNA-seq reference manifold에 잘 투영했고, gene panel에 없는 SFTPB, C1QA를 10-nearest-neighbor scRNA-seq reference averaging으로 impute했다. VisiumHD와의 비교에서 imputed genes의 spatial pattern correlation이 Xenium/VisiumHD에서 직접 측정된 genes의 baseline correlation과 비슷한 수준으로 나왔다.
%% end figure-3 %%

### Figure 4

%% begin figure-4 %%
Figure 4는 histopathology setting이다. Post-MALDI H&E는 matrix crystallization, laser etching, thicker sectioning artifact 때문에 H-optimus-1 embedding이 post-PCF H&E reference와 분리되고, Vahadane stain normalization만으로는 해결되지 않는다. USHER는 post-MALDI embedding을 post-PCF manifold에 정렬해 spatial clustering을 회복했고, raw post-MALDI embedding으로는 실패하던 SMA, PanCK, CD68 protein abundance prediction의 spatial localization을 복원했다. BRAS는 original 0.68에서 USHER 후 0.91, KBET는 0.0에서 0.78로 개선되었다.
%% end figure-4 %%

## 6. 장점

%% begin strengths %%
- Foundation model 자체를 재학습하지 않아도 OOD embedding을 reference space로 맞출 수 있다.
- Unpaired source-target embedding을 다룰 수 있어 matched paired dataset이 부족한 생물학 실험에 적합하다.
- FGW를 사용해 pointwise feature similarity뿐 아니라 kNN graph 기반 local geometry도 보존하려고 한다.
- Entropic filtering으로 low-confidence matching을 버려 downstream task에 유용한 correspondence에 집중한다.
- Transform이 linear 또는 nearly-linear라 해석 가능성이 있고, USHER-L의 near-diagonal matrix는 drift가 modest recalibration임을 보여준다.
- scRNA-seq/Xenium, histopathology/MALDI처럼 서로 다른 modality/assay drift에 적용 가능한 일반 프레임워크를 제안한다.
- 보정된 embedding을 단순히 보기 좋게 섞는 데서 끝내지 않고, unassayed gene imputation과 protein abundance prediction으로 downstream utility를 확인했다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- Preprint 단계이므로 외부 cohort와 다양한 assay 조합에서 독립 검증이 더 필요하다.
- OOD embedding 안에 reference space로 복원 가능한 생물학적 signal이 남아 있어야 한다. Foundation model이 OOD assay에서 완전히 무의미한 embedding을 만들면 alignment만으로 해결하기 어렵다.
- Batch correction과 마찬가지로 과도한 보정이 실제 biology를 지울 위험이 있다.
- Auxiliary signal(cell-type probability, spatial coordinates)이 training 단계의 correspondence warm-start에 쓰이므로, 매우 noisy하거나 biased auxiliary signal에서는 alignment 품질이 흔들릴 수 있다.
- 같은 protocol의 held-out sample에는 잘 일반화했지만, 완전히 다른 gene panel, tissue, disease state, imaging artifact에 어느 정도까지 transfer되는지는 추가 실험이 필요하다.
- Downstream label이 부족한 상황에서는 embedding mixing metric이 좋아진 것과 biological validity가 좋아진 것을 구분하기 어렵다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant에서는 center, library protocol, biopsy processing, platform 차이 때문에 embedding drift가 생길 가능성이 크다. USHER는 한 병원의 well-annotated scRNA-seq/bulk biopsy embedding space를 reference로 두고, 다른 병원 또는 spatial transcriptomics/Xenium/CosMx biopsy embedding을 post-hoc으로 정렬하는 실험에 쓸 수 있다.

특히 scGPT/scFoundation으로 만든 rejection biopsy embedding을 downstream classifier에 넣기 전, OOD center embedding을 reference cohort에 맞춰 이동시키면 cross-center rejection prediction과 graft survival model의 robustness를 비교할 수 있다. 단, rejection-specific biology가 batch처럼 지워지지 않는지 DSA status, histology score, immune cell marker enrichment로 반드시 점검해야 한다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- USHER
- Distribution shift
- OOD embedding
- Optimal transport
- Fused Gromov-Wasserstein
- Entropic filtering
- Foundation model alignment
- scGPT
- Xenium
- MALDI
- Spatial transcriptomics
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%


아직 가져온 PDF highlight는 없습니다. 위 정리는 사용자가 제공한 `2025.11.20.689462v2.full.pdf` 원문을 기준으로 보강했다.

%% end annotations %%

## 11. Bibliography

Pratapa, Aditya, Purushothama Rao Tata와/과Rohit Singh. “USHER: Guiding Foundation Model Representations through Distribution Shifts”. Preprint, bioRxiv, 2025년 12월 14일. [https://doi.org/10.1101/2025.11.20.689462](https://doi.org/10.1101/2025.11.20.689462).


%% Import Date: 2026-05-27T17:17:44.074+09:00 %%
