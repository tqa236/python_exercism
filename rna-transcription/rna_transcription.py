def to_rna(dna_strand: str) -> str:
    dna2rna = {"C": "G", "G": "C", "T": "A", "A": "U"}
    return "".join([dna2rna[x] for x in dna_strand])
