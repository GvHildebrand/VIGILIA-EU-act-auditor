#!/usr/bin/env python3
"""
verify_citations.py — check an audit report against the standard it claims to cite.

This is the script that makes this auditor's output falsifiable. It does not
judge whether a verdict is legally right; no script can. It proves the four
things that go wrong when a language model writes a compliance report:

  1. INVENTED PROVISION   every cited provision id exists in the register.
  2. MISQUOTED PROVISION  every quoted provision appears BYTE-FOR-BYTE at the
                          line it cites, in the authentic OJ text.
  3. SKIPPED OBLIGATION   every obligation in the register appears exactly once.
                          An audit cannot quietly omit the inconvenient ones.
  4. UNGROUNDED VERDICT   severity is recomputed from the published matrix and
                          must match; a finding of breach must point at evidence;
                          INSUFFICIENT_EVIDENCE must say what would resolve it.

Usage:
    python3 _verify/verify_citations.py examples/03_self-audit-vigilia/audit-report.md
    python3 _verify/verify_citations.py --all
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import register  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "provisions" / "article-50.md"
MANIFEST = ROOT / "reference" / "MANIFEST.md"

VERDICTS = {"PASS", "FAIL", "PARTIAL", "NOT_APPLICABLE", "INSUFFICIENT_EVIDENCE", "NOTED"}
# How the evidence behind a verdict was obtained. This is the field that answers
# "what if the operator lied": a reader can see exactly how much of the report
# would collapse if they had.
#   observed  the auditor saw the artifact itself — a rendered surface, a real
#             output file, a response header
#   inferred  derived from something about the artifact — source code, an
#             archive snapshot, a public registry
#   declared  the operator said so, and nothing independent confirms it
#   none      the provision imposes no duty, so there is nothing to evidence
PROVENANCE = {"observed", "inferred", "declared", "none"}
APPLICABILITY = {"in_force", "transitional", "not_yet_applicable"}
AUTHENTIC = ("reference/32024R1689/", "reference/32026R1744/")

REQUIRED = ("id", "provision", "verdict", "severity", "duty_force",
            "applicability", "provenance", "cite", "quote", "finding")

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"
if not sys.stdout.isatty():
    GREEN = RED = YELLOW = DIM = OFF = ""


# ─────────────────────────────────────────────────────────────────────────────
# The severity matrix. Published in rules.md; recomputed here. Any reader can
# check a severity by hand — that is the point of deriving it instead of feeling it.
# ─────────────────────────────────────────────────────────────────────────────

def severity_of(duty_force: str, verdict: str, applicability: str) -> str:
    if verdict in ("PASS", "NOT_APPLICABLE"):
        return "NONE"
    if verdict == "INSUFFICIENT_EVIDENCE":
        return "UNRESOLVED"
    if verdict == "NOTED" or duty_force == "no_direct_duty":
        return "OBSERVATION"
    if applicability == "not_yet_applicable":
        return "OBSERVATION"
    if applicability == "transitional":
        return "MINOR"
    if duty_force == "qualified":
        return "MINOR"
    return "CRITICAL" if verdict == "FAIL" else "MAJOR"


def manifest_fingerprint() -> str:
    """A short digest of reference/'s checksum block: which standard a report saw."""
    text = MANIFEST.read_text(encoding="utf-8")
    block = text.split("<!-- checksums:start -->", 1)[1].split("<!-- checksums:end -->", 1)[0]
    lines = sorted(l.strip() for l in block.splitlines() if l.strip() and not l.startswith("```"))
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()[:16]


# ─────────────────────────────────────────────────────────────────────────────

