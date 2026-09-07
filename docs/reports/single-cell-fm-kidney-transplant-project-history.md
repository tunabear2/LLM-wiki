---
type: report
status: active
rag_priority: high
updated: '2026-09-07'
tags:
- wiki/report
- research/kidney-transplant
- research/single-cell-foundation-model
- research/survival-analysis
---

# Single-cell Foundation Models for Kidney Transplant Prognosis

작성일: 2026-09-07  
기록 범위: 2026-04 ~ 2026-09-05

신장이식 생검 또는 혈액 발현 데이터에서 single-cell foundation model(scFM)이 거부반응과 이식편 생존 예측에 실제로 도움이 되는지 검증한 프로젝트의 최신 종합 기록이다. 초기 scGPT 이진 분류와 bulk microarray → scRNA-seq 전이 실험에서 출발해, 6개 foundation model의 time-to-event 생존 벤치마크와 유전자 임베딩 사전까지 확장했다.

!!! abstract "현재 결론"
    사전학습 가중치 자체는 분명한 정보를 제공하지만, 작은 사건 수의 신장이식 생존 과제에서는 일반적인 cell embedding과 추가 fine-tuning이 강한 비-FM 기준선을 안정적으로 넘지 못했다. 현재 가장 유망한 경로는 foundation model을 샘플 인코더가 아니라 **유전자 축의 사전**으로 사용하는 Geneformer GEP이며, 다음 검증의 핵심은 GSE21374 전체 환자 코호트로 사건 수를 늘리는 것이다.

## 연구 질문

이 프로젝트는 네 가지 질문을 순서대로 다뤘다.

1. Bulk microarray에서 학습한 거부반응 신호가 single-cell 환자 데이터로 전이되는가?
2. 반대 방향인 scRNA-seq → microarray zero-shot 전이는 가능한가?
3. scGPT에서 얻은 전이 원칙이 다른 scFM에도 재현되는가?
4. 6개 scFM이 환자 단위 time-to-event 평가에서 ElasticNet-Cox 같은 기준선을 넘는가?

## 한눈에 보는 연구 흐름

| 시기 | 연구 축 | 대표 결과 |
| --- | --- | --- |
| 2026-04 | scFoundation·CellFM 튜토리얼 및 CellFM PyTorch 이식 | CellFM annotation 98.01%; MindSpore GPU 제약 확인 |
| 2026-04~05 | scGPT 분류와 bulk → scRNA 전이 | 세포별 확률 p60 집계로 16명 환자 AUROC 1.000 |
| 2026-05~06 | 양방향 전이와 adapter 탐색 | sc → array zero-shot 상한 약 0.748; full fine-tuning은 OOD 붕괴 |
| 2026-06~07 | 데이터 확장과 전이 요인 분해 | 동질 kidney 코호트가 19개 데이터셋 병합보다 강함 |
| 2026-07 | 6개 scFM 독립 구현과 생존 엔진 | 모델별 전처리 규약·조용한 실패를 selftest로 고정 |
| 2026-07~08 | 3-stage 생존 파이프라인과 값 전처리 연구 | 값 변환보다 0 집합·시퀀스 예산·도메인 정합이 중요 |
| 2026-08 | 표준 평가층과 기준선 사다리 | FM 6종 중 ElasticNet-Cox에 유의하게 우세한 모델 0개 |
| 2026-08~09 | random-init, 블록 확장, Cox 헤드, GEP | 사전학습 +0.13~0.19; Geneformer GEP Harrell C 0.8471 |

## 핵심 데이터 계약

| 데이터 | 규모 | 프로젝트 내 역할 |
| --- | --- | --- |
| GSE21374, GPL570 | 전체 282 생검·221 환자; 주 분석 105 환자·사건 30 | 유일한 주 time-to-event 라벨, T1 생존 평가 |
| GSE36059 + GSE147089 | 403 + 224 = 627, NR 449 / Rejection 178 | 초기 scGPT bulk 학습셋 |
| E-MTAB-12051 | 16 환자·53,630 cells, QC 후 37,920 cells | 정직한 bulk → scRNA 외부 전이 평가 |
| Kidney scRNA 외부 4종 | 9 환자 규모 | 추가 predict-cell 평가와 sc → sc 실험 |
| Kidney microarray 24종 | 4,578 샘플, 이진 라벨 2,179 | 다중 코호트 확장·LOGO·도메인 분석 |
| PBMC/혈액 17종 | Affymetrix 중심 738 샘플 | 혈액 backbone 및 cross-domain 대조 |
| GEO 재수집 kidney 자료 | biopsy 4,368 / blood 1,975 | PROMAD 2차 가공본을 대체한 적응 코퍼스 후보 |
| KPMP·GTEx kidney | KPMP 225,177 cells / GTEx 89 samples | 음성대조, pseudobulk, depth 기준 |

