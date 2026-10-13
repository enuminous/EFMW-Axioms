"""Ensure the audit rejects public/private axioms, placeholders, and native proofs."""
from pathlib import Path
import subprocess
import tempfile

source = Path("Audit.lean").read_text()
marker = "open Lean in\nrun_cmd do"
assert source.count(marker) == 1
cases = [
    ("public axiom", "axiom EFMWAxioms.auditProbe : False", "EFMWAxioms.auditProbe"),
    ("private axiom", "namespace EFMWAxioms\nprivate axiom auditProbe : False\nend EFMWAxioms", "auditProbe"),
    ("placeholder", "theorem EFMWAxioms.auditProbe : False := by sorry", "sorryAx"),
    ("native proof", "theorem EFMWAxioms.auditProbe : (1 : Nat) = 1 := by native_decide", "Lean.ofReduceBool"),
]
with tempfile.TemporaryDirectory(prefix="AuditProbe", dir=".") as directory:
    probe = Path(directory) / "Probe.lean"
    for label, declaration, expected in cases:
        probe.write_text(source.replace(marker, declaration + "\n\n" + marker))
        result = subprocess.run(
            ["lake", "env", "lean", str(probe)],
            text=True, capture_output=True, timeout=60, check=False,
        )
        output = result.stdout + result.stderr
        if result.returncode == 0 or "Unapproved axiom" not in output or expected not in output:
            raise SystemExit(f"Audit failed to reject {label} for the expected reason:\n{output}")
        print(f"Audit correctly rejected {label}.")
