#!/usr/bin/env python3

# Sestaví jeden Markdown dokument určený jako znalostní podklad pro LLM.
#
# Postup zpracování:
# 1. Načte argumenty, určí kořen projektu, cílový soubor a čas sestavení.
# 2. Rekurzivně najde *.md soubory v docs/, vynechá cílový soubor a cesty
#    uvedené v EXCLUDED_MARKDOWN_PATH_PREFIXES.
# 3. Soubory přirozeně seřadí podle adresářové hierarchie; index.md je vždy
#    první v příslušném adresáři.
# 4. Každý soubor načte jako UTF-8 s volitelným BOM a v tomto pořadí:
#    a) odstraní bloky mezi <!-- llm:exclude:start --> a
#       <!-- llm:exclude:end --> a ověří správné párování markerů,
#    b) odstraní úvodní breadcrumb tvořený Markdown odkazy,
#    c) odstraní samostatné horizontální oddělovače --- mimo bloky kódu
#       a nadbytečné prázdné řádky v jejich bezprostředním okolí.
# 5. Po provedení filtrů přeskočí prázdné dokumenty.
# 6. Před každý zahrnutý dokument vloží jeho relativní cestu a URL vytvořenou
#    z DOCUMENTATION_BASE_URL_PLACEHOLDER, potom připojí filtrovaný obsah.
# 7. Na začátek přidá čas sestavení, výsledek zapíše v UTF-8 a vypíše počty
#    zahrnutých, prázdných a cestou vyloučených Markdown souborů.
#
# python .\tools\build_kramerius_doc.py
# output: .\out\kramerius-doc.md

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath
from urllib.parse import quote


DEFAULT_OUTPUT_NAME = "kramerius-doc.md"
DEFAULT_OUTPUT_DIR = "out"
LLM_EXCLUDE_START_MARKER = "<!-- llm:exclude:start -->"
LLM_EXCLUDE_END_MARKER = "<!-- llm:exclude:end -->"
DOCUMENTATION_BASE_URL_PLACEHOLDER = "{{KRAMERIUS_DOCUMENTATION_BASE_URL}}"
EXCLUDED_MARKDOWN_PATH_PREFIXES = (PurePosixPath("assets/mermaid"),)
BREADCRUMB_PATTERN = re.compile(
    r"^\[Úvod\]\([^\r\n)]+\)"
    r"(?:\s*(?:>|/)\s*\[[^\]\r\n]+\]\([^\r\n)]+\))+\s*$",
    flags=re.IGNORECASE,
)
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})")
HORIZONTAL_RULE_PATTERN = re.compile(r"^ {0,3}---[ \t]*$")


def natural_key(value: str) -> tuple[object, ...]:
    parts = re.split(r"(\d+)", value.casefold())
    return tuple(int(part) if part.isdigit() else part for part in parts)


def markdown_sort_key(path: Path, docs_root: Path) -> tuple[object, ...]:
    relative = path.relative_to(docs_root)
    key: list[object] = []

    for index, part in enumerate(relative.parts):
        is_file_name = index == len(relative.parts) - 1
        if is_file_name and part.casefold() == "index.md":
            key.append((0, ()))
        else:
            key.append((1, natural_key(part)))

    return tuple(key)


def is_excluded_markdown_path(path: Path, docs_root: Path) -> bool:
    relative_path = PurePosixPath(path.relative_to(docs_root).as_posix())
    return any(
        relative_path == prefix or prefix in relative_path.parents
        for prefix in EXCLUDED_MARKDOWN_PATH_PREFIXES
    )


def collect_markdown_files(docs_root: Path, output_path: Path) -> tuple[list[Path], int]:
    files: list[Path] = []
    excluded_count = 0
    resolved_output = output_path.resolve()

    for path in docs_root.rglob("*.md"):
        if not path.is_file():
            continue

        if path.resolve() == resolved_output:
            continue

        if is_excluded_markdown_path(path, docs_root):
            excluded_count += 1
            continue

        files.append(path)

    files.sort(key=lambda item: markdown_sort_key(item, docs_root))
    return files, excluded_count


def remove_llm_excluded_blocks(text: str, path: Path) -> str:
    included_lines: list[str] = []
    exclusion_start_line: int | None = None

    for line_number, line in enumerate(text.splitlines(keepends=True), start=1):
        stripped_line = line.strip()

        if stripped_line == LLM_EXCLUDE_START_MARKER:
            if exclusion_start_line is not None:
                raise ValueError(
                    f"Vnorena LLM exclude sekce v {path} na radku {line_number}; "
                    f"predchozi sekce zacala na radku {exclusion_start_line}."
                )

            exclusion_start_line = line_number
            continue

        if stripped_line == LLM_EXCLUDE_END_MARKER:
            if exclusion_start_line is None:
                raise ValueError(
                    f"Ukoncovaci LLM exclude marker bez zacatku v {path} "
                    f"na radku {line_number}."
                )

            exclusion_start_line = None
            continue

        if (
            LLM_EXCLUDE_START_MARKER in line
            or LLM_EXCLUDE_END_MARKER in line
        ):
            raise ValueError(
                f"LLM exclude marker musi byt na samostatnem radku v {path} "
                f"na radku {line_number}."
            )

        if exclusion_start_line is None:
            included_lines.append(line)

    if exclusion_start_line is not None:
        raise ValueError(
            f"Neukoncena LLM exclude sekce v {path}; "
            f"zacala na radku {exclusion_start_line}."
        )

    return "".join(included_lines)


