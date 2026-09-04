#!/usr/bin/env bash
#
# fetch-sources.sh — retrieve the authentic source documents for this auditor.
#
# Everything in reference/ is derived from the three files this script downloads.
# Nothing in reference/ is typed by hand, summarised, or copied from a secondary
# source. Run this script and then `tools/extract_reference.py` to regenerate the
# entire reference/ tree, then `git diff` to confirm it is byte-identical to what
# is committed here.
#
# WHY NOT eur-lex.europa.eu?
#   The EUR-Lex web front end sits behind a bot challenge: automated requests
#   receive HTTP 202 with a zero-byte body. The EU Publications Office "Cellar"
#   content API serves the same documents, from the same publisher, without it.
#   Cellar is the canonical machine-readable interface to the Official Journal.
#
# The Accept-Language header is required. Cellar rejects a language-less request
# for a multilingual work with HTTP 400.
#
set -euo pipefail

cd "$(dirname "$0")/_source"

fetch () {
  local celex="$1" out="$2" desc="$3"
  echo "→ ${celex}  (${desc})"
  curl -sSL --fail --max-time 180 \
    -H "Accept: application/xhtml+xml" \
    -H "Accept-Language: eng" \
    -o "${out}" \
    "http://publications.europa.eu/resource/celex/${celex}"
  printf '  %s bytes  sha256 %s\n' \
    "$(wc -c < "${out}" | tr -d ' ')" \
    "$(shasum -a 256 "${out}" | cut -d' ' -f1)"
}

# 1. The Act as published in the Official Journal. THIS IS THE AUTHENTIC TEXT.
fetch 32024R1689 32024R1689.xhtml \
  "Regulation (EU) 2024/1689 — Artificial Intelligence Act, OJ L, 2024/1689, 12.7.2024"

# 2. The amending act. Article 50(7) and Article 111(4) come from here.
fetch 32026R1744 32026R1744.xhtml \
  "Regulation (EU) 2026/1744 — Digital Omnibus on AI, OJ L, 2026/1744, 24.7.2026"

# 3. The consolidated text. A documentation tool with NO legal effect; used only
#    to cross-check that our reading of the amendment is correct.
fetch 02024R1689-20260727 02024R1689-20260727.xhtml \
  "Consolidated 02024R1689 — EN — 27.07.2026 — 001.001"

echo
echo "Done. Now run:  python3 tools/extract_reference.py"
