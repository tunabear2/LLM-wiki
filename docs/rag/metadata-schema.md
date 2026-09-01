---
type: rag-config
status: reference
rag_priority: low
updated: 2026-07-20
tags:
- wiki/rag-config
- rag/exclude
---

# LLM-wiki RAG metadata schema

이 문서는 검색 품질을 위한 속성 규약이다. 설정 문서 자체는 검색 결과를 오염시키지 않도록 `rag/exclude`한다.

## 필수 속성

| 속성 | 허용값 | 용도 |
| --- | --- | --- |
| `type` | `report`, `paper`, `concept`, `worklog`, `code-note`, `article`, `workflow`, `index` 등 | 문서 역할 구분 |
| `status` | `active`, `reference`, `reading`, `draft`, `archive` | 최신성·완성도 판단 |
| `rag_priority` | `high`, `medium`, `low` | 답변 근거 우선순위 |
| `updated` | `YYYY-MM-DD` | 상충하는 기록의 최신성 판단 |
| `tags` | Obsidian 속성 목록 | 분류와 색인 제외 |

## 선택 속성

- `created`: 최초 작성일
- `topics`: 연구 주제 목록
- `models`: 언급하거나 평가한 모델 목록
- `datasets`: 사용하거나 설명한 데이터셋 목록
- `citation_key`: Zotero citation key
- `source`: 파생 문서가 가리키는 원본 경로
- `date_range`: worklog 분할본이 포함하는 기간

## 우선순위 정책

동일 주장에 여러 근거가 있으면 다음 순서로 사용한다.

1. `rag_priority: high`이면서 `status: active`인 `reports/` 문서
2. `concept`, `research-question`, `glossary` 문서
3. 개별 논문 노트와 article
4. 검색용 worklog 분할본
5. `rag_priority: low` 문서

worklog는 실행 세부사항과 과거 결과를 확인할 때 사용한다. 현재 결론은 최신 report를 우선한다.

## 색인 제외

다음 중 하나에 해당하면 Copilot 색인에서 제외한다.

- `tags`에 `rag/exclude`가 있는 문서
- `_templates/`, `rag/`, `copilot/` 폴더
- 원본과 내용이 중복되는 대형 worklog
- 평가 질문과 정답을 담은 문서

본문의 inline tag가 아니라 YAML 속성의 `tags`를 사용해야 한다.
