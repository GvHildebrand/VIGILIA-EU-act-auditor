# Article 50 audit — Vigilia (self-audit)

```audit
artifact: Vigilia — https://aivigilia.com — public surfaces
artifact_version: evidence captured 2026-09-03
audited_on: 2026-09-03
auditor: VIGILIA-EU-act-auditor
register_version: 1.0.0
reference_fingerprint: 3fa2319d6595d47a
scope: Article 50 of Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. Public surfaces only; the authenticated workspace was not examined.
trust: observed=5 inferred=4 declared=0 none=2
```

> **Not a fixture, and not independent.** Vigilia is a live service that sells EU
> AI Act audits for €499. It is operated by the same person who wrote this
> auditor. A self-audit is worth exactly as much as its evidence, which is why all
> of it is reproduced in `evidence-pack/` and every citation in this report is
> machine-checkable against the Regulation.

## What was audited

Two AI systems Vigilia puts into service on its public site:

1. **the publishing agent** — an autonomous AI agent that writes and publishes
   research dispatches on AI regulation and safety;
2. **the free compliance checker** — a tool at `/about` that takes a visitor's
   description of their own AI system and returns a generated risk classification.

Evidence was captured from the live site on 2026-09-03: the dispatch page as a
reader meets it, the checker surface with every string shown at it, the complete
machine-readable metadata of a published dispatch, the checker's response
construction, the homepage disclosure section and compliance table, `llms.txt`,
and the site's Organization structured data.

**Scope limit, stated up front.** Only public surfaces were examined. The
authenticated €499 workspace, and any content generated inside it, were not.

## Scoping determination

| Question | Answer | Source |
|---|---|---|
| Provider, deployer, or both? | **Both** — provider under Art. 3(3) and 3(11) ("putting into service … for own use"), deployer when it publishes the output | `system-facts.md:L12` |
| Output modalities generated | Text only | `system-facts.md:L13` |
| Available to persons in the EU? | Yes — `areaServed: EU`, five locales | `documents/structured-data.md` |
| Placed on the market / put into service | **Before 2 August 2026** — dispatch archive runs back to 21 April 2026 | `system-facts.md:L15` |
| Emotion recognition / biometric categorisation? | Neither | `system-facts.md:L16-L17` |
| Text published to inform the public on matters of public interest? | **Yes** — dispatches on AI regulation and safety | `system-facts.md:L19` |
| Law-enforcement authorisation claimed? | No | `system-facts.md:L21` |
| Marking technique for synthetic text | **None found** | `system-facts.md:L23` |

Being **both** provider and deployer is what makes this artifact useful as an
example: unlike the two fixtures, Vigilia is exposed to 50(2) *and* to 50(4), and
the audit has to keep the two duties apart rather than collapsing them into
"do they disclose?".

The placement date puts the 50(2) marking duty inside the Article 111(4)
transitional window, which closes on **2 December 2026** — a determination the
operator's own published compliance table independently reaches.

## Summary

| Verdict | Count |
|---|---|
| PASS | 3 |
| FAIL | 1 |
| PARTIAL | 1 |
| NOT_APPLICABLE | 4 |
| INSUFFICIENT_EVIDENCE | 0 |
| NOTED | 2 |

| Severity | Count |
|---|---|
| CRITICAL | 0 |
| MAJOR | 1 |
| MINOR | 1 |
| UNRESOLVED | 0 |
| OBSERVATION | 2 |
| NONE | 7 |

### How much of this rests on the operator's word

| Evidence | Verdicts | Meaning |
|---|---|---|
| `observed` | 5 | the auditor saw the artifact itself — a rendered surface, a real output file, a response header |
| `inferred` | 4 | derived from something *about* the artifact — source code, an archive snapshot, a public record |
| `declared` | 0 | the operator said so, and nothing independent confirms it |
| `none` | 2 | the provision imposes no duty, so there is nothing to evidence |

**0 of 11 verdicts would collapse if the operator's statements were false.** Every finding
carries its own `provenance`, so you can see which ones. `tools/verify_citations.py`
recomputes these totals from the findings and fails the report if the header
misstates them — an audit may not understate how much it is trusting.

Vigilia discloses its AI authorship better than most publishers and still fails
two obligations, in two different ways.

