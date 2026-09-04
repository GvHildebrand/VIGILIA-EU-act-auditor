# VIGILIA-EU-act-auditor

**An auditor for Article 50 of the EU AI Act.**

**Drop this folder into a Claude project. Claude becomes an auditor that checks
your AI product's disclosures against Article 50 of the EU AI Act — and every
finding it writes can be verified against the law by a script.**

Article 50 has been in force since **2 August 2026**. Infringements sit in the
€15 000 000 / 3 % penalty tier under Article 99(4)(g). One duty inside it —
machine-readable marking of synthetic content — falls due for systems already on
the market on **2 December 2026**.

**Start here → [QUICKSTART.md](QUICKSTART.md)** — nine of the eleven obligations
ruled from one paste and six answers, in five minutes.

![How a finding is checked against the law](docs/how-it-checks.svg)

---

## The problem this is actually solving

Ask any capable language model what Article 50 of the EU AI Act requires. You will
get a confident, fluent, well-organised answer. Some of it will be wrong, and
nothing in the answer will tell you which part.

That is not hypothetical. This repository's own example 03 audits
[Vigilia](https://aivigilia.com), a live service that **sells EU AI Act audits**,
and finds a published article on its site stating that Article 50 obligations
"include public documentation of training data characteristics" and that the
penalty is "1% of global annual turnover". Both are wrong — those are Article 53
obligations, and Article 99(4)(g) sets the Article 50 tier at €15 000 000 or 3 %.
The same repository the auditor came out of also seeds its database with a maximum
fine of "€30M or 6%", which was the figure in the 2021 *draft* proposal.

Nobody was careless. A summary of a standard drifted from the standard, and there
was no step in the pipeline that could notice.

So this auditor is built the other way round. **It has no opinions about the AI
Act.** It has the AI Act, in the folder, hashed, re-fetchable, and every finding it
writes quotes the provision it relies on and cites the line. Then a script checks
each quote against the text, byte for byte, and fails the report if anything was
invented, misquoted, or quietly skipped.

You do not have to trust the auditor. That is the point.

---

## What this does not guarantee

The checks above are deterministic. Everything in this section is not, and no
script can make it so.

**The verdict itself.** The scripts check *form*, not *truth*. Article 50(1) turns
on whether your AI nature is "obvious from the point of view of a natural person
who is reasonably well-informed, observant and circumspect" — a legal standard a
court applies, not a fact you can look up. What you get is an argued position with
the provision attached, not the answer.

**Garbage in.** If your evidence pack says you are a deployer and you are actually
a provider, you get a confidently wrong report that passes every check. The
verifier cannot know your inputs are false.

**Repeatability.** Run the auditor twice and the judgement-heavy obligations can
come out differently, and *both runs pass citation verification*. That is why the
examples ship with pinned verdicts — not to make the model deterministic, which is
impossible, but so the disagreement is visible instead of silent.

**Staleness.** `reference/` is pinned to a date. `make freshness` is how you find
out it has moved; nothing checks automatically.

**What it cannot stop is an operator lying to it** — so it does the next best
thing and says how exposed it is. Every finding records whether its evidence was
`observed` (the auditor saw the artifact), `inferred` (derived from code, an
archive, a register) or `declared` (the operator's word). Every report totals them
and states how many verdicts would collapse if the operator were lying. The
verifier recomputes the totals and fails a report that understates them.

The four shipped examples make the spectrum concrete: a cooperative operator with
a supplied pack lands at `declared=5`, the self-audit of a live public site at
`declared=0`, and an audit of a third-party product nobody can reach at
`observed=0` — where every substantive verdict is `INSUFFICIENT_EVIDENCE`, because
that is the honest answer.

So the claim is not that the output is right. It is that the output is
**checkable** — the provision is named, the quote is real, nothing was skipped,
and the parts that need a human are marked as needing one instead of buried in
fluent prose. That is a smaller claim than most compliance tooling makes, and it
is the only one this repository can keep.

---

## The standard, in `reference/`

Not a summary. Not a link. The legislation.

| File | What |
|---|---|
| `reference/32024R1689/article-50.md` | **Article 50, all seven paragraphs**, verbatim |
| `reference/32024R1689/article-3-definitions.md` | The ten defined terms the obligations turn on |
| `reference/32024R1689/article-99-penalties.md` | Article 99 — where severity is anchored |
| `reference/32024R1689/article-111-113-application.md` | Application dates and transitional provisions |
| `reference/32024R1689/recitals-132-137.md` | The Article 50 recital block |
| `reference/32026R1744/amendments-to-article-50-and-111.md` | **What the Digital Omnibus changed**, verbatim |
| `reference/02024R1689-20260727/article-50-consolidated.md` | The consolidated text, for cross-checking only |
| `reference/_source/*.xhtml` | The three raw documents everything was extracted from |

Retrieved from the **EU Publications Office**, not from a blog:

```bash
bash reference/fetch-sources.sh          # re-fetch from publications.europa.eu
python3 tools/extract_reference.py       # rebuild every provision file
git diff --stat reference/               # empty means byte-identical to the EU's text
```

Provenance, authenticity and SHA-256 for every file are in
[`reference/MANIFEST.md`](reference/MANIFEST.md).

### Most Article 50 material you will find today is out of date

Regulation (EU) 2024/1689 was amended by **Regulation (EU) 2026/1744**, the Digital
Omnibus on AI, in force **27 July 2026**. Two things changed for Article 50, and one
of them changes deadlines:

- **Article 50(7)** was replaced.
- **Article 111(4)** was added: providers of synthetic-content-generating systems
  **placed on the market before 2 August 2026** must comply with **Article 50(2) by
  2 December 2026**.

Article 111(4) is not in the 2024 Official Journal text. An auditor working from
that text alone will tell you a system is in breach today when the Regulation gives
it until December — or will miss the deadline entirely.

Rather than ask you to take that on trust, `tools/verify_references.py` compares the
Official Journal Article 50 against the EU's own consolidated version:

```
ok  cross-check — 9 of 10 Article 50 blocks byte-identical to the consolidated
    text; only paragraph 7 differs
ok  markers — ▼M1 sits on paragraph 7 and nowhere else
```

That is the EU's consolidation confirming, with no human in the loop, exactly what
the amendment did and did not touch.

---

## Use it

[QUICKSTART.md](QUICKSTART.md) is the fastest path. The full route:

### In a Claude project

Upload this folder. Then:

> Audit my product against Article 50. Here is the evidence pack: [attach].

Claude reads `identity.md`, follows `rules.md`, works through the eleven
obligations in `provisions/article-50.provisions.json`, and writes a report using
`templates/audit-report.md`.

### In Claude Code

Clone it and open the directory — `CLAUDE.md` points at the same files. Then verify
what came back:

```bash
python3 tools/verify_citations.py path/to/audit-report.md
```

### What to feed it — the evidence pack

Copy [`templates/evidence-pack/`](templates/evidence-pack/) and fill in four things.
The auditor will not guess any of them; a gap becomes `INSUFFICIENT_EVIDENCE` with a
note saying what would resolve it.

| | |
|---|---|
| **`system-facts.md`** | Provider or deployer? Which modalities? EU availability? **Date placed on the market** — this one decides the 2 December 2026 question. Emotion recognition or biometric categorisation? Law-enforcement authorisation? SME/SMC? |
| **`first-interaction/`** | What a person meets first: chat opener, landing copy, voice script, screenshots. |
| **`outputs/`** | Sample generated output **plus a metadata dump** — `c2patool`, `exiftool -XMP-iptcExt:DigitalSourceType`, watermark detector, response headers. Without this, Article 50(2) cannot be evidenced at all: whether output is "marked in a machine-readable format" is not visible on a screen. |
| **`documents/`** | Terms, privacy policy, product docs, any published disclosure. |

---

## What comes back

Eleven findings, one per obligation — including the ones that pass and the ones
that do not apply. Each finding names the provision, quotes it verbatim, cites the
line, points at the evidence, and carries a severity computed from a published
matrix.

```finding
id: F-02
provision: EUAIA-50-2-MARK
verdict: FAIL
severity: MINOR
duty_force: absolute
applicability: transitional
cite: reference/32024R1689/article-50.md:L16
quote: Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated.
evidence: examples/02_fixture-image-generator/evidence-pack/outputs/sample-portrait-metadata.txt:L11-L15
evidence_quote: $ c2patool sample-portrait.png → No claim found.
finding: Generated images carry no machine-readable provenance mark of any kind, so Article 50(2) is not met; the artifact is inside the Article 111(4) transitional window and owes compliance by 2 December 2026.
remediation: Embed a C2PA manifest at generation time and set XMP-iptcExt:DigitalSourceType to trainedAlgorithmicMedia on every export, before 2 December 2026.
```

**Severity is computed, not felt.** Three inputs, each from the standard: the
penalty tier (Article 99(4)(g) — constant across Article 50), the duty's own force
(`shall` versus "as far as technically feasible"), and whether it is in force,
transitional, or not yet applicable. The matrix is printed in
[`rules.md`](rules.md), so you can recompute any severity by hand — and the verifier
recomputes all of them.

Two results fall out that an opinion-driven tool would get wrong: a **qualified**
duty can never be CRITICAL, and a defect inside a **transitional** window is MINOR
until the window closes, at which point the same evidence returns CRITICAL.

---

## Verify it

```bash
make verify
```

**`tools/verify_references.py`** — every file in `reference/` matches its recorded
SHA-256, and Article 50 in the Official Journal still agrees with the EU's
consolidated version everywhere except paragraph 7.

**`tools/verify_citations.py`** — for a report: every cited provision exists; every
quote appears **byte-for-byte** at the line it cites, in the authentic Official
Journal text; **every obligation in the register appears exactly once**, so nothing
was skipped; severity is recomputed from the matrix and must match; findings of
breach point at real evidence; `INSUFFICIENT_EVIDENCE` says what would resolve it;
`NOT_APPLICABLE` names a failed trigger or a satisfied exemption.

**`tools/verify_pins.py`** — the verdicts of the three shipped examples are
pinned. If the register changes, or somebody re-runs the auditor and it reaches a
different conclusion, the diff shows up as a failing check instead of passing
silently.

Python 3.9+, standard library only. No install, no dependencies, and `make
verify` never touches the network — an auditor you can only check when the EU is
reachable is a worse auditor.

Two commands that *do* need network, deliberately kept out of `make verify`:

```bash
make freshness                      # has the law been amended since reference/ was pinned?
make audit-repo REPO=../my-product  # scan a codebase into a half-filled evidence pack
```

`make freshness` asks the EU Publications Office SPARQL endpoint for every
consolidated version of the Act that exists and compares the newest against what
this repository pins, then re-fetches the three source documents and re-hashes
them. `verify` proves `reference/` is unaltered; `freshness` asks the different
question of whether it is still *current*. A standard that is intact but
superseded is exactly as wrong as one that was edited.

`make audit-repo` reads your codebase and writes an **estate inventory** — every
directory that calls a model or declares an agent, with its modalities, whether
any marking code exists, and whether it renders UI — plus an evidence pack with
the rows a machine can honestly fill — model-provider calls, generation calls by modality,
provenance-marking libraries, candidate disclosure strings, all cited to
`file:line` — and marks every remaining row **NOT ESTABLISHED**. It refuses to
guess provider-versus-deployer, EU availability, or the market-placement date,
because those decide verdicts and a scanner that invented them would be the exact
failure this repository exists to prevent.

### Try to break it

Take a passing report, doctor five things, and run it:

```
$ python3 tools/verify_citations.py /tmp/tamper.md
verifying citations  register 1.0.0 · reference f8a28ecc3811b9dc
  FAIL  /tmp/tamper.md
      - F-01: QUOTE NOT FOUND at reference/32024R1689/article-50.md:L14
        claimed: Providers shall ensure that all AI systems intended to interact directly…
      - F-03: severity 'OBSERVATION' is not what the matrix produces for
        (qualified, PARTIAL, in_force) → 'MINOR'
      - F-04: evidence '…/evidence-pack/audit-log.md:L15' does not resolve to a file
        in this repository
      - F-08: cites reference/02024R1689-20260727/article-50-consolidated.md, which is
        not an authentic OJ text. The consolidated text has no legal effect
      - OBLIGATION NOT AUDITED: EUAIA-50-4-TEXT (Disclose AI-generated text published
        to inform the public on matters of public interest)

1 report(s) failed verification
```

One inserted word, one softened severity, one fabricated evidence path, one
non-authentic citation, one deleted obligation. All five named.

**What this does not do.** It does not check whether a verdict is legally correct.
No script can, and a tool claiming otherwise would be the problem again in a new
costume. It checks that no provision was invented, no quote fabricated, no
obligation skipped, and no severity hand-waved. That is the floor. Above it, you
still need judgement — but you can now see exactly what the judgement was applied to.

---

## What is in here

| | |
|---|---|
| [`identity.md`](identity.md) | Who the auditor is, what it refuses to do |
| [`rules.md`](rules.md) | The procedure, in order, with the severity matrix |
| [`examples.md`](examples.md) | Three worked audits, findings with citations |
| [`reference/`](reference/) | **The standard itself**, verbatim, hashed, re-fetchable |
| [`README.md`](README.md) | This file |
| [`QUICKSTART.md`](QUICKSTART.md) | The five-minute path, and what it cannot answer without a metadata dump |
| [`provisions/`](provisions/) | The eleven obligations, machine-readable — what makes verification possible |
| [`examples/`](examples/) | The reports, and the evidence they ran on |
| [`templates/`](templates/) | The evidence pack to fill in, and the report shape |
| [`tools/`](tools/) | Fetch, extract, verify, check freshness, scan a codebase. Standard library only. |

Four worked audits: a support chatbot ([01](examples/01_fixture-saas-chatbot/)),
an image generator ([02](examples/02_fixture-image-generator/)), a self-audit of a
live commercial service ([03](examples/03_self-audit-vigilia/)) that finds a MAJOR
and a MINOR in its own author's product, and Spotify's AI DJ
([04](examples/04_spotify-ai-dj/)), audited from the public record alone — which
establishes a deep-fake trigger and a 2 December 2026 deadline, and returns
INSUFFICIENT_EVIDENCE for everything that lives inside the app.

---

## Scope, honestly

**Article 50 only.** Not Chapter III high-risk requirements, not the Article 5
prohibitions, not the GPAI obligations in Chapter V, not the GDPR. Article 50(6)
says paragraphs 1 to 4 do not affect Chapter III and are without prejudice to other
Union and national transparency obligations, and recital 137 says compliance with
Article 50 does not make a system or its output lawful. The auditor repeats both on
every report.

**Not legal advice.** Not a conformity assessment. Not a certification. A
documented comparison of an artifact against a published text.

**Article 50(5)'s "applicable accessibility requirements"** point to instruments
not shipped here. The auditor determines whether a disclosure is perceivable and
refers conformance onward, rather than ruling against a standard it cannot quote.

---

## Who made this

Built by **Gregorio von Hildebrand** as the open methodology behind
[Vigilia](https://aivigilia.com)'s Article 50 audit — which is why example 03 is a
self-audit rather than a case study about someone else. If a compliance methodology
cannot survive being pointed at its own author, it is not a methodology.

Vigilia sells the full thing: multi-framework gap analysis across the whole AI Act,
an agent-graph inventory, and a report you can hand a regulator. This folder is the
Article 50 core of it, with the reasoning exposed.

## Licence and reuse

The auditor — prompts, rules, register, scripts, examples — is **MIT**, see
[`LICENSE`](LICENSE).

The legislation in `reference/` is not ours to license. It is reproduced under
**Commission Decision 2011/833/EU** on the reuse of Commission documents, with the
source acknowledged: **© European Union, https://eur-lex.europa.eu**. Only the
Official Journal published in electronic form is authentic — Council Regulation
(EU) No 216/2013, Article 1(2). Full terms in
[`reference/MANIFEST.md`](reference/MANIFEST.md).

This repository is not affiliated with, endorsed by, or speaking for the European
Union or any of its institutions.
