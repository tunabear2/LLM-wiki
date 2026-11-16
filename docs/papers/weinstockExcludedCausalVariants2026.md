---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# Excluded causal variants produce false discoveries in genetic fine-mapping

## 기본 정보

- Citation key: `weinstockExcludedCausalVariants2026`
- Item type: preprint
- Author: Josh Weinstock
- Source: medRxiv v1, posted 2026-11-10 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.09.26367644](https://doi.org/10.64898/2026.11.09.26367644)
- 주 카테고리: `GWAS`

## 1. 한 줄 요약

MAF·indel filter로 causal variant를 fine-mapping 입력에서 빼면 linked proxy가 높은 PIP를 받아 false discovery가 생기며, omitted-causal component를 둔 SuSiE-OUT이 이를 줄인다.

## 2. 연구 질문

Fine-mapping 전의 흔한 MAF·variant-type filter가 실제 locus에서 causal assignment를 얼마나 왜곡하며, 누락된 causal variant 가능성을 모델에 넣어 완화할 수 있는가?

## 3. 데이터와 방법

All of Us 499개 locus에서 unfiltered 분석과 MAF 1% filter, indel 제외 분석을 비교했다. Linked tested variant가 omitted variant의 신호를 대신 받는 경우를 조사하고 RBO 혈액형 locus를 사례로 분석했다. Missing causal component를 허용하는 SuSiE-OUT과 omitted-variant imputation을 비교했다.

## 4. 핵심 결과

- MAF 1% filter 뒤 high-confidence call의 20%가 unfiltered 분석에서 지지되지 않았다.
- Indel까지 제외하면 이 비율은 32%였고, omitted causal variant를 tagging하는 proxy에서 오류가 집중됐다.
- Omitted variant imputation과 SuSiE-OUT은 대부분의 오류를 막았지만 infinitesimal-effect modeling은 일관되게 막지 못했다.

## 5. 한계

단일 저자 preprint이며 499개 All of Us locus 중심 분석이다. 다른 ancestry·phenotype·LD reference와 summary-statistic-only setting에서 calibration과 computational cost를 추가 확인해야 한다.

## 6. 재현 또는 활용 포인트

MAF·INFO·variant-type filter 전후 credible set과 PIP를 비교하고, indel·rare variant가 reference panel에 존재하는지 기록한다. Unfiltered genotype 또는 high-quality imputation을 기준으로 proxy misassignment와 coverage를 평가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient rejection GWAS와 eQTL colocalization에서 rare variant나 indel을 먼저 제거하면 잘못된 regulatory gene을 선택할 수 있음을 경고한다. Fine-mapped variant를 biopsy cell state와 연결하기 전에 omitted-causal sensitivity analysis가 필요하다.

## 8. 관련 키워드

- statistical fine-mapping
- omitted causal variant
- SuSiE-OUT
- indel filtering

## 9. Bibliography

Weinstock, Josh. “Excluded causal variants produce false discoveries in genetic fine-mapping.” _medRxiv_, 2026. [https://doi.org/10.64898/2026.11.09.26367644](https://doi.org/10.64898/2026.11.09.26367644).
