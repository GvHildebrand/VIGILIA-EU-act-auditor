# Article 50 audit — Northwind Support Assistant (fixture)

```audit
artifact: Northwind Support Assistant ("Aria") — examples/01_fixture-saas-chatbot/evidence-pack/
artifact_version: evidence pack captured 2026-08-28
audited_on: 2026-09-03
auditor: VIGILIA-EU-act-auditor
register_version: 1.0.0
reference_fingerprint: f8a28ecc3811b9dc
scope: Article 50 of Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. Nothing else.
trust: observed=4 inferred=0 declared=5 none=2
```

> **Fixture.** Northwind Systems GmbH does not exist. This evidence pack was
> written so that the auditor can be run end to end from a clean clone, with no
> network and no third party's product involved.

## What was audited

An in-app customer-support chatbot sold to EU customers. The pack supplied the
operator's system facts, the first-interaction surface as captured HTML, a sample
transcript export with its provenance metadata, and the published disclosure note.

**Complete for the obligations in play.** The one thing an auditor would normally
have to chase — a metadata dump proving what the output is actually marked with —
was supplied, which is why Article 50(2) could be ruled on at all rather than
returned as INSUFFICIENT_EVIDENCE.

## Scoping determination

| Question | Answer | Source |
|---|---|---|
| Provider, deployer, or both? | Provider | `system-facts.md:L10` |
| Output modalities generated | Text only | `system-facts.md:L11` |
| Available to persons in the EU? | Yes | `system-facts.md:L12` |
| Placed on the market | 2026-08-20 — **after** 2 August 2026 | `system-facts.md:L13` |
| Emotion recognition / biometric categorisation? | Neither | `system-facts.md:L15-L16` |
| Law-enforcement authorisation claimed? | No | `system-facts.md:L19` |
| SME / SMC? | SME, 41 employees | `system-facts.md:L20` |

Two consequences follow and drive several findings below. Because Northwind is a
**provider**, the deployer duties in 50(3) and 50(4) are not its to discharge.
Because the system was placed on the market **after 2 August 2026**, the Article
111(4) transitional window for 50(2) marking is unavailable — the marking duty
was owed in full from launch.

## Summary

| Verdict | Count |
|---|---|
| PASS | 4 |
| FAIL | 0 |
| PARTIAL | 1 |
| NOT_APPLICABLE | 4 |
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

One defect, and it is a MINOR on a qualified duty: the machine-readable mark on
generated text lives in the transcript export and does not survive a user copying
text out of the chat window. Everything else in scope passes, and seven of the
eleven obligations do not apply to this artifact — reported individually, with
the reason, rather than dropped.

**Fix first:** extend provenance marking to the delivery surface, not only the
export path (F-03).

---

## Findings

### F-01 · Article 50(1) · PASS

The assistant is an AI system intended to interact directly with natural persons,
so the trigger is met and Northwind is the provider (examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L10).

Both exemptions were tested and neither applies. **EUAIA-50-1-X2** is out: no
law-enforcement authorisation is claimed (examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L19). **EUAIA-50-1-X1**
— the "obvious" exemption — is the one an operator would reach for, and it was
not needed here, because the disclosure is made explicitly. Had it been argued,
it would have been weak: an assistant given a human first name and no other
signal is exactly the case where a reasonably well-informed, observant and
circumspect person may not know. Northwind does not rely on it.

The disclosure names the system as automated and distinguishes it from the human
support team, which is what the provision asks the natural person to be informed of.

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

### F-02 · Article 50(2), first sentence · PASS

Northwind is a provider of an AI system generating synthetic **text** content, so
50(2) applies. Text is named in the provision alongside audio, image and video,
and operators frequently miss this: a chatbot that never touches an image is
still inside 50(2).

**EUAIA-50-2-X1** was tested and rejected. The assistant composes answers; it does
not perform an assistive function for standard editing, and it does not leave the
user's input substantially unaltered. **EUAIA-50-2-X2** is out for want of any
law-enforcement authorisation.

Article 111(4) does not apply: the system was placed on the market on 2026-08-20
(examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L13), after 2 August 2026, so the marking duty was owed in
full from day one and there is no transitional window to shelter in.

The exported transcript carries a JSON-LD provenance record marking the assistant
turns as artificially generated, including an IPTC digital source type. That is a
mark in a machine-readable format and it is detectable. The obligation is met.

```finding
id: F-02
provision: EUAIA-50-2-MARK
verdict: PASS
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L16
quote: Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated.
evidence: examples/01_fixture-saas-chatbot/evidence-pack/outputs/transcript-export.json:L8-L11
evidence_quote: "syntheticContent": true, "digitalSourceType": "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"
finding: Assistant output carries a machine-readable, detectable provenance mark in the transcript export, satisfying the first sentence of Article 50(2).
```

