from matplotlib import pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 48})
deltax = 5
n = np.arange(100)
x = np.linspace(0, 10*np.pi, num=(10000))
#asubn = (2/np.pi)*(np.sin(x*np.pi*deltax/2)/x)
#integera = (2/np.pi)*(np.sin(n*np.pi*deltax/2)/n)

def asubn(x,deltax):
    return (2/np.pi)*(np.sin(x*np.pi*deltax/2)/x)
def integera(n,deltax):
    return (2/np.pi)*(np.sin(n*np.pi*deltax/2)/n)

fig, ax = plt.subplots(3, 1,sharex='col')
for i in range(3):
    ax[i].plot(x,asubn(x,0.33+i*0.33), 'm', lw=8)
    ans = integera(n,0.33+i*0.33)
    #ans[0] = deltax
    ax[i].plot(x, np.zeros(len(x)), 'k')
    ax[i].set_ylim(-0.3,1.1)
    ax[i].set_xlim(0,10*np.pi)
    ax[i].scatter(n,ans, s=2400)
    ax[i].set_xlabel(r'$n$', fontsize=80)
    ax[i].set_ylabel(r'$a_n$', rotation=45, fontsize=80)
fig.set_figheight(60)
fig.set_figwidth(60)
#plt.title('%s Terms'%(terms), fontsize=(60))
plt.savefig('coefficients.png')
#plt.show()