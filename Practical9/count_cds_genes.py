import re

def count_cds_genes(input_file, stop_codon):
    with open(input_file, 'r') as f:
        contents = f.read()

    genes = re.findall(r'>([^\n]+)\n([ACTG\n]+?)' + stop_codon + r'\n', 
contents)
    output_file = stop_codon + '_stop_genes.fa'

    with open(output_file, 'w') as f:
        for gene_name, sequence in genes:
            cds_count = len(re.findall(stop_codon, sequence))
            fasta_entry = f'>{gene_name} {cds_count}\n{sequence}\n'
            f.write(fasta_entry)

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
stop_codon = input("Input your stop codon (TAA, TAG, or TGA): ")

count_cds_genes(input_file, stop_codon)
