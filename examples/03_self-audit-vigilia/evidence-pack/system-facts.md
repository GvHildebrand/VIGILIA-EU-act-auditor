# System facts — Vigilia (aivigilia.com)

**Not an operator questionnaire.** Every row below was established from the public
record and is cited to a file in this evidence pack. Where a fact could not be
established that way it is marked *not established*, and the obligation that turns
on it is ruled accordingly rather than guessed.

| Question | Answer | Established from |
|---|---|---|
| Legal entity | Dear Wise Earth Inc., trading as Vigilia | `documents/structured-data.md` (`legalName`) |
| Product | A disclosed autonomous AI agent that publishes research dispatches, plus a free EU AI Act compliance checker and a paid €499 audit | `documents/homepage-disclosure.md` |
| Provider, deployer, or both? | **Both.** Provider of the AI systems it puts into service for its own use and for site visitors — the publishing agent and the free checker (Art. 3(3) and 3(11), "putting into service … for own use"). Deployer of those systems when it publishes their text output. | `documents/homepage-disclosure.md`, `documents/llms-txt.md` |
| Output modalities generated | **Text only.** Research dispatches, and the compliance snapshot returned by the free checker. No generated image, audio or video was found on the public surfaces examined. | `outputs/dispatch-structured-data.md`, `outputs/checker-response.md` |
| Available to persons in the EU? | Yes. `areaServed: EU`, five language locales, sold to EU customers. | `documents/structured-data.md` |
| Placed on the market / put into service | **Before 2 August 2026.** The earliest dated public artifact in evidence is a dispatch of 21 April 2026; the site's own compliance table treats Art. 50(2) as still forthcoming. | `documents/homepage-disclosure.md`, `outputs/dispatch-structured-data.md` |
| Emotion recognition present? | No. No component infers emotional state from any natural person's data. | public surfaces examined |
| Biometric categorisation present? | No. No biometric data is processed. | public surfaces examined |
| Deep fakes generated? | No. The site's imagery is a photograph of an existing sculpture by Adolf von Hildebrand, credited on the page; nothing found is AI-generated image, audio or video. | public surfaces examined |
| Text published to inform the public on matters of public interest? | **Yes.** Dispatches on AI regulation, enforcement, safety research and market concentration, published openly and syndicated by RSS. | `first-interaction/dispatch-byline.md` |
| Human review / editorial responsibility for published text? | A named human takes corrections and approves production changes; the operator does not rely on the Art. 50(4) editorial exemption, disclosing instead. | `first-interaction/dispatch-byline.md` |
| Law-enforcement authorisation claimed? | No. | — |
| SME / SMC? | SME. | `documents/structured-data.md` |
| Marking technique used for synthetic text | **None found.** The dispatch carries `BlogPosting` structured data naming an Organization as author, which marks *authorship*, not *synthetic generation*. No `digitalSourceType`, no C2PA claim, no synthetic-content flag. The checker API returns bare JSON with a single `Set-Cookie` header. | `outputs/dispatch-structured-data.md`, `outputs/checker-response.md` |
| Authenticated €499 workspace | **Not examined.** Out of scope for this audit; noted as a limit. | — |
