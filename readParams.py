import scipy



class params:
    def __init__(self, paramsFileName):
        self.paramsFileName = paramsFileName
        #self.paramDict = dict()
        # original parameters

        self.hbar = 1.0546E-34
        self.mLP = 9.109E-31*(1E-4)
        self.gc = (6E-3)*(1E-3)*(1.60218E-19)*(1E12)

        self.gammaC = 0.33E12

        self.R = (0.01E-12)*(1E12)
        self.S = (2E-3)*(1E-3)*(1.60218E-19)*(1E12)


        self.p0 =(1.5E-3)*(1E-3)*(1.60218E-19)*(1E12)
        self.timeSteps = 200
        self.gR = 1
        self.gammaR = 1
        self.D = 1

        # value scales
        self.LENGTH = 1
        self.ENERGY = 1
        self.TIME = 1


        self.initParams()










    def initParams(self):
        self.gR = 2 * self.gc
        self.gammaR = 1.5 * self.gammaC
        self.LENGTH = scipy.sqrt(self.hbar / (self.mLP * self.gammaC))
        self.TIME = 1 / self.gammaC
        self.ENERGY = self.hbar * self.gammaC




class reducedParams(params):
    def __init__(self, paramsFileName):
        super(reducedParams,self).__init__(paramsFileName)
        # scaling parameters
        self.L = self.LENGTH
        self.a = self.hbar / (2 * self.mLP * self.gammaC * self.L ** 2)
        self.SReduced =  self.S / (self.hbar * self.gammaC)
        self.lambdaC =  self.gc / (self.hbar * self.gammaC * self.L ** 2)
        self.lambdaR =  self.gR / (self.hbar * self.gammaC * self.L ** 2)
        self.b =  self.R / (2 * self.L ** 2 * self.gammaC)
        self.beta =  self.gammaR / self.gammaC
        self.eta =  self.R / (self.L ** 2 * self.gammaC)
        self.p0Reduced =  self.p0 * self.L ** 2 / self.gammaC
        self.DReduced =  self.D / (self.L ** 2 * self.gammaC)
        self.timeSteps =  self.timeSteps
        self.fractionTime = 500
        self.gridNum = 100
