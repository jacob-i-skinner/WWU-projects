from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(-4, 4, num=1000)

y0= np.exp(-(x**2)/2)/np.sqrt(np.sqrt(np.pi))
y1= np.exp(-(x**2)/2)*(x)/np.sqrt(np.sqrt(np.pi)*2)
y2= np.exp(-(x**2)/2)*(x**2-1)/np.sqrt(np.sqrt(np.pi)*8)
y3= np.exp(-(x**2)/2)*(x**3-3*x)/np.sqrt(np.sqrt(np.pi)*48)

plt.figure(figsize=(15,15))
plt.plot(x, np.zeros(len(x)), 'k', lw=2)
plt.plot(np.zeros(len(x)), x, 'k', lw=2)
plt.plot(x,y0, 'm', lw=4)
#plt.plot(x,y1, 'm', lw=4)
#plt.plot(x,y2, 'm', lw=4)
#plt.plot(x,y3, 'm', lw=4)
plt.ylim(-0.5,1)
plt.xlim(-4,4)
#plt.xlabel(r"Position (m)", fontsize=60)
#plt.ylabel(r"Temperature (degrees C)", fontsize=60)
plt.title('n=0', fontsize=(40))
plt.savefig('harmonic0.png', dpi=300)