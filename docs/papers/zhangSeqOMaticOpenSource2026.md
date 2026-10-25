---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# Robust and Accessible In Situ Sequencing with an Open-Source Automated Sequencer

## 기본 정보

- Citation key: `zhangSeqOMaticOpenSource2026`
- Item type: bioRxiv preprint
- Authors: A. Zhang; Z. Maltzer; J. Lapka; S. Cheng; et al.
- Source: bioRxiv v1, posted 2026-10-23 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.18.759961](https://doi.org/10.64898/2026.10.18.759961)
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

Seq-o-Matic은 상용 부품으로 fluidics, heated incubation과 imaging을 통합해 large tissue section의 반복 in situ sequencing을 자동화하고 manual run과 비슷한 품질을 더 적은 hands-on time으로 냈다.

## 2. 연구 질문

표적 RNA barcode를 cellular resolution로 읽는 반복 반응·이미징 과정을 전문 장비 없이 재현성 있게 자동화할 수 있는가?

## 3. 데이터와 방법

표준 slide에서 최대 세 개의 연속 18×50 mm 영역을 처리하는 open-source instrument를 구성했다. 두 mouse strain과 neonatal marmoset을 포함한 세 자동 run을 네 manual mouse-brain run과 signal retention, channel specificity, phasing, consensus cell type과 run variation으로 비교했다.

## 4. 핵심 결과

- Manual sequencing 대비 hands-on time을 6–17.5배, total run time을 약 2.6배 줄였다.
- 세 자동 run의 sequencing quality가 네 manual brain과 비슷했다.
- 네 mouse hemisphere의 consensus cell type이 모두 회복됐고 같은 strain 간 유사성이 다른 strain 간 차이보다 커 run variation이 biological difference보다 작았다.

## 5. 한계

검증은 소수 mouse brain과 한 neonatal marmoset에 집중되고 human tissue, kidney biopsy와 site-to-site 재현성은 확인되지 않았다. 상용 부품 조립·유지보수와 시약비를 포함한 전체 도입비용도 별도 평가가 필요하다.

## 6. 재현 또는 활용 포인트

원문의 open-source 설계와 부품 정보를 고정하고 manual control을 같은 tissue·barcode panel에서 병행한다. Cycle별 signal retention, phasing, channel bleed-through와 run-to-run cell-type concordance를 기록한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Allograft biopsy에서 rejection marker RNA와 barcoded perturbation을 넓은 절편에 반복 측정하는 장기 플랫폼 후보다. FFPE/frozen kidney의 autofluorescence, fibrosis와 작은 biopsy 면적에 맞춘 검증이 선행되어야 한다.

## 8. 관련 키워드

- Transcriptomics / Platform
- in situ sequencing
- spatial transcriptomics
- open-source instrumentation

## 9. Bibliography

Zhang, A., et al. “Robust and Accessible In Situ Sequencing with an Open-Source Automated Sequencer.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.18.759961](https://doi.org/10.64898/2026.10.18.759961).
