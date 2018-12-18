# advanced_bioinformatics
Course Project - Quantifying effects of non coding variants

ASB_TFASB.py splits ASB data from files in the format specified by https://media.nature.com/original/nature-assets/ncomms/2016/160418/ncomms11101/extref/ncomms11101-s2.txt by TF

Second, binding preferences of a TFs have been
shown to be heterogeneous across different cell lines. For instance, Arvey et al. comprehensively analysed
ChIP-seq data for 67 TFs across multiple different and found that many cell-type-specific sequence models
were able to capture binding variability, which was primarily due to differences in heteromeric complex
formations
import matplotlib.pyplot as plt
import numpy as np
f = open('../codes/project_data/500bp/LR_input_all_CTCF_500.txt')
f.readline()
lines = f.readlines()
deltaSVM = []
PWM = []
for line in lines:
	line = line.split(',')
	deltaSVM.append(line[0])
	PWM.append(line[1])
PWM = np.array(PWM)
deltaSVM = np.array(deltaSVM)
plt.plot((PWM - min(PWM))(max(PWM) - min(PWM)), (deltaSVM - min(deltaSVM))/(max(deltaSVM) - min(detlaSVM))
plt.show()
