# Master prompt for Codex

You are implementing a research-grade prototype called `molecular-twin-prototype`.

## Objective
Build one reproducible end-to-end pipeline that compares a reference human protein with a single personalized missense variant using molecular dynamics. Do not build a whole-person digital twin yet.

## Mandatory requirements
1. Work incrementally. Run tests after every meaningful change.
2. Never silently change residue numbering, chain ID, amino-acid identity, units, force field, or simulation parameters.
3. Before mutation, verify that the requested reference residue really exists at the requested PDB chain/residue number.
4. Handle structure gaps explicitly. Current PDBFixer has a reported issue where `applyMutations()` can interfere with `findMissingResidues()` on structures with SEQRES gaps. Do not rely on a fragile call order. Add a regression test.
5. Prepare reference and mutant with identical force-field, solvent, ionic-strength, minimization, and equilibration settings.
6. Record software versions, OpenMM compute platform, random seeds, force field, water model, and all simulation settings in machine-readable metadata.
7. CPU execution must work. Use CUDA/OpenCL/HIP automatically when available, but never make GPU availability a correctness requirement.
8. Analysis must include at minimum: backbone RMSD, per-residue RMSF, radius of gyration, SASA, H-bond count, and configurable local metrics around the mutated residue.
9. Produce plots and a structured JSON summary plus a Markdown report.
10. The report must clearly distinguish:
   - curated clinical/genetic evidence,
   - structural model quality,
   - MD-derived hypotheses.
11. Never generate a diagnosis, medication recommendation, dose recommendation, or longevity claim.
12. Add unit tests and at least one small integration test that is cheap enough for CI.

## Implementation order
A. Make CLI/tests green.
B. Implement structure loading and strict residue validation.
C. Implement robust reference/mutant structure preparation.
D. Implement short OpenMM simulation with metadata capture.
E. Implement MDTraj analysis.
F. Add comparison report and plots.
G. Add a single demo protein/variant with a reproducible command.
H. Only after A-G work, add minimal VCF parsing for a pre-selected variant.

## Scientific quality gates
- Reject ambiguous residue mappings instead of guessing.
- Report missing atoms/residues and any repaired structure segments.
- Keep reference and mutant protocols matched.
- Use enough equilibration checks to avoid interpreting obvious setup artifacts.
- Flag short simulations as exploratory.
- Never equate structural difference with clinical effect.

## Deliverable
At completion, I should be able to run something like:

`moltwin run --pdb <PDB_ID> --chain A --mutation ILE-359-LEU --out runs/demo`

and obtain:
- prepared reference structure
- prepared mutant structure
- trajectories
- metadata.json
- metrics.json
- comparison plots
- report.md

Before making changes, inspect the repository and write a short implementation plan. Then implement Phase A only, run tests, report status, and continue phase by phase without inventing results.
