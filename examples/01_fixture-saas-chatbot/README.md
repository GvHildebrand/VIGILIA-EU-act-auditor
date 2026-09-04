# Fixture 01 — Northwind Support Assistant

**This company does not exist.** It is a fixture: a synthetic evidence pack built
so the auditor can be run end to end by anyone who clones this repo, with no
network access and nothing to sign up for.

It models the most common artifact in scope — a customer-support chatbot on a
B2B SaaS product, available to users in the EU, placed on the market *after*
2 August 2026 so that no transitional window applies.

It is here to show two things:

- what a mostly-compliant artifact looks like when every obligation is still
  reported, including the seven that do not apply to it;
- that a **qualified** duty (Article 50(2), second sentence) cannot produce a
  CRITICAL finding however unimpressed the auditor is — the severity matrix
  caps it at MINOR, because the provision's own words cap it.

Run it:

```bash
python3 _verify/verify_citations.py examples/01_fixture-saas-chatbot/audit-report.md
```
