# Molecular Twin Prototype

Research-only prototype for converting a human coding variant into a personalized protein model, running matched reference/mutant molecular dynamics, and producing a structured comparison report.

## Scope v0.1

Input:
- protein structure (PDB ID or local PDB)
- chain ID
- residue mutation (e.g. ILE-359-LEU)
- optional variant metadata from a VCF/JSON fixture

Pipeline:
1. Validate structure and residue identity.
2. Prepare reference structure.
3. Prepare mutant structure.
4. Solvate/neutralize using identical settings.
5. Minimize and equilibrate both systems.
6. Run matched short MD trajectories.
7. Compute RMSD, RMSF, radius of gyration, SASA, H-bond counts, and selected residue distances.
8. Produce JSON + Markdown report with explicit separation of clinical evidence vs simulation output.

## Non-goals
- No diagnosis.
- No medication recommendation.
- No claim that MD predicts clinical outcomes.
- No full-human simulation.

## Recommended environment
OpenMM 8.6+, PDBFixer, MDTraj, NumPy, Pandas, Typer, Pydantic, pytest.

## Codex goal
Implement this repository incrementally, keeping every scientific assumption explicit and tested. Start by making one reference/mutant protein pair reproducible before adding VCF automation or a web UI.
