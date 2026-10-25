---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# DCSMAP: A Hybrid Linear-Pangenome Framework for Accurate and Efficient Read Alignment

## 기본 정보

- Citation key: `yangDCSMAPHybridPangenome2026`
- Item type: bioRxiv preprint
- Authors: Q. Yang; R. Wan; C. Gong; S. Li; Y. Li; Y. Zhang
- Source: bioRxiv v1, posted 2026-10-19 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.18.759502](https://doi.org/10.64898/2026.10.18.759502)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

DCSMAP은 linear alignment가 불확실한 read pair만 XGBoost로 골라 personalized pangenome graph에 다시 매핑해 reference bias와 variant-calling error를 줄이면서 계산량을 억제한다.

## 2. 연구 질문

Linear reference의 속도와 personalized pangenome의 정확도를 selective remapping으로 결합할 수 있는가?

## 3. 데이터와 방법

Linear-alignment feature로 XGBoost classifier를 학습해 graph remapping 대상 read를 선택하고 local indel realignment를 적용했다. GIAB 7개 sample, 두 sequencing platform과 두 read length를 포함한 17개 run에서 BWA-MEM2와 vg personalized-pangenome workflow를 비교했다.

## 4. 핵심 결과

- Held-out classifier AUROC는 0.9831이고 평균 14.80% read pair만 graph로 다시 매핑했다.
- Variant-calling error는 BWA-MEM2보다 46.66%, vg personalized pangenome보다 8.39% 감소했다.
- HG003 DNBSEQ PE150·32 thread에서 personalized-pangenome workflow보다 2–2.5배 빨랐고 allelic balance의 reference bias도 줄었다.

## 5. 한계

GIAB 7개 human sample과 평가한 short-read platform/read length에 한정된다. Training feature와 threshold가 다른 ancestry, complex region, clinical pipeline에 그대로 일반화되는지와 code availability는 확인이 필요하다.

## 6. 재현 또는 활용 포인트

GIAB truth region별 SNP/indel error, difficult-region stratification, allelic balance와 wall time·memory를 함께 비교한다. Classifier calibration과 graph/reference version을 고정한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient WGS의 reference bias를 낮춰 eQTL·allele-specific expression 연결을 개선할 수 있다. HLA/KIR과 고다형성 영역은 별도의 graph와 orthogonal validation이 필요하다.

## 8. 관련 키워드

- DNA-seq / Variant Analysis
- read alignment
- pangenome
- reference bias

## 9. Bibliography

Yang, Q., et al. “DCSMAP: A Hybrid Linear-Pangenome Framework for Accurate and Efficient Read Alignment.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.18.759502](https://doi.org/10.64898/2026.10.18.759502).
