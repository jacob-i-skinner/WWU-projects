from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate
import math
terms = 50
x = np.linspace(-1,1, num=1000)
coef = np.zeros(terms)
An = np.empty(terms)
g1 = lambda x: -2*x-2
g2 = lambda x: 2*x
g3 = lambda x: -2*x+2

for i in range(terms):
    coef[i] = 1
    coef[i-1]= 0
    Pn      = np.polynomial.legendre.Legendre(coef)
    Qn      = lambda x: Pn(x)*(2*i+1)/2
    fn1, fn2, fn3 = lambda x: g1(x)*Qn(x), lambda x: g2(x)*Qn(x), lambda x: g3(x)*Qn(x)
    An[i]   = integrate.quad(fn1, -1, -1/2)[0] + integrate.quad(fn2, -1/2, 1/2)[0] + integrate.quad(fn3, 1/2, 1)[0] 
    

fn = np.polynomial.legendre.Legendre(An)
plt.plot(x, np.zeros(len(x)), 'k', lw=2)
plt.plot(np.zeros(len(x)), x, 'k', lw=2)
plt.plot(x, fn(x), 'm', lw=4)
plt.title('Legendre expansion with 50 terms', fontsize=(20))
#plt.savefig('legendre.png', dpi=300)
plt.show()