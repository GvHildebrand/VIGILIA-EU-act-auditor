# Code of Practice on Transparency of AI-Generated Content

**Status: voluntary. Not reproduced here, on purpose.**

## What it is

A code of practice drawn up under Article 50(7), which the **European Commission
assessed as adequate on 8 July 2026** and the **AI Board on 9 July 2026**, to
facilitate the practical implementation of **Articles 50(2), (4) and (5)**. A draft
was published on 17 December 2025 and the final version in June 2026.

It translates the Article's requirements into concrete technical and organisational
measures — which marking techniques count, how disclosures should be presented —
and it is the obvious place for an operator to look for an accepted technique when
a finding under 50(2) needs remediation.

## Why it is not in this folder

`reference/` holds **the standard this auditor enforces**, and this is not it.

The Code creates no legal obligations. Recital 41 of Regulation (EU) 2026/1744 —
reproduced verbatim at
[`../32026R1744/amendments-to-article-50-and-111.md`](../32026R1744/amendments-to-article-50-and-111.md)
— records that codes of practice under Article 50(7) "have limited legal effect,
and in particular do not grant a presumption of conformity", which is why the
Digital Omnibus removed the Commission's power to approve them by implementing act.

An auditor cannot issue a verdict against a voluntary code, and this one does not.
Shipping the Code alongside the Regulation would invite exactly that confusion, and
would pad `reference/` with a document no finding in this repository cites.

## How the auditor treats it

**Adherence is evidence toward a finding. It is never a verdict.**

An operator who has signed the Code and implemented its marking techniques has
evidence going to Article 50(2), and the auditor records it as such — under the
provision, with the artifact evidence, like any other evidence. An operator who has
not signed it has breached nothing.

Where a finding recommends a remediation, the Code is a legitimate place to point:
see F-02 in
[`../../examples/02_fixture-image-generator/audit-report.md`](../../examples/02_fixture-image-generator/audit-report.md)
and F-02 in
[`../../examples/03_self-audit-vigilia/audit-report.md`](../../examples/03_self-audit-vigilia/audit-report.md).

## Where to get it

Published by the European Commission via the Digital Strategy portal:
<https://digital-strategy.ec.europa.eu/> — see the AI Act transparency pages and
the Commission FAQ on the transparency obligations under Article 50.

If you extend this auditor to check adherence to the Code, put the Code's text in
this folder first, hash it into
[`../MANIFEST.md`](../MANIFEST.md), and give it its own register entries with their
own ids — do not fold voluntary measures into the eleven statutory obligations.
