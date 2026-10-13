import Lean
import EFMWAxioms

/-!
Audit every safe logical EFMWAxioms declaration, including private declarations.
Compiler-only unsafe specializations cannot be used in kernel proofs and are
excluded; all dependencies of the remaining declarations are still traversed.
The only permitted foundational axioms are Lean's standard logical axioms.
This rejects placeholders, custom axioms, and native_decide dependencies.
-/

open Lean in
run_cmd do
  let env ← getEnv
  let allowed : Array Name := #[``propext, ``Classical.choice, ``Quot.sound]
  let mut count := 0
  let mut theoremCount := 0
  for (name, info) in env.constants.toList do
    let userName := privateToUserName name
    if (`EFMWAxioms).isPrefixOf userName && !info.isUnsafe then
      count := count + 1
      if info matches .thmInfo _ then
        theoremCount := theoremCount + 1
      let axioms ← collectAxioms name
      for ax in axioms do
        unless allowed.contains ax do
          throwError "Unapproved axiom {ax} used by {name}"
  if count == 0 then
    throwError "Audit matched no EFMWAxioms declarations"
  logInfo m!"Axiom audit passed: {count} safe logical declarations, {theoremCount} theorem declarations (including generated lemmas)."
