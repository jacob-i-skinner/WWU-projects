from matplotlib import pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 48})

#slits
x = np.linspace(-1,1,num=200)
A = np.zeros(len(x))
for i in range(len(x)):
    if i > 35 and i < 65:
        A[i] = 1
    if i > 135 and i < 165:
        A[i] = 1

#the period of the signal is 2pi


d, w = 3, 0.5

I = lambda x: (np.cos(d*np.pi*x)*np.sin(w*x*np.pi)/(w*x*np.pi))**2

#x = np.linspace(-10,10, num=1000)
plt.figure(figsize=(15,15))
plt.plot(x, A, 'm', lw=4)
#plt.plot(x, I(x), 'm', lw=3)
plt.plot(np.zeros(len(x)), np.linspace(0,2,num=len(x)), 'k', lw=2)
plt.text(-0.75, 1.25, 'd=1\nw=0.3', color = 'm', fontsize=(40))
plt.xlim(-1,1)
plt.ylim(0,1.5)
#plt.savefig('triangle.png', dpi=300)
#plt.xlabel(r"$x/L$", fontsize=40)
#plt.text(0.5, 0.85, r"$I(\frac{x}{L})\,;\,\lambda = 1$", color = 'k', fontsize=(40))
#plt.title('t=%s (s)'%(t), fontsize=(60))
plt.show()