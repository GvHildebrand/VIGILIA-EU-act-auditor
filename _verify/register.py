#!/usr/bin/env python3
"""
register.py — read the obligation register.

The register is [`provisions/article-50.md`](../provisions/article-50.md): plain
markdown, written to be read by a person. This module parses that same file.

There is deliberately no machine-readable copy of the rules. A JSON register would
be faster to parse and impossible for a reader to audit, and an auditor whose rule
set is only legible to its own tooling has reintroduced exactly the opacity this
repository exists to remove. If the two ever disagreed you would have no way to
know which one ran. So there is only one, and it is the readable one.

The format is ordinary markdown, and the parser depends on four conventions:

    ### EUAIA-50-2-MARK              an obligation
    #### EUAIA-50-2-X1 (exemption)   an exemption of the obligation above
    - **key** — value                a field
    > text                           the verbatim provision, one line

Quotes are kept on a single line because they must match the Official Journal
text byte for byte. Re-wrapping them would break the check that makes this
repository worth anything.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "provisions" / "article-50.md"

H3 = re.compile(r"^### (EUAIA-[A-Za-z0-9-]+)\s*$")
H4 = re.compile(r"^#### (EUAIA-[A-Za-z0-9-]+) \((\w+)\)\s*$")
FIELD = re.compile(r"^- \*\*(.+?)\*\* — (.+)$")
QUOTE = re.compile(r"^> (.+)$")
TITLE = re.compile(r"^\*\*(.+?)\*\* — (.+)$")
SECTION = re.compile(r"^## (.+)$")


def _key(k: str) -> str:
    return k.strip().lower().replace(" ", "_").replace("/", "_")


def load(path: Path | None = None) -> dict:
    """Parse the register into {version, obligations: [...], rules: [...]}."""
    text = (path or REGISTER).read_text(encoding="utf-8")
    version = "0"
    m = re.search(r"\*\*Version ([0-9.]+)\.\*\*", text)
    if m:
        version = m.group(1)

    obligations: list[dict] = []
    rules: list[dict] = []
    bucket = obligations           # which list the current heading belongs to
    cur: dict | None = None        # current obligation or rule
    sub: dict | None = None        # current exemption
    awaiting_title = False

    for line in text.splitlines():
        s = SECTION.match(line)
        if s:
            bucket = rules if s.group(1).strip().lower() == "the rules" else obligations
            cur = sub = None
            continue

        m = H4.match(line)
        if m and cur is not None:
            sub = {"id": m.group(1), "kind": m.group(2)}
            # A transitional window is not an escape hatch from the duty — it moves
            # the date the duty falls due. Filing it with the exemptions would let a
            # finding cite it as a `basis` for NOT_APPLICABLE, which is wrong.
            if m.group(2) == "transitional":
                cur["transitional"] = sub
            else:
                cur.setdefault("exemptions", []).append(sub)
            continue

        m = H3.match(line)
        if m:
            cur = {"id": m.group(1), "exemptions": []}
            sub = None
            awaiting_title = True
            bucket.append(cur)
            continue

        if cur is None:
            continue

        if awaiting_title:
            t = TITLE.match(line)
            if t:
                cur["provision"], cur["short"] = t.group(1), t.group(2)
                awaiting_title = False
                continue

        m = FIELD.match(line)
        if m:
            target = sub if sub is not None else cur
            target[_key(m.group(1))] = m.group(2).strip().strip("`")
            continue

        m = QUOTE.match(line)
        if m:
            target = sub if sub is not None else cur
            # first blockquote after a heading is that item's verbatim provision;
            # later ones (an actor definition, a penalty citation) do not overwrite it
            target.setdefault("quote", m.group(1))
            continue

    # a rule's citation blocks reuse `cite`; keep the last one reachable
    for o in obligations:
        o.setdefault("duty_force", "")
        o["source"] = o.get("cite", "")
    for r in rules:
        r["source"] = r.get("cite", "")

    return {"version": version, "obligations": obligations, "rules": rules}


if __name__ == "__main__":
    reg = load()
    print(f"register {reg['version']} — {len(reg['obligations'])} obligations, {len(reg['rules'])} rules")
    for o in reg["obligations"]:
        print(f"  {o['id']:22} {o['duty_force']:14} {len(o['exemptions'])} exemption(s)  {o['source']}")
    for r in reg["rules"]:
        print(f"  {r['id']:22} {r.get('kind','rule')}")
