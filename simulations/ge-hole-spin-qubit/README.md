# Ge/SiGe Hole Spin Qubit — Recovered Snapshot

This directory is a recovered snapshot of the annular-arc double-quantum-dot QTCAD simulation campaign.

## Important limitation

The complete local project directory is not stored in the ChatGPT file workspace. The original project was run locally under an `AnnularArc_SweetSpot_DQD_Ge` directory and included meshes, electrostatic HDF5 checkpoints, production scripts, and numerical result files. Those large/local files are **not reconstructed here**.

This repository snapshot therefore contains:
- a recovered low-field Zeeman tracking script,
- current scientific-status notes,
- the known production-path structure,
- enough provenance to identify what must later be copied from the workstation for a complete archival upload.

## Physics scope

The local project includes work on:
- Ge/SiGe double quantum dots,
- tunnel coupling and charge stability,
- magnetic anisotropy and `G = g^T g`,
- magnetic-field sweet spots,
- electrical susceptibility and charge-noise dephasing,
- conditional `T2*`,
- finite-field states for phonon-limited `T1`,
- coarse/baseline/fine mesh convergence.

## Current recovered status

At the last recovered checkpoint:
- coarse and baseline Zeeman campaigns: 30/30 points per dot,
- fine-left: 18/30 checkpoints,
- fine-right: queued sequentially,
- susceptibility: 24/30 per dot,
- angular susceptibility, sweet-spot, `T2*`, and angular `T1` stages queued,
- only one fine worker was used because peak RSS reached roughly 6.5 GB.

The baseline `G=g^Tg` observables and charge-stability quantities were still provisional/conditional because the fine-mesh and downstream validation campaigns were incomplete.

## Complete archival upload still needed from the workstation

Copy the original local folders when available, especially:
- `AnnularArc_SweetSpot_DQD_Ge/production/`
- `AnnularArc_SweetSpot_DQD_Ge/parameters/`
- `AnnularArc_SweetSpot_DQD_Ge/meshes/`
- `AnnularArc_SweetSpot_DQD_Ge/publication_results/`
- `AnnularArc_SweetSpot_DQD_Ge/codex_work/`

Large binary checkpoints such as `.npz`, `.hdf5`, and meshes should be handled deliberately rather than blindly committed.
