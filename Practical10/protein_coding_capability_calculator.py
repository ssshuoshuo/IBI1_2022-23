import re

def protein_coding_capability(sequence):
    coding_sequence = re.findall('ATG(.*?)TGA', sequence, re.IGNORECASE)
    coding_sequence = ''.join(coding_sequence)
    percentage = 100 * len(coding_sequence) / len(sequence)

    if len(set(sequence) - set('ATCGatcg')) == 0:
        if percentage > 50:
            return percentage, "It's a protein-coding sequence."
        elif percentage < 10:
            return percentage, "It's a non-coding sequence."
        else:
            return percentage, "It's unclear."
    else:
        return 'Illegal character.'

# Example function calls
sequence1 = 'ATGGGGgGGGGgGGGGGGGGGGGGGGGGGGGGGGGGGGGGGTGA'
result1 = protein_coding_capability(sequence1)
print(*result1)

sequence2 = 'ATgaActGA'
result2 = protein_coding_capability(sequence2)
print(*result2)

sequence3 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGAAcTGA'
result3 = protein_coding_capability(sequence3)
print(*result3)

sequence4 = 'ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGAAATGA'
result4 = protein_coding_capability(sequence4)
print(result4)
