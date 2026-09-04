#!/usr/bin/env python3
"""
verify_pins.py — pin the verdicts of the shipped example audits.

WHAT THIS FIXES. `verify_citations.py` constrains the *form* of a report: real
quotes, full coverage, arithmetic severity. It does not constrain the
*conclusion*. Two runs of this auditor over the same evidence can reach different
verdicts on the obligations that turn on judgement — Article 50(1)'s "obvious to
a reasonably well-informed, observant and circumspect person" is a legal standard,
not a lookup — and both runs pass citation verification.

So the examples ship with their verdicts pinned. A pin is a baseline, and it
catches the two things that would otherwise change an example silently:

  1. the repository moved under it — the register was edited, an obligation
     added, the reference text refreshed;
  2. somebody re-ran the auditor and got a different answer.

WHAT THIS IS NOT. It does not make the model deterministic, and it is not
evidence that a pinned verdict is correct. It is a diff. When a fresh run
disagrees with the pin, that is a question to answer, not a failure to suppress —
and the answer may well be that the pin was wrong.

Usage:
    python3 _verify/verify_pins.py                 # check every example
    python3 _verify/verify_pins.py --emit           # (re)write pins from the reports
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_verify"))
from verify_citations import parse_blocks  # noqa: E402

FIELDS = ("verdict", "severity", "applicability")

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"
if not sys.stdout.isatty():
    GREEN = RED = YELLOW = DIM = OFF = ""


def verdicts_of(report: Path) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for f in parse_blocks(report.read_text(encoding="utf-8"), "finding"):
        if "provision" in f:
            out[f["provision"]] = {k: f.get(k, "") for k in FIELDS}
    return dict(sorted(out.items()))


def emit() -> int:
    for report in sorted(ROOT.glob("examples/*/audit-report.md")):
        pin = report.parent / "expected-verdicts.json"
        payload = {
            "_note": (
                "Baseline verdicts for this example. Checked by _verify/verify_pins.py. "
                "A mismatch is a question, not necessarily a defect — see the tool's "
                "docstring. Regenerate deliberately with --emit, never to silence a diff."
            ),
            "report": report.name,
            "verdicts": verdicts_of(report),
        }
        pin.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"  wrote {pin.relative_to(ROOT)}  ({len(payload['verdicts'])} verdicts)")
    return 0


def main() -> int:
    if "--emit" in sys.argv:
        return emit()

    pins = sorted(ROOT.glob("examples/*/expected-verdicts.json"))
    if not pins:
        print(f"{YELLOW}no pins found — run with --emit to create them{OFF}")
        return 0

    problems: list[str] = []
    print("verifying pinned verdicts")
    for pin in pins:
        data = json.loads(pin.read_text(encoding="utf-8"))
        report = pin.parent / data.get("report", "audit-report.md")
        name = pin.parent.name
        if not report.is_file():
            problems.append(f"{name}: pinned report {report.name} is missing")
            continue

        actual = verdicts_of(report)
        expected = data["verdicts"]

        for pid in sorted(set(expected) | set(actual)):
            if pid not in actual:
                problems.append(f"{name}: {pid} is pinned but absent from the report")
            elif pid not in expected:
                problems.append(f"{name}: {pid} is in the report but not pinned — re-emit deliberately")
            else:
                for k in FIELDS:
                    if expected[pid][k] != actual[pid][k]:
                        problems.append(
                            f"{name}: {pid} {k} moved  {expected[pid][k]} → {actual[pid][k]}"
                        )
        if not any(p.startswith(f"{name}:") for p in problems):
            print(f"  {GREEN}ok{OFF}  {name} — {len(actual)} verdicts match the pin")

    if problems:
        print(f"\n{RED}PINNED VERDICTS MOVED{OFF}")
        for p in problems:
            print(f"  - {p}")
        print(
            f"\n  {DIM}If a fresh run produced this, decide which answer is right before "
            f"re-emitting.\n  If the register or reference/ changed, the examples need "
            f"re-auditing, not re-pinning.{OFF}"
        )
        return 1
    print(f"\n{GREEN}all pins hold{OFF}  {DIM}no example changed its mind{OFF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
