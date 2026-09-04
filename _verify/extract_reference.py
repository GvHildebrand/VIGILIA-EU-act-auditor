#!/usr/bin/env python3
"""
extract_reference.py — build reference/ from the authentic sources.

Nothing in reference/ is typed by hand. Every provision file is produced by this
script from the XHTML the EU Publications Office served, so a reader can run

    bash reference/fetch-sources.sh && python3 _verify/extract_reference.py && git diff

and see that the standard shipped in this repo is byte-identical to the standard
the EU publishes today. An empty diff is the proof.

WHAT THIS SCRIPT CHANGES ABOUT THE TEXT
    1. Markup is removed and HTML entities are resolved.
    2. Runs of whitespace — including the non-breaking spaces the OJ uses after
       paragraph numbers — collapse to a single space.
    3. A two-cell OJ list row ("(g)" | "transparency obligations …") is joined
       onto one line as "(g) transparency obligations …".
    Nothing else. No word is added, removed, reordered, or reworded. Quotation
    marks stay the typographic characters the OJ uses (' ' ' '), because a
    finding that quotes this text must match it byte for byte.

Deterministic by construction: no timestamps, no network, no randomness. The
retrieval dates and hashes live in reference/MANIFEST.md, not in these files.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "reference" / "_source"

# ─────────────────────────────────────────────────────────────────────────────
# HTML → ordered text blocks
# ─────────────────────────────────────────────────────────────────────────────

# A short cell such as "(1)", "(g)", "(20)", "(3a)" is a list label whose text
# lives in the next cell. Joining them is what turns the OJ's two-column tables
# back into readable, quotable lines.
LABEL = re.compile(r"^\((?:[0-9]{1,3}[a-z]?|[a-z]{1,2}|[ivxl]{1,6})\)$")


def blocks(fragment: str) -> list[str]:
    """Every <p> in document order, list labels joined to the text they label."""
    raw = re.findall(r"<p\b[^>]*>(.*?)</p>", fragment, flags=re.S)
    out: list[str] = []
    for chunk in raw:
        text = re.sub(r"<[^>]+>", "", chunk)
        text = html.unescape(text)
        #   (the OJ's spacer after "1." and inside dates) folds in here.
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        if out and LABEL.match(out[-1]):
            out[-1] = f"{out[-1]} {text}"
        else:
            out.append(text)
    return out


def blocks_consolidated(fragment: str) -> list[str]:
    """Blockify the consolidated dialect.

    Consolidated texts use a different markup from the OJ: paragraphs are
    ``<div class="norm">`` with the number in a ``<span class="no-parag">``,
    and amended passages are fenced by the change markers ▼M1 / ▼B. Those
    markers are kept — they are the consolidator's own record of which words
    came from the amending act, and dropping them would hide the one thing this
    file exists to show.
    """
    text = re.sub(r"(?is)<(script|style).*?</\1>", "", fragment)
    text = re.sub(r"</span>", "", text)          # keep "7." glued to its text
    # Collapse the source's own newlines FIRST, so that only the block
    # boundaries inserted on the next line become line breaks.
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"</(div|p|td|tr)>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    out: list[str] = []
    for line in text.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            out.append(line)
    return out


def div_by_id(doc: str, div_id: str) -> str:
    """The complete <div> carrying id="div_id", found by depth counting."""
    anchor = re.search(rf'<div[^>]*\bid="{re.escape(div_id)}"', doc)
    if not anchor:
        raise LookupError(f'no <div id="{div_id}"> in source')
    i = anchor.start()
    depth = 0
    for tag in re.finditer(r"<div\b|</div>", doc[i:]):
        depth += 1 if tag.group() == "<div" else -1
        if depth == 0:
            return doc[i : i + tag.end()]
    raise LookupError(f'unbalanced <div id="{div_id}">')


def between(bs: list[str], start: str, end: str) -> list[str]:
    """Blocks from the first matching `start` through the first later `end`."""
    lo = next(i for i, b in enumerate(bs) if re.search(start, b))
    hi = next(i for i, b in enumerate(bs[lo:], lo) if re.search(end, b))
    return bs[lo : hi + 1]


# ─────────────────────────────────────────────────────────────────────────────
# Emit
# ─────────────────────────────────────────────────────────────────────────────

def write(path: Path, title: str, provenance: list[str], body: list[str]) -> None:
    lines = [f"# {title}", ""]
    lines += [f"> {p}" for p in provenance]
    lines += [
        "",
        "> Extracted verbatim by `_verify/extract_reference.py`. Whitespace"
        " normalised; no other change. Cite by line number.",
        "",
        "---",
        "",
    ]
    for b in body:
        lines += [b, ""]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    n = len(path.read_text(encoding="utf-8").splitlines())
    print(f"  {path.relative_to(ROOT)}  ({n} lines)")


OJ = "**Source** Regulation (EU) 2024/1689 (Artificial Intelligence Act), OJ L, 2024/1689, 12.7.2024, ELI: http://data.europa.eu/eli/reg/2024/1689/oj — CELEX 32024R1689. This is the authentic text."
OMNI = "**Source** Regulation (EU) 2026/1744 (Digital Omnibus on AI), OJ L, 2026/1744, 24.7.2026, ELI: http://data.europa.eu/eli/reg/2026/1744/oj — CELEX 32026R1744. This is the authentic text."
CONS = "**Source** Consolidated text 02024R1689 — EN — 27.07.2026 — 001.001, CELEX 02024R1689-20260727."
CONS_DISCLAIMER = (
    "**EUR-Lex states of this consolidated text:** “This text is meant purely as a"
    " documentation tool and has no legal effect. The Union’s institutions do not assume"
    " any liability for its contents. The authentic versions of the relevant acts,"
    " including their preambles, are those published in the Official Journal of the"
    " European Union” — which is why findings cite the OJ text above, and use this"
    " file only to cross-check the amendment."
)

# Definitions Article 50 actually depends on. Nothing else from Article 3 is
# shipped, because an auditor that cannot say why a file is in reference/ should
# not have put it there.
DEFS = {
    1: "‘AI system’ — the gateway term for every obligation",
    3: "‘provider’ — bears 50(1) and 50(2)",
    4: "‘deployer’ — bears 50(3) and 50(4)",
    9: "‘placing on the market’ — triggers the Art. 111(4) transitional window",
    11: "‘putting into service’",
    39: "‘emotion recognition system’ — trigger for 50(3)",
    40: "‘biometric categorisation system’ — trigger for 50(3)",
    60: "‘deep fake’ — trigger for 50(4) first subparagraph",
    63: "‘general-purpose AI model’",
    66: "‘general-purpose AI system’ — named expressly in 50(2)",
}


def main() -> int:
    if not SRC.exists() or not (SRC / "32024R1689.xhtml").exists():
        sys.exit("reference/_source is empty — run reference/fetch-sources.sh first")

    act = (SRC / "32024R1689.xhtml").read_text(encoding="utf-8")
    omni = (SRC / "32026R1744.xhtml").read_text(encoding="utf-8")
    cons = (SRC / "02024R1689-20260727.xhtml").read_text(encoding="utf-8")

    out = ROOT / "reference"
    print("extracting:")

    # 1 ── Article 50, the whole of it.
    write(
        out / "32024R1689" / "article-50.md",
        "Article 50 — Transparency obligations for providers and deployers of certain AI systems",
        [OJ, "**Applies from** 2 August 2026 (Article 113). **Amended** at paragraph 7"
             " only, by Regulation (EU) 2026/1744 — see `../32026R1744/`."],
        blocks(div_by_id(act, "art_50")),
    )

    # 2 ── Only the definitions Article 50 leans on.
    defs_blocks = blocks(div_by_id(act, "art_3"))
    picked: list[str] = []
    for num, why in DEFS.items():
        hit = next(
            (b for b in defs_blocks if b.startswith(f"({num}) ")),
            None,
        )
        if hit is None:
            sys.exit(f"Article 3 definition ({num}) not found — extraction is wrong")
        picked += [f"*Why this definition is here: {why}.*", hit]
    write(
        out / "32024R1689" / "article-3-definitions.md",
        "Article 3 — the definitions Article 50 depends on",
        [OJ, "**Selective.** Only the ten defined terms the Article 50 obligations turn"
             " on are reproduced. Numbering is the Regulation's own."],
        picked,
    )

    # 3 ── Penalties. This is where severity comes from.
    write(
        out / "32024R1689" / "article-99-penalties.md",
        "Article 99 — Penalties",
        [OJ, "**Article 99(4)(g)** is the penalty anchor for every Article 50 finding."
             " Paragraph 6a was inserted by Regulation (EU) 2026/1744 and is not in this"
             " OJ text — see `../32026R1744/`."],
        blocks(div_by_id(act, "art_99")),
    )

    # 4 ── The dates.
    write(
        out / "32024R1689" / "article-111-113-application.md",
        "Articles 111 and 113 — transitional provisions and application dates",
        [OJ, "**Article 111(4)**, the transitional window for Article 50(2), was *added*"
             " by Regulation (EU) 2026/1744 and does not appear in this OJ text. It is"
             " reproduced in `../32026R1744/`."],
        blocks(div_by_id(act, "art_111")) + blocks(div_by_id(act, "art_113")),
    )

    # 5 ── The interpretive recitals.
    rec: list[str] = []
    for n in range(132, 138):
        rec += blocks(div_by_id(act, f"rct_{n}"))
    write(
        out / "32024R1689" / "recitals-132-137.md",
        "Recitals 132–137 — the Article 50 recital block",
        [OJ, "Recitals are interpretive, not operative: they explain how the Article is"
             " meant to be read and may not be cited as the obligation itself. Recital 137"
             " is the reason this auditor refuses to call an artifact 'lawful'."],
        rec,
    )

    # 6 ── What the Digital Omnibus actually changed.
    omni_blocks = blocks(omni)
    amend: list[str] = []
    amend += ["## Recital 38 — why the transitional period exists"]
    amend += blocks(div_by_id(omni, "rct_38"))
    amend += ["## Recital 41 — removal of the implementing-act empowerment in Article 50(7)"]
    amend += blocks(div_by_id(omni, "rct_41"))
    amend += ["## Article 1(20) — Article 50(7) replaced"]
    amend += between(omni_blocks, r"^\(20\) in Article 50, paragraph 7 is replaced", r"^‘7\. The Commission shall encourage")
    amend += ["## Article 1(39) — Article 111(4) added (the transitional window)"]
    amend += between(omni_blocks, r"^\(39\) Article 111 is amended as follows", r"by 2 December 2026")
    write(
        out / "32026R1744" / "amendments-to-article-50-and-111.md",
        "Regulation (EU) 2026/1744 — what the Digital Omnibus changed for Article 50",
        [OMNI, "**In force 27 July 2026.** Article 50(1)–(6) were left untouched. Only"
                " paragraph 7 was replaced, and a transitional window for 50(2) was added"
                " as Article 111(4). An auditor working from the 2024 text alone gets the"
                " deadline wrong."],
        amend,
    )

    # 7 ── The consolidated cross-check.
    write(
        out / "02024R1689-20260727" / "article-50-consolidated.md",
        "Article 50 — consolidated text as at 27 July 2026",
        [CONS, CONS_DISCLAIMER],
        blocks_consolidated(div_by_id(cons, "art_50")),
    )

    print("\ndone. next:  python3 _verify/verify_references.py --write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
