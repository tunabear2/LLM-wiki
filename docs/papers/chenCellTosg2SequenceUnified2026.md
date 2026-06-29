# CellTosg2Sequence: A Unified Text-Omics-Signaling-Graph Large Language Model for Single-Cell Analysis

## 기본 정보

- Citation key: `chenCellTosg2SequenceUnified2026`
- Item type: preprint
- Authors: W. Chen; M. Ye; T. Xu; D. Huang; H. Zhang; H. Li; W. Li; Y. Chen; P. R. Payne; F. Li
- DOI: 10.64898/2026.06.16.732397
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.16.732397v1)
- Source/date: bioRxiv, 2026-06-22

## Abstract

CellTosg2Sequence is a text-prior- and signaling-graph-augmented cell-omics-sentence language model for single-cell analysis. It prepends compact virtual tokens from a curated biomedical knowledge graph to cell sentences, then trains with language-model pretraining, supervised alignment, and ontology-hierarchy reward optimization for free-generation cell-type prediction.

## 1. 한 줄 요약

%% begin one-line-summary %%
CellTosg2Sequence는 single-cell omics sentence에 biomedical text prior와 signaling graph token을 붙여 cell type annotation과 해석을 수행하는 scLLM이다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Expression value와 gene name만으로 cell을 표현하면 disease association, cellular localization, signaling interaction 같은 prior knowledge가 빠진다. 논문은 heterogeneous biomedical KG를 virtual token으로 압축해 cell sentence 앞에 붙이고, ontology reward로 free-generation annotation을 정렬한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Kidney transplant rejection에서는 cell type label뿐 아니라 rejection subtype, cytokine signaling, donor-specific immune activation 같은 prior를 함께 쓰는 annotation이 필요하다. CellTosg2Sequence식 KG token은 Banff lesion, HLA/alloimmune pathway, IFN/TNF signaling prior를 cell annotation과 marker interpretation에 넣는 설계 후보가 된다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- CellTosg2Sequence
- Single-cell large language model
- Biomedical knowledge graph
- Signaling graph
- Cell type annotation
- Ontology reward
- Kidney transplant rejection
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Chen, W., M. Ye, T. Xu, D. Huang, H. Zhang, H. Li, W. Li, et al. "CellTosg2Sequence: A Unified Text-Omics-Signaling-Graph Large Language Model for Single-Cell Analysis." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.16.732397](https://doi.org/10.64898/2026.06.16.732397).
