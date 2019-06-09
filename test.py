import readParams

def main():
    pars=readParams.params('params.ini')
    pars.readFile()
    pars.initParams()
    pars.printParams()



if __name__=='__main__':
    main()