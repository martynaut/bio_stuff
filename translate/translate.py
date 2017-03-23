
"""Script for translating given sequence."""

from translate_dicts import translation_code
import regex as re


def translate(sequence, start=False, Frame='all'):
    if Frame == 'all':
        frames = [0, 1, 2]
    else:
        frames = [int(Frame)]
    if start is True:
        starts = re.finditer(r'ATG.*', sequence, overlapped=True)
        results = [match.group(0) for match in starts]
        # print(results)
        prot_sequences = []
        for j in results:
            prot_sequences.append('')
            for i in range(0, len(j), 3):
                prot_sequences[len(prot_sequences)-1] =\
                    prot_sequences[len(prot_sequences)-1] +\
                    translation_code[j[i:i+3]]
                if len(j[i+3+1:]) < 3:
                    break
    else:
        prot_sequences = ['', '', '']
        for j in frames:
            for i in range(j, len(sequence), 3):
                prot_sequences[j] = prot_sequences[j] +\
                                    translation_code[sequence[i:i+3]]
                if len(sequence[i+3+1:]) < 3:
                    break

    return prot_sequences


# translate('ACTGGTCAGCATGGGCTATGA', Frame = 1, start=True)
