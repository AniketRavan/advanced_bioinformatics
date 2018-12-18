import random
import time

random.seed(time.time())
g = open("SimulatedLRData.txt", "w")
g.write("Chr_Pos_Ref/Alt,DeltaSVMScore,PWMFlankingScore,Label\n")
for i in range(10000):
    l = str(i)+","+str(random.uniform(-1, 1))+","+str(random.uniform(-20,-1))+","+str(random.choice([0,1]))+"\n"
    g.write(l)
g.close()
