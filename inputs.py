import pandas as pd
import CalculatePLV
import numpy as np
import pickle

def inputs(X):
    #open pickle for writing input data
    file_Name = ("TFD/S002/2datasfile10")
    #file_Name = ("1datasfile" + str(i+1))
    fileObject = open(file_Name,'wb')
    print("inside inputs")
    #Calculate phase difference between two electrodes, pickle data into file
    #PLVobject = CalculatePLV.CalcPLV()
    #print ("initialized shizz")
    CallTFD(X, fileObject)
    # here we close the fileObject
    fileObject.close()
    print("now printing files made")
    b = OpenFilesTFD(file_Name, fileObject)

def CallTFD(X, fileObject):
    PLVobject = CalculatePLV.CalcPLV()

    for i in range(1,65):
        phis = PLVobject.CalcTFD(X[i])
        #print(phis)
        #print(phis.size, "size of calcTFD")
        #print (len(X[i]))
        #print (X[i])
        pickle.dump(phis, fileObject)
        #to track progress of pickling
        print ("pickled" + str(i))

def OpenFilesTFD(file_Name, fileObject):
    # we open the file for reading
    fileObject = open(file_Name, 'rb')

    # load the object from the file into var b
    # we'll have to load the object as many times as it has been pickled. Unpickling lies in layers.
    # the file is saved as FIFO
    b = []
    for i in range(1, 65):
        b.append(pickle.load(fileObject))
    print("calling the file again")
    print (len(b), len(b[0]))
    print("the contents")
    print(b)
    #print(b)
    return b


def OpenFilesphasediff(file_Name, fileObject):
    # we open the file for reading
    fileObject = open(file_Name, 'rb')

    # load the object from the file into var b
    # we'll have to load the object as many times as it has been pickled. Unpickling lies in layers.
    # the file is saved as FIFO
    b = []
    for i in range(1, 64):
        for j in range(i, 64):
            b.append(pickle.load(fileObject))
    print (len(b), len(b[0]))

    return b

def Callphasediff(X, fileObject):
    PLVobject = CalculatePLV.CalcPLV()

    for i in range(1,64):
        for j in range(i,64):
            #phis = PLVobject.CalcTFD(X[i])
            phis = PLVobject.phasediff(X[i], X[j])
            pickle.dump(phis, fileObject)
            #to track progress of pickling
            print ("pickled" + str(i))
    return phis

if __name__ == '__main__':
    filename = "PLV_data_raw/S002/S002R10_data.txt"
    X = pd.read_csv(filename, sep=",", header=None)
    inputs(X)
    #print(X[1])
    #for i in range(1,65):
    #    print(i)