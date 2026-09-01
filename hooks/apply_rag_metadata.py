#!/usr/bin/env python3
"""Apply the LLM-wiki RAG metadata schema to Markdown notes.

The script is intentionally conservative: it preserves existing frontmatter
values and only fills fields that are missing. Run it from the repository root.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TODAY = date.today().isoformat()

SKIP_PARTS = {".obsidian", "LLM-wiki", "assets", "copilot"}
RAG_EXCLUDED = {
    "code/logs/2026-06-04-scgpt-worklog.md",
    "code/logs/2026-06-16-scgpt-prognosis-worklog.md",
    "workflows/obsidian-llm-rag.md",
}


def classify(relative: Path) -> tuple[str, str, str, list[str]]:
    """Return type, status, priority, and tags for a note path."""
    path = relative.as_posix()

    if path.startswith("_templates/"):
        return "template", "draft", "low", ["wiki/template", "rag/exclude"]
    if path.startswith("rag/"):
        return "rag-config", "reference", "low", ["wiki/rag-config", "rag/exclude"]
    if path.startswith("code/rag-sources/"):
        return "worklog-chunk", "archive", "medium", ["wiki/worklog-chunk"]
    if relative.name == "index.md":
        return "index", "reference", "low", ["wiki/index"]
    if path == "research-questions.md":
        return "research-question", "active", "high", ["wiki/research-question"]
    if path.startswith("reports/"):
        return "report", "active", "high", ["wiki/report"]
    if path.startswith("papers/"):
        return "paper", "reference", "medium", ["wiki/paper"]
    if path.startswith("articles/"):
        return "article", "reference", "medium", ["wiki/article"]
    if path.startswith(("llm/", "bio-ai/")):
        return "concept", "reference", "high", ["wiki/concept"]
    if path.startswith("code/logs/"):
        return "worklog", "archive", "low", ["wiki/worklog"]
    if path.startswith("code/"):
        return "code-note", "reference", "medium", ["wiki/code-note"]
    if path.startswith("glossary/"):
        return "glossary", "reference", "high", ["wiki/glossary"]
    if path.startswith("workflows/"):
        return "workflow", "reference", "low", ["wiki/workflow"]
    return "note", "reference", "medium", ["wiki/note"]


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text

    match = re.match(r"\A---\n(.*?)\n---\n?", text, flags=re.DOTALL)
    if not match:
        return {}, text

    loaded = yaml.safe_load(match.group(1)) or {}
    if not isinstance(loaded, dict):
        loaded = {}
    return loaded, text[match.end() :]


def update_note(path: Path) -> bool:
    relative = path.relative_to(DOCS)
    note_type, status, priority, default_tags = classify(relative)
    metadata, body = split_frontmatter(path.read_text(encoding="utf-8"))

    metadata.setdefault("type", note_type)
    metadata.setdefault("status", status)
    metadata.setdefault("rag_priority", priority)
    metadata.setdefault("updated", TODAY)

    tags = metadata.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        tags = []
    for tag in default_tags:
        if tag not in tags:
            tags.append(tag)
    if relative.as_posix() in RAG_EXCLUDED and "rag/exclude" not in tags:
        tags.append("rag/exclude")
    metadata["tags"] = tags

    rendered = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip()
    updated = f"---\n{rendered}\n---\n\n{body.lstrip()}"
    old = path.read_text(encoding="utf-8")
    if updated == old:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(DOCS.rglob("*.md")):
        relative = path.relative_to(DOCS)
        if any(part in SKIP_PARTS for part in relative.parts):
            continue
        changed += int(update_note(path))
    print(f"RAG metadata updated: {changed} note(s)")


if __name__ == "__main__":
    main()
