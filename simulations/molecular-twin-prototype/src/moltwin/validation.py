THREE_LETTER_AA = {
    "ALA","ARG","ASN","ASP","CYS","GLN","GLU","GLY","HIS","ILE",
    "LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR","VAL"
}

def validate_mutation_code(reference_aa3: str, alternate_aa3: str) -> None:
    ref = reference_aa3.upper()
    alt = alternate_aa3.upper()
    if ref not in THREE_LETTER_AA:
        raise ValueError(f"Unsupported reference residue: {ref}")
    if alt not in THREE_LETTER_AA:
        raise ValueError(f"Unsupported alternate residue: {alt}")
    if ref == alt:
        raise ValueError("Reference and alternate residues are identical")
