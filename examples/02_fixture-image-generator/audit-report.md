# Article 50 audit — PixelForge (fixture)

```audit
artifact: PixelForge — examples/02_fixture-image-generator/evidence-pack/
artifact_version: evidence pack captured 2026-08-30
audited_on: 2026-09-03
auditor: VIGILIA-EU-act-auditor
register_version: 1.0.0
reference_fingerprint: f8a28ecc3811b9dc
scope: Article 50 of Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. Nothing else.
trust: observed=4 inferred=0 declared=5 none=2
```

> **Fixture.** PixelForge B.V. does not exist. This evidence pack exists so the
> dated applicability rule in Article 111(4) can be exercised against a real
> artifact from a clean clone, with no network.

## What was audited

A text-to-image web app available to users in the EU, audited against Article 50
as the **provider** of the system. The pack supplied the operator's system facts,
the first-interaction surface, a metadata dump of a generated image, and the
relevant terms-of-service excerpt.

The metadata dump is what makes this audit possible. Article 50(2) asks whether
output is marked in a machine-readable format; that question cannot be answered
by looking at a screen, and without a dump the verdict would have been
INSUFFICIENT_EVIDENCE rather than FAIL.

## Scoping determination

| Question | Answer | Source |
|---|---|---|
| Provider, deployer, or both? | Provider | `system-facts.md:L7` |
| Output modalities generated | Image only | `system-facts.md:L8` |
| Available to persons in the EU? | Yes | `system-facts.md:L9` |
| Placed on the market | **2026-01-15 — before 2 August 2026** | `system-facts.md:L10` |
| Emotion recognition / biometric categorisation? | Neither | `system-facts.md:L12-L13` |
| Does the service itself publish output? | No | `system-facts.md:L14` |
| Law-enforcement authorisation claimed? | No | `system-facts.md:L15` |
| SME / SMC? | SME, 19 employees | `system-facts.md:L16` |

The placement date is the fact that decides this audit. Because PixelForge was
placed on the market before 2 August 2026, **Article 111(4)** — added to the
Regulation by Regulation (EU) 2026/1744 and absent from the 2024 Official Journal
text — gives it until **2 December 2026** to comply with Article 50(2).

Because PixelForge is the **provider** and publishes nothing itself, the deployer
duties in Article 50(3) and 50(4) do not fall on it. They fall on its customers
when they publish, which is outside this audit.

## Summary

| Verdict | Count |
|---|---|
| PASS | 0 |
| FAIL | 1 |
| PARTIAL | 0 |
| NOT_APPLICABLE | 8 |
| INSUFFICIENT_EVIDENCE | 0 |
| NOTED | 2 |

| Severity | Count |
|---|---|
| CRITICAL | 0 |
| MAJOR | 0 |
| MINOR | 1 |
| UNRESOLVED | 0 |
| OBSERVATION | 2 |
| NONE | 8 |

### How much of this rests on the operator's word

| Evidence | Verdicts | Meaning |
|---|---|---|
| `observed` | 4 | the auditor saw the artifact itself — a rendered surface, a real output file, a response header |
| `inferred` | 0 | derived from something *about* the artifact — source code, an archive snapshot, a public record |
| `declared` | 5 | the operator said so, and nothing independent confirms it |
| `none` | 2 | the provision imposes no duty, so there is nothing to evidence |

**5 of 11 verdicts would collapse if the operator's statements were false.** Every finding
carries its own `provenance`, so you can see which ones. `tools/verify_citations.py`
recomputes these totals from the findings and fails the report if the header
misstates them — an audit may not understate how much it is trusting.

One live defect: generated images carry no machine-readable provenance mark of any
kind — no C2PA claim, no IPTC digital source type, no watermark.

**Severity today is MINOR. Severity on 2 December 2026 is CRITICAL.** Nothing about
the artifact or the auditor changes between those two dates; the Article 111(4)
transitional window closes, and the matrix returns a different answer from the same
inputs. There are 90 days from the audit date.

| Finding | Severity today | Severity from 2026-12-02 |
|---|---|---|
| F-02 · Article 50(2) marking absent | MINOR | **CRITICAL** |

**Fix first:** embed C2PA and the IPTC digital source type at generation time,
before 2 December 2026 (F-02).

---

## Findings

### F-01 · Article 50(1) · NOT_APPLICABLE

