import numpy as np

class CalcPLV():
    def ambiguity(self, x):
        C = np.fft.fft(x)
        return C

    def autocorrelation(self, x):
        result = np.correlate(x, x, mode='full')
        siz = int(result.size/2)
        return (result[siz:])

    def CalcDistribution(self, x):
        f1 = np.fft.fft(x)
        fin = np.fft.ifft(f1)
        return fin

    def CalcTFD(self, x):
        #print (x, "**")
        acf_x1 = CalcPLV.autocorrelation(self,x)
        #print (acf_x1)
        am_x1 = CalcPLV.ambiguity(self,acf_x1)
        #print(am_x1)
        rih_x1 = CalcPLV.CalcDistribution(self,am_x1)
        #print("**")
        #print(rih_x1)
        return (rih_x1)

    def phasediff(self, x1, x2):
        x3 = CalcPLV.CalcTFD(self, x1)
        x4 = CalcPLV.CalcTFD(self, x2)
        phi = np.angle(x3 * np.conjugate(x4))/(abs(x3)*abs(x4))
        #print (phi)
        return phi


if __name__ == '__main__':
    PLVobject = CalcPLV()

    x1 = [1,2+5j,3+1j]
    x2 = [2,4,6]
    #tfd = PLVobject.CalcTFD(z)
    #d = PLVobject.autocorrelation(z)
    #print (d, type(d))

    phis = PLVobject.phasediff(x1, x2)
    #print(phis)