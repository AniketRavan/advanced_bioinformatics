# Positions are imported from ABS data for every TF independently
# Output written as folder_path/genome_file_TF_filt.fa
#############################################################################################
# Reading from ASB data
import numpy as np

TFlist = ['CTCF', 'POL2', 'PU1', 'RPB2', 'SA1']
#TFlist = ['BATF']
for TFfile in TFlist:
    filename = 'project_data/ASB_Data/ASB_' + TFfile + '.txt'
    fR = open(filename)
    positions_list = [[] for i in range(0,22)]
    ref_nucleotide = [[] for i in range(0,22)]
    alt_nucleotide = [[] for i in range(0,22)]
    for line in fR:
        line = line.replace('\n', '')
        line = line.split('\t')
        chromosome = line[0]
        chromosome_num = int(chromosome.replace('chr',''))
        positions_list[chromosome_num - 1].extend([int(line[1])])
        ref_nucleotide[chromosome_num - 1].extend([line[2]])
        alt_nucleotide[chromosome_num - 1].extend([line[3]])
    fR.close()
    window_size = 18
    #print(len(alt_nucleotide))
    output_path = 'project_data/deltaSVM_data/'
    input_path = '/Users/prakruthiburra/Desktop/Chr/'

    fR = open(output_path + 'deltaSVM_data_' + TFfile + '_ref.fa','w+')
    fA = open(output_path + 'deltaSVM_data_' + TFfile + '_alt.fa','w+')

    for i in range(0, 22):
#############################################################################################
        fG = open(input_path + "chr" + str(i+1) + '.fa', 'r')
        fG.readline() # skip the first line
        genome = fG.readlines()
        fG.close()
        genome = ''.join(genome)
        genome = genome.replace('\n','')
        positions = positions_list[i]
        for j in positions:
            fR.write(">chr"+str(i+1)+"_"+str(j)+"_"+TFfile+"\n")
            fR.write(genome[j - window_size/2 : j + window_size/2 + 1])
            fR.write('\n')
            id = positions.index(j)
            alt = genome[j-window_size/2 : j]+alt_nucleotide[i][id]+genome[j+1: j + window_size/2 + 1]
            fA.write(">chr"+str(i+1)+"_"+str(j)+"_"+TFfile+"\n")
            fA.write(alt)
            fA.write('\n')
    fR.close()
    fA.close()
