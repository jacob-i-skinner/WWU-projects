import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import axes3d
import matplotlib
cmap = matplotlib.cm.get_cmap('seismic')
rcParams.update({'figure.autolayout': True})

#plot the curve
y = np.arange(0, 2*np.pi, 0.001)
Ez = lambda y: np.cos(y)
Ex = lambda y: -np.sin(y)

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.linspace(0, 4*np.pi, num=100) 
y =  -np.sin(x)
z =  np.cos(x)

ax.plot(x, np.zeros(100),np.zeros(100))
ax.plot(x, y, z)
plt.ylabel('$x$')
plt.ylim(-2,2)
plt.xlabel('$y$')
ax.set_zlabel('$z$')
plt.savefig('spiral.pdf')
plt.show()