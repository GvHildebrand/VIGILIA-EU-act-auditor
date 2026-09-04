# Free compliance checker — the interaction surface

Captured 2026-09-03 from <https://aivigilia.com/about>.

The checker takes a description of the visitor's AI system and returns a
generated risk classification with prose reasoning. It is an AI system the
visitor interacts with directly.

## Every string shown at and around the checker, in rendered order

```
Free · instant compliance check
Free preview — no card
No account required for preview
Not legal advice — technical gap analysis
Not sure where you stand? Describe your AI system.
Get an instant EU AI Act risk classification — tier, applicable articles, and
  governance gaps in seconds. No account required.
0/1000
Generate Compliance Snapshot →
```

While a request is in flight the button reads **“Analysing…”**.

## What is not there

**No statement at this surface that the analysis is produced by an AI system.**
The strings above describe the output ("instant", "classification", "snapshot")
and disclaim legal advice, but none of them tells the visitor that the thing
answering them is an AI system.

The only AI disclosure reachable from this page is the site footer —
"Vigilia is an autonomous AI agent, operating with human oversight" — which sits
below the checker, after the point of interaction, and is a statement about the
publisher rather than about this tool's output.

## Source of the strings

`vigilia/messages/en/checker.json` (`form.descriptionLabel`, `form.submit`,
`form.submitting`) and the rendered `/about` page.
