import numpy as np
from matplotlib import pyplot as plt

x = np.linspace (0,2, num = 1000)
circle_top = np.sqrt(1-(x-1)**2)+1
plt.plot(x, circle_top, 'k')
plt.plot(x, -circle_top+2, 'k')
r = ((np.sqrt(2)-1)/2)
small = np.sqrt(r**2-(x-r)**2)+r
plt.plot = (x, small, 'r')
#plt.xlim(0,2)
#plt.ylim(0,2)
plt.show()