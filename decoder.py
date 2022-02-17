CODON = {
    'gct': 'A',
    'gcc': 'A',
    'gca': 'A',
    'gcg': 'A',
    'att': 'I',
    'atc': 'I',
    'ata': 'I',
    'cgt': 'R',
    'cgc': 'R',
    'cga': 'R',
    'cgg': 'R',
    'aga': 'R',
    'agg': 'R',
    'ctt': 'L',
    'ctc': 'L',
    'cta': 'L',
    'ctg': 'L',
    'tta': 'L',
    'ttg': 'L',
    'aat': 'N',
    'aac': 'N',
    'aaa': 'K',
    'aag': 'K',
    'gat': 'D',
    'gac': 'D',
    'atg': 'M',
    'ttt': 'F',
    'ttc': 'F',
    'tgt': 'C',
    'tgc': 'C',
    'cct': 'P',
    'ccc': 'P',
    'cca': 'P',
    'ccg': 'P',
    'caa': 'Q',
    'cag': 'Q',
    'tct': 'S',
    'tcc': 'S',
    'tca': 'S',
    'tcg': 'S',
    'agt': 'S',
    'agc': 'S',
    'gaa': 'E',
    'gag': 'E',
    'act': 'T',
    'acc': 'T',
    'aca': 'T',
    'acg': 'T',
    'tgg': 'W',
    'ggt': 'G',
    'ggc': 'G',
    'gga': 'G',
    'ggg': 'G',
    'tat': 'Y',
    'tac': 'Y',
    'cat': 'H',
    'cac': 'H',
    'gtt': 'V',
    'gtc': 'V',
    'gta': 'V',
    'gtg': 'V',
    'taa': '*',
    'tga': '*',
    'tag': '*'
 }

def complement(sequence: str) -> str:
    complement=""
    for s in sequence:
        if s=='a':
            complement+='t'
        elif s=='t':
            complement+='a'
        elif s=='c':
            complement+='g'
        elif s=='g':
            complement+='c'
    return complement

def decode(sequence: str) -> list:
    nseq = len(sequence)
    amino_acids = []
    for i in range(0, nseq-2, 3):
        amino_acids.append(CODON[sequence[i:i+3]])
    return amino_acids