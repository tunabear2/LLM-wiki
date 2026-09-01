---
type: workflow
status: active
rag_priority: low
updated: 2026-07-20
tags:
- wiki/workflow
- rag/exclude
---

# Obsidian LLM/RAG 운영 가이드

이 Vault는 `docs/`를 Obsidian 원본으로 사용하고 MkDocs로 발행한다. Copilot은 Vault 내부 검색과 답변 생성을 담당하며, 프롬프트·평가 문서는 Git으로 관리한다.

## 현재 구성

```text
Markdown notes
  -> Copilot lexical search (즉시 사용 가능)
  -> local semantic index (qwen3-embedding:0.6b)
  -> Vault QA retrieval
  -> local answer LLM (qwen2.5:7b)
  -> answer with note citations
```

- Copilot 플러그인: `3.3.3`
- 시스템 프롬프트: `copilot/system-prompts/LLM Bio Wiki Research Assistant.md`
- 사용자 명령: `copilot/copilot-custom-prompts/`
- 검색 제외: `copilot`, `_templates`, `rag`, `#rag/exclude`
- 평가 세트: `rag/evaluation.md`이며 정답 누수 방지를 위해 색인 제외
- 로컬 embedding: Ollama `qwen3-embedding:0.6b` (한국어 포함 다국어, 32K context)
- 로컬 답변 모델: Ollama `qwen2.5:7b` (한국어 포함 다국어, 32K context)
- Vault QA 검색 문맥: 상위 `6`개 chunk

## 최초 활성화

1. Obsidian을 다시 열거나 `Reload app without saving` 명령을 실행한다.
2. `Settings -> Community plugins`에서 `Copilot`이 활성화되어 있는지 확인한다.
3. 로컬 사용자는 `Model`에서 `qwen2.5:7b (Ollama)`를 선택한다. 클라우드 사용자는 `Basic -> Set Keys`에서 provider를 선택한다.
4. 클라우드 API 키는 `Obsidian Keychain`에 저장한다. `data.json` 평문 저장은 사용하지 않는다.
5. 기본 시스템 프롬프트로 `LLM Bio Wiki Research Assistant`를 선택한다.

로컬 Ollama 경로에는 API 키나 별도 사용료가 필요하지 않다.

## 권장 모델 경로

### 경로 A: 완전 로컬 RAG (현재 구성)

검색과 답변을 모두 로컬에서 처리하므로 검색된 노트 내용이 외부 provider로 전송되지 않는다.

1. Homebrew로 Ollama를 설치하고 로그인 시 자동 실행한다: `brew install ollama && brew services start ollama`
2. `ollama pull qwen3-embedding:0.6b`와 `ollama pull qwen2.5:7b`를 실행한다.
3. Copilot `Model -> Add model`에서 두 모델을 provider `Ollama`, base URL `http://localhost:11434/v1/`로 등록한다.
4. `QA -> Embedding model`에서 `qwen3-embedding:0.6b`를 선택한다.
5. 채팅 패널의 답변 모델에서 `qwen2.5:7b`를 선택하고 모드를 `vault QA (free)`로 둔다.
6. `Max source chunks`는 로컬 지연을 줄이기 위해 `6`으로 사용한다.

`qwen3:8b`도 설치되어 있지만 Copilot 3.3.3의 Ollama 경로에서는 thinking 비활성화가 일관되게 적용되지 않아 일반 Vault QA의 기본값으로 사용하지 않는다.

### 경로 B: 로컬 임베딩 + 클라우드 LLM

검색은 로컬에서 처리하고 답변만 OpenAI, Anthropic, Google, OpenRouter 중 사용하는 provider로 생성한다. 검색된 상위 문맥은 선택한 provider로 전송되며 API 요금이 발생할 수 있다.

### 경로 C: 클라우드 임베딩 + 클라우드 LLM

추가 로컬 프로그램 없이 시작하려면 OpenAI `text-embedding-3-small` 또는 다국어 embedding provider를 사용한다. 이 경우 색인할 문서 내용이 embedding provider로 전송된다.

embedding model을 변경하면 기존 vector와 호환되지 않으므로 반드시 `Force reindex vault`를 실행한다.

## QA 설정

