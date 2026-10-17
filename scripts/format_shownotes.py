#!/usr/bin/env python3
"""Normalize show notes spacing for copy-paste into podcast platforms.

Rules enforced:
- Title, then one blank line, then first section
- Each **『section』** header on its own line
- Exactly one blank line between header and section content
- Exactly one blank line between sections
- Timestamps: one entry per block, blank line between entries
- Hosts (主播): 子鱼 and Lumi each on their own line, with one blank line between them
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SECTION_HEADER = re.compile(r"^\*\*『(.+?)』\*\*$")
TIMESTAMP_LINE = re.compile(r"^\d{1,2}:\d{2}(:\d{2})?\s")
DEFAULT_CHANNELS = "小宇宙，苹果Podcast，Spotify"


def parse_sections(text: str) -> tuple[str, list[tuple[str, list[str]]]]:
    lines = text.splitlines()
    title: str | None = None
    sections: list[tuple[str, list[str]]] = []
    current_name: str | None = None
    current_content: list[str] = []

    for line in lines:
        match = SECTION_HEADER.match(line.strip())
        if match:
            if current_name is not None:
                sections.append((current_name, current_content))
            current_name = match.group(1)
            current_content = []
            continue

        if current_name is None:
            if line.strip() and title is None:
                title = line.strip()
        else:
            current_content.append(line)

    if current_name is not None:
        sections.append((current_name, current_content))

    if title is None:
        raise ValueError("Missing episode title (first non-empty line before any section header).")

    return title, sections


def trim_block(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def split_paragraphs(lines: list[str]) -> list[list[str]]:
    paragraphs: list[list[str]] = []
    current: list[str] = []

    for line in lines:
        if not line.strip():
            if current:
                paragraphs.append(current)
                current = []
        else:
            current.append(line.rstrip())

    if current:
        paragraphs.append(current)

    return paragraphs


def format_paragraph_block(lines: list[str]) -> list[str]:
    paragraphs = split_paragraphs(lines)
    result: list[str] = []
    for index, paragraph in enumerate(paragraphs):
        result.extend(paragraph)
        if index < len(paragraphs) - 1:
            result.append("")
    return result


def format_timestamps(lines: list[str]) -> list[str]:
    entries: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped and TIMESTAMP_LINE.match(stripped):
            entries.append(stripped)

    result: list[str] = []
    for index, entry in enumerate(entries):
        result.append(entry)
        if index < len(entries) - 1:
            result.append("")
    return result


def format_hosts(lines: list[str]) -> list[str]:
    hosts = [line.strip() for line in lines if line.strip()]
    if len(hosts) >= 2:
        return [hosts[0], "", hosts[1], *hosts[2:]]
    return hosts


def format_section(name: str, lines: list[str]) -> list[str]:
    lines = trim_block(lines)

    if name == "时间戳":
        return format_timestamps(lines)
    if name == "主播":
        return format_hosts(lines)
    if name == "播客渠道":
        if not lines:
            return [DEFAULT_CHANNELS]
        return [line.strip() for line in lines if line.strip()]
    return format_paragraph_block(lines)


def assemble(title: str, sections: list[tuple[str, list[str]]]) -> str:
    output: list[str] = [title, ""]

    for index, (name, content_lines) in enumerate(sections):
        output.append(f"**『{name}』**")
        output.append("")
        output.extend(format_section(name, content_lines))
        if index < len(sections) - 1:
            output.append("")

    return "\n".join(output).rstrip() + "\n"


def format_shownotes(text: str) -> str:
    title, sections = parse_sections(text)
    if not sections:
        raise ValueError("No sections found. Expected headers like **『本期嘉宾』**.")
    return assemble(title, sections)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize show notes section spacing.")
    parser.add_argument("files", nargs="+", type=Path, help="Show notes markdown files")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with code 1 if any file would change",
    )
    args = parser.parse_args()

    changed_any = False

    for path in args.files:
        original = path.read_text(encoding="utf-8")
        formatted = format_shownotes(original)
        if formatted != original:
            changed_any = True
            if args.check:
                print(f"needs formatting: {path}", file=sys.stderr)
            else:
                path.write_text(formatted, encoding="utf-8")
                print(f"formatted: {path}")

    if args.check and changed_any:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
