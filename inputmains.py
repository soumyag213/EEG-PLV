import pandas as pd
import inputs
#a = []


#def inputpatients():
#    for i in range(1,10):
#            if i < 10:
#                i = str(0) + str(i)
#            else:
#                i = str(i)

#            inputsamples(i)

def inputsamples():
    filename = []
    phasedifference = []
    k = ""
    print ("**")
    for i in range(1,15):
        if i<10:
            k = str(0)+str(i)
        else:
            k = str(i)
        filename.append("PLV_data/S002/S002R" + k + "_data.txt")
        X = pd.read_csv(filename[i-1], sep=",", header=None)
        #print(filename[i-1])
        #phasedifference.append(inputs.inputs(X,i))
    #print(filename)
    #print("read file")
    phasedifference.append(inputs.inputs(X, 0))
    #print(phasedifference)



if __name__ == '__main__':
    inputsamples()