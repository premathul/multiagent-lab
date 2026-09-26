"""Structure preparation layer.

Important implementation constraint for Codex:
- Validate residue numbering and chain identity before mutation.
- Do not silently infer a residue if numbering differs.
- Current PDBFixer has a reported interaction between applyMutations() and
  findMissingResidues() for chains with SEQRES gaps. Build tests around this.
- Prefer a workflow that resolves/fixes missing residues before mutation, or use
  an alternate mutation path when necessary, and always verify the final sequence.
"""

from pathlib import Path
from .models import MutationSpec


def prepare_reference_and_mutant(
    pdb_source: str,
    mutation: MutationSpec,
    output_dir: str | Path,
) -> tuple[Path, Path]:
    raise NotImplementedError