!!! note "GSE21374 사건 수 표기"
    프로젝트 기록에는 전체 자료의 사건 수가 51과 42로 함께 등장한다. 51은 생검 행 수준, 42는 환자 중복을 정리한 환자 수준 사건 수로 해석된다. 생존평가에서는 반드시 환자 단위 계약과 중복 생검 처리 규칙을 함께 기록해야 한다.

## 여섯 모델의 독립 구현

모델별 정규화·토큰화·의존성이 달라 공통 wrapper를 두지 않고, 각 모델을 하나의 독립 스크립트로 구성했다. 공통 산출물 형식만 맞추고 내부 규약은 원 구현에 맞춘다.

| 모델 | 핵심 입력 규약 | 기본 cell 표현 | 주요 함정 |
| --- | --- | --- | --- |
| scGPT | normalize-total·log1p 후 비영값 분위수 binning, 무작위 절단 | 마지막 layer의 CLS + 행별 L2, 512-d | flash-attn Wqkv remap 실패 시 attention 12층 랜덤 초기화 |
| Geneformer V2 | Ensembl 변환 후 CP10K/gene-median 기반 rank encoding | 저자 권장 CLS, 768-d | log 입력 미복원 또는 raw counts에 expm1 적용 시 왜곡·overflow |
| scBERT | 고정 16,906-gene panel, log2·clip·정수 절삭 | 비영 위치 평균, 200-d | 위치가 유전자 정체성; microarray 이중 log2 시 표현 압축 |
| scFoundation | 고정 19,264-gene panel + T/S depth token | all pooling 3,072-d 또는 max 768-d | panel 정렬 누락과 padding 미마스킹에 따른 batch-size 의존 |
| scLong | Ensembl 27,874-gene panel, dual Performer 1B | 비영 유전자 평균, 200-d | 공식 cell pooling 부재, 87GB peak와 장시간 학습, LICENSE 미확인 |
| CellFM | 24,078-gene panel, depth cap·정규화·가중 비복원 추출 | cls_token, 1,536-d | MindSpore GPU 불가, panel 정렬·rounding·0-total NaN 함정 |

각 스크립트는 `preprocess`, `embed`, `adapt`, `inspect`, `drift`, `prognosis`, `predict`, `selftest` 흐름을 갖는다. CellFM에는 MindSpore checkpoint를 PyTorch로 옮기는 `convert`도 있다. 적응은 원 self-supervised objective를 유지하며, 생존 헤드는 환자 그룹 CV와 Cox 부분우도, Breslow 기준위험, Uno·Harrell concordance를 사용한다.

## 1. Bulk microarray → single-cell 전이

초기 연구에서 가장 강한 결과가 나온 방향이다.

```text
bulk microarray
  -> frozen kidney-pretrained scGPT
  -> cell/sample representation
  -> small supervised head
  -> single-cell별 rejection probability
  -> 환자별 p60 또는 mean 집계
```

E-MTAB-12051 16명에서 세포별 확률의 60th percentile을 환자 점수로 사용했을 때 AUROC 1.000, balanced accuracy 1.000을 얻었다. 200회 cell bootstrap에서는 AUROC 0.9451 ± 0.041이었다. 이후 QC 데이터와 `adapter_8000` 재현에서는 E-MTAB AUROC 0.833~0.875, GSE195719 AUROC 1.000을 기록했다.

그러나 이 결과를 일반적인 scFM 우위로 읽으면 안 된다.

- Kidney backbone은 E-MTAB AUROC 0.875였지만 human backbone은 0.500이었다.
- Human backbone의 bulk OOF는 오히려 더 높았다. In-domain 성능만으로 backbone을 고르면 전이를 잘못 판단한다.
- Full 또는 last-layer fine-tuning은 CV를 높이면서 target scRNA에서 specificity 0으로 붕괴했다.
- Attention pooling도 array OOF는 높였지만 cross-domain 성능은 낮췄다.

