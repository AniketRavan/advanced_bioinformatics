from itertools import izip
#TFlist = ['CTCF' 'PU1']
TFlist = ['CTCF']
for TFfile in TFlist:
    fname = "LR_input_"+TFfile+".txt"
    f = open(fname, "w")
    f.write("Chr_Pos_Ref/Alt,DeltaSVMScore,PWMFlankingScore,Label\n")
    with open("project_data/SimulatedDeltaSVM_output_CTCF.txt") as textfile1, open("project_data/ASB_data/ASB_sorted_CTCF.txt") as textfile2:
        for x, y in izip(textfile1, textfile2):
            x = x.strip().split()
            y = y.strip().split()
            f.write(x[0]+","+x[1]+","+y[6]+","+y[6]+"\n")
