#!/usr/bin/env python3

# Krok 1: Nacte vybuildenou markdown dokumentaci z ./out/kramerius-doc.md, pokud neni pres --input zadana jina cesta.
# Krok 2: Zjisti cilovy API endpoint a API klic. Nejdriv pouzije argumenty prikazove radky, potom env promenne
#         KRAMERIUS_DOC_API_URL a KRAMERIUS_DOC_API_KEY, a nakonec fallback config z ~/.kramerius-doc-chat/doc_chat_api.json.
# Krok 3: Odesle dokumentaci jako JSON {"text": "..."} metodou POST na endpoint /api/kramerius-doc.
# Krok 4: Vypise JSON odpoved serveru, nebo skonci explicitni chybou pri chybejicim vstupu, konfiguraci nebo neuspesnem HTTP volani.

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


DEFAULT_INPUT_PATH = Path("out") / "kramerius-doc.md"
DEFAULT_CONFIG_PATH = Path.home() / ".kramerius-doc-chat" / "doc_chat_api.json"
DEFAULT_TIMEOUT_SECONDS = 60
ENDPOINT_PATH = "/api/kramerius-doc"
ENV_API_URL = "KRAMERIUS_DOC_API_URL"
ENV_API_KEY = "KRAMERIUS_DOC_API_KEY"


@dataclass(frozen=True)
class ApiConfig:
    base_url: str
    api_key: str


def read_api_config(path: Path) -> ApiConfig:
    if not path.is_file():
        raise FileNotFoundError(f"Konfigurace API neexistuje: {path}")

    config = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(config, dict):
        raise RuntimeError(f"Konfigurace API musi byt JSON objekt: {path}")

    base_url = read_required_text_field(config, "url", path).rstrip("/")
    api_key = read_required_text_field(config, "configKey", path)
    return ApiConfig(base_url=base_url, api_key=api_key)


def read_required_text_field(config: dict[str, object], name: str, path: Path) -> str:
    value = config.get(name)
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"Konfigurace API neobsahuje neprazdne textove pole '{name}': {path}")

    return value.strip()


def endpoint_url(base_url: str) -> str:
    parsed_base_url = base_url.strip().rstrip("/")
    if not parsed_base_url:
        raise RuntimeError("Base URL API nesmi byt prazdne.")

    return parsed_base_url + ENDPOINT_PATH


def read_optional_env(name: str) -> str | None:
    value = os.environ.get(name)
    if value is None or not value.strip():
        return None

    return value.strip()


def read_config_if_needed(config_path: Path, config: ApiConfig | None) -> ApiConfig:
    if config is not None:
        return config

    return read_api_config(config_path)


def read_documentation(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Soubor s dokumentaci neexistuje: {path}")

    text = path.read_text(encoding="utf-8-sig")
    if not text.strip():
        raise RuntimeError(f"Soubor s dokumentaci je prazdny: {path}")

    return text


def publish_documentation(api_url: str, api_key: str, text: str, timeout_seconds: int) -> dict[str, object]:
    payload = json.dumps({"text": text}).encode("utf-8")
    request = urllib.request.Request(
        api_url,
        data=payload,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "X-API-Key": api_key,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            response_body = response.read().decode("utf-8")
            status = response.status
    except urllib.error.HTTPError as error:
        error_body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Upload dokumentace selhal: HTTP {error.code} {error.reason}. Odpoved: {error_body}"
        ) from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Upload dokumentace selhal: {error.reason}") from error

    if status < 200 or status >= 300:
        raise RuntimeError(f"Upload dokumentace selhal: HTTP {status}. Odpoved: {response_body}")

    if not response_body.strip():
        return {"status": status}

    parsed_response = json.loads(response_body)
    if not isinstance(parsed_response, dict):
        raise RuntimeError("API vratilo JSON odpoved, ktera neni objekt.")

    return parsed_response


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Odesle vybuildenou Kramerius dokumentaci do kramerius-doc-chat API."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help=f"Cesta k vybuildene dokumentaci. Vychozi hodnota je {DEFAULT_INPUT_PATH}.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help=f"Cesta ke konfiguraci API. Vychozi hodnota je {DEFAULT_CONFIG_PATH}.",
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="Base URL kramerius-doc-chat API. Pokud neni zadana, pouzije se pole 'url' z konfigurace.",
    )
    parser.add_argument(
        "--api-url",
        default=None,
        help=f"Kompletni upload endpoint. Pokud neni zadan, pouzije se env {ENV_API_URL}, pripadne konfigurace.",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help=f"API klic. Pokud neni zadan, pouzije se env {ENV_API_KEY}, pripadne konfigurace.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"HTTP timeout v sekundach. Vychozi hodnota je {DEFAULT_TIMEOUT_SECONDS}.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.timeout_seconds <= 0:
        raise ValueError("--timeout-seconds musi byt kladne cislo.")

    input_path = args.input.resolve()
    config_path = (args.config if args.config is not None else DEFAULT_CONFIG_PATH).expanduser().resolve()
    config: ApiConfig | None = None

    if args.api_url is not None:
        api_url = args.api_url.strip()
    elif (env_api_url := read_optional_env(ENV_API_URL)) is not None:
        api_url = env_api_url
    else:
        if args.base_url is not None:
            base_url = args.base_url.strip()
        else:
            config = read_config_if_needed(config_path, config)
            base_url = config.base_url
        api_url = endpoint_url(base_url)

    if args.api_key is not None:
        api_key = args.api_key.strip()
    elif (env_api_key := read_optional_env(ENV_API_KEY)) is not None:
        api_key = env_api_key
    else:
        config = read_config_if_needed(config_path, config)
        api_key = config.api_key

    if not api_url:
        raise RuntimeError("Upload endpoint nesmi byt prazdny.")
    if not api_key:
        raise RuntimeError("API klic nesmi byt prazdny.")

    text = read_documentation(input_path)
    response = publish_documentation(api_url, api_key, text, args.timeout_seconds)

    print("Dokumentace byla odeslana.")
    print(json.dumps(response, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
