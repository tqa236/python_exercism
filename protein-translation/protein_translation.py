def proteins(strand):
    codons = {"AUG": "Methionine",
              "UUU": "Phenylalanine", "UUC": "Phenylalanine",
              "UUA": "Leucine", "UUG": "Leucine",
              "UCU": "Serine", "UCC": "Serine",
              "UCA": "Serine", "UCG": "Serine",
              "UAU": "Tyrosine", "UAC": "Tyrosine",
              "UGU": "Cysteine", "UGC": "Cysteine",
              "UGG": "Tryptophan",
              "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}
    proteins = [codons[strand[i:i+3]] for i in range(0, len(strand), 3)]
    return proteins[:None if "STOP" not in proteins
                    else proteins.index("STOP")]
