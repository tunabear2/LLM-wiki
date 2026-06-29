# Cellfm-datasets: A Unified Data Infrastructure for Single-Cell and Spatial Transcriptomics Foundation Model Pretraining

## 기본 정보

- Citation key: `zhangCellfmDatasets2026`
- Item type: preprint
- Authors: L. Zhang; J. Pang; J. Yan; W. Tang; Y. Deng; Y. He
- DOI: 10.64898/2026.06.11.731508
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.06.11.731508v1)
- Source/date: bioRxiv, 2026-06-14

## Abstract

Cellfm-datasets is a data infrastructure artifact for pretraining cell foundation models from single-cell and spatial transcriptomics data. It converts H5AD cohorts into compressed sparse row memmap layouts and exposes them through Hugging Face Dataset and IterableDataset interfaces with metadata, manifests, checksums, spatial coordinates, and distributed sampling support.

## 1. 한 줄 요약

%% begin one-line-summary %%
Cellfm-datasets는 H5AD 기반 single-cell/spatial transcriptomics corpus를 대규모 cell foundation model pretraining에 맞게 sparse memmap과 Hugging Face dataset interface로 바꾸는 데이터 인프라다.
%% end one-line-summary %%

## 2. 핵심 아이디어

%% begin core-idea %%
Foundation model 성능은 architecture뿐 아니라 out-of-core sparse transcriptome을 빠르고 재현 가능하게 sampling하는 data layer에 좌우된다. 이 논문은 shared gene vocabulary, sample metadata, spatial coordinates, manifest, checksum, distributed sharding을 포함한 pretraining용 layout을 제안한다.
%% end core-idea %%

## 3. 내 연구에 적용할 아이디어

%% begin research-ideas %%
Transplant biopsy scRNA/spatial cohort를 여러 기관에서 모을 때 H5AD 파일을 그대로 학습 루프에 넣으면 random mini-batch IO와 metadata 추적이 병목이 된다. Cellfm-datasets 방식은 rejection label, Banff score, donor/recipient metadata, spatial block sampling을 함께 보존하면서 cohort-scale embedding pretraining 또는 continual pretraining을 설계할 때 참고할 수 있다.
%% end research-ideas %%

## 4. 관련 키워드

%% begin keywords %%
- Cellfm-datasets
- Foundation model pretraining
- Single-cell transcriptomics
- Spatial transcriptomics
- H5AD
- CSR memmap
- Hugging Face Dataset
- Transplant cohort infrastructure
%% end keywords %%

## 5. Zotero PDF 하이라이트

%% begin annotations %%

아직 가져온 PDF highlight는 없습니다. 위 정리는 bioRxiv metadata와 abstract를 기준으로 작성했다.

%% end annotations %%

## 6. Bibliography

Zhang, L., J. Pang, J. Yan, W. Tang, Y. Deng, and Y. He. "Cellfm-datasets: A Unified Data Infrastructure for Single-Cell and Spatial Transcriptomics Foundation Model Pretraining." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.06.11.731508](https://doi.org/10.64898/2026.06.11.731508).

