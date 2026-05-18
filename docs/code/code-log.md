# Code Log

이 문서는 연구 과정에서 실제로 사용한 코드, 명령어, notebook, script를 정리하기 위한 공간이다.

목표는 코드를 예쁘게 모아두는 것이 아니라, 나중에 같은 분석을 다시 해야 할 때 바로 재현할 수 있게 만드는 것이다.

## 정리 원칙

각 코드 기록은 다음 정보를 포함한다.

1. 무엇을 하려고 쓴 코드인가?
2. 어떤 데이터에 사용했는가?
3. 실행 환경은 무엇인가?
4. 핵심 코드 또는 명령어는 무엇인가?
5. 결과 파일은 어디에 저장되었는가?
6. 다시 사용할 때 주의할 점은 무엇인가?

## 기록 템플릿

```text
## 날짜 - 코드 이름

### 목적

### 사용 데이터

### 실행 환경

### 코드 또는 명령어

### 결과

### 주의할 점
```

## 2026-05-18 - LLM-wiki 배포

### 목적

로컬에서 수정한 LLM-wiki 문서를 GitHub Pages 사이트에 반영한다.

### 사용 데이터

- `docs/` 안의 Markdown 문서
- `mkdocs.yml`

### 실행 환경

- macOS terminal
- Git
- MkDocs
- GitHub Actions

### 코드 또는 명령어

```bash
cd /Users/dwyun/Documents/LLM-wiki

git status
git add docs mkdocs.yml
git commit -m "Update wiki"
git push origin main
```

### 결과

GitHub Actions가 자동으로 MkDocs 사이트를 빌드하고 GitHub Pages에 배포한다.

사이트 주소:

```text
https://tunabear2.github.io/LLM-wiki/
```

### 주의할 점

새 문서를 사이트 메뉴에 보이게 하려면 `mkdocs.yml`의 `nav:`에도 추가해야 한다.

## 앞으로 정리할 코드 후보

- Single-cell 데이터 전처리 코드
- scGPT 또는 Geneformer 실행 코드
- Embedding 추출 코드
- UMAP 시각화 코드
- Domain shift 평가 코드
- Batch/cohort split 실험 코드

