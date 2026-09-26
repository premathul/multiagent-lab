import pytest
from moltwin.models import MutationSpec
from moltwin.validation import validate_mutation_code

def test_mutation_code():
    spec = MutationSpec(chain_id="A", residue_number=359, reference_aa3="ILE", alternate_aa3="LEU")
    assert spec.pdbfixer_code == "ILE-359-LEU"

def test_identical_mutation_rejected():
    with pytest.raises(ValueError):
        validate_mutation_code("ILE", "ILE")
