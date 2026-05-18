import re


OBSIDIAN_COMMENT_LINE = re.compile(r"(?m)^%%.*?%%\s*$\n?")


def on_page_markdown(markdown, **kwargs):
    return OBSIDIAN_COMMENT_LINE.sub("", markdown)
