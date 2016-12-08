from matplotlib import pyplot as plt
import numpy as np
t = np.linspace(0, 1, num=1000)
terms = 20
F = np.zeros(len(t))
x=0.25
for i in range(len(t)):
    for j in range(0,terms):
        F[i] += np.e**(-(2*j+1)**2*np.pi**2*t[i])*(8/np.pi**2)*((-1)**j)*np.sin((2*j+1)*np.pi*x)/((2*j+1)**2)
plt.figure(figsize=(15,15))
#plt.plot(-np.ones(len(x)), x, 'k', lw=2)
#plt.plot(np.ones(len(x)), x, 'k', lw=2)
plt.plot(t, np.zeros(len(t)), 'k', lw=2)
plt.plot(t,F, 'r', lw=4)
plt.ylim(0,0.51)
plt.xlabel(r"Time (s)", fontsize=60)
plt.ylabel(r"Temperature (degrees C)", fontsize=60)
plt.title('Temp. at L/4', fontsize=(60))
plt.show()