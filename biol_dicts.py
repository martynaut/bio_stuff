
motifs_code = {
    'R': ['G', 'A'],
    'Y': ['U', 'C'],
    'M': ['A', 'C'],
    'K': ['G', 'U'],
    'S': ['G', 'C'],
    'W': ['A', 'U'],
    'H': ['A', 'C', 'U'],
    'B': ['G', 'U', 'C'],
    'V': ['G', 'C', 'A'],
    'D': ['G', 'U', 'A'],
    'N': ['G', 'U', 'A', 'C'],
}

translation_code = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

anti_translation_dict = {
    'Y': ['TAC', 'TAT'],
    'V': ['GTA', 'GTT', 'GTG', 'GTC'],
    'W': ['TGG'],
    'H': ['CAT', 'CAC'],
    'T': ['ACG', 'ACC', 'ACT', 'ACA'],
    'I': ['ATA', 'ATT', 'ATC'],
    'D': ['GAC', 'GAT'],
    'Q': ['CAA', 'CAG'],
    'A': ['GCC', 'GCT', 'GCA', 'GCG'],
    'P': ['CCC', 'CCT', 'CCG', 'CCA'],
    'N': ['AAC', 'AAT'],
    'L': ['CTA', 'CTC', 'TTG', 'CTG', 'TTA', 'CTT'],
    'C': ['TGT', 'TGC'],
    'G': ['GGA', 'GGC', 'GGT', 'GGG'],
    'K': ['AAA', 'AAG'],
    '_': ['TGA', 'TAG', 'TAA'],
    'R': ['CGT', 'CGC', 'AGG', 'AGA', 'CGG', 'CGA'],
    'S': ['AGC', 'TCC', 'TCG', 'TCA', 'AGT', 'TCT'],
    'E': ['GAA', 'GAG'],
    'F': ['TTC', 'TTT'],
    'M': ['ATG'],

}

def make_detranslation_dict():
    anti_translation_dict = {}
    for key, value in translation_code.items():
        if value not in anti_translation_dict.keys():
            anti_translation_dict[value] = [key]
        else:
            anti_translation_dict[value].append(key)
    return anti_translation_dict
