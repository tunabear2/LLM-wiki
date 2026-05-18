# Zotero + Obsidian Workflow

## 목적

Zotero는 논문 PDF와 서지 정보를 관리하고, Obsidian은 `LLM Bio Wiki`의 Markdown 편집기로 사용한다. Zotero에서 가져온 논문 노트는 `docs/papers/`에 저장하고, GitHub Pages에는 MkDocs로 배포한다.

## Obsidian Vault

Obsidian에서 vault로 열 폴더:

```text
/Users/dwyun/Documents/LLM-wiki/docs
```

주의: `docs/LLM-wiki`가 아니라 `docs`를 열어야 한다.

## Zotero Integration 설정

Obsidian에서 `Settings` -> `Community plugins` -> `Zotero Integration`을 활성화한다.

`Settings` -> `Zotero Integration` -> `Import Formats`에서 다음 형식을 만든다.

```text
Name: LLM Wiki Paper Note
Output Path: papers/{{citekey}}.md
Image Output Path: assets/zotero/{{citekey}}/
Image Base Name: figure
Template File: _templates/zotero-paper.md
```

권장 옵션:

```text
Open the created or updated note(s) after import: On
Which notes to open after import: Last imported note
Enable Annotation Concatenation: On
```

## 논문 가져오기

1. Zotero를 실행한다.
2. Zotero에 논문과 PDF를 저장한다.
3. PDF에서 필요한 문장을 highlight한다.
4. Obsidian에서 `Cmd + P`를 누른다.
5. `Zotero Integration: LLM Wiki Paper Note`를 실행한다.
6. Zotero picker에서 논문을 선택한다.
7. `docs/papers/{{citekey}}.md` 문서가 생성되는지 확인한다.

## 배포

문서를 확인한 뒤 다음 명령으로 GitHub에 반영한다.

```bash
git add .
git commit -m "Add paper note"
git push
```
