# Scoring gene importance by interpreting single-cell foundation models

## 기본 정보

- Citation key: `goldScoringGeneImportance2026`
- Item type: journalArticle
- Authors: Maxwell P. Gold; Miguel Reyes; Nathaniel Diamant; Tony Kuo; Ehsan Hajiramezanali; Jane W. Newburger; Mary Beth F. Son; Pui Y. Lee; Gabriele Scalia; Aicha BenTaieb; Sharookh B. Kapadia; Anupriya Tripathi; Hector Corrada Bravo; Graham Heimberg; Tommaso Biancalani
- DOI: 10.1038/s41587-026-03112-5
- PMID: 42204361
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42204361/)
- Source/date: PubMed / Nature Biotechnology, 2026-05-27

## Abstract

Determining a gene's functional importance within a cellular context has long been a challenge because absolute expression level is an unreliable indicator. The paper introduces SIGnature, a framework for scoring gene importance using attributions derived from single-cell RNA-seq foundation models. It uses attribution scores to reduce technical noise, emphasize regulatory genes, support cross-dataset comparison, and query large scRNA-seq atlases for shared disease programs.

## 1. 한 줄 요약

%% begin one-line-summary %%
SIGnature는 single-cell foundation model attribution을 사용해 세포 상태별 gene importance를 계산하고, 대규모 scRNA-seq atlas에서 질병 signature를 검색하는 해석/검색 프레임워크다.
%% end one-line-summary %%

## 2. 배경

%% begin background %%
scRNA-seq에서 어떤 gene이 특정 cell state에 기능적으로 중요한지 판단할 때 expression level만 보면 noise, dropout, batch, cell type composition의 영향을 크게 받는다. Foundation model은 gene-gene context와 cell state representation을 학습하지만, embedding을 그대로 쓰는 것만으로는 어떤 gene이 왜 중요한지 설명하기 어렵다.

이 논문은 pretrained single-cell foundation model의 attribution을 gene importance score로 바꾸면, 단순 발현량보다 regulatory gene과 disease program을 더 잘 포착할 수 있는지 평가한다.
%% end background %%

## 3. 핵심 아이디어

%% begin core-idea %%
SIGnature는 scRNA-seq foundation model에서 gene별 attribution을 계산해 cell context-specific gene importance score를 만든다. 이 attribution score를 gene set 검색과 atlas-scale querying에 사용하면, 여러 study 사이에서 공유되는 disease-associated cell state를 찾을 수 있다. 저자들은 severe COVID-19/sepsis의 MS1 monocyte program을 400개 study에서 검색해 Kawasaki disease와의 연결을 찾고, serum validation으로 이를 확인했다.
%% end core-idea %%

## 4. Method

### Input

%% begin method-input %%
입력은 scRNA-seq dataset, pretrained single-cell foundation model, 그리고 관심 gene set 또는 disease signature다. 논문 사례에서는 MS1 monocyte signature를 중심으로 여러 scRNA-seq study를 검색한다.
%% end method-input %%

### Model Architecture

%% begin method-architecture %%
SIGnature 자체는 새 foundation model이라기보다 foundation model interpretation layer다.

1. scRNA-seq profile을 pretrained single-cell foundation model에 입력한다.
2. Gene별 attribution score를 계산해 각 cell context에서 gene importance를 추정한다.
3. Attribution-derived gene importance를 모아 signature score 또는 searchable index를 만든다.
4. 여러 scRNA-seq study와 disease condition에서 유사 signature를 query한다.

핵심은 absolute expression 대신 foundation model attribution을 gene importance proxy로 사용하는 것이다.
%% end method-architecture %%

### Training Objective

%% begin method-objective %%
새로운 pretraining objective보다 attribution scoring과 querying framework가 중심이다. 목표는 technical noise를 줄이고, regulatory genes를 더 강조하며, 서로 다른 dataset 사이에서도 비교 가능한 gene importance representation을 만드는 것이다.
%% end method-objective %%

### Output

%% begin method-output %%
출력은 gene별/cell별 importance score, gene set query 결과, disease condition 사이의 shared signature association이다. 논문은 MS1 monocyte signature가 COVID-19, sepsis, Kawasaki disease 같은 hyperinflammatory condition과 연결될 수 있음을 보여준다.
%% end method-output %%

## 5. Figure 정리

### Figure 1

%% begin figure-1 %%
SIGnature workflow를 보여주는 그림으로 볼 수 있다. Single-cell foundation model에서 attribution을 계산하고, 이를 gene importance score로 바꾼 뒤 atlas-scale gene set 검색에 사용하는 흐름이다.
%% end figure-1 %%

### Figure 2

%% begin figure-2 %%
주요 결과는 MS1 monocyte signature 검색이다. 저자들은 400개 study를 대상으로 signature association을 찾고, Kawasaki disease serum이 MS1 phenotype을 유도한다는 실험적 validation을 제시한다.
%% end figure-2 %%

## 6. 장점

%% begin strengths %%
- Foundation model을 downstream classifier로만 쓰지 않고 gene-level interpretation에 활용한다.
- Expression level이 아닌 attribution 기반 score를 사용해 regulatory relevance를 더 직접적으로 보려 한다.
- Cross-dataset/cross-disease search에 맞는 framework라 atlas-scale scRNA-seq 활용성이 높다.
- Hyperinflammatory monocyte program처럼 immune disease state를 찾는 예제가 있어 transplant rejection research와 연결 가능성이 있다.
%% end strengths %%

## 7. 한계

%% begin limitations %%
- Attribution score가 causal gene importance를 보장하지는 않는다.
- Foundation model의 pretraining corpus, preprocessing, attribution method 선택에 결과가 의존할 수 있다.
- 논문 사례는 monocyte hyperinflammation 중심이며 kidney transplant rejection에 직접 검증된 것은 아니다.
- Clinical decision marker로 쓰려면 외부 cohort, assay platform, time point별 robustness 검증이 필요하다.
%% end limitations %%

## 8. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서는 rejection biopsy scRNA-seq 또는 public atlas에서 rejection-associated monocyte/macrophage, T cell, endothelial signature를 SIGnature식 attribution score로 재평가할 수 있다. 단순 DEG가 아니라 foundation model이 cell context 안에서 중요하게 보는 gene을 찾으면, rejection subtype marker나 perturbation target 후보를 좁히는 데 도움이 될 수 있다.

특히 antibody-mediated rejection과 T cell-mediated rejection에서 공유/특이 inflammatory programs를 query하고, infection/injury dataset과 비교해 rejection-specific signal인지 확인하는 분석에 맞다.
%% end research-ideas %%

## 9. 관련 키워드

%% begin keywords %%
- SIGnature
- Single-cell foundation model
- Attribution
- Gene importance
- scRNA-seq atlas
- MS1 monocyte
- Hyperinflammation
- Kawasaki disease
- Transplant rejection
%% end keywords %%

## 10. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 PubMed abstract와 article metadata를 기준으로 작성했다.

%% end annotations %%

## 11. Bibliography

Gold, Maxwell P., Miguel Reyes, Nathaniel Diamant, Tony Kuo, Ehsan Hajiramezanali, Jane W. Newburger, Mary Beth F. Son, Pui Y. Lee, Gabriele Scalia, Aicha BenTaieb, Sharookh B. Kapadia, Anupriya Tripathi, Hector Corrada Bravo, Graham Heimberg, and Tommaso Biancalani. "Scoring gene importance by interpreting single-cell foundation models." _Nature Biotechnology_, 2026. [https://doi.org/10.1038/s41587-026-03112-5](https://doi.org/10.1038/s41587-026-03112-5).

