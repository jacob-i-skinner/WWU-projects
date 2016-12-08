from matplotlib import pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 40})
x = np.linspace(0, 1, num=500)
g = np.linspace(0, 1, num=500)
terms = 200
f = np.zeros(len(x))
t=1
for i in range(len(x)):
    for j in range(1,terms):
        f[i] += -(2*np.sin(2*(2*j-1)*np.pi*x[i])/((2*j-1)*np.pi))*np.cos(t*(2*j-1)*np.pi)
plt.figure(figsize=(15,15))
#plt.plot(-np.ones(len(x)), x, 'k', lw=2)
#plt.plot(np.ones(len(x)), x, 'k', lw=2)
#plt.plot(v,G, 'b', lw=8)
plt.plot(x,f+0.5, 'm', lw=4)
plt.plot(x, np.zeros(len(x)), 'k', lw=2)
plt.plot(np.zeros(len(x)), x, 'k', lw=2)
plt.text(0.6, 0.75, r"$u(x',t'=%s)$"%(t), color = 'k', fontsize=(40))
plt.ylim(-0.1,1.1)
plt.xlim(0,1)
plt.show()
#plt.savefig('t=%s'%(t), dpi=300)
#plt.xlabel(r"Position (m)", fontsize=60)
#plt.ylabel(r"Temperature (degrees C)", fontsize=60)
#plt.title('t=%s (s)'%(t), fontsize=(60))