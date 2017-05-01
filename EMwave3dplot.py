from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
cmap = matplotlib.cm.get_cmap('Vega10')


fig = plt.figure()
ax = fig.gca(projection='3d')

n = 10 #number of planes to draw

planes = np.linspace(0,2*np.pi, num=n)
for i in range(n):

    x, y, z = np.meshgrid(planes[i],
                          np.arange(0, 2*np.pi, 1),
                          np.arange(0, 2*np.pi, 1))

    u = 0
    v = -np.sin(x)
    w = np.cos(x)
    ax.quiver(x, y, z, u, v, w, length=0.5, color = cmap(1 - i/n))
plt.xlim(0,2*np.pi)
plt.xlabel('$y$')
plt.ylabel('$z$')
ax.set_zlabel('$x$')
plt.savefig('spiralfield.pdf' )
plt.show()