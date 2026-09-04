# outputs/

Sample generated output, **and its metadata dump**.

This folder decides Article 50(2), and it is the one operators most often arrive
without. The obligation is that outputs are "marked in a machine-readable format
and detectable as artificially generated or manipulated" — a property of the file
or the response, not of the screen. **It cannot be assessed by looking.** Without a
dump, the honest verdict is `INSUFFICIENT_EVIDENCE`, not `PASS`.

One sample per modality, each with the output of whichever apply:

```bash
c2patool sample.png                                  # content credentials
exiftool -a -G1 -s sample.png                        # embedded metadata
exiftool -XMP-iptcExt:DigitalSourceType sample.png   # IPTC digital source type
curl -sSI https://your.api/endpoint                  # response headers
```

For generated **text**, the equivalents are the structured data on the page, the
API response envelope and its headers, and any watermark detector you run. Paste
what the tools actually printed, including "no claim found" and empty output —
absence is the evidence.

Beware the near-miss: `"author": {"@type": "Organization"}` marks *who published*.
It does not mark the content as *artificially generated*, and a machine reading it
learns nothing about synthetic origin. See example 03.
