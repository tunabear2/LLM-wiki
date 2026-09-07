---
type: research-question
status: active
rag_priority: high
updated: '2026-09-07'
tags:
- wiki/research-question
---

# Research Questions

이 문서는 single-cell foundation model을 신장이식 발현 데이터에 적용하면서 남은 핵심 질문과 현재까지의 답을 연결한다. 상세한 실험 근거와 수치는 [최신 프로젝트 종합 보고서](reports/single-cell-fm-kidney-transplant-project-history.md)에 정리했다.

## Q1. Domain shift는 전처리나 fine-tuning으로 해결할 수 있는가?

### 핵심 질문

Single-cell foundation model을 microarray, bulk RNA-seq, scRNA-seq에 함께 적용할 때 조직·플랫폼·코호트 차이를 어떻게 통제할 수 있는가?

### 현재까지의 답

- Bulk microarray → scRNA-seq에서는 kidney-pretrained frozen backbone과 단순한 patient aggregation이 가장 안정적이었다.
- Full fine-tuning, last-layer fine-tuning, side-adapter, block expansion은 in-domain 성능을 높일 수 있지만 cross-domain 일반화를 일관되게 개선하지 못했다.
- 19개 데이터셋의 2,179 샘플 병합보다 비교적 동질적인 kidney 627 샘플이 더 잘 전이됐다.
- 값의 단조 변환보다 0 집합, gene panel, 시퀀스 예산, 절단 seed가 더 중요한 경우가 많았다.
- Gqmap은 array → RNA-seq처럼 기술이 다른 경우에만 후보이며, 같은 기술 코호트 사이에서는 생물학적 차이까지 제거했다.

따라서 “도메인을 지운다”는 하나의 처방보다 source·target의 기술과 조직을 먼저 구분하고, frozen baseline을 기준으로 각 개입을 외부 코호트에서 판정해야 한다.

### 다음 검증

1. Adapt 코퍼스와 외부 평가 코호트의 배열 단위 중복을 제거한다.
2. 동일한 fold에서 frozen과 adapted representation을 paired 비교한다.
3. 기술이 다른 전이와 같은 기술의 cohort transfer를 별도 과제로 유지한다.

## Q2. Foundation model은 강한 비-FM 기준선을 넘는가?

### 현재까지의 답

환자 단위 표준 평가에서 ElasticNet-Cox의 Uno's C는 0.799였다. Survival MLP는 0.795였고, 6개 FM의 frozen 또는 adapted arm 중 ElasticNet보다 우세하다고 주장할 수 있는 모델은 없었다. 이는 “FM이 쓸모없다”는 결론이 아니라, 사건 30건 규모에서 일반 cell embedding이 추가 복잡도를 정당화하지 못했다는 뜻이다.

### 다음 검증

1. GSE21374 전체 282 생검·221 환자를 환자 단위로 정리해 T1b를 평가한다.
2. 모든 arm에 같은 환자 fold와 bootstrap index를 사용한다.
3. Uno's C를 주 지표로 두고 Harrell's C, IBS, 관측 KM을 함께 보고한다.
4. 포화된 calibration slope와 절대 생존확률은 임상적 결과처럼 보고하지 않는다.

## Q3. 사건 수가 현재 성능의 천장인가?

### 현재 가설

서로 다른 표현 적응과 Cox head 재설계가 비슷한 위치에서 포화됐고, 고차원 adapter는 위험점수 스케일과 calibration만 악화했다. 현재 가장 간결한 설명은 backbone이나 head보다 작은 사건 수가 병목이라는 것이다.

### 판정 실험

GSE21374 주 분석 105명·사건 30에서 전체 환자 코호트로 확장했을 때 다음을 본다.

- FM과 ElasticNet의 paired Δ 신뢰구간이 좁아지는가?
- Geneformer GEP 이득이 유지되는가?
- Calibration slope와 위험점수 스케일이 회복되는가?
- 반복 생검을 어떤 환자 단위 규칙으로 대표할 때 결과가 안정적인가?

## Q4. Cell embedding보다 gene embedding prior가 더 적합한가?

### 현재까지의 답

Foundation model을 샘플 인코더로 사용할 때보다 유전자 임베딩을 `X @ E → PCA(k) → Cox`로 사용하는 Geneformer GEP가 더 강했다. Harrell's C 0.8471로 현재 최고 결과지만, zeroing 행렬에서는 0.60 안팎으로 무너졌다. 이득은 `β = Ew`라는 직접 계수 제약보다 임베딩이 유도한 저차원 부분공간에서 나타났다.

### 다음 검증

1. Zero 없는 log2 RMA를 GEP 입력 계약으로 고정한다.
2. `β = E V_k u + δ`로 저차원 prior와 residual gene effect를 분리한다.
3. 실제 embedding, 유전자 순열 embedding, random embedding을 같은 fold에서 비교한다.
4. GSE21374 전체 코호트와 독립 time-to-event 데이터 GSE112927에서 재검증한다.

## 공통 판정 원칙

- 환자 단위 split·bootstrap을 사용한다.
- In-domain CV와 cross-domain transfer를 분리해 보고한다.
- Pretrained, random-init, label shuffle, 유전자 치환 대조를 함께 둔다.
- 체크포인트·전처리·readout·adapter 조합을 지문으로 고정한다.
- 하류 지표 하나로 embedding collapse나 조용한 로딩 실패를 판단하지 않는다.

## 관련 문서

- [Single-cell FM Kidney Transplant Project](reports/single-cell-fm-kidney-transplant-project-history.md)
- [Kidney Transplant Rejection Classification](reports/kidney-transplant-rejection-classification-summary.md)
- [Single-cell Foundation Models](papers/single-cell-foundation-models.md)
- [scGPT](bio-ai/scgpt.md)
- [Geneformer](bio-ai/geneformer.md)
