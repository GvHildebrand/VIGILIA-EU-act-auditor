#!/usr/bin/env python3
"""
check_freshness.py — ask the EU whether the law under this auditor has moved.

`verify_references.py` proves reference/ is unaltered since it was fetched. It
cannot tell you that the EU has published something newer, and a standard that
is intact but superseded is exactly as wrong as one that was edited.

Two questions, both answered by the publisher:

  1. NEWER CONSOLIDATION  The Publications Office SPARQL endpoint is asked for
     every consolidated version of Regulation (EU) 2024/1689 that exists. If one
     is newer than the version this repository pins, the Act has been amended
     again and reference/ is behind.

  2. CHANGED SOURCE       The three pinned documents are re-fetched and hashed
     against reference/MANIFEST.md. Official Journal texts are immutable, so a
     mismatch here means something more surprising than an amendment.

NEEDS NETWORK. Deliberately not part of `make verify`, which must stay runnable
offline — an auditor you can only check when the EU is reachable is a worse
auditor. Run this before an audit you intend to rely on.

Usage:
    python3 _verify/check_freshness.py          # exit 1 if reference/ is behind
    python3 _verify/check_freshness.py --quiet  # only speak up when something is wrong
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "reference"
MANIFEST = REF / "MANIFEST.md"

SPARQL = "http://publications.europa.eu/webapi/rdf/sparql"
CELLAR = "http://publications.europa.eu/resource/celex/{}"
BASE_CELEX = "32024R1689"

QUERY = """PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?id WHERE {
  ?w cdm:resource_legal_id_celex ?id .
  FILTER(STRSTARTS(STR(?id), "%s"))
} ORDER BY ?id""" % ("0" + BASE_CELEX[1:])

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"
if not sys.stdout.isatty():
    GREEN = RED = YELLOW = DIM = OFF = ""


def get(url: str, headers: dict[str, str], timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as fh:
        return fh.read()


def pinned_consolidation() -> str | None:
    """The consolidated CELEX id this repository ships, from the folder name."""
    for d in sorted(REF.iterdir()):
        if d.is_dir() and re.fullmatch(r"0\d{4}R\d{4}-\d{8}", d.name):
            return d.name
    return None


def recorded_hashes() -> dict[str, str]:
    text = MANIFEST.read_text(encoding="utf-8")
    block = text.split("<!-- checksums:start -->", 1)[1].split("<!-- checksums:end -->", 1)[0]
    out = {}
    for line in block.splitlines():
        line = line.strip()
        if line and not line.startswith("```"):
            digest, _, name = line.partition("  ")
            out[name.strip()] = digest.strip()
    return out


def check_consolidations(quiet: bool) -> list[str]:
    pinned = pinned_consolidation()
    if pinned is None:
        return ["cannot tell which consolidated version this repo pins"]
    try:
        raw = get(
            SPARQL + "?" + urllib.parse.urlencode(
                {"query": QUERY, "format": "application/sparql-results+json"}
            ),
            {"Accept": "application/sparql-results+json"},
        )
        versions = sorted(
            b["id"]["value"] for b in json.loads(raw)["results"]["bindings"]
        )
    except (urllib.error.URLError, KeyError, ValueError, TimeoutError) as exc:
        print(f"  {YELLOW}??{OFF}  could not reach the SPARQL endpoint: {exc}")
        print(f"      {DIM}freshness unknown — this is not a pass{OFF}")
        return []

    if not versions:
        return ["SPARQL returned no consolidated versions — query or endpoint changed"]

    newest = versions[-1]
    if newest > pinned:
        return [
            f"reference/ pins {pinned} but the EU has published {newest}. "
            f"The Act has been amended again.\n"
            f"        Run `make refresh`, read the diff, re-verify every shipped "
            f"report, and bump the register if an obligation changed.\n"
            f"        All known consolidations: {', '.join(versions)}"
        ]
    if not quiet:
        print(f"  {GREEN}ok{OFF}  consolidation — {pinned} is the newest the EU publishes")
        print(f"      {DIM}known versions: {', '.join(versions)}{OFF}")
    return []


def check_sources(quiet: bool) -> list[str]:
    recorded = recorded_hashes()
    problems: list[str] = []
    checked = 0
    for path in sorted((REF / "_source").glob("*.xhtml")):
        rel = str(path.relative_to(REF))
        celex = path.stem
        try:
            data = get(
                CELLAR.format(celex),
                {"Accept": "application/xhtml+xml", "Accept-Language": "eng"},
            )
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"  {YELLOW}??{OFF}  could not re-fetch {celex}: {exc}")
            continue
        live = hashlib.sha256(data).hexdigest()
        checked += 1
        if recorded.get(rel) != live:
            problems.append(
                f"{celex} no longer matches what is recorded in MANIFEST.md.\n"
                f"        Official Journal texts do not change — investigate before "
                f"trusting any report that cites this file."
            )
    if not problems and checked and not quiet:
        print(f"  {GREEN}ok{OFF}  sources — {checked} pinned documents still hash to their recorded value")
    return problems


def main() -> int:
    quiet = "--quiet" in sys.argv
    if not quiet:
        print("checking freshness against publications.europa.eu")
    problems = check_consolidations(quiet) + check_sources(quiet)
    if problems:
        print(f"\n{RED}reference/ MAY BE STALE{OFF}")
        for p in problems:
            print(f"  - {p}")
        return 1
    if not quiet:
        print(f"\n{GREEN}reference/ is current{OFF}  {DIM}the EU publishes nothing newer{OFF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
