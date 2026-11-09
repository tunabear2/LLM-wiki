---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# DirectClean: Artifact-Aware Preprocessing and Read Rescue for Oxford Nanopore Direct-cDNA Transcriptome Sequencing

## 기본 정보

- Citation key: `guoDirectCleanArtifactAware2026`
- Item type: journal article
- Authors: Qingxiang Guo; Yangyang Li; Rendong Yang
- Source: NAR Genomics and Bioinformatics; PubMed indexed 2026-11-01
- Original: [DOI: 10.1093/nargab/lqag132](https://doi.org/10.1093/nargab/lqag132); [PMID: 42966957](https://pubmed.ncbi.nlm.nih.gov/42966957/); [PMC: PMC13722937](https://pmc.ncbi.nlm.nih.gov/articles/PMC13722937/); [code](https://github.com/ylab-hi/DirectClean); [GEO: GSE277934](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277934); [Zenodo](https://doi.org/10.5281/zenodo.20418867)
- 주 카테고리: `Transcriptomics / Platform`
- 관련 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

DirectClean은 ONT direct-cDNA의 foldback, primer, internal-adapter, homopolymer template-switch artifact를 탐지하면서 회수 가능한 chimera를 junction 단위로 분할해 유효 read를 보존한다.

## 2. 연구 질문

Direct-cDNA 고유 chimera를 제거하되 isoform과 fusion 분석에 쓸 수 있는 read segment를 과도하게 버리지 않는 preprocessing이 가능한가?

## 3. 데이터와 방법

Strand orientation, artifact removal, recoverable chimera splitting을 한 workflow로 통합했다. 네 direct-cDNA dataset에서 Pychopper와 비교하고 semi-synthetic chimera로 junction rescue 정확도를 확인했다. Split-derived read의 novel transcript model enrichment도 untouched read와 비교했다.

## 4. 핵심 결과

- 네 dataset에서 Pychopper보다 read와 base를 일관되게 더 보존했다.
- VCaP에서 read retention은 65.2% 대 57.6%였고 raw chimeric-read rate는 30.9%에서 16.9%로 줄었다.
- Adapter-associated·A/T-rich chimera를 회수했으며 split-derived read가 novel transcript model을 과도하게 만들지 않았다.

## 5. 한계

평가는 direct-cDNA와 네 dataset에 한정되며 direct RNA, PCR-cDNA, 다양한 basecaller/library version으로 일반화하려면 추가 검증이 필요하다. Semi-synthetic truth가 실제 복합 artifact를 모두 재현하지 못하며 downstream fusion truth의 실험 검증도 별도 필요하다.

## 6. 재현 또는 활용 포인트

Raw·cleaned·split read를 구분해 retention, chimera rate, mapping, isoform, fusion precision을 단계별 기록한다. Pychopper와 같은 input·basecaller·reference에서 비교하고 주요 fusion과 novel isoform은 short-read/RT-PCR로 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Allograft biopsy long-read에서 rejection-associated isoform과 fusion-like artifact를 분리하는 전처리 후보다. 낮은 RNA input과 degraded tissue에서 read rescue가 주는 이득과 false junction 위험을 함께 측정해야 한다.

## 8. 관련 키워드

- Oxford Nanopore direct-cDNA
- chimeric artifact
- read rescue
- isoform sequencing

## 9. Bibliography

Guo, Qingxiang, Yangyang Li, and Rendong Yang. “DirectClean: Artifact-Aware Preprocessing and Read Rescue for Oxford Nanopore Direct-cDNA Transcriptome Sequencing.” _NAR Genomics and Bioinformatics_, 2026. [https://doi.org/10.1093/nargab/lqag132](https://doi.org/10.1093/nargab/lqag132).
