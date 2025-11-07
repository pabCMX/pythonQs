import numpy as np
import matplotlib.pyplot as plt


mu = 0.000001
sigma = 0.000001
time = 100
p0 = 100

np.random.seed(1)
returns = np.random.normal(loc=mu, scale=sigma, size=time)
price = p0*(1+returns).cumprod()
fig, ax = plt.subplots()
ax.plot(price)
plt.show()