The trigger is met — a prompt box that answers you is an AI system intended to
interact directly with natural persons — so this obligation has to be reasoned to
a conclusion rather than waved away.

**EUAIA-50-1-X1 is satisfied.** The test is not whether PixelForge said the words
"you are interacting with an AI system"; it is whether the fact is obvious from
the point of view of a natural person who is reasonably well-informed, observant
and circumspect, taking into account the circumstances and the context of use.
Here the product name, the H1, the sub-head, the field placeholder and the primary
button all say so, and the entire proposition of the service is that a model draws
the picture. A person of that description cannot arrive at a generated image
without knowing a machine made it.

Recorded as NOT_APPLICABLE with the exemption named, **not** as a PASS. The
distinction matters: PASS would assert that PixelForge discharged a duty it never
owed, and would hide the fact that the position rests on an exemption which a
redesign could remove. If the service were rebranded around a named persona and
the AI framing dropped from the surface, this verdict flips and there is no
disclosure in place to fall back on.

```finding
id: F-01
provision: EUAIA-50-1
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L14
quote: Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system
basis: EUAIA-50-1-X1
evidence: examples/02_fixture-image-generator/evidence-pack/first-interaction/landing-copy.md:L5-L11
evidence_quote: H1: AI image generation for teams · Sub-head: Describe what you want. Our AI model draws it in seconds. · Button: Generate with AI
finding: The trigger is met but the exemption in Article 50(1) is satisfied: the AI nature of the service is obvious from the product name, headline, sub-head, field placeholder and primary button.
```

### F-02 · Article 50(2), first sentence · FAIL · MINOR

PixelForge is the provider of an AI system generating synthetic image content.
The trigger is met and neither exemption saves it: generating an image from a text
prompt is not an assistive function for standard editing and does not leave input
data substantially unaltered (**EUAIA-50-2-X1**), and no law-enforcement
authorisation is claimed (**EUAIA-50-2-X2**).

The evidence is unambiguous. `c2patool` reports no claim, the IPTC digital source
type tag is absent, and the operator confirms there is no watermark or
steganographic mark of any kind. The optional visible caption is not a machine-
readable mark, and it is off by default in any case. The provision requires the
output to be **marked in a machine-readable format** and **detectable as
artificially generated or manipulated**. Neither limb is met.

**Why this is MINOR and not CRITICAL.** PixelForge was placed on the market on
2026-01-15, before 2 August 2026. Article 111(4), added to the Regulation by
Regulation (EU) 2026/1744, gives providers in exactly that position until
2 December 2026 to take the necessary steps to comply with Article 50(2). On the
date of this audit that deadline has not passed, so the severity matrix returns
MINOR. This is the standard's determination, not the auditor's leniency — and it
is not available at all to an auditor reading only the 2024 Official Journal text,
where Article 111(4) does not exist.

