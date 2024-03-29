import numpy as np
import readParams
import matplotlib.pyplot as plt


class waveFunction:
    def __init__(self, _parameterReduced):
        self.N = _parameterReduced.gridNum
        self.paramsReduced = _parameterReduced
        self.psiSpace = np.zeros((self.N, self.N), dtype=complex)
        self.phiWavevector = np.zeros((self.N, self.N), dtype=complex)


class reservoir:
    def __init__(self, _parameterReduced):
        self.N = _parameterReduced.gridNum
        self.nSpace = np.zeros((self.N, self.N), dtype=complex)
        self.nWavevector = np.zeros((self.N, self.N), dtype=complex)


class solver:
    def __init__(self, _parameterReduced):
        self.paramsR = _parameterReduced
        self.wv = waveFunction(_parameterReduced)


        self.nR = reservoir(_parameterReduced)
        self.N = _parameterReduced.gridNum
        self.M = _parameterReduced.timeSteps
        #self.recordWv2=np.array((self.M,self.N,self.N))

        self.deltaT = 1 / _parameterReduced.fractionTime
        self.wv.psiSpace += np.sqrt(self.paramsR.p0Reduced * self.deltaT) / self.paramsR.gridNum ** 2
        #outMatName='1.txt'
        #print(self.wv.psiSpace)
        #z=np.absolute(self.wv.psiSpace)
        #print(z.max())
        #with open(outMatName,'wb') as f:
         #   for line in np.absolute(self.wv.psiSpace):
          #      np.savetxt(f,line,fmt='%.4f')
        #########
        self.U = np.zeros((self.N, self.N), dtype=complex)
        self.P = np.zeros((self.N, self.N), dtype=complex)
        self.incrPhiWavevector = np.zeros((self.N, self.N), dtype=complex)
        self.incrNWavevector = np.zeros((self.N, self.N), dtype=complex)
        for k1 in range(0, self.N):
            k1C = self.centralize(k1)
            s1 = k1C ** 2
            for k2 in range(0, self.N):
                k2C = self.centralize(k2)
                sum2temp = s1 + k2C ** 2
                sum2temp *= self.deltaT
                self.incrPhiWavevector[k1][k2] = np.exp(-1j * self.paramsR.a * sum2temp)
                self.incrNWavevector[k1][k2] = np.exp(-1j * self.paramsR.DReduced * sum2temp)
                self.U[k1][k2] = self.paramsR.SReduced * sum2temp / 2
                self.P[k1][k2] = self.paramsR.p0Reduced * sum2temp / 2

    def centralize(self, k):
        return k - (self.N / 2 - 1)

    def evolve(self):
        #print("Enter evolve()")
        for m in range(1, self.M+1):
            ##update nR
            R = np.zeros((self.N, self.N), dtype=complex)
            R -= self.paramsR.beta + self.paramsR.eta * np.absolute(self.wv.psiSpace) ** 2


            incr1 = np.exp(-R * self.deltaT / 2)
            self.nR.nSpace = np.multiply(self.nR.nSpace, incr1)
            self.nR.nWavevector = np.fft.fft2(np.fft.fftshift(self.nR.nSpace))
            self.nR.nWavevector = np.multiply(self.nR.nWavevector, self.incrNWavevector)
            self.nR.nSpace = np.fft.ifftshift(np.fft.ifft2(self.nR.nWavevector))
            self.nR.nSpace = np.multiply(self.nR.nSpace, incr1)
            self.nR.nSpace += self.P


            ##update wv

            deltaF = self.paramsR.lambdaC * np.absolute(self.wv.psiSpace) ** 2 + (
                        self.paramsR.lambdaR + self.paramsR.b * 1j) * self.nR.nSpace - 1j / 2
            F = self.U + deltaF * self.deltaT

            expf = np.exp(-1j * F / 2)
            self.wv.psiSpace = np.multiply(self.wv.psiSpace, expf)
            self.wv.phiWavevector = np.fft.fft2(np.fft.fftshift(self.wv.psiSpace))
            self.wv.phiWavevector = np.multiply(self.wv.phiWavevector, self.incrPhiWavevector)
            self.wv.psiSpace = np.fft.ifftshift(np.fft.ifft2(self.wv.phiWavevector))
            self.wv.psiSpace = np.multiply(self.wv.psiSpace, expf)
           # self.recordWv2[m,]=np.absolute(self.wv.psiSpace)**2
            #save space
            spTmp=np.absolute(self.wv.psiSpace)**2
            outFileName='space'+str(m)+'.png'



            imSp=plt.imshow(spTmp,cmap='jet',interpolation='bilinear',extent=(-self.N/2+1,self.N/2,-self.N/2+1,self.N/2))
            plt.colorbar(imSp)
            plt.title('X Space Density at Step = '+str(m))
            plt.savefig(outFileName)
            plt.clf()

            #save wavevector
            wvkTmp=np.absolute(self.wv.phiWavevector)**2
            ofNamephi='wavevector'+str(m)+'.png'
            imWv=plt.imshow(wvkTmp,cmap='jet',interpolation='bilinear',extent=(-self.N/2+1,self.N/2,-self.N/2+1,self.N/2))
            plt.colorbar(imWv)
            plt.title('K Space Density at Step = '+str(m))
            plt.savefig(ofNamephi)
            plt.clf()





class solveAndPrint:
    def __init__(self, fileName):

        parsReduced = readParams.reducedParams(fileName)
        solution = solver(parsReduced)
        solution.evolve()
        psiSpaceNorm2=np.absolute(solution.wv.psiSpace)**2
        #plt.imshow(psiSpaceNorm2)
        #plt.show()