def show(path: Path) -> str:
    """A readable label for a report that may live outside this repository."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_blocks(text: str, kind: str) -> list[dict[str, str]]:
    """Fenced ```kind blocks of `key: value` lines, in document order."""
    out = []
    for body in re.findall(rf"^```{kind}\n(.*?)^```", text, flags=re.S | re.M):
        rec: dict[str, str] = {}
        for line in body.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            key, sep, val = line.partition(":")
            if sep:
                rec[key.strip()] = val.strip()
        out.append(rec)
    return out


def resolve(cite: str) -> tuple[Path, int, int] | None:
    """'reference/x.md:L14' or 'reference/x.md:L14-L18' → (path, start, end)."""
    m = re.fullmatch(r"(.+?):L(\d+)(?:-L(\d+))?", cite.strip())
    if not m:
        return None
    path = ROOT / m.group(1)
    if not path.is_file():
        return None
    start = int(m.group(2))
    return path, start, int(m.group(3) or start)


def check_report(path: Path, register: dict) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems: list[str] = []
    obligations = {o["id"]: o for o in register["obligations"]}

    # ── header ──────────────────────────────────────────────────────────────
    heads = parse_blocks(text, "audit")
    if len(heads) != 1:
        problems.append(f"expected exactly one ```audit header block, found {len(heads)}")
    else:
        head = heads[0]
        for key in ("artifact", "audited_on", "register_version", "reference_fingerprint", "trust"):
            if key not in head:
                problems.append(f"audit header is missing '{key}'")
        if head.get("register_version") not in (None, register["version"]):
            problems.append(
                f"report was written against register {head['register_version']}, "
                f"but the register here is {register['version']}"
            )
        fp = manifest_fingerprint()
        if head.get("reference_fingerprint") not in (None, fp):
            problems.append(
                f"report cites reference fingerprint {head['reference_fingerprint']}, "
                f"but reference/ now fingerprints {fp} — the standard moved under this report"
            )

    # ── findings ────────────────────────────────────────────────────────────
    findings = parse_blocks(text, "finding")
    if not findings:
        return problems + ["no ```finding blocks in this report"]

    seen: dict[str, int] = {}
    for i, f in enumerate(findings, 1):
        tag = f.get("id", f"#{i}")

        missing = [k for k in REQUIRED if k not in f]
        if missing:
            problems.append(f"{tag}: missing field(s) {', '.join(missing)}")
            continue

        pid = f["provision"]
        seen[pid] = seen.get(pid, 0) + 1

        # 1 — invented provision
        if pid not in obligations:
            problems.append(f"{tag}: provision '{pid}' is not in the register")
            continue
        ob = obligations[pid]

        # vocabulary
        if f["verdict"] not in VERDICTS:
            problems.append(f"{tag}: verdict '{f['verdict']}' is not one of {sorted(VERDICTS)}")
            continue
        if f["applicability"] not in APPLICABILITY:
            problems.append(f"{tag}: applicability '{f['applicability']}' is not one of {sorted(APPLICABILITY)}")
            continue
        if f["duty_force"] != ob["duty_force"]:
            problems.append(
                f"{tag}: duty_force '{f['duty_force']}' contradicts the register, "
                f"which records '{ob['duty_force']}' for {pid}"
            )

        # a rule of construction is NOTED, and only a rule of construction is
        if (ob["duty_force"] == "no_direct_duty") != (f["verdict"] == "NOTED"):
            problems.append(
                f"{tag}: NOTED is for provisions that impose no duty on the audited party, "
                f"and every such provision must use it ({pid} is '{ob['duty_force']}')"
            )

        if f["provenance"] not in PROVENANCE:
            problems.append(
                f"{tag}: provenance '{f['provenance']}' is not one of {sorted(PROVENANCE)}"
            )
        elif (f["provenance"] == "none") != (f["verdict"] == "NOTED"):
            problems.append(
                f"{tag}: provenance 'none' is only for NOTED provisions that impose no duty, "
                f"and every NOTED finding must use it"
            )

        # 2 — misquoted provision
        loc = resolve(f["cite"])
        if loc is None:
            problems.append(f"{tag}: cite '{f['cite']}' does not resolve to a file and line")
        else:
            fpath, lo, hi = loc
            rel = str(fpath.relative_to(ROOT))
            if not rel.startswith(AUTHENTIC):
                problems.append(
                    f"{tag}: cites {rel}, which is not an authentic OJ text. "
                    f"The consolidated text has no legal effect — cite {' or '.join(AUTHENTIC)}"
                )
            span = "\n".join(fpath.read_text(encoding="utf-8").splitlines()[lo - 1:hi])
            if f["quote"] not in span:
                problems.append(
                    f"{tag}: QUOTE NOT FOUND at {f['cite']}\n"
                    f"        claimed: {f['quote'][:100]}…"
                )

        # 4 — ungrounded verdict
        expect = severity_of(ob["duty_force"], f["verdict"], f["applicability"])
        if f["severity"] != expect:
            problems.append(
                f"{tag}: severity '{f['severity']}' is not what the matrix produces for "
                f"({ob['duty_force']}, {f['verdict']}, {f['applicability']}) → '{expect}'"
            )
        if f["verdict"] in ("FAIL", "PARTIAL", "PASS") and not f.get("evidence"):
            problems.append(f"{tag}: a {f['verdict']} verdict must cite evidence in the artifact")
        # An evidence locator that points inside this repository must resolve.
        # Fabricating a path to a file that is not there is the artifact-side
        # equivalent of misquoting the standard.
        ev = f.get("evidence", "")
        if ev.startswith("examples/"):
            evloc = resolve(ev) if ":L" in ev else (ROOT / ev, 0, 0)
            if evloc is None or not evloc[0].is_file():
                problems.append(f"{tag}: evidence '{ev}' does not resolve to a file in this repository")
        if f["verdict"] == "INSUFFICIENT_EVIDENCE" and not f.get("evidence_needed"):
            problems.append(f"{tag}: INSUFFICIENT_EVIDENCE must state what would resolve it")
        # NOT_APPLICABLE is a ruling, not a shrug: say whether the trigger was
        # never met or a named exemption was satisfied, and name the exemption.
        if f["verdict"] == "NOT_APPLICABLE":
            basis = f.get("basis", "")
            known = {e["id"] for e in ob.get("exemptions", [])}
            if not basis:
                problems.append(
                    f"{tag}: NOT_APPLICABLE must record a basis — 'trigger_not_met' "
                    f"or the id of the exemption that was satisfied"
                )
            elif basis != "trigger_not_met" and basis not in known:
                problems.append(
                    f"{tag}: basis '{basis}' is not trigger_not_met and is not an "
                    f"exemption of {pid} ({', '.join(sorted(known)) or 'none defined'})"
                )
        if f["applicability"] == "transitional" and "2 December 2026" not in f.get("finding", ""):
            problems.append(
                f"{tag}: a transitional finding must name the deadline the artifact is "
                f"running against (2 December 2026, Article 111(4))"
            )

    # 5 — the report must state, correctly, how much of itself rests on trust
    counts: dict[str, int] = {k: 0 for k in PROVENANCE}
    for f in findings:
        if f.get("provenance") in counts:
            counts[f["provenance"]] += 1
    stated = (heads[0].get("trust", "") if heads else "").strip()
    expect = " ".join(f"{k}={counts[k]}" for k in ("observed", "inferred", "declared", "none"))
    if stated and stated != expect:
        problems.append(
            f"the audit header claims trust '{stated}' but the findings give '{expect}'. "
            f"A report may not misstate how much of itself depends on the operator's word."
        )

    # 3 — skipped or duplicated obligation
    for oid in obligations:
        n = seen.get(oid, 0)
        if n == 0:
            problems.append(f"OBLIGATION NOT AUDITED: {oid} ({obligations[oid]['short']})")
        elif n > 1:
            problems.append(f"{oid} is audited {n} times; each obligation gets exactly one verdict")

    if not problems:
        counts: dict[str, int] = {}
        for f in findings:
            counts[f["verdict"]] = counts.get(f["verdict"], 0) + 1
        vt: dict[str, int] = {}
        for f in findings:
            vt[f["verdict"]] = vt.get(f["verdict"], 0) + 1
        tally = "  ".join(f"{k} {v}" for k, v in sorted(vt.items()))
        print(f"  {GREEN}ok{OFF}  {show(path)}")
        print(f"      {len(findings)} findings, all {len(obligations)} obligations covered")
        print(f"      {DIM}{tally}{OFF}")
        print(f"      {DIM}evidence: {expect}{OFF}")
    return problems


def main() -> int:
    reg = register.load(REGISTER)

    if "--all" in sys.argv:
        reports = sorted(ROOT.glob("examples/*/audit-report.md"))
        if not reports:
            print(f"{YELLOW}no reports found under examples/{OFF}")
            return 0
    else:
        args = [a for a in sys.argv[1:] if not a.startswith("-")]
        if not args:
            print(__doc__)
            return 2
        reports = [Path(a) if Path(a).is_absolute() else ROOT / a for a in args]

    print(f"verifying citations  {DIM}register {reg['version']} · reference {manifest_fingerprint()}{OFF}")
    failed = 0
    for report in reports:
        if not report.is_file():
            print(f"  {RED}!!{OFF}  {report}: no such file")
            failed += 1
            continue
        problems = check_report(report, reg)
        if problems:
            failed += 1
            print(f"  {RED}FAIL{OFF}  {show(report)}")
            for p in problems:
                print(f"      - {p}")

    if failed:
        print(f"\n{RED}{failed} report(s) failed verification{OFF}")
        return 1
    print(f"\n{GREEN}all reports verified{OFF}  {DIM}every quote checked against the authentic text{OFF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
