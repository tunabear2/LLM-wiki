---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# Systematic Evaluation of Transcript Normalization across Long-read Platforms

## 기본 정보

- Citation key: `paniaguaSystematicEvaluationTranscript2026`
- Item type: bioRxiv preprint
- Authors: Alejandro Paniagua; Fabian Jetzinger; Sonia Tarazona; Ana Conesa
- Source: bioRxiv v1, posted 2026-10-15 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.10.757893](https://doi.org/10.64898/2026.10.10.757893); [pipeline](https://github.com/alexpan00/transcript_bias); [plots](https://github.com/alexpan00/length_bias_plots); [large inputs](https://doi.org/10.5281/zenodo.22109031)
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

PacBio와 ONT long-read RNA-seq의 길이 편향이 달라 같은 normalization을 공유할 수 없으며, PacBio에는 TPM이 유용하지만 ONT에서는 TPM이 abundance를 왜곡할 수 있음을 실증했다.

## 2. 연구 질문

Long-read transcript quantification에서 reconstruction/quantifier와 normalization의 조합이 platform별 abundance 정확도에 어떤 영향을 주는가?

## 3. 데이터와 방법

Mouse tissue mixture, LongBench lung-cancer cell line, iNeuron 세 dataset에서 SIRV/ERCC spike-in과 matched Illumina를 기준으로 삼았다. PacBio Iso-Seq·Kinnex와 ONT cDNA·direct RNA를 Bambu, FLAIR, IsoQuant, Oarfish, Kallisto로 처리하고 CPM, TPM, CQN, EDASeq, scaled median ratio를 비교했다.

## 4. 핵심 결과

- TPM은 PacBio의 short-molecule depletion을 상쇄했지만 ONT abundance에는 심한 왜곡을 만들었다.
- ONT에서는 CQN·EDASeq가 length bias를 완화했지만 unadjusted CPM을 크게 넘지는 못했다.
- FLAIR는 짧은 SIRV absolute error가 낮았고, Oarfish·Kallisto 같은 reference-restricted quantifier는 matched short-read 검증에서 reconstruction tool보다 안정적이었다.

## 5. 한계

세 dataset과 평가한 protocol/version에 한정된다. 기존 CQN/EDASeq는 static annotation length를 covariate로 써 5′ truncation, internal priming과 partial molecule의 비선형 편향을 충분히 설명하지 못했다. 한 저자는 PacBio in-kind 지원과 ONT 협업을 밝혔다.

## 6. 재현 또는 활용 포인트

Snakemake pipeline, raw accession과 plot script가 공개된다. Platform별로 spike-in RMSE, length/position bias와 matched short-read correlation을 함께 보고하고, TPM을 관성적으로 공통 적용하지 않는다.

## 7. Transcriptomics·신장이식 연구와의 연결

Kidney biopsy의 full-length isoform·splicing을 PacBio/ONT로 검증할 때 platform별 normalization을 분리해야 한다. Short-read bulk cohort와 합칠 때도 gene-level 일치만으로 isoform abundance 정확도를 가정하면 안 된다.

## 8. 관련 키워드

- Transcriptomics / Platform
- Bulk RNA-seq
- long-read RNA-seq
- normalization benchmark

## 9. Bibliography

Paniagua, Alejandro, et al. “Systematic Evaluation of Transcript Normalization Methods and Quantification Pipelines across Long-read Sequencing Platforms.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.10.757893](https://doi.org/10.64898/2026.10.10.757893).
