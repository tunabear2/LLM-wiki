---
type: paper
status: reference
rag_priority: high
updated: '2026-11-09'
tags:
- wiki/paper
---

# Somatic Structural Variation Discovery on Cancer Pangenome Graphs

## 기본 정보

- Citation key: `karaSomaticStructuralVariation2026`
- Item type: preprint
- Authors: M. Kara; A. Ashyralyyev; C. Alkan
- Source: bioRxiv v1, posted 2026-11-06 (not peer reviewed)
- Original: [DOI: 10.64898/2026.11.05.764632](https://doi.org/10.64898/2026.11.05.764632); [code](https://github.com/BilkentCompGen/janus)
- 주 카테고리: `DNA-seq / Variant Analysis`

## 1. 한 줄 요약

JANUS는 matched tumor-normal PacBio HiFi read로 personal pangenome graph를 만들고 tumor-only path를 찾아 정렬 없이 somatic SV 후보를 빠르게 호출한다.

## 2. 연구 질문

Linear reference alignment의 비용과 reference bias를 줄이면서 저순도·저coverage·다중 tumor sample에서 somatic structural variant sensitivity를 유지할 수 있는가?

## 3. 데이터와 방법

Matched normal과 tumor HiFi read의 LCP core로 colored de Bruijn-like graph를 구성한다. Tumor read만 통과하는 site를 찾고 주변의 짧은 snippet만 mapping한다. CASTLE의 tumor-normal 5쌍에서 18-caller consensus와 비교하고, 20-tumor patient simulation에서 joint graph calling을 pairwise run과 비교했다.

## 4. 핵심 결과

- CASTLE 5쌍에서 mean F1 0.887로 다음 caller 0.858보다 높았다.
- 5× coverage에서는 F1 0.489 대 0.362, 20% purity에서는 0.683 대 0.520으로 low-signal 조건의 격차가 컸다.
- 16 thread에서 tumor-normal 한 쌍을 평균 약 11분에 분석해 같은 장비의 read alignment만 수행하는 시간보다 약 24배 빨랐다.

## 5. 한계

실제 평가는 PacBio HiFi의 5쌍에 집중되며 ONT·short-read·다양한 cancer type 일반화는 미확인이다. 18-caller consensus는 완전한 orthogonal truth가 아니고 graph parameter와 breakpoint validation의 영향을 받을 수 있다. Clinical low-purity specimen에서의 prospective 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Truth-set 정의, coverage, tumor purity, sample 수, SV type·size·repeat context별 precision/recall을 기록한다. Joint와 pairwise calling을 같은 hardware에서 비교하고 주요 breakpoint는 assembly 또는 PCR로 별도 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Post-transplant malignancy나 clonal evolution에서 여러 시점 tumor를 공동 분석하고 SV–fusion/expression outlier를 연결하는 후보이다. Donor–recipient germline 차이와 chimerism을 tumor-specific path로 오인하지 않도록 matched normal 설계가 필수다.

## 8. 관련 키워드

- somatic structural variant
- pangenome graph
- PacBio HiFi
- joint calling

## 9. Bibliography

Kara, M., A. Ashyralyyev, and C. Alkan. “Somatic Structural Variation Discovery on Cancer Pangenome Graphs.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.05.764632](https://doi.org/10.64898/2026.11.05.764632).
