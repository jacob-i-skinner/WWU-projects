import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

#plot the curve
d = 10**-6
n = np.arange(1, 4, 0.00001)
T = lambda x: 6*(6.25+(x**-2)*(1-x**2)*(2.25-x**2)*(np.sin(x*2*np.pi*d/(5*10**-7))**2))**-1
#plt.plot(np.array([0,2*np.pi]), np.zeros(2), 'k-')
plt.plot(n, T(n), lw=4)
plt.scatter(1.1365142, 0.9936898, lw=8)

#plt.plot(np.array([0,2*np.pi]), np.ones(2), 'r--')
plt.savefig('glasses.pdf')
plt.show()