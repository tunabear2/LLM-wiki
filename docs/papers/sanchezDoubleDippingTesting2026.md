---
type: paper
status: reference
rag_priority: high
updated: '2026-10-12'
tags:
- wiki/paper
---

# “Double-Dipping” in Testing for Phenotypic Differences with scRNA-seq

## 기본 정보

- Citation key: `sanchezDoubleDippingTesting2026`
- Item type: preprint
- Authors: Nicolas Sanchez; Louis Etourneau; Elizabeth Purdom
- Source: bioRxiv v1, posted 2026-10-06; indexed 2026-10-08 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.02.756269](https://doi.org/10.64898/2026.10.02.756269); [code](https://github.com/epurdom/scSampleSimScripts)
- 주 카테고리: `scRNA-seq`

## 1. 한 줄 요약

같은 expression data로 cell cluster를 정한 뒤 그 cluster 안에서 phenotype DE를 검사하면 강한 phenotype signal에서 FDR이 부풀 수 있으며, phenotype effect를 제거한 embedding으로 clustering하면 이를 완화할 수 있다.

## 2. 연구 질문

Cell type을 정하는 selection 단계와 phenotype 차이를 검정하는 단계를 같은 scRNA-seq data로 수행할 때 sample-level DE의 false discovery가 증가하는가?

## 3. 데이터와 방법

Phenotype effect, cluster resolution과 sample 구조를 바꾼 광범위한 simulation으로 clustering 후 DE의 FDR·power를 평가했다. Uncorrected embedding clustering과 phenotype/sample variation을 제거하는 batch-corrected embedding을 비교하고, 실제 데이터에서 위험을 진단할 phenotype-imbalance measure를 제안했다. 공개 scRNA-seq datasets로 simulation 설정을 보완했다.

## 4. 핵심 결과

- 강한 phenotype 차이가 clustering을 좌우하면 naive workflow에서 FDR이 심하게 증가했다.
- Batch correction 뒤 clustering은 시험한 조건에서 뚜렷한 power 손실 없이 FDR inflation을 해소했다.
- 제안한 phenotype imbalance 지표가 simulation의 false-discovery proportion과 함께 움직여 위험 진단에 쓸 수 있었다.

## 5. 한계

결론은 simulation design과 사용한 correction·clustering·DE 조합에 의존한다. Phenotype을 제거하는 correction은 관심 있는 연속 cell state까지 지울 수 있으므로 모든 분석에서 기계적으로 적용하면 안 된다. 실제 cohort의 ground-truth false discovery는 직접 알 수 없다.

## 6. 재현 또는 활용 포인트

Cluster별 donor/phenotype imbalance를 먼저 보고, cell-level 검정보다 donor-level pseudobulk를 기본 비교군으로 둔다. Clustering embedding에 phenotype signal을 남긴 경우 independent annotation 또는 sample-splitting sensitivity analysis를 추가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection 상태가 강한 expression shift를 만들면 rejection-specific cluster를 먼저 발견한 뒤 같은 세포에서 DEG를 검정하는 분석이 특히 취약하다. Donor 단위 replicate, 외부 kidney reference와 imbalance 진단을 함께 써야 한다.

## 8. 관련 키워드

- post-selection inference
- double-dipping
- differential expression
- false discovery rate

## 9. Bibliography

Sanchez, Nicolas, Louis Etourneau, and Elizabeth Purdom. “‘Double-Dipping’ in Testing for Phenotypic Differences with scRNA-seq.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.02.756269](https://doi.org/10.64898/2026.10.02.756269).
