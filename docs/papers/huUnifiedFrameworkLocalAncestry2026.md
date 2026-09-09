---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# A unified framework for local-ancestry-aware genetic association analysis across biobanks

## 기본 정보

- Citation key: huUnifiedFrameworkLocalAncestry2026
- Item type: medRxiv preprint
- Authors: Linfeng Hu; Taotao Tan; Kai Yuan; Ying Wang; Bram L. Gorissen; Yi-Sian Lin; Pragati Kore; Wenhan Lu; Ravi Mandla; Zhuozheng Shi; Kangcheng Hou; Konrad J. Karczewski; Hailiang Huang; Benjamin M. Neale; Mark J. Daly; Alicia R. Martin; Bogdan Pasaniuc; Elizabeth G. Atkinson; Wei Zhou
- DOI: 10.64898/2026.08.09.26360047
- URL: [medRxiv](https://www.medrxiv.org/content/10.64898/2026.08.09.26360047v1)
- Source/date: medRxiv v1, 2026-08-11
- 주 카테고리: GWAS

## 1. 한 줄 요약

FELIX는 local ancestry를 압축 저장하고 shared·ancestry-specific association model을 적응 결합해 admixed participant를 대규모 GWAS와 PRS에 포함하는 framework다.

## 2. 연구 질문

Global-ancestry cluster로 표본을 나누며 admixed individual을 제외하는 기존 GWAS 대신, local ancestry를 직접 모델링해 검정력과 cross-population prediction을 높일 수 있는가?

## 3. 데이터와 방법

Compact local-ancestry genotype 표현 FELIXla와 shared-effect·ancestry-specific GLMM을 Cauchy test로 결합하는 FELIXassoc를 제안했다. Simulation, All of Us 240,038명·24 phenotype·약 104만 HapMap3 marker와 UK Biobank 4개 ancestry validation을 사용했다.

## 4. 핵심 결과

All of Us에서 기존 global-ancestry clustering이 제외하던 participant 12.1%를 보존하고 genome-wide significant locus를 15.4% 더 발견했다고 보고했다. UK Biobank validation에서도 여러 phenotype의 polygenic-score prediction이 개선됐다.

## 5. 한계

Peer review 전이며 local-ancestry inference 오류가 association에 전달될 수 있다. 평가는 HapMap3 common variant와 AoU·UKB 중심이어서 rare variant, HLA처럼 복잡한 영역, 다른 admixture history에 대한 일반화가 남아 있다.

## 6. 재현 또는 활용 포인트

- 도구: [ZhouLabGenetics/FELIX](https://github.com/ZhouLabGenetics/FELIX)
- 재현 분석: [ZhouLabGenetics/FELIX_manuscript_code](https://github.com/ZhouLabGenetics/FELIX_manuscript_code)
- Global ancestry PC 보정, ancestry-stratified meta-analysis, FELIX를 같은 sample에서 비교한다.
- Local-ancestry inference tool·reference panel과 marker QC를 명시하고 추정 불확실성에 대한 sensitivity analysis를 둔다.
- Discovery 증가뿐 아니라 ancestry별 effect consistency와 외부 PRS calibration을 확인한다.

## 7. Transcriptomics·신장이식 연구와의 연결

다양한 ancestry의 donor·recipient rejection 또는 graft-outcome GWAS에서 표본 제외와 ancestry-dependent effect 손실을 줄이는 설계로 확장할 수 있다. 이후 eQTL·cell-type transcriptomics colocalization으로 locus 기능을 해석할 수 있다.

## 8. 관련 키워드

- GWAS
- Local ancestry
- Admixed populations
- Multi-ancestry
- GLMM
- Polygenic score

## 9. Bibliography

Hu, Linfeng, et al. “A Unified Framework for Local-ancestry-aware Genetic Association Analysis across Biobanks.” medRxiv, 2026. [https://doi.org/10.64898/2026.08.09.26360047](https://doi.org/10.64898/2026.08.09.26360047).
