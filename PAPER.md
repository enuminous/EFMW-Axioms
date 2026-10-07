# From Axiom Sheet to Testable Structure

This repository reconstructs the March 6, 2025 EFMW axiom sheet as a formal research program.

The historical document mixed conceptual claims with equations of uneven mathematical quality. Several expressions are dimensionally incomplete or do not encode the prose claim they accompany. Rather than silently repair those formulas and then call the result "proved physics", this project preserves each original idea while replacing it with a typed mathematical surrogate.

The twelve surrogates are implemented in `EFMWAxioms/Axioms.lean`.

The central methodological rule is:

> Lean can prove consequences of an assumption. It cannot prove that nature satisfies the assumption.

Accordingly, the repository distinguishes:
- historical source claim;
- formal mathematical representation;
- machine-checked consequence;
- physical validation status.

See `index.html` for the full paper and item-by-item reconstruction.
