# Code Log

이 문서는 연구 과정에서 실제로 사용한 코드, 명령어, notebook, script를 정리하기 위한 공간이다.

목표는 코드를 예쁘게 모아두는 것이 아니라, 나중에 같은 분석을 다시 해야 할 때 바로 재현할 수 있게 만드는 것이다. 개별 작업 로그는 `docs/code/logs/` 폴더에 하나씩 따로 저장한다.

## 정리 원칙

각 코드 기록은 다음 정보를 포함한다.

1. 무엇을 하려고 쓴 코드인가?
2. 어떤 데이터에 사용했는가?
3. 실행 환경은 무엇인가?
4. 핵심 코드 또는 명령어는 무엇인가?
5. 결과 파일은 어디에 저장되었는가?
6. 다시 사용할 때 주의할 점은 무엇인가?

## 로그 목록

| 날짜 | 작업 | 설명 |
| --- | --- | --- |
| 2026-05-18 | [LLM-wiki 배포](logs/2026-05-18-llm-wiki-deploy.md) | 로컬 Markdown 문서를 GitHub Pages에 반영하는 기본 명령어 |
| 2026-05-18 | [scGPT domain transfer](logs/2026-05-18-scgpt-domain-transfer.md) | Bulk microarray에서 학습한 classifier를 scRNA-seq 환자 임베딩에 적용하는 domain shift 실험 |
| 2026-05-20 | [scGPT rejection worklog](logs/2026-05-20-scgpt-rejection-worklog.md) | RMA 전처리, pseudo-count 변환, scGPT embedding transfer, p60 patient score, Transformer MIL, 환자 추론 실험 정리 |
| 2026-05-22 | [scGPT rejection end-to-end fine-tuning v1/v2](logs/2026-05-22-scgpt-rejection-end2end-v1-v2.md) | scGPT encoder + rejection head v1과 domain adapter/ fold-wise pos_weight를 추가한 v2 비교 |
| 2026-05-26 | [scGPT rejection end-to-end fine-tuning v3/v4](logs/2026-05-26-scgpt-rejection-end2end-v3-v4.md) | v3 nonzero gene tokenization/raw count normalization과 v4 adapter/L2-norm ablation 정리 |
| 2026-06-01 | [Prognosis microarray-to-SC adapter](logs/2026-06-01-prognosis-microarray-adapter.md) | 최종 frozen scGPT encoder + residual adapter + prognosis head 모델 정리 |

## 기록 템플릿

```text
# 날짜 - 코드 이름

## 목적

## 사용 데이터

## 실행 환경

## 코드 또는 명령어

## 결과

## 주의할 점
```

## 앞으로 정리할 코드 후보

- Single-cell 데이터 전처리 코드
- scGPT 또는 Geneformer 실행 코드
- Embedding 추출 코드
- UMAP 시각화 코드
- Domain shift 평가 코드
- Batch/cohort split 실험 코드