**On 2 December 2026 this same evidence produces CRITICAL**, with no change to the
auditor, the register, or the artifact. That is 90 days from the audit date.

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
evidence: examples/02_fixture-image-generator/evidence-pack/outputs/sample-portrait-metadata.txt:L11-L15
evidence_quote: $ c2patool sample-portrait.png → No claim found. · $ exiftool -XMP-iptcExt:DigitalSourceType → (no output — tag not present)
finding: Generated images carry no machine-readable provenance mark of any kind, so Article 50(2) is not met; the artifact is inside the Article 111(4) transitional window and owes compliance by 2 December 2026.
remediation: Embed a C2PA manifest at generation time and set XMP-iptcExt:DigitalSourceType to trainedAlgorithmicMedia on every export, before 2 December 2026. The Code of Practice on Transparency of AI-Generated Content, assessed adequate by the Commission on 8 July 2026, describes accepted techniques for exactly this. The visible caption may stay, but it is not what Article 50(2) asks for.
```

### F-03 · Article 50(2), second sentence · NOT_APPLICABLE

This obligation measures the quality of a marking solution — whether it is
effective, interoperable, robust and reliable so far as technically feasible. Its
trigger presupposes that some technique is in place. Here there is none, so there
is nothing whose quality can be assessed.

Reported rather than folded into F-02 deliberately. Merging them would let one
defect be counted twice and would make the audit look worse than the standard
says it is. The absence of any marking is a failure of the first sentence of
50(2), and it is scored there once. When PixelForge implements marking, this
obligation activates and gets its own verdict against the state of the art.

The finding still names 2 December 2026 because the applicability of the whole of
50(2) to this artifact is governed by the Article 111(4) window.

```finding
id: F-03
provision: EUAIA-50-2-QUALITY
verdict: NOT_APPLICABLE
severity: NONE
duty_force: qualified
applicability: transitional
provenance: declared
cite: reference/32024R1689/article-50.md:L16
quote: Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards.
basis: trigger_not_met
evidence: examples/02_fixture-image-generator/evidence-pack/system-facts.md:L17
evidence_quote: **None.** No C2PA manifest, no IPTC digital source type, no watermark, no steganographic mark.
finding: No marking technique exists, so there is no technical solution whose effectiveness, interoperability, robustness or reliability can be assessed; the underlying 50(2) duty is scored once at F-02 and falls due on 2 December 2026.
```

### F-04 · Article 50(3), first limb · NOT_APPLICABLE

No emotion recognition system and no biometric categorisation system within
Article 3(39) and 3(40). A text-to-image model that renders a face is doing
neither: it categorises no one and infers no emotional state from any natural
person's data.

```finding
id: F-04
provision: EUAIA-50-3-INFORM
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: declared
cite: reference/32024R1689/article-50.md:L18
quote: Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system
basis: trigger_not_met
evidence: examples/02_fixture-image-generator/evidence-pack/system-facts.md:L12-L13
evidence_quote: Emotion recognition present? No. · Biometric categorisation present? No.
finding: Neither an emotion recognition system nor a biometric categorisation system is deployed, so the Article 50(3) trigger is not met.
```

### F-05 · Article 50(3), second limb · NOT_APPLICABLE

Follows F-04: the limb binds a deployer whose system has already met the 50(3)
trigger, and that trigger is not met. Nothing is said here about PixelForge's data
protection position generally, which is outside this auditor's scope.

```finding
id: F-05
provision: EUAIA-50-3-DATA
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: declared
cite: reference/32024R1689/article-50.md:L18
quote: and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable.
basis: trigger_not_met
evidence: examples/02_fixture-image-generator/evidence-pack/system-facts.md:L13
evidence_quote: Biometric categorisation present? No.
finding: The Article 50(3) trigger is not met, so its data-protection limb does not arise.
```

### F-06 · Article 50(4), first subparagraph · NOT_APPLICABLE

This is the finding most likely to be got wrong, and getting it wrong produces a
false CRITICAL against a company that owes nothing.

PixelForge generates photorealistic images of people. Some of them will constitute
deep fakes within Article 3(60) once someone publishes them. But Article 50(4)
binds **deployers** — the natural or legal person using the system under their own
authority — and PixelForge is the **provider**. It generates images and returns
them to the requesting user; it publishes nothing itself.

The duty is real, and it lands on PixelForge's customers when they publish. The
terms of service already tell them so, which is good practice though not something
Article 50 requires of a provider. The provider's own transparency duty for this
artifact is 50(2), and it is scored at F-02.

An auditor that ruled FAIL here would be inventing an obligation, and would be
wrong in a way that costs the audited party real money.

```finding
id: F-06
provision: EUAIA-50-4-DEEPFAKE
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: declared
cite: reference/32024R1689/article-50.md:L20
quote: Deployers of an AI system that generates or manipulates image, audio or video content constituting a deep fake, shall disclose that the content has been artificially generated or manipulated.
basis: trigger_not_met
evidence: examples/02_fixture-image-generator/evidence-pack/system-facts.md:L7
evidence_quote: **Provider.** PixelForge builds and operates the service under its own name. Customers who generate and then publish images are deployers in their own right; this audit does not cover them.
finding: Article 50(4) falls on deployers; PixelForge is the provider and publishes nothing, so the trigger is not met against this party — the duty arises for customers who publish, and is outside the scope of this audit.
```

### F-07 · Article 50(4), second subparagraph · NOT_APPLICABLE

The system generates no text at all, so nothing it produces can be text published
with the purpose of informing the public on matters of public interest. The
provider/deployer point at F-06 would be a second answer if it were needed.

```finding
id: F-07
provision: EUAIA-50-4-TEXT
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: declared
cite: reference/32024R1689/article-50.md:L22
quote: Deployers of an AI system that generates or manipulates text which is published with the purpose of informing the public on matters of public interest shall disclose that the text has been artificially generated or manipulated.
basis: trigger_not_met
evidence: examples/02_fixture-image-generator/evidence-pack/system-facts.md:L8
evidence_quote: **Image only.** Photorealistic and illustrative stills. No audio, video or text generation.
finding: No text is generated, so the Article 50(4) second-subparagraph trigger is not met.
```

### F-08 · Article 50(5), first sentence · NOT_APPLICABLE

Article 50(5) governs the manner in which **the information referred to in
paragraphs 1 to 4** is provided to natural persons. It is a rule about how a
disclosure is delivered; it does not create a disclosure of its own.

Work through what is left standing. 50(1) is disapplied by its own exemption
(F-01), so there is no paragraph 1 information to deliver. 50(3) and 50(4) are not
triggered (F-04 to F-07). The one obligation that does bite, 50(2), requires the
**output** to be marked in a machine-readable format and detectable — a duty owed
to machines and downstream detectors, not information provided to a natural person
at a moment of first interaction or exposure.

So there is nothing for 50(5) to govern on this artifact, and the verdict is
NOT_APPLICABLE with the reasoning on the record.

**This is a reasoned reading and the auditor flags it as such.** It turns on
50(5)'s "information … provided to the natural persons concerned" not reaching a
machine-readable marking duty. Two things would change it: PixelForge losing the
50(1) exemption through a redesign, or a Commission guidance or court reading that
extends 50(5) to the 50(2) mark. Either would make this a live obligation. It is
recorded here rather than buried so that a reader who disagrees can see exactly
what was decided and on what basis.

```finding
id: F-08
provision: EUAIA-50-5-MANNER
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L24
quote: The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure.
basis: trigger_not_met
evidence: examples/02_fixture-image-generator/evidence-pack/first-interaction/landing-copy.md:L11
evidence_quote: There is no separate statement in the form "you are interacting with an AI system".
finding: No obligation under Article 50(1) to (4) requires information to be provided to natural persons for this artifact, so Article 50(5) has nothing to govern.
```

### F-09 · Article 50(5), second sentence · NOT_APPLICABLE

Follows F-08 for the same reason: with no paragraph 1 to 4 information to provide,
there is no information whose accessibility can be assessed. If the 50(1) exemption
ceases to hold, this obligation activates together with F-08 and both will need
evidence about how the disclosure is exposed to assistive technology.

```finding
id: F-09
provision: EUAIA-50-5-ACCESS
verdict: NOT_APPLICABLE
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L24
quote: The information shall conform to the applicable accessibility requirements.
basis: trigger_not_met
evidence: examples/02_fixture-image-generator/evidence-pack/first-interaction/landing-copy.md:L11
evidence_quote: There is no separate statement in the form "you are interacting with an AI system".
finding: With no Article 50(1) to (4) information in play, there is no disclosure whose accessibility can be assessed.
```

### F-10 · Article 50(6) · NOTED · OBSERVATION

Reported so this document is not over-read. PixelForge's one live Article 50 defect
sits inside a transitional window; that is a statement about Article 50 and nothing
else. Copyright and training-data questions, the GPAI obligations in Chapter V, and
any national rule on synthetic media are all untouched by this audit, and recital
137 is explicit that transparency compliance does not make the use of a system or
its output lawful.

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
finding: Reported as a scoping observation: this audit speaks only to Article 50 and not to Chapter III, Chapter V, or any other Union or national obligation.
```

### F-11 · Article 50(7) · NOTED · OBSERVATION

Binds the Commission, not PixelForge. Its practical relevance here is direct: the
Code of Practice on Transparency of AI-Generated Content was assessed adequate by
the Commission on 8 July 2026 and by the AI Board on 9 July 2026 for Articles
50(2), (4) and (5), and it is the natural place for PixelForge to look for an
accepted marking technique before 2 December 2026.

Adherence is voluntary and confers no presumption of conformity — recital 41 of
Regulation (EU) 2026/1744 says so in terms. Signing it would be evidence toward
F-02, never a verdict on it.

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
finding: Reported as an observation: Article 50(7) binds the Commission, and adherence to the transparency Code of Practice is voluntary evidence rather than compliance.
```

---

## Attestation

| | |
|---|---|
| Standard | Regulation (EU) 2024/1689, Article 50, as amended by Regulation (EU) 2026/1744 |
| Authentic text | OJ L, 2024/1689, 12.7.2024 — shipped verbatim in `reference/32024R1689/` |
| Reference fingerprint | `f8a28ecc3811b9dc` |
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
