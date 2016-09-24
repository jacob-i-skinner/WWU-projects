import numpy as np
from matplotlib import pyplot as plt

t = np.linspace (0,2, num = 1000)
plt.figure(figsize = (25,25))
fig = plt.subplot(111, projection = 'polar')
r = np.abs(-t+1)  
theta = -np.pi*t/4
plt.plot(theta, r, 'm')
plt.show()