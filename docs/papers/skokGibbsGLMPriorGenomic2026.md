---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# GLM-Prior: a genomic language model for transferable sequence-derived priors in gene regulatory network inference

## 기본 정보

- Citation key: `skokGibbsGLMPriorGenomic2026`
- Item type: journal article
- Authors: Claudia Skok Gibbs; Angelica Chen; Richard Bonneau; Kyunghyun Cho
- Journal: Nature Communications 17, 10225 (2026)
- DOI: 10.1038/s41467-026-77381-8
- PMID: [42791261](https://pubmed.ncbi.nlm.nih.gov/42791261/)
- URL: [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13614953/); [DOI](https://doi.org/10.1038/s41467-026-77381-8)
- Source/date: published 2026-09-14; newly indexed in PubMed 2026-09-25
- 주 카테고리: Bio AI
- 교차 카테고리: scRNA-seq

## 1. 한 줄 요약

GLM-Prior는 genomic language model로 TF–target gene interaction prior를 만들고 이를 scRNA-seq 기반 GRN inference에 결합해, matched chromatin assay가 없는 포유류 맥락에서도 사용할 수 있는 sequence-derived regulatory scaffold를 제안한다.

## 2. 연구 질문

불완전한 curated interaction과 cell-type-specific chromatin accessibility에 의존하는 기존 GRN prior를 보완하기 위해, nucleotide sequence만으로 다른 종과 세포 맥락에 전이 가능한 TF–gene prior를 만들 수 있는가?

## 3. 데이터와 방법

850종 genome으로 사전학습된 250M-parameter Nucleotide Transformer를 TF motif sequence와 gene-body sequence의 쌍을 입력받는 binary classifier로 fine-tune했다. YEASTRACT, STRING과 TRRUST의 interaction을 positive label로 사용하고 미주석 pair를 unlabeled negative로 취급했다. Yeast, hESC, HepG2, mESC, mouse dendritic cell과 mouse hematopoietic stem cell의 6개 맥락에서 single-species, species-transfer와 multi-species 학습을 비교했다. 독립 reference network와 겹치는 TF–gene pair를 학습에서 제거하고 세 random seed로 평가했으며, 생성한 prior를 scRNA-seq 기반 PMF-GRN에 넣고 Inferelator-Prior와 CellOracle prior 및 세 GRN inference 방법을 교차 비교했다.

## 4. 핵심 결과

GLM-Prior는 평가한 5개 mammalian context 중 4개에서 가장 높은 prior AUPRC를 보였다. mHSC에서는 AUPRC 0.44–0.49로 chance와 shuffled control의 0.37을 넘었고, PMF-GRN 결합 후 0.52로 증가했다. HepG2에서는 0.30에서 0.38, mESC에서는 0.23에서 0.27로 개선됐다. 반면 yeast는 0.02, mDC는 0.09로 사실상 chance 수준이었다. 전체 비교에서는 downstream algorithm보다 입력 prior의 품질이 최종 GRN 성능을 더 강하게 제한했다.

## 5. 한계

미주석 interaction을 negative처럼 학습하므로 실제 미발견 edge가 label noise로 포함될 수 있고, negative downsampling이 유용한 pair를 제외할 수 있다. 6개 cell-line reference network도 완전한 regulatory map이 아니다. Gene-body 입력은 composition, 길이, gene-family와 annotation density 같은 proxy를 포함할 가능성이 있으며, distal enhancer, 3D genome과 cell-type-specific chromatin 상태를 직접 표현하지 않는다. 종간 전이는 가까운 mammalian species에서는 작동했지만 yeast에서는 일반화되지 않았다.

## 6. 재현 또는 활용 포인트

- 코드: [cskokgibbs/GLM-Prior](https://github.com/cskokgibbs/GLM-Prior)
- 모델·tokenized dataset·prior·GRN: [Hugging Face collection](https://huggingface.co/collections/cskokgibbs/glm-prior)
- Archived code: [Zenodo](https://doi.org/10.5281/zenodo.21110427)
- Public GEO scRNA-seq, BEELINE reference, YEASTRACT·STRING·TRRUST와 공개 ATAC-seq accession을 사용한다.
- 논문 설정은 4대 H100, 10 epoch, 세 random seed이며, chance·shuffled-sequence·shuffled-prediction control과 AUPRC를 함께 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 biopsy scRNA-seq에 matched ATAC-seq가 없을 때 immune, endothelial과 renal parenchymal cell의 TF–target prior를 만들고 expression으로 제한적으로 보정하는 출발점이 될 수 있다. 다만 현재 검증은 cell line 중심이므로 rejection과 stable graft cohort에서 donor-level 분리, 외부 reference와 perturbation evidence를 사용해 다시 검증해야 한다.

## 8. 관련 키워드

- Bio AI
- Genomic language model
- Gene regulatory network
- Sequence-derived prior
- scRNA-seq
- Cross-species transfer

## 9. Bibliography

Skok Gibbs, Claudia, Angelica Chen, Richard Bonneau, and Kyunghyun Cho. “GLM-Prior: A Genomic Language Model for Transferable Sequence-Derived Priors in Gene Regulatory Network Inference.” _Nature Communications_ 17 (2026): 10225. [https://doi.org/10.1038/s41467-026-77381-8](https://doi.org/10.1038/s41467-026-77381-8).
