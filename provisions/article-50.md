# The register — Article 50, obligation by obligation

> **Version 1.0.0.** This file is the auditor's rule set. It is read by
> the auditor and by `_verify/verify_citations.py`, which is the whole point: there
> is no machine-only copy of the rules. What you read here is what runs.

**Standard.** Regulation (EU) 2024/1689 (Artificial Intelligence Act) — CELEX `32024R1689`, ELI http://data.europa.eu/eli/reg/2024/1689/oj.
As amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI), CELEX 32026R1744, in force 27 July 2026.

**Scope.** Article 50 only. Chapter III, Article 5 prohibitions and the GPAI obligations of Chapter V are out of scope and are not audited.

**How to read it.** Each `##` heading is one atomic obligation and gets exactly one
verdict in every audit report — eleven headings, eleven verdicts, including the two
that impose no duty. Every quote below appears byte for byte at the line it cites,
in the authentic Official Journal text under `reference/`. You can check any of them
by hand:

```bash
grep -n "shall ensure that the outputs" reference/32024R1689/article-50.md
```

Rules at the bottom supply dates and the penalty tier. They are cited by findings and
never carry a verdict of their own.

---

## The obligations


### EUAIA-50-1

**Article 50(1)** — Tell people they are talking to an AI

- **actor** — provider
- **duty force** — absolute
- **trigger** — The system is an AI system intended to interact directly with natural persons.
- **cite** — `reference/32024R1689/article-50.md:L14`

> Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system

Actor defined at `reference/32024R1689/article-3-definitions.md:L16`:

> ‘provider’ means a natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has an AI system or a general-purpose AI model developed and places it on the market or puts the AI system into service under its own name or trademark, whether for payment or free of charge;

#### EUAIA-50-1-X1 (exemption)

- **test** — Is the AI nature obvious to a reasonably well-informed, observant and circumspect person, in the circumstances and context of use? The test is that hypothetical person, not the auditor's own impression and not the operator's assertion.
- **cite** — `reference/32024R1689/article-50.md:L14`

> unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use

#### EUAIA-50-1-X2 (exemption)

- **test** — Is the system authorised by law to detect, prevent, investigate or prosecute criminal offences? The exemption is itself disapplied where the system is available for the public to report a criminal offence.
- **cite** — `reference/32024R1689/article-50.md:L14`

> This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

**Evidence required**

- The first screen, message or utterance a user meets, captured as text or a screenshot.
- Where the disclosure is claimed to be 'obvious', the operator's stated basis for that — context of use, audience, surrounding copy.


### EUAIA-50-2-MARK

**Article 50(2), first sentence** — Mark synthetic output machine-readably and make it detectable

- **actor** — provider
- **duty force** — absolute
- **trigger** — The system, including a general-purpose AI system, generates synthetic audio, image, video or text content.
- **cite** — `reference/32024R1689/article-50.md:L16`
- **transitional** — EUAIA-111-4: if The AI system was placed on the market before 2 August 2026. the duty falls due 2026-12-02

> Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated.

#### EUAIA-50-2-X1 (exemption)

- **test** — Does the system perform an assistive function for standard editing, or leave the input data and its semantics substantially unaltered? Spell-check and autocorrect sit here; generating a paragraph does not.
- **cite** — `reference/32024R1689/article-50.md:L16`

> This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof

#### EUAIA-50-2-X2 (exemption)

- **test** — Is the system authorised by law to detect, prevent, investigate or prosecute criminal offences?
- **cite** — `reference/32024R1689/article-50.md:L16`

> or where authorised by law to detect, prevent, investigate or prosecute criminal offences.

#### EUAIA-111-4 (transitional)

- **condition** — The AI system was placed on the market before 2 August 2026.
- **deadline** — 2026-12-02
- **effect** — The Article 50(2) marking duty is owed by 2 December 2026 rather than 2 August 2026. A system inside this window is still non-conforming, but the severity matrix scores it MINOR and the finding must name the deadline.
- **cite** — `reference/32026R1744/amendments-to-article-50-and-111.md:L34`

> Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, that have been placed on the market before 2 August 2026 shall take the necessary steps in order to comply with Article 50(2) by 2 December 2026.

**Evidence required**

- A sample output file of each modality the system generates.
- A metadata dump of that file (C2PA manifest, IPTC digital source type, watermark detector output, or equivalent). Without it this obligation cannot be evidenced and the verdict is INSUFFICIENT_EVIDENCE — a visible on-screen label is not a machine-readable mark.
- The date the system was placed on the market, which decides whether Article 111(4) applies.

**Common error.** Treating a visible badge, watermark or 'Generated by AI' caption as compliance. 50(2) requires the output to be marked in a machine-readable format AND detectable; the visible disclosure is what 50(4) and 50(5) ask for, and they are different obligations on a different actor.


### EUAIA-50-2-QUALITY

**Article 50(2), second sentence** — The marking technique must be effective, interoperable, robust and reliable

- **actor** — provider
- **duty force** — qualified
- **qualifier** — as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art
- **trigger** — The Article 50(2) marking duty applies and some marking technique is in place.
- **cite** — `reference/32024R1689/article-50.md:L16`
- **transitional** — EUAIA-111-4: if The AI system was placed on the market before 2 August 2026. the duty falls due 2026-12-02

> Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards.

#### EUAIA-111-4 (transitional)

- **condition** — The AI system was placed on the market before 2 August 2026.
- **deadline** — 2026-12-02
- **effect** — The Article 50(2) marking duty is owed by 2 December 2026 rather than 2 August 2026. A system inside this window is still non-conforming, but the severity matrix scores it MINOR and the finding must name the deadline.
- **cite** — `reference/32026R1744/amendments-to-article-50-and-111.md:L34`

> Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, that have been placed on the market before 2 August 2026 shall take the necessary steps in order to comply with Article 50(2) by 2 December 2026.

**Evidence required**

- A statement of the marking technique used and its standard, if any.
- Any evidence about survival of the mark through common transformations (re-encode, screenshot, crop), which is what 'robust' is measured against.

**Note.** This is a qualified duty. The auditor may not score it as an absolute failure; the severity matrix caps a qualified duty at MINOR unless no technique exists at all, in which case the failure belongs to EUAIA-50-2-MARK.


### EUAIA-50-3-INFORM

**Article 50(3), first limb** — Tell people exposed to emotion recognition or biometric categorisation

- **actor** — deployer
- **duty force** — absolute
- **trigger** — The deployed system is an emotion recognition system or a biometric categorisation system as defined in Article 3(39) and 3(40).
- **cite** — `reference/32024R1689/article-50.md:L18`

> Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system

Actor defined at `reference/32024R1689/article-3-definitions.md:L20`:

> ‘deployer’ means a natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity;

#### EUAIA-50-3-X1 (exemption)

- **test** — Is the system permitted by law to detect, prevent or investigate criminal offences, with safeguards and in accordance with Union law?
- **cite** — `reference/32024R1689/article-50.md:L18`

> This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

**Evidence required**

- Whether any deployed component infers emotions or categorises people by biometric data. Sentiment analysis of typed text is not emotion recognition within Article 3(39) — check the definition before ruling.
- If yes, the notice given to exposed persons and where it appears.


### EUAIA-50-3-DATA

**Article 50(3), second limb** — Process the personal data lawfully under the data-protection acquis

- **actor** — deployer
- **duty force** — absolute
- **trigger** — The Article 50(3) trigger is met.
- **cite** — `reference/32024R1689/article-50.md:L18`

> and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable.

**Evidence required**

- The lawful basis recorded for the processing, and the DPIA if one exists.

**Note.** This auditor does not audit the GDPR. It records whether Article 50(3)'s cross-reference is evidenced, and otherwise returns INSUFFICIENT_EVIDENCE and points at a data-protection review. Claiming a GDPR verdict here would be outside the scope this auditor declares in identity.md.


### EUAIA-50-4-DEEPFAKE

**Article 50(4), first subparagraph** — Disclose deep-fake image, audio or video

