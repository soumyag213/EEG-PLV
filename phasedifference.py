import pandas as pd
import pickle
import numpy as np


def loads():

        file_Name = "TFD/1datasfile14"
        fileObject = open(file_Name, 'rb')
        b = []
        for i in range(1, 65):
            b.append(pickle.load(fileObject))
        print("calling the file again")
        print (len(b), len(b[0]))
        Calcphased(b)
        #print(b)


def Calcphased(b):
    c = [[0 for g in range(64)] for h in range(64)]
    #print(len(c), len(c[0]))
    for i in range(64):
        for j in range(64):
            a = np.angle(b[i] * np.conjugate(b[j]))
            g = a/(abs(b[i])*abs(b[j]))
            #d = np.exp(g)
            f = sum(g)
            h = f*(1/len(b[0]))
            c[i][j] = h
        #print(c[1][0])
    print (len(c), len(c[0]))
    writes(c)


def writes(c):
    file_write = "PLV/1plvs14"
    fileObjWrite = open(file_write, 'wb')
    pickle.dump(c, fileObjWrite)

    fileObject = open("1plvs1", 'rb')

    print(pickle.load(fileObject))


if __name__ == '__main__':
    b = loads()