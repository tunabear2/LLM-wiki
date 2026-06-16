# Evaluating the learnability of single-cell large language models on multiple tasks

## 기본 정보

- Citation key: `yanEvaluatingLearnabilitySingleCell2026`
- Item type: journalArticle
- Authors: Y. Yan; X. Wang; D. Song
- DOI: 10.1186/s12864-026-12975-6
- PMID: 42249309
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42249309/)
- Source/date: PubMed / BMC Genomics, 2026-06 watch window

## Abstract

The paper evaluates representative single-cell foundation models, including Geneformer and scGPT, across perturbation prediction and cell type annotation. It questions whether larger pretrained models consistently improve downstream biological tasks, and reports that benefits are task-dependent: stronger for annotation, weaker or limited for perturbation prediction under the tested settings.

## 1. 한 줄 요약

%% begin one-line-summary %%
Geneformer와 scGPT를 여러 task에서 비교해, 대규모 pretraining과 model scaling이 cell type annotation에는 도움이 되지만 perturbation prediction에서는 제한적일 수 있음을 보인 benchmark 논문이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
논문은 scFM의 "bigger is better" 가정을 직접 검증한다. 실제 데이터와 synthetic complexity 조건에서 Geneformer/scGPT를 평가해, cell type annotation처럼 representation transfer가 중요한 task와 perturbation prediction처럼 causal/generalization이 필요한 task의 learnability가 다르다고 주장한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection 연구에서는 scFM embedding을 쓰더라도 task별 baseline을 반드시 둬야 한다. Cell type/subtype annotation 보조에는 Geneformer나 scGPT가 유용할 가능성이 크지만, rejection response나 gene perturbation 후보를 예측할 때는 raw expression, DEG, pathway, GRN, simpler supervised model과 비교해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Single-cell foundation model
- Geneformer
- scGPT
- Benchmark
- Learnability
- Perturbation prediction
- Cell type annotation
- Scaling law
- Transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 PubMed abstract와 article metadata를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Yan, Y., X. Wang, and D. Song. "Evaluating the learnability of single-cell large language models on multiple tasks." _BMC Genomics_, 2026. [https://doi.org/10.1186/s12864-026-12975-6](https://doi.org/10.1186/s12864-026-12975-6).