- **actor** — deployer
- **duty force** — absolute
- **trigger** — The deployed system generates or manipulates image, audio or video content constituting a deep fake as defined in Article 3(60).
- **cite** — `reference/32024R1689/article-50.md:L20`

> Deployers of an AI system that generates or manipulates image, audio or video content constituting a deep fake, shall disclose that the content has been artificially generated or manipulated.

#### EUAIA-50-4-X1 (exemption)

- **test** — Is the use authorised by law to detect, prevent, investigate or prosecute criminal offence?
- **cite** — `reference/32024R1689/article-50.md:L20`

> This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offence.

#### EUAIA-50-4-X2 (limitation)

- **test** — Does the content form part of an evidently artistic, creative, satirical, fictional or analogous work or programme? This does not remove the duty — it reduces it to disclosing the existence of the generated content in a way that does not hamper the display or enjoyment of the work. A finding that treats this as a full exemption is wrong.
- **cite** — `reference/32024R1689/article-50.md:L20`

> Where the content forms part of an evidently artistic, creative, satirical, fictional or analogous work or programme, the transparency obligations set out in this paragraph are limited to disclosure of the existence of such generated or manipulated content in an appropriate manner that does not hamper the display or enjoyment of the work.

**Evidence required**

- Whether generated image/audio/video resembles existing persons, objects, places, entities or events and would falsely appear authentic — the Article 3(60) test.
- The disclosure shown to viewers, and where it sits relative to the content.


### EUAIA-50-4-TEXT

**Article 50(4), second subparagraph** — Disclose AI-generated text published to inform the public on matters of public interest

- **actor** — deployer
- **duty force** — absolute
- **trigger** — The deployed system generates or manipulates text which is published with the purpose of informing the public on matters of public interest.
- **cite** — `reference/32024R1689/article-50.md:L22`

> Deployers of an AI system that generates or manipulates text which is published with the purpose of informing the public on matters of public interest shall disclose that the text has been artificially generated or manipulated.

#### EUAIA-50-4-X3 (exemption)

- **test** — Is the use authorised by law to detect, prevent, investigate or prosecute criminal offences?
- **cite** — `reference/32024R1689/article-50.md:L22`

> This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offences

#### EUAIA-50-4-X4 (exemption)

- **test** — Has the content undergone human review or editorial control AND does a natural or legal person hold editorial responsibility for the publication? Both limbs are required. A human glancing at the output without anyone holding editorial responsibility does not meet it, and neither does a named responsible person who reviews nothing.
- **cite** — `reference/32024R1689/article-50.md:L22`

> where the AI-generated content has undergone a process of human review or editorial control and where a natural or legal person holds editorial responsibility for the publication of the content.

**Evidence required**

- Whether the published text is AI-generated, and whether its subject matter informs the public on matters of public interest.
- If the editorial exemption is claimed: the review process, and the named natural or legal person holding editorial responsibility.
- The disclosure as it appears to a reader of the published text — not only in a machine-readable file such as llms.txt or an RSS feed.


### EUAIA-50-5-MANNER

**Article 50(5), first sentence** — Clear, distinguishable, and no later than first interaction or exposure

- **actor** — provider or deployer, following whichever of 50(1)–(4) applies
- **duty force** — absolute
- **trigger** — Any of Article 50(1) to (4) applies to the artifact.
- **cite** — `reference/32024R1689/article-50.md:L24`

> The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure.

**Evidence required**

- Where each disclosure appears in the user journey, and what the user has already seen or done before reaching it.

**Note.** This is the obligation most often failed by artifacts that pass everything else: the disclosure exists, but it is in a footer, a settings page, a terms document or a machine-readable file rather than at first interaction or exposure.


### EUAIA-50-5-ACCESS

**Article 50(5), second sentence** — The disclosure itself must be accessible

- **actor** — provider or deployer, following whichever of 50(1)–(4) applies
- **duty force** — absolute
- **trigger** — Any of Article 50(1) to (4) applies to the artifact.
- **cite** — `reference/32024R1689/article-50.md:L24`

> The information shall conform to the applicable accessibility requirements.

