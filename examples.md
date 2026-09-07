# Examples

Three worked audits. All three are in [`examples/`](examples/) with the evidence
they ran on, and all three pass `_verify/verify_citations.py` — every quote below is
checked byte for byte against the Regulation before this repository is committed.

```
$ python3 _verify/verify_citations.py --all
verifying citations  register 1.0.0 · reference 3fa2319d6595d47a
  ok  examples/01_fixture-saas-chatbot/audit-report.md
      11 findings, all 11 obligations covered
      NOTED 2  NOT_APPLICABLE 4  PARTIAL 1  PASS 4
  ok  examples/02_fixture-image-generator/audit-report.md
      11 findings, all 11 obligations covered
      FAIL 1  NOTED 2  NOT_APPLICABLE 8
  ok  examples/03_self-audit-vigilia/audit-report.md
      11 findings, all 11 obligations covered
      FAIL 1  NOTED 2  NOT_APPLICABLE 4  PARTIAL 1  PASS 3

all reports verified  every quote checked against the authentic text
```

Start with [**00 — how it actually runs**](examples/00_how-it-runs.md): the folder
doing the work with no tool involved, and the same finding checked by hand with
one `grep`.

| | Artifact | What it demonstrates |
|---|---|---|
| [01](examples/01_fixture-saas-chatbot/) | Support chatbot (fixture) | A mostly-compliant artifact, and why a **qualified** duty caps at MINOR |
| [02](examples/02_fixture-image-generator/) | Image generator (fixture) | A **dated** applicability rule, and an exemption that is genuinely satisfied |
| [03](examples/03_self-audit-vigilia/) | **Vigilia — live, real, ours** | What the auditor says when the answer is inconvenient |

---

## 01 — A PASS is a finding

Most audit tools list problems. An audit says what you comply with, and shows the
evidence for that too.

> ### F-01 · Article 50(1) · PASS
>
> ```finding
> id: F-01
> provision: EUAIA-50-1
> verdict: PASS
> severity: NONE
> duty_force: absolute
> applicability: in_force
> cite: reference/32024R1689/article-50.md:L14
> quote: Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system
> evidence: examples/01_fixture-saas-chatbot/evidence-pack/first-interaction/chat-widget.html:L11
> evidence_quote: You are chatting with Aria, an AI assistant. Aria is an automated system, not a member of the Northwind support team.
> finding: The first message in the thread informs the user they are interacting with an AI system, so the obligation is met without reliance on any exemption.
> ```

Open `reference/32024R1689/article-50.md`, go to line 14, and the quote is there.
That is the whole idea.

### And a qualified duty cannot be inflated

The second sentence of Article 50(2) qualifies itself — "as far as this is
technically feasible". Northwind's marking works in the transcript export but does
not survive a user copying text out of the chat window, which for a text-generating
system is the ordinary path. That is a real defect. It is still MINOR:

> ```finding
> id: F-03
> provision: EUAIA-50-2-QUALITY
> verdict: PARTIAL
> severity: MINOR
> duty_force: qualified
> applicability: in_force
> ```

Not because the auditor is being generous. Because the matrix in
[`rules.md`](rules.md) returns MINOR for `(qualified, PARTIAL, in_force)`, and the
verifier rejects any other value.

---

## 02 — Severity is computed from the date, not from indignation

PixelForge generates images and marks nothing at all. No C2PA claim, no IPTC
digital source type, no watermark. On its face, a total failure of Article 50(2).

It scores **MINOR**.

> ### F-02 · Article 50(2), first sentence · FAIL · MINOR
>
> ```finding
> id: F-02
> provision: EUAIA-50-2-MARK
> verdict: FAIL
> severity: MINOR
> duty_force: absolute
> applicability: transitional
> cite: reference/32024R1689/article-50.md:L16
> quote: Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated.
> evidence: examples/02_fixture-image-generator/evidence-pack/outputs/sample-portrait-metadata.txt:L11-L15
> evidence_quote: $ c2patool sample-portrait.png → No claim found. · $ exiftool -XMP-iptcExt:DigitalSourceType → (no output — tag not present)
> ```

Because PixelForge was placed on the market on 15 January 2026 — before 2 August
2026 — **Article 111(4)** gives it until **2 December 2026**:

