# scVision: A vision foundation model for single-cell biology via spatial gene cartography

## 기본 정보

- Citation key: `yesilogluScVision2026`
- Item type: preprint
- Authors: Ridvan Yesiloglu; Sakib Mostafa; James Zou; Ash Alizadeh; Jiajun Wu; Lei Xing; Ehsan Adeli; Md Tauhidul Islam
- DOI: 10.48550/arXiv.2607.14163
- URL: [Link](https://arxiv.org/abs/2607.14163)
- Source/date: arXiv, 2026-07-15

## 1. 한 줄 요약

scVision은 각 cell transcriptome을 gene token sequence가 아니라 gene-gene co-expression layout 위의 연속 이미지로 렌더링하고, masked image modeling으로 vision transformer encoder를 pretraining한 single-cell foundation model이다.

## 2. 왜 중요한가

대부분의 scFM은 gene 순위나 token sequence를 사용하면서 expression magnitude와 gene 간 인접 구조를 일부 잃는다. 이 논문은 optimal transport로 genes를 공통 2D cartography에 배치하고 cell을 image처럼 표현해, frozen encoder 상태에서도 cell type annotation, gene program recovery, multi-study integration을 평가한다.

## 3. 내 연구에 연결할 점

Kidney transplant rejection scRNA-seq에서 HLA, IFN response, endothelial activation, cytotoxic T/NK program처럼 co-expressed gene module이 공간 texture로 보존되는지 확인할 수 있다. 특히 token-based scGPT/Geneformer embedding과 scVision embedding을 같은 external cohort에서 비교하면 normalization과 gene-order 가정의 영향을 분리해 볼 수 있다.

## 4. Bibliography

Yesiloglu, Ridvan, Sakib Mostafa, James Zou, Ash Alizadeh, Jiajun Wu, Lei Xing, Ehsan Adeli, and Md Tauhidul Islam. "A vision foundation model for single-cell biology via spatial gene cartography." _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2607.14163](https://doi.org/10.48550/arXiv.2607.14163).
