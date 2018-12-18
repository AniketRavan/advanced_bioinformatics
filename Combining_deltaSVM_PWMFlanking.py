from itertools import izip
#TFlist = ['CTCF' 'PU1']
TFlist = ['CTCF']
for TFfile in TFlist:
    fname = "LR_input_trimmed2_"+TFfile+".txt"
    f = open(fname, "w")
    #f.write("DeltaSVMScore,PWMFlankingScore,Label\n")
    #f.write("DeltaSVMScore,Label\n")
    f.write("PWMFlankingScore,Label\n")
    with open("project_data/deltaSVM_output_CTCF") as textfile1, open("project_data/ASB_data/ASB_sorted_CTCF_pwm.txt") as textfile2:
        for x, y in izip(textfile1, textfile2):
            x = x.strip().split()
            y = y.strip().split()
            #f.write(x[1]+","+y[7]+","+y[6]+"\n")
            #f.write(x[1]+","+y[6]+"\n")
            f.write(y[7]+","+y[6]+"\n")