`Settings -> Copilot -> QA`에서 다음 값을 사용한다.

| 설정 | 값 |
| --- | --- |
| Enable Semantic Search | embedding model 준비 후 켬 |
| Enable Inline Citations | 켬 |
| Auto-index strategy | `ON MODE SWITCH` |
| Enable Folder and Graph Boosts | 켬 |
| Exclusions | `copilot, _templates, rag, #rag/exclude` |
| Inclusions | 비움 |
| Max source chunks | `6` |
| Lexical Search RAM Limit | `100 MB` |
| Disable index loading on mobile | 켬 |
| Enable Index Sync | 기본적으로 끔; 기기마다 재색인 |

Copilot 3.3.3의 로컬 vector index는 Vault 루트의 `.copilot-index/`에 저장되며 Git에서 제외한다.

초기 설정 후 명령 팔레트에서 순서대로 실행한다.

1. `Count total vault tokens`
2. `Force reindex vault`
3. `List indexed files`
4. `Inspect index by note paths`로 report, paper, worklog chunk를 표본 확인

## 검색 우선순위

- 현재 연구 결론: `reports/`, `research-questions.md`
- 개념과 정의: `llm/`, `bio-ai/`, `glossary/`
- 외부 연구 근거: `papers/`, `articles/`
- 실행 상세와 과거 경과: `code/rag-sources/`
- 원본 대형 worklog: 보존하되 색인 제외

YAML의 `rag_priority`는 검색 엔진의 숫자 가중치가 아니라 LLM이 검색 결과 사이의 우선순위를 판단하기 위한 신호다. 실제 검색에는 folder/graph boost와 제외 정책도 함께 사용한다.

## 긴 worklog 관리

`hooks/build_rag_worklog_sources.py`는 원본 `2026-06-16-scgpt-prognosis-worklog.md`를 날짜 범위별 작은 문서로 생성한다.

```bash
.venv/bin/python hooks/build_rag_worklog_sources.py
```

- 원본은 `rag/exclude`로 중복 색인하지 않는다.
- 생성 문서는 `code/rag-sources/`에서 검색한다.
- 원본이 갱신되면 스크립트를 다시 실행하고 incremental index를 새로 고친다.
- 현재 결론이 worklog와 다르면 최신 report를 우선한다.

## 품질 평가

설정이나 모델을 변경한 뒤 `rag/evaluation.md`의 Q1~Q10을 새 대화에서 실행한다. 질문별 8점, 전체 평균 8.5점을 합격선으로 사용한다.

특히 다음 실패를 확인한다.

- 기대한 최신 report 대신 과거 worklog를 우선함
- 수치에 출처가 없음
- 검색되지 않은 논문이나 실험을 생성함
- 연구용 결과를 임상적 확정으로 표현함
- 평가 문서 자체가 검색되어 정답이 누수됨

## 보안 원칙

- API 키를 Markdown, Git, `.obsidian/plugins/copilot/data.json`에 직접 쓰지 않는다.
- 새 설치에서는 Obsidian Keychain을 사용한다.
- 환자 식별정보가 포함된 노트는 `tags`에 `rag/exclude`를 추가하거나 별도 제외 폴더로 옮긴다.
- 클라우드 LLM을 사용할 때는 검색된 문맥 일부가 provider로 전송된다는 점을 전제로 한다.
- Copilot Plus의 파일 변환·웹 기능은 명시적으로 실행할 때만 사용한다.

## 유지보수

새 문서를 만든 뒤 다음을 확인한다.

1. 템플릿의 `type`, `status`, `rag_priority`, `updated`, `tags`를 채운다.
2. 현재 결론을 담은 report는 `high`, 원시 worklog는 `low`로 둔다.
3. 민감하거나 중복된 문서는 `rag/exclude`한다.
4. `Index (refresh) vault`를 실행한다.
5. 중요한 결론 변경이면 평가 세트를 다시 실행한다.

참고: [Copilot Vault Search and Indexing](https://github.com/logancyang/obsidian-copilot/blob/3.3.3/docs/vault-search-and-indexing.md), [Copilot System Prompts](https://github.com/logancyang/obsidian-copilot/blob/3.3.3/docs/system-prompts.md)
