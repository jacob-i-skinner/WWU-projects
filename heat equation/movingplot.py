from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0, 1, num=1000)
terms = 20
F = np.zeros(len(x))
y = np.ones(len(x))
for i in range(len(x)):
    if  x[i] <= 0.5:
        y = 2*x
    else:
        y[i] = -2*x[i]+2
for k in range(3):
    t = k/10
    for i in range(len(x)):
        for j in range(0,terms):
            F[i] += np.e**(-(2*j+1)**2*np.pi**2*t)*(8/np.pi**2)*((-1)**j)*np.sin((2*j+1)*np.pi*x[i])/((2*j+1)**2)
    plt.figure(figsize=(20,10))
    #plt.plot(-np.ones(len(x)), x, 'k', lw=2)
    #plt.plot(np.ones(len(x)), x, 'k', lw=2)
    plt.plot(x, np.zeros(len(x)), 'k', lw=2)
    plt.plot(x, y, 'k', lw=4)
    plt.plot(x,F, 'r', lw=4)
    plt.ylim(0,1.5)
    plt.title('time = %s(s)'%(t), fontsize=(60))
    plt.savefig('temp%s.png'%(t))