# EU AI Act Article 50 Auditor
# Python 3.9+, standard library only. No install step, no dependencies.

.PHONY: verify references citations refresh clean help

help:
	@echo "make verify      check the standard is intact and every report cites it correctly"
	@echo "make references  checksums + Official Journal vs consolidated cross-check"
	@echo "make citations   verify every audit report in examples/"
	@echo "make refresh     re-fetch the law from the EU and rebuild reference/ (needs network)"

verify: references citations

references:
	@python3 tools/verify_references.py

citations:
	@python3 tools/verify_citations.py --all

# Re-fetch from publications.europa.eu and rebuild every provision file.
# `git diff` afterwards should be empty: that is the proof the text shipped here
# is byte-identical to the text the EU serves today.
refresh:
	@bash reference/fetch-sources.sh
	@python3 tools/extract_reference.py
	@git diff --stat reference/ || true
	@echo
	@echo "An empty diff above means reference/ matches the EU's current text."
	@echo "If it is not empty, the law moved. Read the diff before regenerating hashes."

clean:
	@find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
