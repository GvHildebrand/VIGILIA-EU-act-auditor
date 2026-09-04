# Evidence pack

Copy this folder, fill it in, hand the whole thing to the auditor.

Four inputs. The auditor rules on what is here and **does not infer what is
missing** — a gap becomes `INSUFFICIENT_EVIDENCE` with a note saying what would
resolve it, not a guess dressed as a finding.

| | |
|---|---|
| `system-facts.md` | The scoping facts. Most audits turn on two of them: provider or deployer, and the date placed on the market. |
| `first-interaction/` | What a person meets first. |
| `outputs/` | Sample generated output **and its metadata dump**. |
| `documents/` | Terms, privacy policy, product docs, published disclosures. |

Worked packs to copy the shape from: [`examples/01_fixture-saas-chatbot/evidence-pack/`](../../examples/01_fixture-saas-chatbot/evidence-pack/)
(complete), [`examples/03_self-audit-vigilia/evidence-pack/`](../../examples/03_self-audit-vigilia/evidence-pack/)
(built from a live site's public record).
