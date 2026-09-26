from pathlib import Path
import typer
from rich import print
from .models import MutationSpec
from .validation import validate_mutation_code

app = typer.Typer(no_args_is_help=True)

@app.command()
def validate(chain: str, residue: int, ref: str, alt: str):
    """Validate a mutation specification before expensive modeling."""
    validate_mutation_code(ref, alt)
    spec = MutationSpec(
        chain_id=chain,
        residue_number=residue,
        reference_aa3=ref.upper(),
        alternate_aa3=alt.upper(),
    )
    print(f"[green]Valid mutation:[/green] {spec.pdbfixer_code} chain={spec.chain_id}")

@app.command()
def status():
    """Show implementation status for the research prototype."""
    print("[yellow]v0.1 scaffold:[/yellow] validation works; prep/simulation/analysis are TODO")
