# Positions are imported from ABS data for every TF independently
# Output written as folder_path/genome_file_TF_filt.fa
#############################################################################################
# Reading from ASB data
import numpy as np

TF = 'BATF'

filename = '/home/aniket/Desktop/bioinfo/CS598SS/codes/project_data/ASB_Data/ASB_' + TF + '.txt'
fR = open(filename)
positions_list = [[] for i in range(0,22)]
ref_nucleotide = [[] for i in range(0,22)]
for line in fR:
    line = line.replace('\n', '')
    line = line.split('\t')
    chromosome = line[0]
    chromosome_num = int(chromosome.replace('chr',''))
    positions_list[chromosome_num - 1].extend([int(line[1])])
    ref_nucleotide[chromosome_num - 1].extend([line[2]])
fR.close()
window_size = 5000
folder_path = '/home/aniket/Desktop/bioinfo/CS598SS/project_data/genome/'
# positions = [43023]  # Obtained from ASB data

#############################################################################################
for i in range(0, 22):
    genome_file = 'chr' + str(i + 1)
    fW = open(folder_path + genome_file + '_' + TF + '_filt.fa','w')
    fR = open(folder_path + genome_file + '.fa')
    fR.readline() # skip the first line
    genome = fR.readlines()
    fR.close()
    genome = ''.join(genome)
    genome = genome.replace('\n','')
    positions = positions_list[i]
    ref_nucleotides = ref_nucleotide[i]
    for i in positions:
        fW.write(genome[i - window_size/2 : i + window_size/2 - 1])
        fW.write('\n')
    fW.close()
    
