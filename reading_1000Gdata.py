#### This program reads ASB data from a file (hardcoded in the script) and generates 1 file per TF  with ASB data ####
import numpy as np

#### Generating a list of TFs in the ASB data ####
TF = []
with open("project_data/ASB.auto.v2.1.aug16.txt") as f:
    next(f)
    for line in f:
        line = line.split("\t")
        tf = line[3].split("_")[0]
        print(tf)
        TF.append(tf)
TF = np.unique(TF)
print(TF)

#### Writing ASB data to files, one file per TF ####
with open("project_data/ASB.auto.v2.1.aug16.txt") as f:
    #Skip header
    next(f)
    for line in f:
        line = line.split()
        #print(line)
        tf = line[3].split("_")[0]
        ref_allele= line[4]
        #Existence of multiple alternate alleles separated by ;
        alt_alleles = line[5].split(";")
        #print(ra, aa)
        nt_count = {}
        nt_count['A'] = int(line[6])
        nt_count['C'] = int(line[7])
        nt_count['G'] = int(line[8])
        nt_count['T'] = int(line[9])
        g = open("ASB_"+tf+".txt", "a+")
        #print(temp_count)
        ref_allele_count = nt_count[ref_allele]
        for alt_allele in alt_alleles:
            l = line[0]+"\t"+str(line[1])+"\t"+ref_allele+"\t"+alt_allele+"\t"+str(ref_allele_count)+"\t"+str(nt_count[alt_allele])+"\n"
            g.write(l)
        g.close()
