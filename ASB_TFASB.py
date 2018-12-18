#### This program reads ASB data from a file (hardcoded in the script) and generates 1 file per TF  with ASB data ####
import numpy as np

#### Generating a list of TFs in the ASB data ####
TF = []
with open("project_data/ASB.auto.v2.1.aug16.txt") as f:
    next(f)
    for line in f:
        line = line.split("\t")
        tf = line[3].split("_")[0]
        #print(tf)
        TF.append(tf)
TF = np.unique(TF)
f.close()
#print(TF)

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
        p = line[10]
        g = open("project_data/ASB_data/ASB_"+tf+".txt", "a+")
        #print(temp_count)
        ref_allele_count = nt_count[ref_allele]
        for alt_allele in alt_alleles:
            #print(p)
            if(float(p)<0.05):
                l = line[0]+"\t"+str(line[1])+"\t"+ref_allele+"\t"+alt_allele+"\t"+str(ref_allele_count)+"\t"+str(nt_count[alt_allele])+"\t1\n"
            else:
                l = line[0]+"\t"+str(line[1])+"\t"+ref_allele+"\t"+alt_allele+"\t"+str(ref_allele_count)+"\t"+str(nt_count[alt_allele])+"\t0\n"
            g.write(l)
        g.close()

#### Generating a list of TFs in the ASB data ####
TF = []
with open("project_data/ASB_other_GMs_1based.txt") as f:
    next(f)
    for line in f:
        tf = line[5]
        #print(tf)
        TF.append(tf)
TF = np.unique(TF)
#print(TF)

#### Writing ASB data to files, one file per TF ####
with open("project_data/ASB_other_GMs_1based.txt") as f:
    #Skip header
    next(f)
    count = 0
    for line in f:
        count += 1
        line = line.split()
        #print(line)
        tf = line[5]
        ref_allele= line[2]
        #Existence of multiple alternate alleles separated by ;
        alt_allele = line[3]
        #print(ra, aa)
        g = open("project_data/ASB_data/ASB_"+tf+".txt", "a+")
        #print(temp_count)
        ref_allele_count = line[6]
        alt_allele_count = line[7]
        if(line[10] == "ASB"):
            l = line[0]+"\t"+str(line[1])+"\t"+ref_allele+"\t"+alt_allele+"\t"+str(ref_allele_count)+"\t"+str(alt_allele_count)+"\t1\n"
        else:
            l = line[0]+"\t"+str(line[1])+"\t"+ref_allele+"\t"+alt_allele+"\t"+str(ref_allele_count)+"\t"+str(alt_allele_count)+"\t0\n"
        g.write(l)
        g.close()
