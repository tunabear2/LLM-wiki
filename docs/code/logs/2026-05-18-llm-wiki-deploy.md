# 2026-05-18 - LLM-wiki 배포

## 목적

로컬에서 수정한 LLM-wiki 문서를 GitHub Pages 사이트에 반영한다.

## 사용 데이터

- `docs/` 안의 Markdown 문서
- `mkdocs.yml`

## 실행 환경

- macOS terminal
- Git
- MkDocs
- GitHub Actions

## 코드 또는 명령어

```bash
cd /Users/dwyun/Documents/LLM-wiki

git status
git add docs mkdocs.yml
git commit -m "Update wiki"
git push origin main
```

## 결과

GitHub Actions가 자동으로 MkDocs 사이트를 빌드하고 GitHub Pages에 배포한다.

사이트 주소:

```text
https://tunabear2.github.io/LLM-wiki/
```

## 주의할 점

새 문서를 사이트 메뉴에 보이게 하려면 `mkdocs.yml`의 `nav:`에도 추가해야 한다.

`mkdocs serve`로 로컬 미리보기를 켜둔 경우, 터미널을 종료하면 로컬 서버는 꺼진다. 하지만 이미 배포된 GitHub Pages 사이트는 계속 유지된다.

