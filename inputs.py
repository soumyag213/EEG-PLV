import pandas as pd
import CalculatePLV
import numpy as np
import pickle
X = pd.read_csv('PLV_data/S001/S001R01/S001R01_data.txt', sep=",", header=None)
def inputs(X,i):
    #open pickle for writing input data
    file_Name = ("testfile"+str(i))
    fileObject = open(file_Name,'wb')

    #x1 = X[1]
    #x2 = X[2]
    #x3 = X[3]

    #Calculate phase difference between two electrodes, pickle data into file
    PLVobject = CalculatePLV.CalcPLV()

    for i in range(1,3):
        for j in range(i,3):
            phis = PLVobject.phasediff(X[i], X[j])
            pickle.dump(phis, fileObject)
            #to track progress of pickling
            print ("pickled" + str(i))


    # here we close the fileObject
    fileObject.close()
    # we open the file for reading
    fileObject = open(file_Name,'rb')

    # load the object from the file into var b
    # we'll have to load the object as many times as it has been pickled. Unpicklimg lies in layers.
    # the file is saved as FIFO
    b = []
    for i in range(1,3):
        for j in range(i,3):
            b.append(pickle.load(fileObject))
    print (b)
    return b






