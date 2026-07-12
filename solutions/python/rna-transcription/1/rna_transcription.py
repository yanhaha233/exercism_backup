"""DNA转换"""

def to_rna(dna_strand):
    """DNA转换"""
    result = "" 
    
    for letter in dna_strand:
        if letter == "G":
            result += "C"
        elif letter == "C":
            result += "G"
        elif letter == "T":
            result += "A"
        else:
            result += "U"


    return result
