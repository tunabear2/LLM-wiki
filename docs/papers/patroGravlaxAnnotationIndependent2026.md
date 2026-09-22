---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# Gravlax: an annotation-independent molecular evidence archive for scRNA-seq

## 기본 정보

- Citation key: `patroGravlaxAnnotationIndependent2026`
- Item type: preprint
- Author: Rob Patro
- DOI: 10.64898/2026.09.18.752708
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.18.752708v1); [DOI](https://doi.org/10.64898/2026.09.18.752708); [code](https://github.com/COMBINE-lab/gravlax)
- Source/date: bioRxiv v1, posted 2026-09-21; not peer reviewed
- 주 카테고리: scRNA-seq
- 교차 카테고리: Transcriptomics / Platform

## 1. 한 줄 요약

Gravlax는 annotation에 종속된 cell-by-gene matrix 대신 UMI·barcode·alignment geometry 사이의 분자 관계를 compact archive로 보존해, 미래 annotation 재정량과 cohort-wide novel-splice query를 빠르게 수행한다.

## 2. 연구 질문

Raw read나 대형 alignment를 계속 보관하지 않고도 scRNA-seq molecule evidence를 annotation-independent하게 남겨, annotation이 바뀔 때 재정량하고 아직 정의되지 않은 feature를 검색할 수 있는가?

## 3. 데이터와 방법

Gene assignment와 UMI collapse가 사용하는 shared geometry, placement, barcode와 UMI equality 관계를 충분통계로 정리해 seekable·content-authenticated archive에 저장한다. Archive를 content-addressed collection으로 묶어 복사 없이 cohort query를 routing한다. Human 10x 3′ dataset 4개와 archive 8개의 federated index에서 크기, replay fidelity, 속도와 novel-junction query를 평가했다.

## 4. 핵심 결과

Archive는 read당 11–18 bit로 tag-preserving CRAM보다 9.0–12.7배 작았다. Replay한 count matrix와 직접 STARsolo 결과의 차이는 normalized UMI mass 0.24–0.75%였고, GENCODE v32→v49 변경의 2.12–4.64%보다 작았다. 같은 thread budget에서 재정량은 STARsolo보다 34–82배 빨랐다. 8개 archive의 federated index는 전체 크기의 2.96%였고 recurrent unannotated splice event를 9초에 검색했다.

## 5. 한계

주 검증은 human 10x 3′ chemistry에 한정되고 replay는 완전히 동일하지 않다. Raw sequence와 base quality를 모두 보존하는 범용 FASTQ 대체재가 아니므로 새로운 alignment algorithm, variant·editing 분석에는 부족할 수 있다. Long-read·full-length·multiome chemistry 검증도 필요하며 현재 preprint다.

## 6. 재현 또는 활용 포인트

- Genome build, aligner와 barcode/UMI correction 설정을 archive manifest에 남긴다.
- Matrix replay error를 cell, gene, UMI mass와 splice feature별로 보고한다.
- Annotation update 전후 차이와 archive approximation error를 분리한다.
- Rust implementation과 archive hash를 함께 기록해 cohort collection의 provenance를 보존한다.

## 7. Transcriptomics·신장이식 연구와의 연결

여러 시기·기관의 kidney-biopsy scRNA-seq를 장기간 재주석하거나 recurrent novel splice event를 찾을 때 저장·재처리 비용을 낮출 수 있다. 다만 donor/recipient variant와 allele-specific expression을 연구한다면 raw read 보존 정책을 대체해서는 안 된다.

## 8. 관련 키워드

- scRNA-seq
- Molecular archive
- Annotation independence
- UMI quantification
- Reproducibility

## 9. Bibliography

Patro, Rob. “Gravlax: An Annotation-Independent Molecular Evidence Archive for Single-Cell RNA-seq.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.18.752708](https://doi.org/10.64898/2026.09.18.752708). Preprint; not peer reviewed.
