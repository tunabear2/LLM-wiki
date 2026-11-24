---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# RapidGLM: genome-scale differential expression, CRISPR screen and eQTL analysis

## 기본 정보

- Citation key: `hungRapidGLMGenomeScale2026`
- Item type: preprint
- Authors: Ling-Hong Hung; Ka Yee Yeung
- Source: bioRxiv v1, posted 2026-11-19 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.18.767389](https://doi.org/10.64898/2026.11.18.767389)
- 주 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

RapidGLM은 count model에 특화한 Newton fitting과 batched resampling으로 DESeq2·edgeR·SCEPTRE·cis-eQTL 분석을 CPU에서 가속하는 C++ engine이다.

## 2. 연구 질문

Genome-scale differential expression, Perturb-seq와 cis-eQTL의 수백만 회귀·수십억 resampling을 reference method와 결과를 맞추면서 한 node에서 실용적으로 실행할 수 있는가?

## 3. 데이터와 방법

Negative-binomial·quasi-likelihood count regression의 정확한 Hessian, shared design computation과 vectorized kernel을 구현했다. DESeq2·edgeR, Gasperini·Replogle CRISPR screen의 SCEPTRE, Geuvadis cis-eQTL permutation을 reference output과 비교하고 동일 core에서 runtime을 측정했다. C, Python, R, command-line interface와 MIT license를 제공한다.

## 4. 핵심 결과

- 네 분석에서 reference tool의 변동 범위 안에 드는 결과를 보이며 동일 core에서 2.5–17.8배 빠르게 실행됐다.
- Gasperini screen 2,800만 test는 SCEPTRE 11.6시간 대비 44분이었고, 더 정확한 small-P 확인을 켜도 2.8시간이었다.
- PyDESeq2의 inference backend로 교체한 분석도 한 thread에서 2.8배 빨라졌다.

## 5. 한계

Copyleft reference code를 읽지 않은 clean-room 구현이라 공개 문서에 없는 edge-case 규칙은 다를 수 있다. cis-eQTL만 다루며 trans-eQTL·fine-mapping은 포함하지 않는다. GPU용 tensorQTL·jaxQTL을 CPU에서만 비교했고 timing은 제한된 hardware에서 측정됐다.

## 6. 재현 또는 활용 포인트

RapidGLM·reference tool version, dispersion·filter·random seed, thread 수와 small-P tail 검증 설정을 기록한다. 속도만 아니라 effect size, rank, P-value tail, FDR discovery overlap을 확인하고 기존 pipeline에는 drop-in backend부터 시험한다.

## 7. Transcriptomics·신장이식 연구와의 연결

여러 rejection phenotype·cell perturbation·donor/recipient genotype을 반복 비교할 때 계산 병목을 줄일 수 있다. 임상 결론을 바꾸기 전 기존 DESeq2·edgeR 결과와 patient-level design에서 수치 일치와 small-sample calibration을 먼저 확인해야 한다.

## 8. 관련 키워드

- differential expression
- negative-binomial GLM
- Perturb-seq
- cis-eQTL
- high-performance computing

## 9. Bibliography

Hung, Ling-Hong, and Ka Yee Yeung. “RapidGLM: Genome-Scale Differential Expression, CRISPR Screen and eQTL Analysis.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.18.767389](https://doi.org/10.64898/2026.11.18.767389).
