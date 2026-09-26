"""OpenMM simulation layer.

Codex should implement deterministic matched setup for reference and mutant:
- same force field and water model
- same padding and ionic strength
- same minimization/equilibration protocol
- recorded OpenMM platform and version
- independent but recorded random seeds
- CPU fallback; GPU when available
"""

from pathlib import Path
from .models import SimulationConfig


def run_md(prepared_pdb: str | Path, output_dir: str | Path, config: SimulationConfig) -> dict:
    raise NotImplementedError