def remove_leading_breadcrumb(text: str) -> str:
    lines = text.splitlines()
    first_content_index = next(
        (index for index, line in enumerate(lines) if line.strip()),
        None,
    )
    if first_content_index is None:
        return text

    if BREADCRUMB_PATTERN.fullmatch(lines[first_content_index].strip()) is None:
        return text

    del lines[first_content_index]
    while first_content_index < len(lines) and not lines[first_content_index].strip():
        del lines[first_content_index]

    return "\n".join(lines)


def remove_horizontal_rules(text: str) -> str:
    included_lines: list[str] = []
    fence_character: str | None = None
    fence_length = 0
    removed_rule_pending = False

    for line in text.splitlines(keepends=True):
        fence_match = FENCE_PATTERN.match(line)
        if fence_match is not None:
            if removed_rule_pending:
                if included_lines:
                    included_lines.append("\n")
                removed_rule_pending = False

            marker = fence_match.group(1)
            if fence_character is None:
                fence_character = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_character and len(marker) >= fence_length:
                fence_character = None
                fence_length = 0

            included_lines.append(line)
            continue

        if (
            fence_character is None
            and HORIZONTAL_RULE_PATTERN.fullmatch(line.rstrip("\r\n")) is not None
        ):
            while included_lines and not included_lines[-1].strip():
                included_lines.pop()
            removed_rule_pending = True
            continue

        if removed_rule_pending:
            if not line.strip():
                continue

            if included_lines:
                included_lines.append("\n")
            removed_rule_pending = False

        included_lines.append(line)

    return "".join(included_lines)


def read_non_empty_text(path: Path, docs_root: Path) -> str | None:
    text = path.read_text(encoding="utf-8-sig")
    text = remove_llm_excluded_blocks(text, path)
    text = remove_leading_breadcrumb(text)
    text = remove_horizontal_rules(text)

    if not text.strip():
        return None

    return text.strip()


def format_generated_at(value: str | None) -> str:
    if value is None:
        return datetime.now().astimezone().isoformat(timespec="seconds")

    parsed_value = value.strip()
    if not parsed_value:
        raise ValueError("Cas generovani nesmi byt prazdny.")

    if parsed_value.endswith("Z"):
        parsed_value = parsed_value[:-1] + "+00:00"

    parsed_datetime = datetime.fromisoformat(parsed_value)
    if parsed_datetime.tzinfo is None:
        parsed_datetime = parsed_datetime.astimezone()

    return parsed_datetime.isoformat(timespec="seconds")


def documentation_url_template(path: Path, docs_root: Path) -> str:
    relative_path = PurePosixPath(path.relative_to(docs_root).as_posix())
    if relative_path.name.casefold() == "index.md":
        route_parts = relative_path.parts[:-1]
    else:
        route_parts = (*relative_path.parts[:-1], relative_path.stem)

    encoded_route = "/".join(quote(part, safe="-._~") for part in route_parts)
    if not encoded_route:
        return DOCUMENTATION_BASE_URL_PLACEHOLDER + "/"

    return f"{DOCUMENTATION_BASE_URL_PLACEHOLDER}/{encoded_route}/"


def build_document(root: Path, output_path: Path, generated_at: str | None) -> tuple[int, int, int]:
    docs_root = root / "docs"
    if not docs_root.is_dir():
        raise NotADirectoryError(f"Adresar s dokumentaci neexistuje: {docs_root}")

    markdown_files, excluded_count = collect_markdown_files(docs_root, output_path)
    if not markdown_files:
        raise RuntimeError(f"Nebyly nalezeny zadne markdown soubory v {docs_root}.")

    included_count = 0
    skipped_empty_count = 0
    chunks: list[str] = [
        f"Build date: {format_generated_at(generated_at)}",
        "",
    ]

    for path in markdown_files:
        text = read_non_empty_text(path, docs_root)
        if text is None:
            skipped_empty_count += 1
            continue

        relative_path = path.relative_to(docs_root).as_posix()
        chunks.append(f"=== {relative_path} ===")
        chunks.append(documentation_url_template(path, docs_root))
        chunks.append("")
        chunks.append(text)
        chunks.append("")
        included_count += 1

    if included_count == 0:
        raise RuntimeError("Vsechny nalezene markdown soubory jsou prazdne.")

    output_path.write_text("\n".join(chunks).rstrip() + "\n", encoding="utf-8")
    return included_count, skipped_empty_count, excluded_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Slouci markdown dokumentaci Krameria do jednoho souboru."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Korenovy adresar projektu. Vychozi hodnota je nadrazeny adresar slozky tools.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=f"Vystupni soubor. Vychozi hodnota je {DEFAULT_OUTPUT_DIR}/{DEFAULT_OUTPUT_NAME} v koreni projektu.",
    )
    parser.add_argument(
        "--generated-at",
        default=None,
        help="Cas generovani ve formatu ISO 8601. Bez hodnoty se pouzije aktualni lokalni cas.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"Korenovy adresar neexistuje: {root}")

    output_path = args.output if args.output is not None else root / DEFAULT_OUTPUT_DIR / DEFAULT_OUTPUT_NAME
    if not output_path.is_absolute():
        output_path = root / output_path
    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    included_count, skipped_empty_count, excluded_count = build_document(root, output_path, args.generated_at)
    print(f"Vytvoreno: {output_path}")
    print(f"Zahrnuto markdown souboru: {included_count}")
    print(f"Preskoceno prazdnych souboru: {skipped_empty_count}")
    print(f"Preskoceno vyloucenych markdown souboru: {excluded_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
