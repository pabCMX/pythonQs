import numpy as np
import matplotlib.pyplot as plt
from CorpList import corpCreator as cc


corpNum = 30
time = 23400
corpList = cc.corpList(corpNum)
subplotYAxis = 3
subplotXAxis = round(corpNum/subplotYAxis)
fig, axs = plt.subplots(subplotYAxis, subplotXAxis)
j = k = 0


for i,arr in enumerate(corpList):
    name = arr[0]
    p0 = arr[1]
    mu = arr[2]
    sigma = arr[3]
    np.random.seed(arr[4])
    returns = np.random.normal(loc=mu, scale=sigma, size=time)
    price = p0*(1+returns).cumprod()
    axs[j, k].plot(price)
    axs[j, k].set_title(name)
    if j == subplotYAxis-1:
        k += 1
        j = 0
    else:
        j += 1
plt.show()