### F-03 · Article 50(2), second sentence · PARTIAL · MINOR

The second sentence of 50(2) is a **qualified** duty: the technical solution must
be effective, interoperable, robust and reliable *as far as this is technically
feasible*, having regard to the type of content, cost, and the acknowledged state
of the art. The auditor therefore does not ask whether the solution is ideal. It
asks whether it does the job the provision names, within feasibility.

Interoperability is satisfied — JSON-LD with an IPTC digital source type is a
published vocabulary, not a private flag. Effectiveness is where it falls short,
and Northwind says so itself: the mark lives in the export path, so any text a
user selects and copies out of the chat window leaves the mark behind. For a
text-generating system, copy-out is not an edge case; it is the normal way the
output travels.

Marking plain text robustly is genuinely hard, and the provision's feasibility
qualifier is there for exactly that difficulty. That is why this is PARTIAL and
not FAIL, and why the severity matrix caps a qualified duty at MINOR regardless
of how the auditor feels about it. A defect on a qualified duty cannot be
promoted to CRITICAL — the provision's own words forbid it.

```finding
id: F-03
provision: EUAIA-50-2-QUALITY
verdict: PARTIAL
severity: MINOR
duty_force: qualified
applicability: in_force
provenance: declared
cite: reference/32024R1689/article-50.md:L16
quote: Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards.
evidence: examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L21
evidence_quote: No mark travels with text a user copies out of the chat window.
finding: A machine-readable mark exists and is interoperable, but it does not travel with the output on the ordinary copy-out path, so the solution is not effective across the system's normal use.
remediation: Extend marking to the delivery surface, not only the export: attach the provenance record to the clipboard payload where the platform allows, and state in the disclosure that copied text carries no mark. Record the feasibility assessment for text watermarking against the state of the art, since the provision measures this duty against that.
```

### F-04 · Article 50(3), first limb · NOT_APPLICABLE

The trigger requires an emotion recognition system or a biometric categorisation
system within Article 3(39) and 3(40). Neither is present: the operator states no
emotional state is inferred and no biometric data is processed.

Recorded rather than skipped, because this is a common false positive. Sentiment
scoring of typed support tickets is often described internally as "emotion
detection" while falling outside Article 3(39), and the reverse mistake — an
avatar that reads facial expression buried in an onboarding flow — is how this
obligation gets missed. The determination rests on the operator's stated facts;
if those facts are wrong, this verdict is wrong with them.

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
evidence: examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L15
evidence_quote: No. The assistant does not infer emotional state. It performs no sentiment classification of any kind.
finding: No emotion recognition or biometric categorisation system is deployed, so the Article 50(3) trigger is not met.
```

### F-05 · Article 50(3), second limb · NOT_APPLICABLE

This limb travels with the first: it binds a deployer of a system that has already
met the 50(3) trigger. That trigger is not met, so the cross-reference to
Regulation (EU) 2016/679 does not arise under Article 50.

This says nothing about whether Northwind's processing complies with the GDPR.
That question is outside this auditor's declared scope and it is not answered here.

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
evidence: examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L16
evidence_quote: No. No biometric data is processed.
finding: The Article 50(3) trigger is not met, so its data-protection limb does not arise; GDPR compliance generally is outside this audit's scope.
```

### F-06 · Article 50(4), first subparagraph · NOT_APPLICABLE

Two independent reasons, either sufficient.

First, the system generates no image, audio or video content at all, so nothing
can constitute a deep fake within Article 3(60).

Second — and worth stating because it decides many real audits — this obligation
falls on the **deployer**. Northwind is the provider. A provider whose system can
produce deep fakes does not thereby acquire the 50(4) duty; its duty is 50(2).
Reading 50(4) as a provider obligation is the most frequent scoping error in this
Article, and it usually produces a false CRITICAL.

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
evidence: examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L11
evidence_quote: **Text only.** No image, audio or video generation.
finding: No image, audio or video is generated, and in any event Northwind is a provider rather than the deployer on whom Article 50(4) falls.
```

### F-07 · Article 50(4), second subparagraph · NOT_APPLICABLE

The trigger has two limbs and both must hold: the text must be **published**, and
published **with the purpose of informing the public on matters of public
interest**. Assistant output here is delivered inside a private one-to-one support
session to the person who asked. It is not published, and support answers about
API key rotation do not inform the public on a matter of public interest.

Northwind is also the provider rather than the deployer, which would be a second
answer if the first were in doubt.

The contrast is worth holding on to: the same underlying model, used to generate
posts on a company blog about regulation or public health, would engage this
obligation squarely. Fixture 03 in this repository is exactly that case.

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
evidence: examples/01_fixture-saas-chatbot/evidence-pack/system-facts.md:L18
evidence_quote: No. All output is delivered inside a private one-to-one support session to the individual who asked. Nothing generated is published.
finding: The generated text is neither published nor directed at informing the public on matters of public interest, so the Article 50(4) second-subparagraph trigger is not met.
```

