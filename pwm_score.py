# k for calculating deltaSVM is 10 
# flanking region for PWM score is 1 kb long (500 bp on both sides): line[1] - 9 - 500, line[1] + 10 + 500
# PFMs obtained from JASPAR
import numpy as np
pfm = np.empty(shape=(0,14), dtype=float)
with open("../project_data/MA1102.1.pfm") as f:
    next(f)
    for line in f:
        line = line.split()
        for i in range(0,len(line)):
            line[i] = float(line[i])
        pfm = np.append(pfm, [line], axis=0)

f.close()
# Reading hg19 sequence file
genome = ''
with open("../project_data/chr22.fa") as f:
    next(f)
    for line in f:
        genome = genome + line.replace('\n','')
        
seq_mat = np.zeros((4, len(genome)))
# indices are defined in the order A, C, G, T
def nucleotide2ind(char):
    switcher = {
        'A': 0,
        'a': 0,
        'C': 1,
        'c': 1,
        'G': 2,
        'g': 2,
        'T': 3,
        't': 3,
    }
    return switcher.get(char)
for i in range(0, len(genome)):
    if (genome[i] != 'N' and genome[i] != 'n'):
        seq_mat[nucleotide2ind(genome[i]),i] = 1        

pfm_transpose = np.transpose(pfm)
position = 51066536
window = seq_mat[:, position : position + 14]
pfm_score = np.trace(np.matmul(pfm_transpose, window))

