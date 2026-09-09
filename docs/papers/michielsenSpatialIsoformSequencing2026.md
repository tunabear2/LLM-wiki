---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# Spatial isoform sequencing at single-cell resolution reveals cell-type-specific spatial isoform variability in multiple brain cell types

## 기본 정보

- Citation key: michielsenSpatialIsoformSequencing2026
- Item type: journalArticle
- Authors: Lieke Michielsen; Andrey D. Prjibelski; Careen Foord; Yelizaveta Spiegelman; Taewoo Kim; Wen Hu; Julien Jarroux; Justine Hsu; Rebecca Pfeil; Xinyi Zhang; Li Gan; Alexandru I. Tomescu; Iman Hajirasouliha; Hagen U. Tilgner
- Journal: Nature Methods
- DOI: 10.1038/s41592-026-03211-w
- URL: [Publisher](https://www.nature.com/articles/s41592-026-03211-w)
- Source/date: published 2026-09-04
- 주 카테고리: Transcriptomics / Platform
- 교차 카테고리: scRNA-seq

## 1. 한 줄 요약

Spl-ISO-Seq2와 Spl-IsoQuant-2·Spl-IsoFind는 Stereo-seq barcode에 long read를 연결해 single-cell spatial isoform과 cell-type-specific spatial variability를 측정한다.

## 2. 연구 질문

공간 좌표와 세포형을 유지하면서 full-length isoform을 single-cell 수준으로 읽고, cell composition 때문이 아닌 isoform-specific spatial pattern을 찾을 수 있는가?

## 3. 데이터와 방법

500-nm Stereo-seq에서 PacBio·Oxford Nanopore long read와 short read를 연결하는 Spl-ISO-Seq2를 만들었다. Spl-IsoQuant-2는 여러 barcode platform의 isoform을 할당하고, Spl-IsoFind는 Moran’s I와 cell-type-constrained permutation으로 spatially variable isoform을 검정했다. 성체 mouse brain 연속 절편과 공개 Visium HD·human hippocampus 자료를 사용했다.

## 4. 핵심 결과

기존 10-µm 방식보다 공간 barcode 해상도를 20배 높였다. 발견한 spatially variable isoform의 58.6%가 둘 이상의 dataset에서 재현됐고, 274개 후보 중 229개가 cell-type composition을 제한한 permutation 후에도 유의했다. Snap25와 Rps24 등에서 cell-type-specific spatial isoform pattern을 제시했다.

## 5. 한계

주요 공간 실험은 mouse brain에 집중됐다. 10-µm 절편의 z축 중첩과 glial doublet, nuclear-stain 기반 segmentation이 세포 할당을 제한하며 엄격한 doublet 제거는 검정력을 낮춘다. Human hippocampus 표본과 sequencing depth도 제한적이고 신장·FFPE 적용은 검증되지 않았다.

## 6. 재현 또는 활용 포인트

- Raw data: SRA BioProject PRJNA1282707
- Isoform assignment: [algbio/spl-IsoQuant](https://github.com/algbio/spl-IsoQuant)
- Spatial test: [tilgnerlab/Spl-IsoFind](https://github.com/tilgnerlab/Spl-IsoFind)
- 전체 재현 코드: [tilgnerlab/Spl-IsoFind_reproducibility](https://github.com/tilgnerlab/Spl-IsoFind_reproducibility)
- Cell-type composition을 고정한 null model과 donor·section 재현성을 함께 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

거부반응 병변에서 immune·tubular cell의 isoform과 위치를 함께 볼 수 있는 유망한 플랫폼이다. 먼저 fresh-frozen 신장 조직의 RNA quality, segmentation과 depth를 검증하고 short-read splicing 및 targeted PCR과 교차 확인해야 한다.

## 8. 관련 키워드

- Transcriptomics / Platform
- Spatial transcriptomics
- Long-read RNA sequencing
- Isoform
- Single-cell
- Alternative splicing

## 9. Bibliography

Michielsen, Lieke, et al. “Spatial Isoform Sequencing at Single-cell Resolution Reveals Cell-type-specific Spatial Isoform Variability in Multiple Brain Cell Types.” Nature Methods, 2026. [https://doi.org/10.1038/s41592-026-03211-w](https://doi.org/10.1038/s41592-026-03211-w).
