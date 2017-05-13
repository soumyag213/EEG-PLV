import numpy as np

def autoco(X):
    i = len(X)
    #print (i)
    acf = [[0 for g in range(3)] for h in range(2)]
    for n in range(i):
        for t in range(i):
            m = (n+t)%i
            acf[n][t] = X[n]*np.conjugate(X[m])
    print(acf)

if __name__ == '__main__':
    X = [1,2,3,4,5]
    autoco(X)