---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# Genome-Wide LD Scores for Heritability and Genetic Correlation across Ancestries

## 기본 정보

- Citation key: `jeongSUMMITGenomeWideLD2026`
- Item type: bioRxiv preprint
- Authors: M. Jeong; Z. Liu; J. Ni; U. An; S. Han; A. Anand; P. Anand; M. Boffelli; S. Sankararaman
- Source: bioRxiv v1, posted 2026-10-22 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.20.760508](https://doi.org/10.64898/2026.10.20.760508); [code](https://github.com/sriramlab/SUMMIT)
- 주 카테고리: `GWAS`

## 1. 한 줄 요약

SUMMIT은 random projection으로 genome-wide LD score를 계산해 long-range LD가 강한 structured·admixed population에서도 GWAS summary-statistic heritability와 genetic correlation의 bias를 줄인다.

## 2. 연구 질문

Local-window LD approximation이 취약한 non-European·admixed cohort에서 genome-wide LD를 효율적으로 반영해 summary-statistic inference를 개선할 수 있는가?

## 3. 데이터와 방법

Genome-wide·annotation-specific LD score를 random projection으로 추정하고 moment estimator와 결합했다. UK Biobank의 European, South Asian, admixed African-European genotype을 바탕으로 한 simulation과 40개 trait에서 기존 방법과 heritability·cross-ancestry genetic correlation을 비교했다.

## 4. 핵심 결과

- Simulation에서 prior method보다 accuracy가 높고 bias가 낮았으며 non-European ancestry에서 gain이 가장 컸다.
- 40개 trait의 common-SNP heritability는 ancestry 간 대체로 일치했고 WGS 기반 최근 추정치에 더 가까웠다.
- Cross-ancestry genetic correlation은 FDR<0.05에서 South Asian 23개, admixed African-European 3개를 찾았고 cov-LDSC는 각각 0개와 2개였다.

## 5. 한계

UK Biobank의 세 ancestry setting과 common SNP 중심 검증이라 더 다양한 ancestry, rare variant와 small transplant cohort에 대한 calibration은 미확인이다. Summary statistic과 reference genotype의 ancestry·QC mismatch가 남을 수 있고 preprint 단계다.

## 6. 재현 또는 활용 포인트

MIT-licensed code, example와 manuscript reproduction script가 공개된다. Reference genotype, LD-score mode, annotation, sample overlap과 summary-statistic QC를 기록하고 LDSC/cov-LDSC와 simulation으로 bias를 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

다양한 ancestry의 donor·recipient GWAS에서 rejection·graft outcome의 heritability와 kidney/immune annotation enrichment를 비교하는 후보다. Sample size가 작은 이식 cohort에서는 meta-analysis와 uncertainty가 우선이다.

## 8. 관련 키워드

- GWAS
- LD score
- multi-ancestry
- genetic correlation

## 9. Bibliography

Jeong, M., et al. “Genome-Wide LD Scores Enable Robust Heritability and Genetic Correlation Estimation from Summary Statistics across Genetic Ancestries.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.20.760508](https://doi.org/10.64898/2026.10.20.760508).
