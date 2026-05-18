# Paper Notes

Zotero와 Obsidian으로 가져온 논문 정리 문서를 모아두는 공간입니다.

## LLM / Transformer

- [Attention Is All You Need](vaswaniAttentionAllYou2023.md)

## 사용 흐름

1. Zotero에 논문과 PDF를 저장한다.
2. Obsidian에서 `Zotero Integration: LLM Wiki Paper Note`를 실행한다.
3. 생성된 `docs/papers/*.md` 문서를 읽고 직접 요약을 채운다.
4. `mkdocs serve`로 확인한다.
5. `git add .`, `git commit`, `git push`로 GitHub Pages에 반영한다.