| | |
|---|---|
| **MAJOR** | F-08 · the free compliance checker generates AI prose with no disclosure at the point of interaction. The only AI disclosure on that page is the footer, below the tool and after the fact. |
| **MINOR** | F-02 · no machine-readable mark of synthetic content on any output. Inside the Article 111(4) window until **2 December 2026**, after which the same evidence returns CRITICAL. |

Three PASS, four NOT_APPLICABLE, two OBSERVATION. The strong human-facing
disclosure that earns the passes on 50(1) and 50(4) does nothing for 50(2), which
is a duty owed to machines — and that gap is the single most instructive thing in
this report.

**Fix first:** one line of disclosure at the checker (F-08). It is the most severe
finding and the cheapest to remedy. Then marking, before 2 December 2026 (F-02).

---

## Findings

### F-01 · Article 50(1) · PASS

Vigilia puts two AI systems into service that interact directly with natural
persons: the publishing agent, whose output a reader meets on every dispatch, and
the free compliance checker, which answers a visitor's description of their own AI
system. The trigger is met for both.

The duty in 50(1) is to ensure the natural persons concerned **are informed** that
they are interacting with an AI system. They are. The dispatch byline says so
above the headline; the site footer says so on every page, including the page
carrying the checker; `llms.txt` says so again for machine consumers. There is no
persona, no human byline, and nothing that would lead a reader to think otherwise.

Neither exemption was relied on. **EUAIA-50-1-X2** is out — no law-enforcement
authorisation. **EUAIA-50-1-X1**, the "obvious" carve-out, would have been
arguable for a service whose entire identity is a disclosed AI agent, but it is
not needed and is not claimed: Vigilia states the fact outright.

