# Article 50 audit — <ARTIFACT NAME>

<!--
  TEMPLATE. Copy this file, fill it in, delete these comments.
  The ```audit and ```finding blocks are parsed by tools/verify_citations.py.
  Prose outside them is for the reader and is not parsed — put your reasoning
  there, not inside the blocks.

  Rules that will fail verification if you break them:
    · one ```finding block per obligation in provisions/article-50.provisions.json
    · exactly one, no more, no fewer — eleven blocks
    · `quote` must appear byte-for-byte at `cite`, in an authentic OJ text
    · `severity` must be what the matrix in rules.md produces
    · FAIL / PARTIAL / PASS need `evidence`; INSUFFICIENT_EVIDENCE needs
      `evidence_needed`; NOT_APPLICABLE needs `basis`
    · every finding needs `provenance`, and the header `trust` line must match
    · a `transitional` finding must name 2 December 2026
-->

```audit
artifact: <name, and the URL or path of what was audited>
artifact_version: <commit, release or retrieval date of the artifact>
audited_on: <YYYY-MM-DD>
auditor: EU AI Act Article 50 Auditor
register_version: 1.0.0
reference_fingerprint: f8a28ecc3811b9dc
scope: Article 50 of Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. Nothing else.
trust: observed=0 inferred=0 declared=0 none=0   # recomputed and checked by verify_citations.py
```

## What was audited

<One paragraph: what the artifact is, which surfaces were examined, and what
was supplied in the evidence pack. Name what was NOT supplied — the reader
needs to know where the audit was working blind.>

## Scoping determination

| Question | Answer | Source in the evidence pack |
|---|---|---|
| Provider, deployer, or both? | | |
| Which output modalities are generated? | | |
| Available to persons in the EU? | | |
| Placed on the market / put into service on | | |
| Emotion recognition or biometric categorisation present? | | |
| Law-enforcement authorisation claimed? | | |
| SME / SMC? | | |

<Every row must come from the evidence pack. A row the pack does not answer is
recorded as "not stated" and forces INSUFFICIENT_EVIDENCE on every obligation
that turns on it. The auditor does not fill these in from inference.>

## Summary

| Verdict | Count |
|---|---|
| PASS | |
| FAIL | |
| PARTIAL | |
| NOT_APPLICABLE | |
| INSUFFICIENT_EVIDENCE | |
| NOTED | |

| Severity | Count |
|---|---|
| CRITICAL | |
| MAJOR | |
| MINOR | |
| UNRESOLVED | |
| OBSERVATION | |

<Two or three sentences. The bottom line, then the single most important thing
to fix. No adjectives that the findings do not support.>

---

## Findings

### F-01 · <provision id> · <VERDICT>

<Prose: what the provision requires, what the artifact does, and why that is or
is not compliance. Reason about the exemptions explicitly — name the ones you
tested and rejected, not only the one you applied.>

```finding
id: F-01
provision: EUAIA-50-1
verdict: PASS
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed        # observed | inferred | declared | none (NOTED only)
cite: reference/32024R1689/article-50.md:L14
quote: <the words of the provision, byte for byte>
evidence: <path or URL, with a line or selector>
evidence_quote: <what the artifact actually says or does>
finding: <one sentence stating the determination>
remediation: <what would make it pass, in the provision's own terms; omit for PASS>
```

<Repeat for all eleven obligations.>

---

## Attestation

| | |
|---|---|
| Standard | Regulation (EU) 2024/1689, Article 50, as amended by Regulation (EU) 2026/1744 |
| Reference fingerprint | `f8a28ecc3811b9dc` |
| Register version | 1.0.0 |
| Citations verified | `python3 tools/verify_citations.py <this file>` |

**Scope limits.** This audit covers Article 50 and nothing else. Article 50(6)
provides that paragraphs 1 to 4 do not affect the requirements of Chapter III and
are without prejudice to other transparency obligations in Union or national law.
Recital 137 provides that compliance with these transparency obligations is not to
be interpreted as indicating that the use of the system or its output is lawful.

**This is not legal advice** and not a conformity assessment. It is a documented
comparison of an artifact against a published text, produced so that every
statement in it can be checked against that text.
