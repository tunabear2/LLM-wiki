---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Effective Biological Representation Learning by Masking Gene Expression

## 기본 정보

- Citation key: `kenyonDeanEffectiveBiologicalRepresentation2026`
- Item type: arXiv preprint
- Authors: Kian Kenyon-Dean; Alina Selega; Ihab Bendidi; Jordan M. Sorokin; Luca Bertinetto; David Errington; Hayley Donnella; Oren Kraus
- DOI: 10.48550/arXiv.2605.31562
- URL: [Link](https://arxiv.org/abs/2605.31562)
- Source/date: arXiv, 2026-05-29

## Abstract

RNA sequencing produces rich and diverse datasets of gene expression, offering compelling insights into cellular state and function that have many applications in drug discovery. Modeling such data is challenging due to inherent technical noise and experimental batch effects, as evidenced by many existing transcriptomic foundation models underperforming relative to linear baselines. The authors introduce TxFM, a self-supervised masked autoencoder for RNA-seq count data, and argue that strong transcriptomic representation learning depends on architecture and curated training data rather than only atlas scale.

## 1. 한 줄 요약

%% begin one-line-summary %%
TxFM은 다양한 RNA-seq count를 masked autoencoding으로 학습해, 큰 atlas-scale 모델보다 작은 curated corpus에서도 강한 transcriptomics representation을 만들 수 있음을 보인 transcriptomics foundation model이다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
Single-cell/transcriptomics foundation model은 대규모 gene expression data를 학습하지만, downstream task에서 단순 linear baseline보다 항상 낫지는 않다는 비판이 있다. 특히 technical noise, batch effect, count distribution, sparse expression을 잘 다루지 못하면 깊은 모델이 raw count의 정보를 충분히 이기기 어렵다.

이 논문은 "데이터를 더 크게 모으는 것"보다 "RNA-seq count에 맞는 self-supervised objective와 curated corpus를 쓰는 것"이 representation quality에 더 중요할 수 있다는 문제의식에서 출발한다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
TxFM은 일부 gene expression만 보여주고 나머지 gene expression을 복원하는 masked autoencoder다. Encoder는 unmasked gene token으로 sample/cell embedding을 만들고, decoder는 전체 gene expression vector를 재구성한다. DiverseRNA-1.4M이라는 curated RNA-seq corpus로 학습해, 훨씬 큰 atlas-scale corpus로 학습한 일부 transcriptomic FM보다 transfer와 gene representation에서 더 좋은 결과를 보고한다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 RNA-seq gene expression count vector다. 모델은 library-size normalization과 log transformation을 적용한 뒤, 각 sample에서 일부 gene만 unmasked input으로 사용한다.

Pretraining corpus는 DiverseRNA-1.4M으로 제시되며, 저자들은 데이터 규모 자체보다 다양한 조건과 품질 관리를 갖춘 corpus curation이 중요하다고 강조한다.
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
TxFM은 asymmetric masked autoencoder 구조다.

1. Gene마다 learnable gene embedding을 둔다.
2. Unmasked gene token은 gene embedding과 expression value를 결합해 만든다.
3. Transformer encoder가 unmasked gene token과 CLS token을 처리한다.
4. CLS embedding을 sample-level representation으로 사용한다.
5. Lightweight decoder가 전체 gene expression vector를 복원한다.

핵심 설계는 high mask ratio, count-aware reconstruction, decoder output stabilization이다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
Self-supervised objective는 masked gene expression reconstruction이다. 논문은 RNA-seq count 특성에 맞춘 Poisson-style reconstruction loss와 activation 설계가 transfer performance에 중요하다고 보고한다.

비교 관점은 "foundation model embedding이 normalized raw count보다 추가 정보를 제공하는가"이며, ablation으로 architecture, loss, mask ratio, data curation의 영향을 분리한다.
%% end method-objective %%

### Output

%% begin method-output %%
출력은 sample/cell-level transcriptomic embedding과 gene-level learned representation이다. Downstream에서는 sample representation quality, perturbation/drug-discovery 관련 transfer, gene-gene relationship recall 등을 평가한다.
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
TxFM의 masked autoencoder 구조를 설명하는 그림으로 볼 수 있다. 일부 gene expression만 encoder에 넣고, decoder가 전체 expression profile을 복원하도록 학습하면서 sample-level embedding과 gene representation을 동시에 얻는다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
주요 결과는 curated corpus와 count-aware MAE 설계가 transcriptomic representation quality를 끌어올린다는 비교다. 저자들은 TxFM이 훨씬 큰 atlas-scale FM과 linear baseline을 상대로도 강한 transfer 성능을 보였다고 주장한다.
%% end figure-2 %%

## 6. 장점

%% begin strengths %%
- scRNA-seq뿐 아니라 broader RNA-seq count representation learning 문제를 정면으로 다룬다.
- Foundation model이 raw count baseline을 이겨야 한다는 실용적인 평가 기준을 둔다.
- 데이터 규모보다 corpus curation과 objective 설계의 중요성을 강조한다.
- Kidney transplant rejection처럼 cohort size가 제한된 transcriptomics task에서 pretrained embedding의 실질적 value를 점검하는 기준으로 유용하다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- arXiv preprint라 peer review 전이다.
- 초록 기준으로는 kidney, transplant, immune rejection에 직접 특화된 실험은 아니다.
- TxFM이 기존 scGPT, Geneformer, scFoundation과 어떤 preprocessing/vocabulary 차이를 갖는지 실제 적용 전 확인이 필요하다.
- 모델과 corpus 접근성이 downstream 재현성의 핵심 변수가 된다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection 연구에서는 TxFM embedding을 raw pseudobulk/bulk expression, scFoundation/scGPT embedding, clinical covariate와 나란히 비교할 수 있다. 특히 rejection label이 적은 상황에서 embedding-only가 아니라 "embedding + raw expression + clinical" 조합이 실제로 baseline을 넘는지 검증하는 데 적합하다.

또한 TxFM의 high-mask reconstruction 관점은 rejection marker gene이 noisy하거나 부분적으로 missing한 platform에서도 robust한 patient/cell representation을 만드는 데 참고할 수 있다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- TxFM
- Transcriptomics foundation model
- Masked autoencoder
- RNA-seq count
- Gene expression representation
- Self-supervised learning
- Data curation
- Drug discovery
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 arXiv abstract와 검색 metadata를 기준으로 작성했다.

%% end annotations %%

## 11. Bibliography

Kenyon-Dean, Kian, Alina Selega, Ihab Bendidi, Jordan M. Sorokin, Luca Bertinetto, David Errington, Hayley Donnella, and Oren Kraus. "Effective Biological Representation Learning by Masking Gene Expression." arXiv, 2026. [https://doi.org/10.48550/arXiv.2605.31562](https://doi.org/10.48550/arXiv.2605.31562).