That the information *exists* is this obligation. **Whether it reaches the person
clearly and at the right moment is Article 50(5), and that is where the checker
runs into trouble** — see F-08. Keeping the two apart is the difference between a
finding that can be acted on and a vague complaint.

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
evidence: examples/03_self-audit-vigilia/evidence-pack/first-interaction/dispatch-byline.md:L13
evidence_quote: By Vigilia — an autonomous AI agent, human-supervised. How this is written →
finding: Natural persons are informed they are interacting with an AI system, by the dispatch byline and by a site-wide disclosure on every page; no exemption is relied on.
```

### F-02 · Article 50(2), first sentence · FAIL · MINOR

Vigilia is the provider of AI systems generating synthetic **text**: the dispatches
and the checker's snapshot prose. Article 3(11) makes putting a system into service
"for own use" enough to be a provider, so running the publishing agent for its own
site does not take Vigilia outside 50(2).

Neither exemption applies. The systems compose original prose rather than perform
an assistive function for standard editing (**EUAIA-50-2-X1**), and no
law-enforcement authorisation is claimed (**EUAIA-50-2-X2**).

**The output is not marked.** The dispatch carries `BlogPosting` structured data
whose `author` is an `Organization` named Vigilia. That is a machine-readable
statement about *who published* — a machine reading it learns the author is an
organisation, and learns nothing about whether the text was artificially
generated. There is no IPTC `digitalSourceType`, no C2PA claim, no synthetic-content
flag, no watermark. The checker is worse: its handler sets exactly one header, a
rate-limiting cookie, and no field in the payload marks the generated prose.

This is the finding that matters most, because it is the one the operator would be
most tempted to argue away. The disclosure practice here is unusually strong —
byline, colophon, footer, `llms.txt`, a public compliance table. **None of it is a
machine-readable mark.** 50(2) is not a disclosure obligation dressed in technical
language; it is a separate duty owed to machines and downstream detectors, and
excellent human-facing disclosure does not discharge it.

**Severity.** Vigilia was on the market before 2 August 2026 — the dispatch archive
runs back to 21 April 2026 — so Article 111(4), added by Regulation (EU) 2026/1744,
gives it until **2 December 2026**. The matrix therefore returns MINOR today. The
operator's own published table already states this deadline and counts down to it,
which is corroboration rather than mitigation: knowing the date does not mark the
output. On 2 December 2026 the same evidence returns CRITICAL.

```finding
id: F-02
provision: EUAIA-50-2-MARK
verdict: FAIL
severity: MINOR
duty_force: absolute
applicability: transitional
provenance: observed
cite: reference/32024R1689/article-50.md:L16
quote: Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated.
evidence: examples/03_self-audit-vigilia/evidence-pack/outputs/dispatch-structured-data.md:L34-L40
evidence_quote: digitalSourceType (IPTC, e.g. trainedAlgorithmicMedia) — No · C2PA manifest or content credential — No · Any syntheticContent / aiGenerated flag — No
finding: No output of either text-generating system carries a machine-readable mark identifying it as artificially generated; structured-data authorship marks the publisher, not the synthetic origin of the text, so Article 50(2) is not met and falls due on 2 December 2026.
remediation: Add IPTC `digitalSourceType: trainedAlgorithmicMedia` to the dispatch structured data and a provenance field or response header to the checker's payload, before 2 December 2026. The Code of Practice on Transparency of AI-Generated Content — assessed adequate by the Commission on 8 July 2026 for exactly this obligation — is the place to take the technique from. Keep the byline and colophon: they discharge 50(4), not 50(2).
```

### F-03 · Article 50(2), second sentence · NOT_APPLICABLE

This obligation grades a marking solution against effectiveness, interoperability,
robustness and reliability so far as technically feasible. No marking technique is
in place, so there is nothing to grade.

Kept separate from F-02 on purpose. Folding it in would score one defect twice and
make the audit look harsher than the standard is. When marking is implemented this
obligation activates and is assessed against the state of the art — and marking
plain text robustly is hard enough that the feasibility qualifier will do real
work then.

The 2 December 2026 date governs the applicability of 50(2) as a whole to this
artifact and is repeated here for that reason.

```finding
id: F-03
provision: EUAIA-50-2-QUALITY
verdict: NOT_APPLICABLE
severity: NONE
duty_force: qualified
applicability: transitional
provenance: inferred
cite: reference/32024R1689/article-50.md:L16
quote: Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards.
basis: trigger_not_met
evidence: examples/03_self-audit-vigilia/evidence-pack/system-facts.md:L23
evidence_quote: **None found.** The dispatch carries `BlogPosting` structured data naming an Organization as author, which marks *authorship*, not *synthetic generation*.
finding: No marking technique exists, so no technical solution's quality can be assessed; the underlying duty is scored once at F-02 and falls due on 2 December 2026.
```

### F-04 · Article 50(3), first limb · NOT_APPLICABLE

No emotion recognition system and no biometric categorisation system within
Article 3(39) and 3(40). The checker classifies a *system description* into a risk
tier; it processes no biometric data and infers no emotional state from any natural
person. Classifying text is not biometric categorisation, and the definitions in
`reference/32024R1689/article-3-definitions.md` are what settle that.

```finding
id: F-04
provision: EUAIA-50-3-INFORM
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: inferred
cite: reference/32024R1689/article-50.md:L18
quote: Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system
basis: trigger_not_met
evidence: examples/03_self-audit-vigilia/evidence-pack/system-facts.md:L16-L17
evidence_quote: Emotion recognition present? No. … Biometric categorisation present? No. No biometric data is processed.
finding: Neither an emotion recognition system nor a biometric categorisation system is operated, so the Article 50(3) trigger is not met.
```

### F-05 · Article 50(3), second limb · NOT_APPLICABLE

Follows F-04. The limb binds a deployer whose system has met the 50(3) trigger, and
that trigger is not met. This is not a statement about Vigilia's data protection
position generally, which is outside the scope this auditor declares.

```finding
id: F-05
provision: EUAIA-50-3-DATA
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: inferred
cite: reference/32024R1689/article-50.md:L18
quote: and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable.
basis: trigger_not_met
evidence: examples/03_self-audit-vigilia/evidence-pack/system-facts.md:L17
evidence_quote: Biometric categorisation present? No. No biometric data is processed.
finding: The Article 50(3) trigger is not met, so its data-protection limb does not arise.
```

### F-06 · Article 50(4), first subparagraph · NOT_APPLICABLE

No generated image, audio or video was found on the public surfaces examined. The
site's principal image is a photograph of an existing sculpture by Adolf von
Hildebrand, credited on the page — a photograph of a real object, not synthetic
media, and nothing about it would falsely appear authentic within Article 3(60).

Scope limit stated plainly: this determination covers the public surfaces in the
evidence pack. The authenticated €499 workspace was not examined. If report
generation there produces synthetic imagery, this obligation would need to be
re-run against it.

```finding
id: F-06
provision: EUAIA-50-4-DEEPFAKE
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: inferred
cite: reference/32024R1689/article-50.md:L20
quote: Deployers of an AI system that generates or manipulates image, audio or video content constituting a deep fake, shall disclose that the content has been artificially generated or manipulated.
basis: trigger_not_met
evidence: examples/03_self-audit-vigilia/evidence-pack/system-facts.md:L18
evidence_quote: No. The site's imagery is a photograph of an existing sculpture by Adolf von Hildebrand, credited on the page; nothing found is AI-generated image, audio or video.
finding: No generated image, audio or video content was found on the public surfaces examined, so nothing can constitute a deep fake; the authenticated workspace was outside the scope of this audit.
```

### F-07 · Article 50(4), second subparagraph · PASS

This is the obligation Vigilia is most exposed to and the one it handles best.

The trigger is met on both limbs and it is not close. The dispatches are AI-
generated text, they are published openly and syndicated by RSS, and their subject
matter — AI regulation, enforcement action, safety research, market concentration —
is squarely informing the public on matters of public interest. Vigilia is the
deployer of the system that generates them.

**The editorial exemption is available and is not used.** EUAIA-50-4-X4 needs two
limbs together: human review or editorial control, *and* a natural or legal person
holding editorial responsibility. Vigilia has a named human taking corrections and
approving production changes, so it could plausibly argue the exemption and publish
nothing. It discloses instead — byline, colophon, footer — which is the stronger
position and the one the obligation is written to encourage. An auditor should say
so when an operator declines a lawful escape hatch.

The disclosure states the substance the provision asks for: that the text is the
work of an autonomous AI agent. Placement and manner are assessed at F-08, and on
this surface they are also good — the byline sits above the headline.

```finding
id: F-07
provision: EUAIA-50-4-TEXT
verdict: PASS
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L22
quote: Deployers of an AI system that generates or manipulates text which is published with the purpose of informing the public on matters of public interest shall disclose that the text has been artificially generated or manipulated.
evidence: examples/03_self-audit-vigilia/evidence-pack/first-interaction/dispatch-byline.md:L13-L15
evidence_quote: By Vigilia — an autonomous AI agent, human-supervised. … The disclosure sits above the headline and above the body text, in the byline position, before any of the article can be read.
finding: AI-generated text published to inform the public on matters of public interest is disclosed as such in the byline and colophon of every dispatch, without recourse to the editorial-responsibility exemption.
```

### F-08 · Article 50(5), first sentence · PARTIAL · MAJOR

50(5) governs how the information under paragraphs 1 to 4 reaches people: clearly,
distinguishably, and **at the latest at the time of the first interaction or
exposure**. Two surfaces are in play and they diverge.

**The dispatches pass, comfortably.** The disclosure is in the byline, above the
headline, before a word of the article can be read. It is its own element, plainly
worded, and repeated in a colophon at the end. This is what "at the latest at the
time of first exposure" looks like when it is done properly.

**The free compliance checker does not.** A visitor lands on the page, reads
"Describe your AI system", types a description of their own system, presses
"Generate Compliance Snapshot", and receives generated prose telling them their
regulatory risk tier. Nothing at that surface says the analysis is produced by an
AI system. The strings around it — "instant", "classification", "snapshot", "Not
legal advice — technical gap analysis" — describe the output and disclaim advice;
none of them makes the disclosure. The only AI disclosure reachable is the site
footer, which sits *below* the tool, is encountered *after* the interaction, and
speaks about the publisher rather than about this tool's output.

So the information required by 50(1) exists (F-01) but is not provided in a clear
and distinguishable manner at the latest at the time of first interaction on the
surface where the interaction actually happens. That is a PARTIAL, and on an
absolute duty in force the matrix returns **MAJOR** — the most severe finding in
this report.

It is worth naming the irony rather than softening it: the checker whose purpose is
to find Article 50 gaps in other people's products contains one. It is also the
cheapest defect here to fix — a single line above the button.

```finding
id: F-08
provision: EUAIA-50-5-MANNER
verdict: PARTIAL
severity: MAJOR
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L24
quote: The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure.
evidence: examples/03_self-audit-vigilia/evidence-pack/first-interaction/checker-surface.md:L27-L33
evidence_quote: **No statement at this surface that the analysis is produced by an AI system.** … The only AI disclosure reachable from this page is the site footer … which sits below the checker, after the point of interaction.
finding: The disclosure is delivered at first exposure on the dispatch pages but not on the free compliance checker, where the only AI disclosure is a site footer encountered after the interaction.
remediation: Put the disclosure at the checker itself, above or beside the submit control — for example "This analysis is generated by Vigilia, an AI system" — and repeat it on the returned snapshot. One line, at the surface where the first interaction happens.
```

### F-09 · Article 50(5), second sentence · PASS

Ruled narrowly, for the reason the register records: the applicable accessibility
requirements live in other instruments, principally Directive (EU) 2019/882 and
Directive (EU) 2016/2102, and those texts are **not** in this repository's
`reference/`. Pronouncing conformity with a standard the folder does not contain
would be precisely the opinion-generating this auditor exists to avoid.

What the evidence does establish is that the disclosures are perceivable. The
byline is server-rendered live text inside a semantic `aside`, in normal reading
order, with no `aria-hidden`; it is not an image, not a background, and not
conveyed by colour alone. The dagger glyph beside it is decorative and carries no
meaning the text does not also carry. The colophon and footer are likewise plain
text. A screen-reader user meets the same disclosure a sighted reader does, at the
same point.

Full conformance assessment against the accessibility directives is referred
onward, not asserted. Note also that this verdict is about the disclosure that
exists; on the checker surface the problem at F-08 is that there is no disclosure
to make accessible.

```finding
id: F-09
provision: EUAIA-50-5-ACCESS
verdict: PASS
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L24
quote: The information shall conform to the applicable accessibility requirements.
evidence: examples/03_self-audit-vigilia/evidence-pack/first-interaction/dispatch-byline.md:L20-L28
evidence_quote: Server-rendered live text in a semantic `aside`, reachable in normal reading order. Not an image, not a background, not conveyed by colour alone, and carrying no `aria-hidden`.
finding: The disclosures that exist are programmatically available text in normal reading order, so they are perceivable by assistive technology; conformance with the accessibility directives themselves is outside the shipped reference and is referred onward.
```

### F-10 · Article 50(6) · NOTED · OBSERVATION

Reported so this document cannot be quoted as more than it is. Vigilia sells EU AI
Act audits; a favourable Article 50 report about itself would be a marketing asset,
and the boundary matters more here than usual.

This audit says nothing about Chapter III, nothing about Article 5, nothing about
the GPAI obligations in Chapter V, and nothing about the GDPR. Recital 137 is
explicit that compliance with the transparency obligations is not to be read as
indicating that the use of an AI system or its output is lawful.

```finding
id: F-10
provision: EUAIA-50-6
verdict: NOTED
severity: OBSERVATION
duty_force: no_direct_duty
applicability: in_force
provenance: none
cite: reference/32024R1689/article-50.md:L26
quote: Paragraphs 1 to 4 shall not affect the requirements and obligations set out in Chapter III, and shall be without prejudice to other transparency obligations laid down in Union or national law for deployers of AI systems.
finding: Reported as a scoping observation: this audit covers Article 50 only and does not speak to Chapter III, Chapter V, the GDPR, or any national obligation.
```

### F-11 · Article 50(7) · NOTED · OBSERVATION

Binds the Commission, not Vigilia, so there is nothing here to comply with.

Directly relevant all the same: the Code of Practice on Transparency of AI-Generated
Content was assessed adequate by the Commission on 8 July 2026 and by the AI Board
on 9 July 2026 for Articles 50(2), (4) and (5). It is where the marking technique
missing at F-02 should come from, and the remediation there points at it.

Adherence is voluntary and confers no presumption of conformity — recital 41 of
Regulation (EU) 2026/1744 says so. Signing it would be evidence toward F-02, never
a verdict on it. This paragraph is also the single provision of Article 50 that the
Digital Omnibus amended.

```finding
id: F-11
provision: EUAIA-50-7
verdict: NOTED
severity: OBSERVATION
duty_force: no_direct_duty
applicability: in_force
provenance: none
cite: reference/32024R1689/article-50.md:L28
quote: The AI Office shall encourage and facilitate the drawing up of codes of practice at Union level to facilitate the effective implementation of the obligations regarding the detection and labelling of artificially generated or manipulated content.
finding: Reported as an observation: Article 50(7) binds the Commission, and adherence to the transparency Code of Practice would be voluntary evidence toward F-02 rather than compliance in itself.
```

---

## Matters noted outside the scope of this audit

An audit reports what it was asked to look at. It should also say when it walked
past something a reasonable reader would want to know, rather than pretending not
to have seen it. The following is **not** an Article 50 finding, carries no
verdict and no severity, and is recorded here because it was encountered while
gathering evidence.

The dispatch used as the evidence artifact —
[*Commission Enforces AI Act Transparency from 2 August 2026*](https://aivigilia.com/blog/commission-enforces-ai-act-transparency-2-august-2026),
published 25 August 2026 — **described Article 50 incorrectly**, in three ways
that the text shipped in this repository's `reference/` contradicts directly.

| The dispatch said | The Regulation says |
|---|---|
| "Article 50 imposes transparency obligations on providers of general-purpose AI models." | Article 50 binds providers and deployers of **certain AI systems**. Obligations on providers of general-purpose AI **models** are Article 53, in Chapter V. |
| Those obligations "include public documentation of training data characteristics, computational resources used, testing procedures, and known limitations", plus adversarial testing and serious-incident tracking for systemic-risk models. | Those are the Article 53(1) and Article 55(1) obligations, and they have applied since **2 August 2025**. Article 50's seven paragraphs are reproduced in full at `reference/32024R1689/article-50.md` and contain none of them. |
| "Penalties for non-compliance with Article 50 are structured at 1% of global annual turnover." | Article 99(4)(g) puts Article 50 in the **EUR 15 000 000 or 3 %** tier. The 1 % figure is Article 99(5), which penalises supplying incorrect, incomplete or misleading information to authorities — a different infringement. |

The error understated the penalty exposure of the provision by a factor of three
and attached it to the wrong actor. It also ran through the article's argument:
the fragility research it reported bears on the Article 53 and 55 documentation
duties, not on Article 50 at all.

**Corrected on 3 September 2026**, the same day this audit was run, across the
English original and all four translations, with a dated correction notice
carried at the top of each. The commit is
[`3f990ea`](https://github.com/GvHildebrand/vigilia) in the Vigilia repository.
The argument survived the correction; it simply lands on the right provisions now.

This is the failure mode the whole repository is built around, found in the
operator's own work: a summary of a standard, written by an AI, drifting from the
standard, published, and read by people who had no way to check it. The article
sat on the site of a company that sells Article 50 audits, for nine days.

It is also the reason `reference/` exists in the form it does. Nothing in this
report could have made that mistake and survived `verify_citations.py`, because
every claim in the eleven findings above quotes the provision it relies on and the
script checks the quote against the authentic text, byte for byte. The dispatch had
no such check, and so it went out wrong — and stayed wrong until something with a
copy of the law read it.

**Still outstanding, and outside this audit:** the same citation discipline has not
been run over the rest of the published archive, and the generator that produced
the error is upstream in a separate repository.

---

## Attestation

| | |
|---|---|
| Standard | Regulation (EU) 2024/1689, Article 50, as amended by Regulation (EU) 2026/1744 |
| Authentic text | OJ L, 2024/1689, 12.7.2024 — shipped verbatim in `reference/32024R1689/` |
| Reference fingerprint | `3fa2319d6595d47a` |
| Register version | 1.0.0 |
| Obligations in register | 11 — all reported above |

Check every citation in this report against the text it cites:

```bash
python3 tools/verify_citations.py <this file>
```

**Scope limits.** This audit covers Article 50 and nothing else. Article 50(6)
provides that paragraphs 1 to 4 do not affect the requirements and obligations of
Chapter III and are without prejudice to other transparency obligations in Union
or national law. Recital 137 provides that compliance with the transparency
obligations is not to be interpreted as indicating that the use of the AI system
or its output is lawful.

**This is not legal advice** and it is not a conformity assessment. It is a
documented comparison of an artifact against a published text, written so that
every statement in it can be checked against that text.
