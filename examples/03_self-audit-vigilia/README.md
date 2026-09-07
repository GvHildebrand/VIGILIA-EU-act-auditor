# Example 03 — a self-audit of Vigilia

Not a fixture. **Vigilia is the product this auditor's methodology came out of** —
a live service at [aivigilia.com](https://aivigilia.com) that sells EU AI Act
audits for €499, run by the same person who wrote this repository.

So it gets audited by its own auditor, in public, and it did not come out clean.

**Run twice.** The first run, 2026-09-03, returned one MAJOR and one MINOR. The
operator shipped a fix and the audit was re-run on 2026-09-06. The MAJOR is now a
PASS. Both states are kept — the superseded capture is preserved in the evidence
pack, and the finding carries its own history — because a remediation you cannot
check against what it replaced is a claim, not a record.

| | First run, 2026-09-03 | Re-run, 2026-09-06 |
|---|---|---|
| **F-08** · disclosure at the point of interaction on the free checker | PARTIAL · **MAJOR** | **PASS** — disclosure now sits above the submit control and repeats on the snapshot, in five languages |
| **F-02** · machine-readable marking of synthetic content | FAIL · **MINOR** | **FAIL · MINOR, still open** — inside the Article 111(4) window until 2 December 2026 |
| PASS | three | four |

There is an obvious reason not to publish this: it is a list of ways a commercial
product falls short, written by its own operator, on the internet, permanently.

It is here anyway, because an auditor whose only worked examples are invented
companies that behave exactly as the auditor expects has demonstrated nothing.
The interesting question about any audit tool is what it says when the answer is
inconvenient — and then whether anything changes because it said it.

Evidence was captured from the live site on 2026-09-06, with the 2026-09-03
capture preserved beneath it, and is reproduced in `evidence-pack/` so the
findings can be checked without trusting this summary.
The audit covers **public surfaces only** — the authenticated €499 workspace was
not examined, and the report says so.

```bash
python3 _verify/verify_citations.py examples/03_self-audit-vigilia/audit-report.md
```
