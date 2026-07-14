# Task-adapted biological foundation models uncover perturbation-centric representations

## 기본 정보

- Citation key: `parejaLorenteTaskAdaptedBiological2026`
- Item type: preprint
- Authors: E. Pareja-Lorente and P. Aloy
- DOI: 10.64898/2026.06.30.735584
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.30.735584v1)
- Source/date: bioRxiv, 2026-07-05

## Abstract

This paper fine-tunes scGPT, originally pretrained on more than 30 million single-cell transcriptomes, on over three million LINCS L1000 perturbation profiles with a supervised objective that predicts perturbation identity. The adaptation shifts the latent space from cellular-state representation toward perturbation-centric representation, aligning chemical and genetic perturbation responses across heterogeneous conditions. The resulting embeddings improve nearest-neighbor recovery and classification of perturbation identity, while also capturing chemical similarity, mechanisms of action, compound-target relationships, and functional relationships between genetic perturbations.

## 1. 한 줄 요약

%% begin one-line-summary %%
scGPT를 perturbation identity 예측 objective로 재학습하면 cell-state 중심 embedding이 perturbation-centric latent space로 바뀌어 MOA와 chemical-genetic 관계를 더 잘 회수한다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Foundation model의 latent space는 pretraining objective가 무엇을 요구했는지에 강하게 의존한다. 논문은 scGPT checkpoint를 그대로 쓰는 대신 LINCS L1000 perturbation profile에 supervised adaptation을 적용해, 같은 perturbation이 서로 다른 조건에서 가까워지는 embedding space를 만든다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서 scGPT embedding을 cell type annotation에만 쓰지 않고, IFN/TNF stimulation, immunosuppression, ischemia-reperfusion, anti-rejection therapy response 같은 perturbation label로 objective-driven adaptation을 설계할 수 있다. 단, L1000/bulk perturbation과 kidney single-cell rejection state 사이의 modality gap은 external validation으로 따로 확인해야 한다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- scGPT
- Perturbation-centric representation
- LINCS L1000
- Mechanism of action
- Chemical-genetic association
- Objective-driven adaptation
- Kidney transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Pareja-Lorente, E., and P. Aloy. "Task-adapted biological foundation models uncover perturbation-centric representations." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.30.735584](https://doi.org/10.64898/2026.06.30.735584).
