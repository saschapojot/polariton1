import configparser

class params:
    def __init__(self,paramsFileName):
        self.paramsFileName=paramsFileName
        # original parameters
        self.hbar=1.0546E-34
        self.mLP=1
        self.gc=1
        self.gR=1
        self.gammaC=1
        self.gammaR=1
        self.R=1
        self.S=1
        # reduced parameters
        self.LENGTH=1
        self.ENERGY=1
        self.TIME=1


    def stringToFloat(self, valString):
        return float(valString)

    def readFile(self):
        reader=configparser.ConfigParser()
        reader.read(self.paramsFileName)
        sections=reader.sections()
        for parts in sections:
            for keys in reader[parts]:
                if keys=="mLP":
                    self.mLP=self.stringToFloat(reader[parts][keys])
                elif keys=="gc":
                    self.gc=self.stringToFloat(reader[parts][keys])
                elif keys=="gammaC":
                    self.gammaC=self.stringToFloat(reader[parts][keys])
                elif keys=="R":
                    self.R=self.stringToFloat(reader[parts][keys])
                elif keys=="S":
                    self.S=self.stringToFloat(reader[parts][keys])

    def initParams(self):
        self.gR=2*self.gc
        self.gammaR=1.5*self.gammaC
        #######