### F-08 · Article 50(5), first sentence · PASS

50(5) governs the manner of every disclosure required by paragraphs 1 to 4. Here
one such disclosure is in play — the 50(1) notice — and 50(5) asks two things of
it: that it be clear and distinguishable, and that it arrive no later than the
first interaction.

Timing is satisfied strictly: the notice is the first message in the thread, ahead
of any user input. Clarity and distinguishability are satisfied by its own
paragraph, carrying its own style hook, stating in plain words both what the
system is and what it is not.

This is the obligation most often failed by artifacts that pass everything else.
A disclosure that exists only in a footer, a settings page, a terms document or a
machine-readable file is not provided at the time of first interaction. Northwind
also publishes the disclosure in its documentation, but that is not what earns
this verdict — the in-thread notice is.

```finding
id: F-08
provision: EUAIA-50-5-MANNER
verdict: PASS
severity: NONE
duty_force: absolute
applicability: in_force
provenance: observed
cite: reference/32024R1689/article-50.md:L24
quote: The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure.
evidence: examples/01_fixture-saas-chatbot/evidence-pack/first-interaction/chat-widget.html:L11
evidence_quote: You are chatting with Aria, an AI assistant.
finding: The Article 50(1) disclosure is delivered as the first message of the conversation, in its own clearly distinguished paragraph, before any user interaction.
```

### F-09 · Article 50(5), second sentence · PASS

The second sentence of 50(5) asks that the information conform to the applicable
accessibility requirements. This auditor rules narrowly here, and says why in the
register: the accessibility requirements themselves live in other instruments —
principally Directive (EU) 2019/882 and Directive (EU) 2016/2102 — and those texts
are **not** shipped in this repository's `reference/`. Ruling on conformance with
a standard the folder does not contain would be exactly the opinion-generating
this auditor exists to avoid.

What can be determined from the evidence is whether the disclosure is perceivable
at all by assistive technology, and it is. It is live DOM text inside a container
with an explicit dialog role and an accessible name; it is not an image, not
background CSS, not colour alone, and it carries no `aria-hidden`. A screen-reader
user reaches it in the same reading order as a sighted user.

Full conformance assessment against the accessibility directives is referred
onward rather than asserted.

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
evidence: examples/01_fixture-saas-chatbot/evidence-pack/first-interaction/chat-widget.html:L4-L12
evidence_quote: <div class="nw-chat" role="dialog" aria-label="Northwind Support Assistant"> … <p class="nw-msg nw-msg--system">You are chatting with Aria, an AI assistant.
finding: The disclosure is programmatically available text within a labelled dialog, so it is perceivable by assistive technology; conformance with the accessibility directives themselves is referred onward as outside the shipped reference.
```

### F-10 · Article 50(6) · NOTED · OBSERVATION

A rule of construction, not a duty, and reported on every audit so that no reader
mistakes what this document is.

Northwind's Article 50 position is good. That is not a statement about Chapter III,
about Article 5, about the GDPR, or about any national transparency rule. Recital
137 puts it plainly: compliance with these transparency obligations is not to be
read as indicating that the use of the system or its output is lawful.

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
finding: Reported as a scoping observation: a clean Article 50 result does not speak to Chapter III or to any other Union or national transparency obligation.
```

### F-11 · Article 50(7) · NOTED · OBSERVATION

Addressed to the Commission, not to the audited party — there is nothing here for
Northwind to comply with, and an auditor that scored it would be inventing a duty.

Its practical relevance is the Code of Practice on Transparency of AI-Generated
Content, which the Commission and the AI Board assessed as adequate on 8 and 9
July 2026 for Articles 50(2), (4) and (5). Adherence is voluntary and creates no
obligation. For the copy-out gap found at F-03, the Code is the obvious place to
look for an accepted technique — and adherence would be recorded as evidence
toward 50(2), never as a verdict in its own right.

Note also that this paragraph is the one part of Article 50 the Digital Omnibus
changed: see `reference/32026R1744/amendments-to-article-50-and-111.md`.

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
finding: Reported as an observation: Article 50(7) binds the Commission, not the audited party, and adherence to the transparency Code of Practice is voluntary evidence rather than a verdict.
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
