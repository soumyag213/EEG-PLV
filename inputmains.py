import pandas as pd
import inputs
#a = []
filename = []
phasedifference = []
for i in range(1,2):
    filename.append("PLV_data/S001/S001R0"+ str(i)+"/S001R0" + str(i) + "_data.txt")
    X = pd.read_csv(filename[i-1], sep=",", header=None)
    phasedifference.append(inputs.inputs(X,i))

print(phasedifference)