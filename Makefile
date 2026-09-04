# EU AI Act Article 50 Auditor
# Python 3.9+, standard library only. No install step, no dependencies.

.PHONY: verify references citations pins freshness audit-repo refresh emit-pins clean help

help:
	@echo "make verify              the standard is intact, every report cites it correctly, no verdict moved"
	@echo "make freshness           ask the EU whether the law has been amended since (needs network)"
	@echo "make audit-repo REPO=..  scan a codebase into a half-filled evidence pack"
	@echo "make refresh             re-fetch the law from the EU and rebuild reference/ (needs network)"
	@echo
	@echo "  references             checksums + Official Journal vs consolidated cross-check"
	@echo "  citations              every quote in every report, byte for byte"
	@echo "  pins                   verdicts of the shipped examples have not moved"
	@echo "  emit-pins              re-record those verdicts (deliberate act, read tools/verify_pins.py first)"

# Offline by design. An auditor you can only check when the EU is reachable is a
# worse auditor, so nothing in `verify` touches the network.
verify: references citations pins

references:
	@python3 tools/verify_references.py

citations:
	@python3 tools/verify_citations.py --all

pins:
	@python3 tools/verify_pins.py

emit-pins:
	@python3 tools/verify_pins.py --emit

# Needs network. verify/ proves reference/ is unaltered; this asks the different
# question of whether it is still current.
freshness:
	@python3 tools/check_freshness.py

# Turn a codebase into an evidence pack with the machine-knowable rows filled in
# and everything else marked NOT ESTABLISHED.  make audit-repo REPO=../my-product
audit-repo:
	@test -n "$(REPO)" || (echo "usage: make audit-repo REPO=/path/to/product [OUT=./audit-workspace]"; exit 1)
	@python3 tools/scan_repo.py "$(REPO)" --out "$(or $(OUT),./audit-workspace)"

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
