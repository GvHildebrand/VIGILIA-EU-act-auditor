# Reference manifest — provenance, authenticity, integrity

This folder holds **the standard itself**, not a description of it. Every finding
this auditor issues quotes one of these files and cites it by line number, so a
reader can open the finding, open the provision, and check that the two match.

Three questions a reader should be able to answer without trusting anybody, and
where this manifest answers them:

| Question | Answer |
|---|---|
| Where did this text come from? | § Provenance — CELEX id, exact URL, retrieval date, and the script that fetched it |
| Is it the *authentic* text? | § Authenticity — and no, the consolidated file is not, and this manifest says so |
| Has it been altered since? | § Integrity — SHA-256 for every file, checked by `tools/verify_references.py` |

---

## Provenance

Retrieved **3 September 2026** by `reference/fetch-sources.sh` from the
**EU Publications Office Cellar API** — `http://publications.europa.eu/resource/celex/{CELEX}`
with `Accept: application/xhtml+xml` and `Accept-Language: eng`.

*Why not eur-lex.europa.eu?* Its web front end sits behind a bot challenge and
returns HTTP 202 with a zero-byte body to automated requests. Cellar is the same
publisher's machine-readable interface to the same documents, and it answers.

| File | Document | CELEX | ELI |
|---|---|---|---|
| `_source/32024R1689.xhtml` | Regulation (EU) 2024/1689 (Artificial Intelligence Act), OJ L, 2024/1689, 12.7.2024 | `32024R1689` | http://data.europa.eu/eli/reg/2024/1689/oj |
| `_source/32026R1744.xhtml` | Regulation (EU) 2026/1744 (Digital Omnibus on AI), OJ L, 2026/1744, 24.7.2026 | `32026R1744` | http://data.europa.eu/eli/reg/2026/1744/oj |
| `_source/02024R1689-20260727.xhtml` | Consolidated text 02024R1689 — EN — 27.07.2026 — 001.001 | `02024R1689-20260727` | — |

The seven provision files under `32024R1689/`, `32026R1744/` and
`02024R1689-20260727/` are generated from those three sources by
`tools/extract_reference.py`. **Nothing in this folder is typed by hand.** To
prove it:

```bash
bash reference/fetch-sources.sh && python3 tools/extract_reference.py && git diff --stat
```

An empty diff means the standard shipped here is byte-identical to the standard
the EU serves today.

**The only alterations the extractor makes**, all mechanical and documented in
its header: markup removed, HTML entities resolved, runs of whitespace (including
the non-breaking spaces the OJ places after paragraph numbers) collapsed to a
single space, and two-cell OJ list rows joined onto one line. No word is added,
removed, reordered or reworded, and the OJ's typographic quotation marks are
preserved, because findings quote this text byte for byte.

---

## Authenticity

**The OJ text is authentic. The consolidated text is not.** This distinction is
load-bearing and the auditor is built on it.

Council Regulation (EU) No 216/2013 of 7 March 2013 on the electronic publication
of the Official Journal of the European Union, Article 1(2) (CELEX `32013R0216`):

> "Without prejudice to Article 3, only the Official Journal published in
> electronic form (hereinafter 'the electronic edition of the Official Journal')
> shall be authentic and shall produce legal effects."

EUR-Lex says this of every consolidated text, including ours:

> "This text is meant purely as a documentation tool and has no legal effect. The
> Union's institutions do not assume any liability for its contents. The authentic
> versions of the relevant acts, including their preambles, are those published in
> the Official Journal of the European Union."

**Therefore:** findings cite `32024R1689/` and `32026R1744/` — the OJ texts. The
consolidated file is shipped for one job only: an independent check that our
reading of the amendment is right (below). A finding that cites only the
consolidated text is a defect, and `tools/verify_citations.py` rejects it.

---

## The cross-check

Article 50 was amended between its publication and today. Rather than ask a reader
to take our word for what changed, the two texts are compared mechanically by
`tools/verify_references.py`, which asserts:

- the OJ Article 50 and the consolidated Article 50 contain the **same ten blocks**;
- **nine are byte-identical**;
- **exactly one differs — paragraph 7** — and the consolidator's own ▼M1 change
  marker sits on that paragraph and no other.

That is the EU's own consolidation confirming, without any human interpretation,
that Regulation (EU) 2026/1744 left Article 50(1)–(6) untouched. It is also why
this auditor can enforce 50(1)–(6) from the 2024 text with confidence, and why it
knows the 2 December 2026 deadline in Article 111(4) exists at all.

---

## Reuse

Reproduced under **Commission Decision 2011/833/EU of 12 December 2011 on the
reuse of Commission documents**, which authorises reuse of documents held by the
Commission and by the Publications Office free of charge, provided the source is
acknowledged and the meaning is not distorted.

Source acknowledgement: **© European Union, https://eur-lex.europa.eu**
This repository is not affiliated with, endorsed by, or speaking for the European
Union or any of its institutions. It reproduces published legislation so that
findings can be checked against it.

The `LICENSE` at the repo root covers the auditor — the prompts, rules, register
and scripts. It does not, and cannot, cover the legislation in this folder, which
carries the terms above.

---

## Integrity

SHA-256 for every file here. Verify with:

```bash
python3 tools/verify_references.py
```

Regenerate after a legitimate refresh with `--write`. Regenerating is not a fix
for a mismatch: if a hash changed and you did not refresh the sources on purpose,
the text under your auditor moved and every finding citing it is suspect.

<!-- checksums:start -->

```
c402f8efdad18abc0d186cb20d95ceeb9b6099703dc18bea8efdf82cdbd1c37b  02024R1689-20260727/article-50-consolidated.md
ff5d63cc5f6711de119bd9684c86b875ef54bc948ea54a2daace301ec665c522  32024R1689/article-111-113-application.md
8106a99de453252147e4f1026d3b597f1520c6b2208767df05d7073960a042a9  32024R1689/article-3-definitions.md
9d358f426e891ee4ff36726d34155ab51060f9c3c36fba4c6e9d1af80331acf0  32024R1689/article-50.md
3d311b0817bcd382855b98927ead7f46a5e8f6ffb930378f389ef12779be8097  32024R1689/article-99-penalties.md
0a829ff5309a4374bd5ac7a8a92c3aa03dfc64c740b5368275d33403d371c217  32024R1689/recitals-132-137.md
ce119c46802eebee951d80663f9d0f86cc5378494136b4c9392c3a2a6b72f625  32026R1744/amendments-to-article-50-and-111.md
5e7719f77e8a606b257dc25958ee3222c4383300a5a34270a5b850a2ce8b8715  _source/02024R1689-20260727.xhtml
8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a  _source/32024R1689.xhtml
9d754652b867722807e4219c85912ce354233e58a1b4eb8c7752b4d1922993db  _source/32026R1744.xhtml
2f17b79fe74b3909ef211aea39dc661627fdd06c9b770fd26b4d6c641846c8ee  code-of-practice/README.md
a7fa63f459e52ba9a84597309758de3c7c1a2bfda04f06cde6e7175e2c98a769  fetch-sources.sh
```

<!-- checksums:end -->
