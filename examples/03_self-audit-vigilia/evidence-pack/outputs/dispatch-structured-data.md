# Dispatch page — machine-readable metadata, in full

Captured 2026-09-03. This is the complete provenance-relevant machine-readable
content of the page. Reproduced so the Article 50(2) finding can be checked
rather than believed.

## `application/ld+json` — BlogPosting

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Commission Enforces AI Act Transparency from 2 August 2026",
  "datePublished": "2026-08-25T09:26:47.600Z",
  "dateModified": "2026-08-25T09:26:47.600Z",
  "author":    { "@type": "Organization", "name": "Vigilia",
                 "url": "https://aivigilia.com/mission#how-vigilia-works" },
  "publisher": { "@type": "Organization", "name": "Vigilia",
                 "url": "https://aivigilia.com" },
  "inLanguage": "en",
  "articleSection": "AI Safety Watch",
  "wordCount": 993
}
```

## Provenance-relevant meta tags

```html
<meta property="article:author" content="Vigilia"/>
```

## What is absent

| Marking a machine could read as "this is synthetic" | Present? |
|---|---|
| `digitalSourceType` (IPTC, e.g. `trainedAlgorithmicMedia`) | **No** |
| C2PA manifest or content credential | **No** |
| Any `syntheticContent` / `aiGenerated` flag | **No** |
| Watermark or steganographic mark in the text | **No** |
| Response header asserting AI generation | **No** |

`"author": {"@type": "Organization", "name": "Vigilia"}` is a machine-readable
statement about **who published**. A machine reading it learns the author is an
organisation. It does not learn the text was artificially generated — which is
what Article 50(2) requires the output to be marked and detectable as.

The earliest dispatch in the public archive is dated **21 April 2026**, which is
the evidence that the service was on the market before 2 August 2026.
