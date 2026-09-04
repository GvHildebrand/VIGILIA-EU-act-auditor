# Example 03 — a self-audit of Vigilia

Not a fixture. **Vigilia is the product this auditor's methodology came out of** —
a live service at [aivigilia.com](https://aivigilia.com) that sells EU AI Act
audits for €499, run by the same person who wrote this repository.

So it gets audited by its own auditor, in public, and it does not come out clean.

| | |
|---|---|
| One **MAJOR** | the free compliance checker generates AI text with no disclosure at the point of interaction |
| One **MINOR** | no machine-readable marking of synthetic content anywhere — inside the Article 111(4) window until 2 December 2026 |
| Three PASS | the dispatch byline, the disclosure route under 50(4), the accessibility of the disclosure |

There is an obvious reason not to publish this: it is a list of ways a commercial
product falls short, written by its own operator, on the internet, permanently.

It is here anyway, because an auditor whose only worked examples are invented
companies that behave exactly as the auditor expects has demonstrated nothing.
The interesting question about any audit tool is what it says when the answer is
inconvenient.

Evidence was captured from the live site on 2026-09-03 and is reproduced in
`evidence-pack/` so the findings can be checked without trusting this summary.
The audit covers **public surfaces only** — the authenticated €499 workspace was
not examined, and the report says so.

```bash
python3 tools/verify_citations.py examples/03_self-audit-vigilia/audit-report.md
```
