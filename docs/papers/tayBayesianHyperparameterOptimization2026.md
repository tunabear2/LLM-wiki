# Bayesian Hyperparameter Optimization Improves scGPT Fine-Tuning for Single-Cell Multi-Omics Integration

## 기본 정보

- Citation key: `tayBayesianHyperparameterOptimization2026`
- Item type: journalArticle
- Authors: Darren Y. Jun Tay; N. Q. Khanh Le; Marcus C. Heng Chua
- DOI: 10.1093/bioinformatics/btag374
- PMID: 42286785
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42286785/)
- Source/date: PubMed / Bioinformatics, 2026-06 watch window

## Abstract

Foundation models such as scGPT can support single-cell multi-omics integration, but downstream fine-tuning is sensitive to hyperparameter choices. This paper evaluates Bayesian hyperparameter optimization as a systematic alternative to manual scGPT fine-tuning, aiming to improve robustness, reproducibility, and dataset-specific performance.

## 1. 한 줄 요약

%% begin one-line-summary %%
scGPT fine-tuning에서 learning rate, regularization, batch/training 설정을 Bayesian optimization으로 고르면 single-cell multi-omics integration 성능과 재현성을 높일 수 있다는 실용적 최적화 논문이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Single-cell foundation model은 pretrained checkpoint만으로 끝나지 않고, downstream dataset에 맞춘 fine-tuning 전략이 성능을 크게 좌우한다. 이 논문은 manual search 대신 Bayesian optimization을 사용해 scGPT fine-tuning hyperparameter를 체계적으로 탐색하고, multi-omics integration task에서 더 안정적인 설정을 찾는 방향을 제시한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection dataset은 cohort 수, batch, cell type composition, assay platform 차이가 커서 scGPT fine-tuning 결과가 hyperparameter에 민감할 수 있다. Rejection/non-rejection 분류나 cross-cohort integration을 할 때 Optuna/BoTorch류 Bayesian search를 fold 안에서만 수행하고, external validation cohort는 완전히 남겨두는 실험 설계가 필요하다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- scGPT
- Hyperparameter optimization
- Bayesian optimization
- Single-cell multi-omics
- Fine-tuning
- Batch integration
- Kidney transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 PubMed abstract와 article metadata를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Tay, Darren Y. Jun, N. Q. Khanh Le, and Marcus C. Heng Chua. "Bayesian Hyperparameter Optimization Improves scGPT Fine-Tuning for Single-Cell Multi-Omics Integration." _Bioinformatics_, 2026. [https://doi.org/10.1093/bioinformatics/btag374](https://doi.org/10.1093/bioinformatics/btag374).

