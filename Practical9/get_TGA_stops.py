import re

def extract_TGA_genes(input_file, output_file):
    with open(input_file, 'r') as f:
        contents = f.read()
    
    genes = re.findall(r'>[^|\n]+(\n[ACTG\n]+?)TGA\n', contents)
    extracted_sequences = '\n'.join(genes)
    
    with open(output_file, 'w') as f:
        f.write(extracted_sequences)

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'TGA_genes.fa'

extract_TGA_genes(input_file, output_file)
