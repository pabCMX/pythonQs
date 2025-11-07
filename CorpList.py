from math import ceil
import random
import numpy as np
import secrets as st
class corpCreator:

    #
    # Creates a list of corporation tickers and generates a random set of
    # conditional variables for a simple brownian function.
    # @return array with [ticker, p0, mu, sigma, seed]
    #
    def corpList(corpNum):
        letterList = []
        corpList = []
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        tempString = ""
        corpName = ""
        corpInfo = []

        for i in range(0,corpNum):
            for j in range (0, random.randint(2,4)):
                letterList.append(alphabet[random.randint(0,25)])
            for k in letterList:
                tempString = tempString + k
            corpName = tempString.upper()
            if corpList.count(corpName) == 0:
                corpList.append(corpName)
                letterList = []
                tempString = ""
            else:
                letterList = []
                tempString = ""
        for i in corpList:
            seed = st.randbits(32)
            np.random.seed(seed)
            p0 = round(np.random.normal(250,1000),4)
            mu = round(np.random.normal(0,0.0000002), 8)
            sigma = round(np.random.normal(0,0.00009),8)
            if p0 < 0:
                p0 *= -1
            if sigma < 0:
                sigma *= -1
            if mu < 0:
                mu *= -1
            tempInfo = [i, p0, mu, sigma, seed]
            corpInfo.append(tempInfo)
        return corpInfo




