# How it actually runs

The claim in the README is that **the auditor is the folder** — that `identity.md`,
`rules.md`, `provisions/article-50.md` and `reference/` do the work, and `_verify/`
only checks it afterwards.

This is that claim, shown rather than asserted. Nothing below runs any tool. The
verification at the end is a separate act, and it happens *after* the audit already
exists.

---

## 1. What is loaded

Drop the folder into a Claude project, or open it in Claude Code. `CLAUDE.md`
points at four files and stops:

```
identity.md                 who you are, what you refuse to do
rules.md                    the procedure, in order, and the severity matrix
provisions/article-50.md    the eleven obligations
reference/                  the law — your only source of law
```

No tool has run. No script has been invoked. There is nothing to install.

## 2. What is said

```
Audit this against Article 50. Follow rules.md, and give every obligation in the
register a verdict.

WHAT A USER MEETS FIRST
  [the opening message of a support chatbot, pasted as rendered HTML]

SIX FACTS
1. Provider, deployer, or both?      → Provider
2. What does it generate?            → Text only
3. Available to people in the EU?    → Yes
4. Date placed on the market?        → 2026-08-20
5. Emotion or biometric?             → Neither
6. Public-interest text published?   → No

I have NOT supplied a metadata dump of generated output.
```

## 3. What comes back

The auditor works `rules.md` in order — scope, then applicability per obligation,
then evidence, then verdict, then severity, then citation form. For each of the
eleven it produces a block like this one, taken verbatim from
[`01_fixture-saas-chatbot/audit-report.md`](01_fixture-saas-chatbot/audit-report.md):

```finding
id: F-01
provision: EUAIA-50-1
verdict: PASS
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L14
quote: Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system
evidence: examples/01_fixture-saas-chatbot/evidence-pack/first-interaction/chat-widget.html:L11
evidence_quote: You are chatting with Aria, an AI assistant. Aria is an automated system, not a member of the Northwind support team.
finding: The first message in the thread informs the user they are interacting with an AI system, so the obligation is met without reliance on any exemption.
```

Every value in it came from a markdown file a person can open:

| Field | Comes from |
|---|---|
| `provision`, `duty_force` | `provisions/article-50.md` |
| `quote`, `cite` | `reference/32024R1689/article-50.md` |
| `severity` | the matrix printed in `rules.md` |
| `verdict`, `finding` | the auditor's judgement, which is the part no file can supply |
| `evidence` | what you handed it |

## 4. Checking it by hand

Take the `cite` and the `quote` and look:

```bash
$ grep -n "natural persons concerned are informed" reference/32024R1689/article-50.md
```

The line comes back, and it is line 14, and the words match. That is the entire
verification mechanism. You have now done what `_verify/verify_citations.py` does,
for one finding, with one command that ships with your operating system.

Do it eleven times and you have checked the whole report.

## 5. Why the scripts exist anyway

Doing it eleven times by hand is tedious, and tedium is where checks stop
happening. So:

```bash
make verify
```

runs the same comparison across every quote in every shipped report, plus three
things a person doing it by hand would probably skip: that **every** obligation got
a verdict rather than only the convenient ones, that each severity is what the
published matrix returns for its inputs, and that the report's own trust totals
match its findings.

It produces no findings and changes no verdicts. Delete `_verify/` and the auditor
still audits — you just have to check its homework yourself.

---

**The order matters.** The audit is written by reading markdown. The checking is a
separate act, performed afterwards, by anyone, with or without the tooling. An
auditor that needed its scripts in order to reach a conclusion would have moved
the reasoning into code, where you cannot read it — and that is the failure this
folder is arranged to avoid.
