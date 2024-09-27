# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import cmath

def R(p):
    if np.random.uniform() < p:
        return 1
    else:
        return -1

def h(z,d,dk):
    v = (d**2)/dk
    if d > 0:
        a = 1/2 + 1/2*np.sqrt(v/(16+v))
    else:
        a = 1/2 - 1/2*np.sqrt(v/(16+v))

    r= complex(z + 2*np.sqrt((dk*(1-a))/a))
    s = complex(z - 2*np.sqrt((dk*a)/(1-a)))
    return (r**(1-a))*(s**a)

def hk(z0,k,dk,d):
    for i in range(k):
        z = h(z0,d[k-1 - i],dk)
        z0 = z
    return z

#simular n pasos de sle(kappa)
kappa = 3
n=15000
Delta_k = 1/n

d = [R(1/2)*np.sqrt(kappa*Delta_k) for i in range(n)]
u = [sum(d[:i+1]) for i in range(len(d))]
#u = [np.exp(i) for i in u]
z0 = 0
sle=[z0]


for k in range(1,n):
    #z = hk(z0,k,1/n,d)
    z = hk(z0,k,Delta_k,d)
    sle.append(z)

sle1=[]
sle2=[]
for z in sle:
    sle1.append(z.real)
    sle2.append(z.imag)

#gráfica
plt.plot(sle1,sle2,color='k',linewidth=0.5)


