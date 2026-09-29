---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# FedEdgeR: 개인정보를 공유하지 않는 연합 edgeR

## 기본 정보

- Citation key: `songFedEdgeRFederatedPrivacy2026`
- Item type: preprint
- Authors: Xun Song; Zhiwei Wei
- Source: bioRxiv (posted 2026-09-24; not peer reviewed)
- DOI: [10.64898/2026.09.17.752480](https://doi.org/10.64898/2026.09.17.752480)
- Original: [bioRxiv v1](https://www.biorxiv.org/content/10.64898/2026.09.17.752480v1)
- 주 카테고리: `Bulk RNA-seq`
- 교차 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

FedEdgeR는 secure multi-party computation으로 edgeR의 분산 추정과 GLM 검정을 연합 실행해, 원시 count를 기관 밖으로 보내지 않고 중앙 통합 분석과 사실상 같은 차등발현 결과를 냈다.

## 2. 연구 질문

환자 수준 RNA-seq count를 공유할 수 없는 다기관 환경에서 edgeR의 정규화·분산 추정·음이항 GLM 검정을 연합화하면서 pooled 분석의 통계적 결과를 보존하고 전통적 메타분석보다 일관된 결과를 낼 수 있는가?

## 3. 데이터와 방법

- secure multi-party computation으로 중간 충분통계량을 보호하면서 IRLS GLM, common/trended/tagwise dispersion, likelihood-ratio test를 연합 계산했다.
- TCGA-BRCA(n=227), GSE144269(n=139), melanoma anti-PD-1 반응 코호트(n=131), 소규모 paired oral 자료(n=6)를 3개 client에 균형·불균형 분할해 시험했다.
- 중앙 pooled edgeR 및 Fisher, Stouffer, random-effects, RankProd 메타분석과 비교했다.

## 4. 핵심 결과

- 중앙 edgeR와의 −log10 P-value Pearson 상관은 모든 평가에서 0.99999 이상이었고, 상위 100개 유전자 일치율 100%, FDR 0.05 기준 F1은 1이었다.
- 70/20/10 불균형 client 분할과 반응군 비율 차이에서도 pooled 결과와의 일치가 유지됐다.
- 실행시간은 자료에 따라 약 21초–8.6분이었고, IRLS round당 통신량은 2.5 MB 미만이었다.

## 5. 한계

- 실제 기관 분할은 melanoma 코호트 한 사례이고, 나머지는 공개 자료의 모의 분할이라 운영 환경의 네트워크·거버넌스를 검증하지 않았다.
- 형식적 differential privacy를 제공하지 않으며, 두 client 환경에서는 집계 통계로부터 정보가 노출될 가능성이 있다. 위협 모델도 honest-but-curious 가정에 제한된다.
- TMM 정규화 인자는 중앙에서 계산했으며 완전 연합 정규화는 해결되지 않았다.
- 동료평가 전 preprint이고 실제 임상 컨소시엄 배치 및 FeatureCloud 통합은 향후 과제다.

## 6. 재현 또는 활용 포인트

- [GitHub](https://github.com/XunSong02/FedEdgeR)에 코드, Conda 환경, 고정 seed와 end-to-end 실행 예제가 공개됐다.
- 버전 고정 산출물은 [Zenodo](https://doi.org/10.5281/zenodo.20450301)에서 제공된다.
- 자연 발생 기관 분할로 pooled 결과의 수치 동등성을 다시 확인하고, round 수·통신량·실패 복구와 함께 정규화 단계의 개인정보 흐름도 점검해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

원시 생검 RNA-seq를 한곳에 모으기 어려운 다기관 신장이식 코호트의 차등발현 분석에 직접 관련된다. 센터·시퀀싱 chemistry·임상 공변량을 설계행렬에 포함하고 안전한 연합 정규화를 마련해야 하며, SMPC가 법적·윤리적 자료공유 승인을 대체하지는 않는다.

## 8. 관련 키워드

- federated analysis
- differential expression
- edgeR
- secure multi-party computation
- bulk RNA-seq
- privacy-preserving genomics

## 9. Bibliography

Song X, Wei Z. FedEdgeR: federated and privacy-preserving edgeR for differential gene expression analysis. *bioRxiv*. Posted September 24, 2026. doi:[10.64898/2026.09.17.752480](https://doi.org/10.64898/2026.09.17.752480).