즉 이 방향의 실무 원칙은 **도메인에 맞는 frozen backbone + 단순 readout + 환자 단위 집계**다.

## 2. scRNA-seq → microarray 전이

반대 방향은 구조적으로 더 어려웠다. 912개 조합과 후속 실험을 거쳐 다음을 확인했다.

| 접근 | 대표 AUROC | 해석 |
| --- | ---: | --- |
| scGPT Transformer CLS | 0.40~0.47 | cross-platform rejection 신호 손실 |
| Raw gene-space model | 약 0.65 | CLS보다 안정적 |
| Gene-embedding table projection | 약 0.71 | Transformer 없이 유전자 사전만 사용 |
| Transductive consensus/co-training | 최대 0.748 | label-free 전이의 관측 상한 |
| 수작업 또는 scGPT-weighted signature | 약 0.81~0.82 | 생물학적 prior를 허용한 경우 |
| Array-supervised embedding model | 약 0.840 | target label을 허용하면 가능 |

Sc와 array에서 학습한 최적 판별축의 cosine은 0.076으로 거의 직교했다. Array 내부에는 신호가 있지만 sc source의 판별축이 그대로 전달되지 않았다. 따라서 순수 sc → array zero-shot으로 AUROC 0.80 이상을 목표로 하는 경로는 닫고, target 감독 또는 명시적 생물학 사전을 요구하는 문제로 재정의했다.

## 3. 데이터 양보다 도메인 정합

Kidney microarray 19개 데이터셋을 2,179 샘플로 확장하면 in-domain 성능은 올라갔지만 E-MTAB 전이는 0.50으로 떨어졌다. 반면 GSE36059+GSE147089의 비교적 동질적인 627 샘플 학습셋은 E-MTAB에서 0.77~0.88을 유지했다.

이 결과에서 세 가지 조건이 분리됐다.

- 균형 잡힌 source label
- 조직과 플랫폼이 비교적 동질적인 코호트
- 충분한 시퀀스 예산

`max_seq_len=8000`은 약 16,333개 비영 유전자 중 49%를 보게 해 깨끗한 source에서 전이를 개선했다. 그러나 이질적인 다중 코호트에서는 시퀀스를 늘려도 domain overfit을 해결하지 못했다.

## 4. Fine-tuning과 적응의 한계

서로 다른 세 종류의 적응을 독립적으로 시험했다.

1. Backbone full fine-tuning 또는 last-N layer 학습
2. 백본을 동결한 per-block side-adapter
3. 마지막 backbone block을 복제하는 gated block expansion

In-domain에서는 full fine-tuning이 좋아지는 경우가 있었지만, cross-domain에서는 frozen이 더 강했다. Side-adapter와 block expansion도 6개 모델에서 유의한 일관 개선을 만들지 못했다. Self-supervised validation loss가 크게 내려가도 downstream 생존 성능은 좋아지지 않았다.

Random-init 대조가 중요한 해석을 제공했다. scGPT PANP-CPM arm에서 pretrained frozen은 약 0.739, random-init은 0.557~0.605로 나타나 사전학습 가중치의 기여가 +0.13~+0.19였다. 즉 “사전학습이 무의미하다”가 아니라, **이미 존재하는 사전학습 정보를 작은 생존 코호트에서 추가 적응으로 안정적으로 개선하지 못했다**는 결론이다.

## 5. 표준 생존 벤치마크

평가 단위를 환자로 고정하고, 같은 fold와 환자 단위 bootstrap을 모든 arm에 적용했다. 주 지표는 Uno's C이며 Harrell's C, time-dependent AUC, Brier/IBS, calibration, 관측 Kaplan–Meier를 함께 기록했다.

### 최신 T1 순위

