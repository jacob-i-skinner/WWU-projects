from matplotlib import pyplot as plt
import numpy as np
t = np.linspace(0, 1, num=1000)
terms = 100
n = np.arange(0,terms)
F = np.zeros(terms)
dF = np.zeros(terms)
for i in range(terms):
    for j in range(0,i):
        F[i] += (-(2*j+1)**2*np.pi**2)*(8/np.pi**2)*((-1)**j)*np.sin((2*j+1)*np.pi*0.5)/((2*j+1)**2)

#for i in range(len(t)):
#    for j in range(0,terms):
#        F[i] += (-(2*j+1)**2*np.pi**2)*np.e**(-(2*j+1)**2*np.pi**2*t[i])*(8/np.pi**2)*((-1)**j)*np.sin((2*j+1)*np.pi*0.5)/((2*j+1)**2)

plt.figure(figsize=(15,15))
#plt.plot(-np.ones(len(x)), x, 'k', lw=2)
#plt.plot(np.ones(len(x)), x, 'k', lw=2)
plt.plot(t, np.zeros(len(t)), 'k', lw=2)
plt.plot(n,F, 'r.', lw=4)
#plt.ylim(0,1)
plt.ylabel(r"$\frac{dT}{dt}$ $(\frac{\degree C}{s})$", fontsize=60)
plt.xlabel(r"number of terms calculated", fontsize=60)
plt.title('Time derivative of temp. at (L/2, 0)', fontsize=(60))
plt.show()