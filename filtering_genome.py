#import numpy as np
# Positions should be imported from ABS data for every TF independently
#############################################################################################
window_size = 5000
folder_path = '../project_data/'
positions = [43023]  # Obtained from ASB data
genome_file = 'chr22'
TF = 'TF'
#############################################################################################
fW = open(folder_path + genome_file + TF + '_filt.fa','w')
fR = open(folder_path + genome_file + '.fa')
fR.readline() # skip the first line
genome = fR.readlines()
fR.close()
genome = ''.join(genome)
genome = genome.replace('\n','')
for i in positions:
    fW.write(genome[i - 2500 : i + 2499])
    fW.write('\n')
fW.close()
