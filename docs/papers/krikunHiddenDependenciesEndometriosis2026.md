---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# Hidden Dependencies in Endometriosis Microarray Classifiers

## 기본 정보

- Citation key: `krikunHiddenDependenciesEndometriosis2026`
- Item type: preprint
- Authors: Elena Krikun; Abedalrhman Alkhateeb
- Source: medRxiv v1, posted 2026-11-17 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.15.26368137](https://doi.org/10.64898/2026.11.15.26368137)
- 주 카테고리: `Microarray`

## 1. 한 줄 요약

Endometriosis microarray classifier의 외부검증을 재구성해 GEO accession 간 동일 CEL 재사용, test outcome을 사용한 ComBat과 acquisition-date confounding이 성능을 크게 부풀렸음을 보인 audit다.

## 2. 연구 질문

서로 다른 GEO accession을 독립 cohort로 간주한 microarray classifier가 실제로는 sample duplication·outcome leakage·scan-date signal에 의존했는가?

## 3. 데이터와 방법

압축 해제한 CEL 파일의 SHA-256을 비교하고 matrisome elastic-net과 5-gene random forest를 재구성했다. ComBat에 전달한 test label을 바꾸는 intervention, 3,582개 constrained label refit, duplicate 제거, GSE51981 324-probe nested benchmark와 date-held-out 평가를 수행했다.

## 4. 핵심 결과

- Test CEL 37개 중 26개(70.3%)가 training array와 byte-identical했다.
- True test outcome을 ComBat에 넣은 deduplicated 분석의 median balanced accuracy는 0.881이었지만 outcome을 숨기면 0.549로 떨어졌다.
- Matching training copy를 제거하자 다른 classifier의 pooled AUC가 1.000에서 0.323으로 감소했고, date-only model은 healthy-control 비교에서 molecular model보다 높은 AUC를 보였다.

## 5. 한계

이 연구는 공개 자료와 기존 pipeline의 재구성이며 원 논문의 교정 성능을 제시하지 않는다. 일부 metadata와 전처리 선택을 완전히 복원하지 못할 수 있고 endometriosis 외 질환·platform으로 일반화하려면 추가 audit가 필요하다.

## 6. 재현 또는 활용 포인트

Accession이 아니라 raw-file hash, sample ID, patient, acquisition date로 중복을 검사한다. Batch correction은 train에만 fit하고 test outcome에 접근하지 않도록 pipeline으로 고정하며 date/center-only baseline과 nested external validation을 반드시 비교한다.

## 7. Transcriptomics·신장이식 연구와의 연결

여러 GEO 신장이식 microarray cohort를 합칠 때 같은 biopsy가 다른 accession·논문에 재사용될 위험이 있다. CEL hash와 patient/date provenance를 먼저 만들고 ComBat에 rejection label이 새지 않도록 fold 안에서만 보정해야 한다.

## 8. 관련 키워드

- microarray
- sample duplication
- data leakage
- ComBat
- external validation

## 9. Bibliography

Krikun, Elena, and Abedalrhman Alkhateeb. “Hidden Dependencies in Endometriosis Microarray Classifiers: Sample Reuse, Outcome-Informed Batch Correction, and Diagnostic Reassessment.” _medRxiv_, 2026. [https://doi.org/10.64898/2026.11.15.26368137](https://doi.org/10.64898/2026.11.15.26368137).
