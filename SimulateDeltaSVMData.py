import random
f = open("project_data/deltaSVM_data/deltaSVM_data_CTCF_alt.fa", "r")
g = open("project_data/SimulatedDeltaSVM_output_CTCF.txt", "w")
for line in f:
    line = line.replace("\n", "")
    g.write(line+"\t"+str(random.uniform(-20,20))+"\n")
    f.next()
