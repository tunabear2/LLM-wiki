#!/usr/bin/env python3
"""Build smaller RAG source notes from the canonical scGPT prognosis worklog.

The original worklog remains untouched as the archival source. Copilot excludes
that original via the ``rag/exclude`` tag and indexes these generated chunks.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SOURCE = DOCS / "code/logs/2026-06-16-scgpt-prognosis-worklog.md"
OUTPUT = DOCS / "code/rag-sources"

GROUPS = {
    "2026-06": ("scGPT prognosis worklog — 2026-06", "2026-06-01..2026-06-16"),
    "2026-05-31": ("scGPT prognosis worklog — 2026-05-31", "2026-05-31"),
    "2026-05-26-to-30": ("scGPT prognosis worklog — 2026-05-26~30", "2026-05-26..2026-05-30"),
    "2026-05-18-to-24": ("scGPT prognosis worklog — 2026-05-18~24", "2026-05-18..2026-05-24"),
    "2026-05-early": ("scGPT prognosis worklog — 2026-05 early", "2026-04-30..2026-05-17"),
}


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    match = re.match(r"\A---\n.*?\n---\n?", text, flags=re.DOTALL)
    return text[match.end() :] if match else text


def group_for(header: str) -> str:
    match = re.search(r"(2026)-(\d{2})-(\d{2})", header)
    if not match:
        return "2026-05-early"
    value = tuple(int(part) for part in match.groups())
    if value >= (2026, 6, 1):
        return "2026-06"
    if value >= (2026, 5, 31):
        return "2026-05-31"
    if value >= (2026, 5, 26):
        return "2026-05-26-to-30"
    if value >= (2026, 5, 18):
        return "2026-05-18-to-24"
    return "2026-05-early"


def main() -> None:
    body = strip_frontmatter(SOURCE.read_text(encoding="utf-8"))
    sections = re.split(r"(?=^## )", body, flags=re.MULTILINE)
    buckets: dict[str, list[str]] = {key: [] for key in GROUPS}

    for section in sections:
        if not section.startswith("## "):
            continue
        header = section.splitlines()[0]
        buckets[group_for(header)].append(section.rstrip())

    OUTPUT.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for slug, (title, date_range) in GROUPS.items():
        metadata = {
            "type": "worklog-chunk",
            "status": "archive",
            "rag_priority": "medium",
            "updated": date.today().isoformat(),
            "date_range": date_range,
            "source": "code/logs/2026-06-16-scgpt-prognosis-worklog.md",
            "topics": ["single-cell", "kidney-transplant", "prognosis"],
            "models": ["scGPT"],
            "tags": ["wiki/worklog-chunk"],
        }
        frontmatter = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False).rstrip()
        sections_text = "\n\n".join(buckets[slug])
        output = (
            f"---\n{frontmatter}\n---\n\n"
            f"# {title}\n\n"
            "> [!note] 검색용 분할본\n"
            "> 원본은 [2026-06-16 scGPT prognosis worklog]"
            "(../logs/2026-06-16-scgpt-prognosis-worklog.md)입니다. "
            "결론이 충돌하면 최신 `reports/` 문서를 우선합니다.\n\n"
            f"{sections_text}\n"
        )
        target = OUTPUT / f"scgpt-prognosis-{slug}.md"
        target.write_text(output, encoding="utf-8")
        written.append(target)

    index = OUTPUT / "index.md"
    links = "\n".join(f"- [{GROUPS[p.stem.removeprefix('scgpt-prognosis-')][0]}]({p.name})" for p in written)
    index.write_text(
        "---\n"
        "type: index\n"
        "status: reference\n"
        "rag_priority: low\n"
        f"updated: {date.today().isoformat()}\n"
        "tags:\n"
        "- wiki/index\n"
        "- rag/exclude\n"
        "---\n\n"
        "# scGPT prognosis RAG sources\n\n"
        "긴 원본 worklog를 검색 가능한 크기로 나눈 파생 문서입니다.\n\n"
        f"{links}\n",
        encoding="utf-8",
    )
    print(f"RAG worklog sources built: {len(written)} chunk(s)")


if __name__ == "__main__":
    main()