| 모델 또는 기준선 | Uno's C | 해석 |
| --- | ---: | --- |
| ElasticNet-Cox | **0.799** | 비교 기준 |
| Survival MLP | 0.795 | ElasticNet과 실질적으로 동률 |
| Geneformer adapted | 0.791 | FM 중 최고권이지만 기준선 우위 아님 |
| PCA16-Cox | 0.785 | 저차원 선형 기준선 |
| scGPT adapted | 0.779 | 기준선 미달 |
| Random survival forest | 0.778 | 비선형 기준선 |
| scFoundation | 0.751 | 기준선 미달 |
| scBERT | 0.746 | 기준선 미달 |
| scLong | 0.701 | 기준선 미달 |
| CellFM | 0.671 | 기준선 미달 |
| Clinical Cox | 0.507 | 임상 변수만으로는 제한적 |
| Kaplan–Meier only | 0.500 | 비개인화 기준선 |

!!! warning "판정"
    어떤 FM arm도 ElasticNet-Cox보다 우세하다고 주장할 수 없었다. FM 6종의 calibration slope도 0.08~0.25로 붕괴해 해당 형태의 개별 생존확률은 보고에 부적합했다. 판별 순위와 관측 KM은 사용할 수 있지만, 포화된 절대 확률을 임상적 위험도로 해석해서는 안 된다.

주 분석의 사건이 30건뿐이라 표현과 head를 늘릴수록 분산이 커졌다. 서로 다른 adapter와 Cox head 설계가 같은 지점에서 포화된 것은 병목이 backbone이나 head보다 **사건 수**에 있다는 근거다.

## 6. Gene-embedding prior: 가장 유망한 경로

Cell embedding 대신 foundation model의 유전자 임베딩 행렬을 사용했다.

```text
sample × gene expression X
  -> foundation-model gene embedding E
  -> X @ E
  -> fold 내부 PCA(k)
  -> Cox model
```

Geneformer GEP는 Harrell's C 0.8471을 기록했고 5개 seed 모두 ElasticNet-Cox보다 높았다. 유전자 임베딩을 고정한 permutation 대조에서는 실제 임베딩이 40개 추첨을 모두 넘었다. Bootstrap 차이는 아직 0을 포함했지만, 지금까지 가장 유망하고 가장 좁은 불확실성 구간을 보였다.

모델별 GEP Harrell's C는 다음과 같았다.

| Gene embedding source | Harrell's C |
| --- | ---: |
| Geneformer | **0.8468~0.8471** |
| scFoundation | 0.8087 |
| scGPT | 0.7922 |
| scBERT | 0.7837 |
| scLong | 0.7799 |
| CellFM | 0.7753 |

이 이득은 `β = Ew`처럼 Cox 계수 공간을 직접 제한할 때는 재현되지 않았고, `X@E` 이후 PCA로 저차원 절단할 때 나타났다. 따라서 다음 가설은 **유전자 사전으로 유도한 부분공간 + 저차원 규제**다.

중요한 한계도 있다. Geneformer GEP는 dense log2 RMA에서 0.8468이었지만 zeroed log2에서는 0.6018, PANP CPM에서는 0.5760으로 무너졌다. GEP에는 0 없는 log2 RMA 입력을 고정하고, 일반 cell embedding 경로의 zeroing 처방과 분리해야 한다.

## 7. 전처리에서 실제로 중요했던 것

### Zero set

0을 어디에 찍는지는 토큰화 규약에 따라 큰 영향을 줬다.

- Geneformer의 rank encoding은 dense RMA에서 sample 간 순위가 비슷해져 붕괴했고, zeroing으로 일부 회복했다.
- scGPT는 값의 단조 변환에 거의 불변이었고, 0 집합과 어떤 유전자가 시퀀스에 들어오는지가 중요했다.
- PANP는 고정 `log2 < 5`보다 코호트 간 zero 비율 격차를 0.081에서 0.024로 줄였다.
- GEP는 반대로 zeroing에 매우 취약했다.

### Non-zero values

비영 값의 변환은 예상보다 작은 축이었다. Geneformer 파일럿에서 전처리 arm에 따른 array↔single-cell 적응 손실 차이는 0.02%에 불과했다. scGPT는 순위 보존 값 변환에 비트 단위로 불변이었다.

### Sequence budget

Bulk sample은 비영 유전자가 16,000개 이상이지만 single-cell은 수백 개 수준이다. 제한된 시퀀스 길이에서 scGPT·CellFM·Geneformer는 bulk 유전자의 대부분을 버린다. 특히 scGPT와 CellFM의 무작위 절단은 bulk에서 seed에 따른 표현 변동의 가장 큰 원인이었다. 값 변환보다 절단 seed ensemble이 더 실질적인 개선을 보였다.