**Evidence required**

- How the disclosure is exposed to assistive technology — text alternative, programmatic role, contrast, and whether it survives with images or styling disabled.

**Note.** 'Applicable accessibility requirements' points outside this Regulation, principally to Directive (EU) 2019/882 and Directive (EU) 2016/2102 where they bind the operator. Those texts are NOT in this repository's reference/ folder, so this auditor rules only on evidence that the disclosure is or is not perceivable by assistive technology, and refers the conformance question onward rather than inventing a verdict under a standard it does not ship.


### EUAIA-50-6

**Article 50(6)** — Article 50 compliance is not compliance with anything else

- **actor** — none — a rule of construction
- **duty force** — no_direct_duty
- **trigger** — Always. Reported on every audit as a scoping statement.
- **cite** — `reference/32024R1689/article-50.md:L26`

> Paragraphs 1 to 4 shall not affect the requirements and obligations set out in Chapter III, and shall be without prejudice to other transparency obligations laid down in Union or national law for deployers of AI systems.

**Note.** Reported as an OBSERVATION so that no reader can mistake a clean Article 50 report for a clean bill of health. Recital 137 is the interpretive support: reference/32024R1689/recitals-132-137.md.


### EUAIA-50-7

**Article 50(7)** — Codes of practice — an instruction to the Commission, not to the audited party

- **actor** — none — addressed to the Commission
- **duty force** — no_direct_duty
- **trigger** — Always. Reported as an OBSERVATION where a code of practice is relevant to the artifact.
- **cite** — `reference/32024R1689/article-50.md:L28`

> The AI Office shall encourage and facilitate the drawing up of codes of practice at Union level to facilitate the effective implementation of the obligations regarding the detection and labelling of artificially generated or manipulated content.

**Note.** Adherence to the Code of Practice on Transparency of AI-Generated Content is voluntary and creates no obligation. It may be recorded as evidence toward 50(2), (4) and (5), never as a verdict. See reference/code-of-practice/.

---

## The rules

Cited by findings. Never verdicted.

### EUAIA-113

**Article 113, second paragraph** — application date

- **value** — 2026-08-02
- **cite** — `reference/32024R1689/article-111-113-application.md:L28`

> It shall apply from 2 August 2026.

**Note.** Article 50 sits in Chapter IV and takes the general application date. It has been in force since 2 August 2026.

### EUAIA-111-4

**Article 111(4), added by Regulation (EU) 2026/1744** — transitional window

- **value** — 2026-12-02
- **cite** — `reference/32026R1744/amendments-to-article-50-and-111.md:L34`

> Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, that have been placed on the market before 2 August 2026 shall take the necessary steps in order to comply with Article 50(2) by 2 December 2026.

**Note.** Applies only to Article 50(2), and only to systems placed on the market before 2 August 2026. Absent from the 2024 OJ text — an auditor working from that text alone will get this deadline wrong.

### EUAIA-99-4-g

**Article 99(4)(g)** — penalty

- **tier** — EUR 15 000 000 or 3 % of total worldwide annual turnover, whichever is higher
- **SME / SMC** — For SMEs including start-ups (Art. 99(6)) and SMCs (Art. 99(6a), inserted by Regulation (EU) 2026/1744) the cap is whichever is LOWER.

- **cite** — `reference/32024R1689/article-99-penalties.md:L34`

> transparency obligations for providers and deployers pursuant to Article 50.

- **cite** — `reference/32024R1689/article-99-penalties.md:L20`

> shall be subject to administrative fines of up to EUR 15 000 000 or, if the offender is an undertaking, up to 3 % of its total worldwide annual turnover for the preceding financial year, whichever is higher

- **cite** — `reference/32024R1689/article-99-penalties.md:L38`

> In the case of SMEs, including start-ups, each fine referred to in this Article shall be up to the percentages or amount referred to in paragraphs 3, 4 and 5, whichever thereof is lower.

**Note.** Every Article 50 finding carries this single penalty tier. Severity in this auditor therefore does NOT come from the size of the fine — it is constant — but from duty force and applicability status. See rules.md.
