#### This program reads ASB data from a file (hardcoded in the script) and generates 1 file per TF  with ASB data ####
counts = {}
ref_allele = {}
alt_allele = {}
with open("project_data/ASB.auto.v2.1.aug16.txt") as f:
    next(f)
    for line in f:
        line = line.split()
        print(line)
        ra= line[4]
        aa = line[5].split(";")
        print(ra, aa)
        temp_count = {}
        temp_count['A'] = int(line[6])
        temp_count['C'] = int(line[7])
        temp_count['G'] = int(line[8])
        temp_count['T'] = int(line[9])
        print(temp_count)
        ref_allele[(line[1], line[2], line[3])] = temp_count[ra]
        alt_allele[(line[1], line[2], line[3])] = 0
        for i in aa:
		if (temp_count[i] >= 10):
	            alt_allele[(line[1], line[2], line[3])] += temp_count[i]
print(alt_allele)

