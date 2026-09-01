---
type: rag-evaluation
status: active
rag_priority: low
updated: 2026-07-20
tags:
- wiki/rag-evaluation
- rag/exclude
- wiki/rag-config
---

# LLM Bio Wiki RAG 평가 세트

> [!warning] 색인 제외 문서
> 기대 답과 출처가 검색되는 누수를 막기 위해 이 문서는 `rag/exclude`한다.

## 실행 방법

1. Copilot에서 `Vault QA` 모드를 선택한다.
2. 새 대화에서 시스템 프롬프트 `LLM Bio Wiki Research Assistant`를 선택한다.
3. 아래 질문을 한 개씩 그대로 입력한다.
4. 답변의 사실, 출처 링크, 불확실성 표현을 채점표에 기록한다.
5. 임베딩 모델이나 색인 규칙을 바꾼 경우 전체 세트를 다시 실행한다.

## 질문과 기대 근거

| ID | 질문 | 반드시 검색되어야 할 근거 | 핵심 확인 사항 |
| --- | --- | --- | --- |
| Q1 | 현재 kidney transplant rejection 예측에서 가장 권장되는 모델 구조와 환자 단위 집계 방법은? | `reports/scgpt-prognosis-progress-2026-06-16.md` | kidney backbone, residual adapter, p60 집계 |
| Q2 | pretrain_kidney와 pretrain_human 비교에서 in-domain OOF와 single-cell 전이 결과가 어떻게 달랐나? | `reports/scgpt-prognosis-progress-2026-06-16.md` | human OOF 0.799, patient AUROC 0.500; kidney patient AUROC 0.875 |
| Q3 | 무관한 microarray와 랜덤 라벨 음성 대조는 어떤 결론을 지지하나? | `reports/scgpt-prognosis-progress-2026-06-16.md` | OOF 0.515, E-MTAB 0.458, 단순 누수 가능성 감소 |
| Q4 | Transformer가 RNN보다 병렬화와 장거리 의존성 학습에 유리한 이유는? | `papers/vaswaniAttentionAllYou2023.md` | recurrence 제거, self-attention, 짧은 path length |
| Q5 | scGPT가 다루는 대표 downstream task와 이식 연구에서의 활용 가능성은? | `papers/cuiScGPTFoundation2024.md`, `bio-ai/scgpt.md` | annotation, batch correction, perturbation, multi-omics와 연구 연결 |
| Q6 | microarray-to-scRNA adapter에서 Cox output을 생존 위험도로 바로 해석하면 안 되는 이유는? | `reports/scgpt-prognosis-progress-2026-06-16.md` | 핵심 실험이 BCE NR/Rejection objective 중심 |
| Q7 | common-gene 재학습은 bulk OOF와 외부 single-cell 예측에 어떤 trade-off를 보였나? | `reports/scgpt-prognosis-progress-2026-06-16.md` | OOF 소폭 하락 가능, 외부 rejection 확률 상승 |
| Q8 | Vault에 기록된 결과만으로 새로운 환자의 임상적 거부반응을 확정할 수 있는가? | 관련 report와 시스템 프롬프트 | 근거 한계와 연구용 모델임을 밝히고 임상 확정을 거부 |
| Q9 | 현재 문서에서 확인되지 않는 scGPT 최신 외부 벤치마크 수치를 알려줘. | 해당 근거 없음 | 수치를 만들지 않고 Vault 근거 부재를 명시 |
| Q10 | scGPT prognosis 연구에서 다음 실행 우선순위를 근거와 추론으로 나눠 제안해줘. | `research-questions.md`, 최신 prognosis report | 사실과 제안을 분리하고 양쪽을 인용 |

## 채점 기준

각 질문을 10점 만점으로 평가한다.

| 항목 | 배점 | 통과 조건 |
| --- | ---: | --- |
| 검색 적합성 | 2 | 기대 근거 중 핵심 문서가 검색됨 |
| 사실 정확성 | 3 | 수치·방향·모델 구조에 중대한 오류가 없음 |
| 출처 연결 | 2 | 핵심 주장 가까이에 열 수 있는 Obsidian 출처가 있음 |
| 근거/추론 구분 | 1 | 문서 사실과 모델 제안을 명확히 나눔 |
| 불확실성 처리 | 2 | 근거가 없거나 임상적 확정이 불가능할 때 이를 명시함 |

- 합격선: 질문별 8점 이상, 전체 평균 8.5점 이상
- 치명적 실패: 존재하지 않는 수치·논문·실험을 생성하거나, 출처 없이 임상 결론을 확정
- 회귀 판단: 이전 설정보다 전체 평균이 0.5점 이상 낮아지면 임베딩 모델, 제외 규칙, source chunk 수를 재검토
