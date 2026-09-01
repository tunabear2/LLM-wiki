# LLM-wiki

Obsidian Vault를 원본으로 관리하고 MkDocs Material로 발행하는 LLM·Bio AI 연구 위키입니다.

- Vault: `docs/`
- Web build: `mkdocs build --strict`
- LLM/RAG 운영 가이드: `docs/workflows/obsidian-llm-rag.md`
- RAG 메타데이터 적용: `.venv/bin/python hooks/apply_rag_metadata.py`
- 대형 worklog 검색본 생성: `.venv/bin/python hooks/build_rag_worklog_sources.py`
