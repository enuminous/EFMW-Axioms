# EFMW Axioms

A reconstruction and formalization of the March 6, 2025 EFMW axiom sheet.

This repository separates three layers:

1. **historical claim** — what the 2025 text asserted;
2. **typed mathematical surrogate** — a proposition or structure precise enough for Lean;
3. **physical status** — whether the statement is established, testable, underdefined, or still speculative.

Lean proves consequences of the formal assumptions. It does **not** prove that the axioms describe nature.

## Site

Open `index.html` for the paper-style public presentation.

## Lean

- `EFMWAxioms/Axioms.lean` — typed formalization of all 12 axioms/corollaries
- `EFMWAxioms/Main.lean` — exported theorem surface
- `lakefile.toml`
- `lean-toolchain`

Build with:

```bash
lake update
lake build
```

## Status

The 2025 equations are preserved historically in the site, but dimensionally inconsistent expressions are **not** silently promoted into formal physics. Their Lean counterparts formalize the intended logical content instead.

CC BY 4.0.
