# Warm Research Wiki UI components

이 파일은 `exclude_docs`의 `_templates/*` 규칙으로 빌드에서 제외되는 작성자용 예시입니다.

## Callout

```markdown
!!! tip "Key point"
    기본 callout은 pale yellow 배경을 사용합니다.
```

## Note

```markdown
!!! note "Note"
    보조 설명과 구현 메모에 사용합니다.
```

## Warning

```markdown
!!! warning "Validation required"
    데이터 누수, 과해석, 재현성 위험처럼 주의가 필요한 내용에 사용합니다.
```

## Tag

문서 frontmatter의 `tags`를 사용하면 article header 아래에 자동으로 표시됩니다.

```yaml
---
updated: '2026-08-10'
tags:
- scGPT
- single-cell
- transplant
---
```

본문에서 직접 사용할 때는 다음 markup을 사용합니다.

```html
<span class="kb-tag">scGPT</span>
```

## ArticleCard

홈이나 index 문서에서 중요한 최신 문서 3–5개에만 사용합니다.

```html
<a class="kb-article-card" href="target/">
  <span class="kb-card__category">Single-cell AI</span>
  <span class="kb-card__title">Article title</span>
  <span class="kb-card__description">한두 문장의 설명입니다.</span>
  <time class="kb-card__date" datetime="2026-08-10">2026.08.10</time>
</a>
```

## TableOfContents

별도 markup은 필요하지 않습니다. 문서의 `##`, `###` heading에서 Material for MkDocs가 오른쪽 sticky TOC를 자동 생성합니다. 모바일에서는 기본 Material 동작에 따라 접힙니다.
