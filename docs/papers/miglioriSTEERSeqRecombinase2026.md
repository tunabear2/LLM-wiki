---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# STEER-seq: A Recombinase-Based Platform for Pooled Multimodal Single-Cell Perturbation Screening

## 기본 정보

- Citation key: `miglioriSTEERSeqRecombinase2026`
- Item type: preprint
- Authors: Valentina Migliori; Chenqu Suo; Otto Dufva; Ivan Gyulev; Krzysztof Polanski; et al.
- Source: bioRxiv v1, posted 2026-10-09 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.08.757551](https://doi.org/10.64898/2026.10.08.757551); [code](https://github.com/Teichlab/STEER); [Zenodo](https://doi.org/10.5281/zenodo.21510149)
- 주 카테고리: `Transcriptomics / Platform`
- 관련 카테고리: `scRNA-seq`

## 1. 한 줄 요약

STEER-seq는 Bxb1 landing pad에 ORF를 단일 copy로 넣어 integration site·copy-number confounding을 줄이고 perturbation identity를 scRNA 또는 joint RNA–ATAC에서 읽는다.

## 2. 연구 질문

Random viral integration 없이 동일한 promoter와 genomic context에서 대규모 gain-of-function perturbation을 정량 비교할 수 있는가?

## 3. 데이터와 방법

Human iPSC의 CLYBL safe-harbour locus에 Bxb1 landing pad를 만들고 promoterless donor library를 irreversible cassette exchange로 삽입했다. Barcode로 perturbation을 추적하고 scRNA-seq 또는 RNA–chromatin accessibility를 함께 측정했다. Focused hematopoietic screen, multimodal screen과 약 2,000 human coding-sequence pooled screen을 수행했다.

## 4. 핵심 결과

- SPI1 단독 발현이 cytokine 없이 HSC/MPP-like progenitor를 유도했고 transient induction 뒤 multilineage potential이 유지됐다.
- Joint RNA–ATAC에서 RUNX2-driven osteoblast program과 perturbation-induced GRN을 연결했다.
- 대규모 screen에서 neural progenitor, melanocyte, vascular smooth muscle-like state와 pluripotency 유지 factor를 찾았다.

## 5. 한계

강한 CAG-driven overexpression은 endogenous dosage·timing을 재현하지 않는다. 분화가 길어지면 transgene expression이 감소했고 genomic locus별 안정성도 다를 수 있다. Sufficiency screen이므로 loss-of-function이나 생리적 필요성을 직접 입증하지 않는다.

## 6. 재현 또는 활용 포인트

Landing-pad clone, cassette-exchange efficiency, barcode assignment threshold와 single-copy 확인을 기록한다. ORF expression과 barcode concordance, unperturbed control, RNA·ATAC replicate와 differentiation batch를 함께 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection-associated TF 후보를 endothelial·tubular·immune progenitor에서 기능적으로 시험하고 RNA–chromatin response를 함께 읽는 플랫폼으로 확장할 수 있다. 하지만 iPSC overexpression 결과를 성체 allograft cell에 바로 일반화하면 안 된다.

## 8. 관련 키워드

- pooled perturbation screen
- Bxb1 recombinase
- single-cell multiome
- gain of function

## 9. Bibliography

Migliori, Valentina, et al. “STEER-seq: A Recombinase-Based Platform for Pooled Multimodal Single-Cell Perturbation Screening.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.08.757551](https://doi.org/10.64898/2026.10.08.757551).
