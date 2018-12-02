import numpy as np
file_object = open("wgEncodeAwgDnaseDukeAosmcUniPk.narrowPeak","r")

# Read range of peaks
peak_range = np.empty(shape=(0,2), dtype=int)
for line in file_object:
	words = line.split()
	peak_range_el = np.array(words[1:3])
	peak_range_el = peak_range_el.astype(int)
	if (peak_range_el[1] - peak_range_el[0] > 200):
		peak_range_el = peak_range_el.astype(int)
	peak_range = np.append(peak_range, [peak_range_el], axis=0)
	

print np.shape(peak_range)
print peak_range[3,:]

# Read sequence
file_object = open("Homo_sapiens.GRCh37.74.dna.chromosome.1.fa","r")
sequence = np.array(file_object.read())

windows = np.array([])
for i in range(0, len(peak_range)):
	for j in range(0, peak_range[i,1] - peak_range[i,0] + 200):
		windows = np.append(windows, sequence[peak_range[i,0] - 100 + j:peak_range[i,0] - 100 + j + 200])

	
	
print len(windows)
