# Quickstart — a real audit in five minutes

**Nine of the eleven obligations can be ruled from one paste and six answers.**
The other two are about machine-readable marking, and they need one command run
against a real generated file. This page gets you the nine now and the last two
in another two minutes.

## 1. Load the auditor

**Claude project:** upload this folder.
**Claude Code:** clone it and open the directory — `CLAUDE.md` does the rest.

## 2. Paste this, filled in

```
Audit this against Article 50. Follow rules.md, and give every obligation in the
register a verdict.

WHAT A USER MEETS FIRST
<Paste what a person actually encounters before they have done anything: your
chatbot's opening message, your landing copy above the fold in rendered order,
your voice agent's first line, the byline area of a published page.
Paste the HTML if you have it — whether a disclosure is real text or a styled
image decides the accessibility limb of Article 50(5), and you cannot tell from
plain text.>

SIX FACTS
1. Provider, deployer, or both?
   → (Provider = you develop it and put it on the market or into service under
      your own name, including for your own use. Deployer = you use it under your
      authority. Many operators are both.)
2. What does it generate?
   → (text / image / audio / video / nothing)
3. Available to people in the EU?
   →
4. Date placed on the market or put into service?
   → (Before 2 August 2026 changes the deadline. Give the date, not "a while ago".)
5. Does anything infer emotional state, or categorise people by biometric data?
   →
6. Is generated text published to inform the public on matters of public interest?
   → (Both limbs. A company blog on your industry usually qualifies; a support
      reply does not.)
   If yes, who holds editorial responsibility for it?
   →

I have NOT supplied a metadata dump of generated output.
```

**Keep that last line.** It is what stops the auditor guessing at Article 50(2).
You will get `INSUFFICIENT_EVIDENCE` for two obligations instead of a verdict, and
that is the correct answer — whether your output carries a machine-readable mark
is a property of the file, not of anything visible on a screen. A tool that ruled
on it from a screenshot would be making it up.

## 3. What you get

| | |
|---|---|
| **9 obligations ruled** | 50(1) disclosure · 50(3) emotion and biometric, both limbs · 50(4) deep fakes · 50(4) public-interest text · 50(5) manner and accessibility · 50(6) and 50(7) as scoping observations |
| **2 unresolved** | 50(2) marking and its quality — `INSUFFICIENT_EVIDENCE`, with a note saying exactly what would settle them |

Every one of the nine arrives with the provision quoted verbatim, cited to a line
in `reference/`, pointed at your evidence, and carrying a severity computed from
the matrix in [`rules.md`](rules.md) rather than from an opinion.

## 4. Close the last two

Generate one real output per modality, run whichever applies, and paste exactly
what it prints — including empty output and "no claim found". Absence is the
evidence.

```bash
c2patool sample.png                                   # content credentials
exiftool -XMP-iptcExt:DigitalSourceType sample.png    # IPTC digital source type
exiftool -a -G1 -s sample.png                         # everything embedded
curl -sSI https://your.api/endpoint                   # response headers
```

For generated **text**: the structured data on the rendered page, the API response
envelope, and its headers.

Watch for the near-miss. `"author": {"@type": "Organization"}` marks *who
published*. A machine reading it learns nothing about whether the text was
artificially generated, which is what Article 50(2) actually asks. That exact
mistake is [finding F-02 in the self-audit](examples/03_self-audit-vigilia/audit-report.md).

## 5. Check what came back

```bash
python3 _verify/verify_citations.py path/to/audit-report.md
```

This is the part that makes the report worth anything. It fails if a provision was
invented, a quote does not appear byte-for-byte at the line it cites, an obligation
was skipped, or a severity is not what the matrix produces. **A report that does
not pass is not finished.**

It does **not** check whether a verdict is legally right. Nothing can — see
[what this does not guarantee](README.md#what-this-does-not-guarantee).

---

## Auditing a whole codebase instead

```bash
make audit-repo REPO=/path/to/your/product
```

Reads the repository and writes an evidence pack with the machine-knowable rows
filled in and cited to `file:line` — model-provider calls, generation calls by
modality, provenance-marking libraries, candidate disclosure strings. Everything
else it marks **NOT ESTABLISHED**, because provider-versus-deployer, EU
availability and the market-placement date decide verdicts, and a scanner that
invented them would be the exact failure this repository exists to prevent.

Complete those rows, then come back to step 2.

---

## Before you rely on any of it

```bash
make freshness
```

Asks the EU whether the Act has been amended since `reference/` was pinned. A
standard that is intact but superseded is exactly as wrong as one that was edited.
