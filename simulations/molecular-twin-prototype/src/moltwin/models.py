from pydantic import BaseModel, Field

class MutationSpec(BaseModel):
    chain_id: str = Field(min_length=1, max_length=4)
    residue_number: int = Field(gt=0)
    reference_aa3: str = Field(min_length=3, max_length=3)
    alternate_aa3: str = Field(min_length=3, max_length=3)

    @property
    def pdbfixer_code(self) -> str:
        return f"{self.reference_aa3.upper()}-{self.residue_number}-{self.alternate_aa3.upper()}"

class SimulationConfig(BaseModel):
    temperature_k: float = 300.0
    pressure_bar: float = 1.0
    timestep_fs: float = 2.0
    equilibration_ps: float = 100.0
    production_ps: float = 1000.0
    report_interval_steps: int = 1000
    padding_nm: float = 1.0
    ionic_strength_m: float = 0.15
    random_seed: int = 20260923

class TwinRunSpec(BaseModel):
    pdb_id: str | None = None
    pdb_path: str | None = None
    mutation: MutationSpec
    simulation: SimulationConfig = SimulationConfig()
