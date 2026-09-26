from dataclasses import dataclass, asdict
from pathlib import Path
import json

@dataclass
class ComparisonMetrics:
    reference_mean_rmsd_nm: float | None = None
    mutant_mean_rmsd_nm: float | None = None
    reference_rg_nm: float | None = None
    mutant_rg_nm: float | None = None
    notes: list[str] | None = None

    def to_json(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(asdict(self), indent=2))


def compare_trajectories(reference_traj: str, mutant_traj: str, topology: str) -> ComparisonMetrics:
    """Placeholder for MDTraj-based matched trajectory analysis.

    Codex should implement RMSD, RMSF, Rg, SASA, H-bond counts, and configurable
    local residue metrics. It must align trajectories consistently and preserve units.
    """
    raise NotImplementedError