> "Providers of AI systems, including general-purpose AI systems, generating
> synthetic audio, image, video or text content, that have been placed on the
> market before 2 August 2026 shall take the necessary steps in order to comply
> with Article 50(2) by 2 December 2026."
>
> — `reference/32026R1744/amendments-to-article-50-and-111.md:L34`

**That paragraph does not exist in the 2024 Official Journal text.** It was added
by Regulation (EU) 2026/1744, in force 27 July 2026. An auditor working from the
AI Act as published — which is what you get from most blog posts, most PDFs, and
most language models — cannot reach this answer.

On 2 December 2026 the same evidence returns **CRITICAL**, with no change to the
auditor, the register or the artifact.

### An exemption that actually applies

PixelForge never says "you are interacting with an AI system". It does not have to:

> ```finding
> id: F-01
> provision: EUAIA-50-1
> verdict: NOT_APPLICABLE
> severity: NONE
> basis: EUAIA-50-1-X1
> quote: Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system
> evidence_quote: H1: AI image generation for teams · Sub-head: Describe what you want. Our AI model draws it in seconds. · Button: Generate with AI
> ```

`NOT_APPLICABLE` with the exemption named — **not** `PASS`. PASS would assert that
a duty was discharged. PixelForge discharged nothing; it is relying on the
"obvious to a reasonably well-informed, observant and circumspect person"
carve-out, and a rebrand around a named persona would take that away with no
disclosure to fall back on. The report says so.

---

## 03 — The self-audit

[Vigilia](https://aivigilia.com) is a live service that sells EU AI Act audits for
€499. It is operated by the person who wrote this repository. It gets audited here
by its own auditor, and it does not come out clean.

**MAJOR, found on 2026-09-03 and remediated on 2026-09-06** — the free compliance
checker generated AI prose about the visitor's regulatory exposure, and nothing at
that surface said an AI produced it. This is the finding as it stood at the first
run; it is now a PASS, and the superseded evidence is kept in the pack:

> ```finding
> id: F-08
> provision: EUAIA-50-5-MANNER
> verdict: PARTIAL
> severity: MAJOR
> duty_force: absolute
> applicability: in_force
> cite: reference/32024R1689/article-50.md:L24
> quote: The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure.
> evidence: examples/03_self-audit-vigilia/evidence-pack/first-interaction/checker-surface.md:L27-L33
> finding: The disclosure is delivered at first exposure on the dispatch pages but not on the free compliance checker, where the only AI disclosure is a site footer encountered after the interaction.
> ```

**MINOR, still open** — no machine-readable mark on any output, inside the
Article 111(4) window until 2 December 2026. Vigilia's structured data names an `Organization` as
author, which tells a machine *who published*, not *that the text is synthetic*.

The instructive part is that Vigilia's human-facing disclosure is genuinely
excellent — byline above the headline, colophon, footer, `llms.txt`, a public
compliance countdown — and **none of it discharges Article 50(2)**, which is a duty
owed to machines. Strong disclosure practice and machine-readable marking are
different obligations, and one does not buy the other.

### What the auditor found on the way past

The report also carries a section headed *Matters noted outside the scope of this
audit*. The dispatch used as the evidence artifact states that Article 50 imposes
obligations on providers of general-purpose AI **models**, that those include
training-data documentation, and that the penalty is 1 % of global turnover.

All three are wrong, and `reference/` contradicts each of them: those are Article
53 and 55 obligations, and Article 99(4)(g) puts Article 50 in the €15 000 000 /
3 % tier. The 1 % figure is Article 99(5), a different infringement.

It is recorded as an out-of-scope observation with no verdict and no severity —
an auditor reports what it walked past, and does not smuggle it into findings
under a provision it does not belong to.

That error is the reason this repository is built the way it is. It is a summary of
a standard, written by an AI, drifting from the standard, published on the site of
a company that audits that standard for a living, with nothing in the pipeline able
to catch it. Nothing in the eleven findings above could have made that mistake and
survived, because every one of them quotes the provision it relies on and a script
checks the quote against the authentic text.

---

## Run them yourself

```bash
python3 _verify/verify_references.py          # the standard is intact
python3 _verify/verify_citations.py --all     # the reports quote it correctly
```

Then try to break one — change a quote, drop a finding, downgrade a severity, cite
the consolidated text instead of the Official Journal. The verifier names what you
did. There is a transcript of exactly that in [`README.md`](README.md).
