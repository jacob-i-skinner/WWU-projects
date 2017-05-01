import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import axes3d
import matplotlib
cmap = matplotlib.cm.get_cmap('seismic')
rcParams.update({'figure.autolayout': True})

#plot the curve
y = np.arange(0, 2*np.pi, 0.001)
E = lambda y: np.sin(y)
plt.plot(np.array([0,2*np.pi]), np.zeros(2), 'k-')
plt.plot(y, E(y))

#plot the vectors
n = 15 #number of vectors to draw
vectors = np.zeros((n,6))
x = np.linspace(0, 2*np.pi, num=n)
for i in range(n):
    vectors[i][0] = x[i]
    vectors[i][3] = E(x[i])
#print(vectors)
X, Y, U, V = zip(*vectors)
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
plt.plot(np.array([0,2*np.pi]), np.ones(2), 'r--')
plt.plot(np.array([0,2*np.pi]), -np.ones(2), 'r--')
plt.xlim(0, 2*np.pi)
plt.ylabel('$B$ in the $z$ direction, in units of $\\frac{E_0}{c}$')
plt.xlabel('$y$ in units of $2\pi * \lambda$')
plt.savefig('By.pdf')
plt.show()