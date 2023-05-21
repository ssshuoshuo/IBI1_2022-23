import re

def count_coding_sequences(seq):
    start_codons = ["ATG"]
    stop_codons = ["TAA", "TGA", "TAG"]
    coding_sequences = 0
    
    for start_codon in start_codons:
        start_positions = [m.start() for m in re.finditer(start_codon, 
seq)]
        
        for start_pos in start_positions:
            for stop_codon in stop_codons:
                stop_pos = seq.find(stop_codon, start_pos + 3)
                if stop_pos != -1 and (stop_pos - start_pos) % 3 == 0:
                    coding_sequences += 1
                    break
    
    return coding_sequences

seq = "ATGCAATCGACTACGATCTGAGAGGGCCTAA"
codeseq = count_coding_sequences(seq)
print(codeseq)
