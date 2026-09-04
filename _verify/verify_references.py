#!/usr/bin/env python3
"""
verify_references.py — prove the standard in reference/ is unaltered and coherent.

Three checks:

  1. INTEGRITY   every file under reference/ hashes to what MANIFEST.md records.
  2. CROSS-CHECK the OJ Article 50 and the consolidated Article 50 agree on
                 nine of ten blocks and differ on exactly one — paragraph 7 —
                 which is the EU's own consolidation confirming what Regulation
                 (EU) 2026/1744 did and did not change.
  3. MARKERS     the consolidator's ▼M1 change marker sits on paragraph 7 and
                 nowhere else in Article 50.

Usage:
    python3 _verify/verify_references.py            # verify, exit 1 on failure
    python3 _verify/verify_references.py --write    # regenerate the checksum block

--write is for a deliberate refresh of the sources. It is not a way to make a
failing check pass: if a hash moved and you did not refresh on purpose, the text
underneath the auditor changed and every finding that cites it is suspect.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "reference"
MANIFEST = REF / "MANIFEST.md"
START, END = "<!-- checksums:start -->", "<!-- checksums:end -->"

OJ_ART50 = REF / "32024R1689" / "article-50.md"
CONS_ART50 = REF / "02024R1689-20260727" / "article-50-consolidated.md"

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"
if not sys.stdout.isatty():
    GREEN = RED = DIM = OFF = ""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def tracked() -> list[Path]:
    """Every reference file, in a stable order. MANIFEST.md excludes itself."""
    return sorted(
        p for p in REF.rglob("*")
        if p.is_file() and p != MANIFEST and not p.name.startswith(".")
    )


def blocks_of(path: Path) -> list[str]:
    """The provision blocks of an extracted file — everything after the rule."""
    text = path.read_text(encoding="utf-8")
    if "\n---\n" not in text:
        raise SystemExit(f"{path.name}: no provenance rule — not an extracted file")
    body = text.split("\n---\n", 1)[1]
    return [line for line in body.split("\n") if line.strip()]


# ─────────────────────────────────────────────────────────────────────────────

def check_integrity() -> list[str]:
    recorded: dict[str, str] = {}
    manifest = MANIFEST.read_text(encoding="utf-8")
    if START not in manifest:
        return ["MANIFEST.md has no checksum block — run with --write"]
    block = manifest.split(START, 1)[1].split(END, 1)[0]
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("```"):
            continue
        digest, _, name = line.partition("  ")
        if digest and name:
            recorded[name.strip()] = digest.strip()

    problems: list[str] = []
    seen = set()
    for path in tracked():
        rel = str(path.relative_to(REF))
        seen.add(rel)
        if rel not in recorded:
            problems.append(f"not in manifest: reference/{rel}")
        elif recorded[rel] != sha256(path):
            problems.append(f"HASH MISMATCH: reference/{rel}")
    for rel in recorded:
        if rel not in seen:
            problems.append(f"manifest lists a file that is gone: reference/{rel}")
    if not problems:
        print(f"  {GREEN}ok{OFF}  integrity — {len(recorded)} files match their recorded SHA-256")
    return problems


def check_cross() -> list[str]:
    problems: list[str] = []
    oj = blocks_of(OJ_ART50)
    cons_raw = blocks_of(CONS_ART50)
    markers = [i for i, b in enumerate(cons_raw) if b in ("▼M1", "▼B")]
    cons = [b for b in cons_raw if b not in ("▼M1", "▼B")]

    if len(oj) != len(cons):
        return [f"Article 50 block count differs: OJ {len(oj)}, consolidated {len(cons)}"]

    differing = [i for i, (a, b) in enumerate(zip(oj, cons)) if a != b]
    expected = [i for i, b in enumerate(cons) if b.startswith("7. ")]

    if differing != expected:
        problems.append(
            f"expected exactly paragraph 7 to differ between the OJ and consolidated "
            f"texts; differing block indexes {differing}, paragraph 7 at {expected}"
        )
    else:
        print(
            f"  {GREEN}ok{OFF}  cross-check — {len(oj) - 1} of {len(oj)} Article 50 blocks "
            f"byte-identical to the consolidated text; only paragraph 7 differs"
        )

    # ▼M1 must open immediately before paragraph 7.
    if not markers:
        problems.append("consolidated Article 50 carries no ▼M1/▼B change markers")
    else:
        first = markers[0]
        after = cons_raw[first + 1] if first + 1 < len(cons_raw) else ""
        if cons_raw[first] != "▼M1" or not after.startswith("7. "):
            problems.append(
                "the ▼M1 change marker does not sit on paragraph 7 — the amendment "
                "touched something this auditor does not know about"
            )
        else:
            print(f"  {GREEN}ok{OFF}  markers — ▼M1 sits on paragraph 7 and nowhere else")
    return problems


def write_manifest() -> None:
    lines = [START, "", "```", *(f"{sha256(p)}  {p.relative_to(REF)}" for p in tracked()), "```", "", END]
    text = MANIFEST.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    MANIFEST.write_text(head + "\n".join(lines) + tail, encoding="utf-8")
    print(f"wrote {len(tracked())} checksums to reference/MANIFEST.md")


def main() -> int:
    if "--write" in sys.argv:
        write_manifest()
        return 0

    print("verifying reference/")
    problems = check_integrity() + check_cross()
    if problems:
        print(f"\n{RED}FAILED{OFF}")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"\n{GREEN}reference/ verified{OFF}  {DIM}the standard is intact{OFF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
