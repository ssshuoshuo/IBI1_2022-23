import pandas as pd
import re


def align(seq1, seq2, blosum_matrix):
    score = 0
    identity = 0
    for i, j in zip(seq1, seq2):
        score += blosum_matrix[i][j]
        if i == j:
            identity += 1
    return score, identity


def read_blosum_matrix(filename):
    data = pd.read_excel(filename, index_col=0)
    return data.to_dict()


def read_fasta_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    sequence = ''.join(lines[1:]).replace('\n', '')
    return sequence


blosum_matrix = read_blosum_matrix('BLOSUM.xlsx')

human = read_fasta_file('ACE2_human.fa')
mouse = read_fasta_file('ACE2_mouse.fa')
cat = read_fasta_file('ACE2_cat.fa')

human_mouse_score, human_mouse_identity = align(human, mouse, 
blosum_matrix)
cat_mouse_score, cat_mouse_identity = align(cat, mouse, blosum_matrix)
human_cat_score, human_cat_identity = align(human, cat, blosum_matrix)

print("human, mouse:", human_mouse_score, human_mouse_identity)
print("cat, mouse:", cat_mouse_score, cat_mouse_identity)
print("human, cat:", human_cat_score, human_cat_identity)
