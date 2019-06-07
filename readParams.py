import configparser
import scipy
import io
import re



class params:
    def __init__(self,paramsFileName):
        self.paramsFileName=paramsFileName
        self.paramDict=dict()
        # original parameters
        self.hbar=1.0546E-34
        self.mLP= 9.109E-31*1E-4
        self.gc=(6E-3)*(1E-3)*(1.60218E-19)*(1E12)
        self.gR=1
        self.gammaC= 0.33E12
        self.gammaR=1
        self.R=(0.01E-12)*(1E12)
        self.S=(2E-3)*(1E-3)*(1.60218E-19)*(1E12)
        self.D=1
        self.p0=(1.5E-3)*(1E-3)*(1.60218E-19)*(1E12)
        self.timeSteps=100
        # value scales
        self.LENGTH=1
        self.ENERGY=1
        self.TIME=1




    def stringToFloat(self, valString):
        return float(valString)

    def loadFile(self):
        return tuple(io.open(self.paramsFileName,'r'))
    def parseLine(self,oneLine):
        patternSection=re.compile("\[\w+\]#*")
        patternComment=re.compile("\s*#")
        patternKeyval=re.compile("\s*\w+=\w+#*")

    def readFile(self):
        linesBuffer=self.loadFile()








    def initParams(self):
        self.gR=2*self.gc
        self.gammaR=1.5*self.gammaC
        self.LENGTH=scipy.sqrt(self.hbar/(self.mLP*self.gammaC))
        self.TIME=1/self.gammaC
        self.ENERGY=self.hbar*self.gammaC


    def printParams(self):
        print(self.mLP)
        print(self.gc)
        print(self.gammaC)
        print(self.R)
        print(self.S)
        print(self.D)
        print(self.p0)



class reducedParams:
    def __init__(self, _parameters):
        #scaling parameters
        self.L=_parameters.LENGTH
        self.gammaC=_parameters.gammaC
        self.hbar = 1.0546E-34
        self.mLP=_parameters.mLP
        #reduced parameters
        self.a=self.hbar/(2*self.mLP*self.gammaC*self.L**2)
        self.SReduced=_parameters.S/(self.hbar*self.gammaC)
        self.lambdaC=_parameters.gc/(self.hbar*self.gammaC*self.L**2)
        self.lambdaR=_parameters.gR/(self.hbar*self.gammaC*self.L**2)
        self.b=_parameters.R/(2*self.L**2*self.gammaC)
        self.beta=_parameters.gammaR/self.gammaC
        self.eta=_parameters.R/(self.L**2*self.gammaC)
        self.p0Reduced=_parameters.p0*self.L**2/self.gammaC
        self.DReduced=_parameters.D/(self.L**2*self.gammaC)
        self.timeSteps=_parameters.timeSteps
        self.fractionTime=500
        self.gridNum=100





