---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Causal intervention validation of gene regulatory signals in scGPT

## 기본 정보

- Citation key: `kendiukhovCausalInterventionValidation2026`
- Item type: journalArticle
- Authors: Ihor Kendiukhov
- DOI: 10.1016/j.jbi.2026.105080
- PMID: [42398561](https://pubmed.ncbi.nlm.nih.gov/42398561/)
- URL: [Link](https://doi.org/10.1016/j.jbi.2026.105080)
- Source/date: PubMed / Journal of Biomedical Informatics, 2026-07-03

## Abstract

This paper tests whether causal interventions on scGPT gene tokens recover transcription-factor target dependencies that align with curated regulatory references and transfer to real perturbation data. The analysis uses Tabula Sapiens kidney, lung, and immune subsets, an external lung atlas, and CRISPR perturbation datasets. It reports tissue-conditional reference alignment, strongest and most robust in lung, but balanced perturbation-transfer AUROC near 0.50, meaning the model-internal signal should not be treated as biological causality.

## 1. 한 줄 요약

%% begin one-line-summary %%
scGPT gene token intervention은 일부 tissue에서 curated TF-target reference와 맞는 model-internal regulatory signal을 보이지만, 실제 CRISPR perturbation response로는 잘 transfer되지 않아 causal biology claim에는 신중해야 한다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Attention weight나 attribution score만으로 scGPT가 gene regulation을 학습했다고 주장하기 어렵기 때문에, 논문은 TF token 값을 ablation/swap하고 target gene readout 변화를 측정한다. Reference alignment와 perturbation transfer를 분리해 평가하고, cell count, negative sampling, readout strategy, activation patching, classical GRN baseline을 함께 비교한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서 scGPT로 IFN, HLA, cytotoxicity, endothelial activation 관련 TF-target edge를 뽑을 때, 이 결과를 regulatory hypothesis 후보로만 사용해야 한다. 특히 kidney subset에서는 sample scaling에서 signal이 약해졌으므로, rejection cohort 안의 external validation, perturb-seq/CRISPR reference, pathway-level holdout metric을 별도로 붙이는 설계가 필요하다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- scGPT
- Gene regulatory network
- Causal intervention
- Foundation model interpretability
- Perturbation transfer
- Tabula Sapiens kidney
- Kidney transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 PubMed metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Kendiukhov, Ihor. "Causal intervention validation of gene regulatory signals in scGPT." _Journal of Biomedical Informatics_, 2026. [https://doi.org/10.1016/j.jbi.2026.105080](https://doi.org/10.1016/j.jbi.2026.105080).