### Gene-wise quantile mapping

Gqmap은 array → RNA-seq처럼 기술이 다른 축을 맞출 때만 고려할 수 있다. 같은 array 기술의 코호트 사이에서는 유전자별 생물학적 차이까지 지워 외부 AUROC를 0.748에서 0.463으로 낮췄다. Array 내부 예후나 같은 기술의 외부 검증에는 사용하지 않는다.

## 8. 검증과 엔지니어링 원칙

이 프로젝트에서 모델 성능만큼 중요한 산출물은 조용한 실패를 막는 검증 규약이었다.

- 환자 단위 분할과 bootstrap을 사용하고 cell 또는 반복 생검 누수를 막는다.
- 공식 구현과 이식본을 수치 또는 비트 단위로 대조한다.
- Checkpoint·vocab·adapter·readout·전처리 규약을 지문으로 묶는다.
- `strict=False`, NaN 입력, 누락된 attention key, scale mismatch는 경고가 아니라 중단한다.
- Selftest의 skip과 pass를 분리한다.
- Label shuffle, 무관 데이터, 유전자 치환, random-init 같은 음성대조를 함께 둔다.
- Adaptation loss 감소를 downstream 성능 향상으로 해석하지 않는다.
- Kaplan–Meier는 모델 예측이 아니라 관측 `event_time`과 `event`로 그린다.
- 생존 시간의 원점은 이식일이 아니라 **생검일**이다.

실제로 발견된 실패에는 scGPT attention 12층 랜덤 초기화, Geneformer raw counts의 expm1 overflow, scBERT 이중 log2, scFoundation batch-size 의존, CellFM rounding에 의한 유전자 소실, scLong 실행 인자 중복, 낡은 survival head 재사용 등이 포함된다. 하류 AUROC나 kNN 하나만으로는 이런 실패를 안정적으로 발견할 수 없었다.

## 해석의 경계

현재 근거로 말할 수 있는 것:

- Kidney-specific pretrained representation은 bulk → scRNA 전이에 유용했다.
- 사전학습 가중치는 random-init 대비 분명한 이득이 있다.
- 일반적인 fine-tuning과 adapter는 작은 survival cohort에서 안정적인 추가 이득을 만들지 못했다.
- 강한 비-FM 기준선과 환자 단위 평가가 필수다.
- Geneformer gene embedding prior는 후속 검증 가치가 있다.

아직 말할 수 없는 것:

- 특정 scFM이 임상적으로 배포 가능한 생존확률을 제공한다.
- FM이 ElasticNet-Cox보다 일반적으로 우월하다.
- GEP의 0.8471이 독립 코호트에서도 유지된다.
- E-MTAB 16명에서의 높은 rejection AUROC가 넓은 환자군에 그대로 일반화된다.

## 다음 단계

1. GSE21374 전체 282 생검·221 환자를 환자 단위 계약으로 정리해 T1b를 재평가한다.
2. `β = E V_k u + δ` 형태로 GEP 저차원 부분공간과 residual gene effect를 분리한다.
3. GEP는 zero 없는 log2 RMA를 고정하고, 무작위 절단 모델은 seed ensemble을 정식화한다.
4. Adapt 코퍼스에서 GSE21374 재등재 배열과 외부 평가 코호트 중복을 배열 단위로 제거한다.
5. ElasticNet의 fold별 `alpha_max` 불일치를 고치고 유전자-level penalty grid를 확장한다.
6. 독립 time-to-event 자료인 GSE112927 전혈 RNA-seq를 별도 T3 과제로 평가한다.

## 관련 문서

- [Kidney Transplant Rejection Classification](kidney-transplant-rejection-classification-summary.md)
- [scGPT Worklog Summary — 2026-06 snapshot](scgpt-worklog-summary.md)
- [Microarray-to-scRNA Prognosis Adapter — 2026-06 snapshot](microarray-to-scrna-prognosis-adapter.md)
- [Transplant Prognosis Model Notes — early design](transplant-prognosis-model-notes.md)
- [Single-cell Foundation Models](../papers/single-cell-foundation-models.md)
- [Geneformer](../bio-ai/geneformer.md)
- [scGPT](../bio-ai/scgpt.md)
