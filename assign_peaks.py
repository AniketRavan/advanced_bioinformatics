import numpy as np
import math
import matplotlib.pyplot as plt
file_object = open("../project_data/wgEncodeAwgDnaseDukeAosmcUniPk.narrowPeak","r")

def nucleotide2num(char):
    switcher = {
        'A': 0,
        'C': 1,
        'G': 2,
	'T': 3,
    }
    return switcher.get(char)



def kmer2index(string):
	score = 0;
	multiplier = 1;
	for i in range(0,len(string)):
		score = score + nucleotide2num(string[len(string) - i - 1])*multiplier
		multiplier = multiplier*4;
	return score
	

feature_length = 100
# Read range of peaks
peak_range = np.empty(shape=(0,2), dtype=int)
for line in file_object:
	words = line.split()
	peak_range_el = np.array(words[1:3])
	peak_range_el = peak_range_el.astype(int)
#	if (peak_range_el[1] - peak_range_el[0] > 200):
#		peak_range_el = peak_range_el.astype(int)
	peak_range = np.append(peak_range, [peak_range_el], axis=0)
	

#print np.shape(peak_range)
#print peak_range[3,:]
file_object.close()

# Read sequence
file_object = open("../project_data/Homo_sapiens.GRCh37.74.dna.chromosome.1.fa","r")
#	sequence = np.array(file_object.read())
line = file_object.readline()
sequence = ''
for line in file_object:
	sequence = sequence + line.replace('\n','')
#print len(sequence)
#print len(peak_range)


# Generate vector of window-indices having binding events
event_window_index = []
for i in range(0, len(peak_range)):
	lower_bound = int(math.ceil((peak_range[i,0] - 500)/200))
	upper_bound = int(math.floor((peak_range[i,1] - 500)/200) + 1)
	event_window_index = np.append(event_window_index, range(lower_bound, upper_bound))


# Counting k-mers
k = 5
kmer_matrix = np.array([[0]*(4**k)]*len(event_window_index))

idx = 0 # index of element in event_window_index
for i in event_window_index:
	windows = sequence[400 + 200*int(i):600 + 200*int(i)] #i is a float
	if (windows.find('N') == -1):
		for j in range(0,len(windows)):		
			kmer_matrix[idx][kmer2index(windows[j: j+k])] += 1
	idx += 1
			# windows = np.append(windows, sequence[x:x+200])	
mat_file = np.matrix(kmer_matrix)
with open('positive_set.txt','wb') as f:
    for line in mat_file:
        np.savetxt(f, line, fmt='%.2f')

plt.plot(range(0, 4**k), kmer_matrix[20][:])
plt.show()
