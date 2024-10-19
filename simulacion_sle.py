# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import cmath

#función para simular una variable aleatoria Rademacher
def R(p):
    if np.random.uniform() < p:
        return 1
    else:
        return -1

#función de trazado h_k
def h(z,d,dk):
    v = (d**2)/dk
    if d > 0:
        a = 1/2 + 1/2*np.sqrt(v/(16+v))
    else:
        a = 1/2 - 1/2*np.sqrt(v/(16+v))

    r= complex(z + 2*np.sqrt((dk*(1-a))/a))
    s = complex(z - 2*np.sqrt((dk*a)/(1-a)))
    return (r**(1-a))*(s**a)

#función para evaluar la composición de k funciones de trazado
def hk(z0,k,dk,d):
    for i in range(k):
        z = h(z0,d[k-1 - i],dk)
        z0 = z
    return z

#simular n pasos de sle(kappa)
kappa = 3
n=10000
Delta_k = 1/n

#simular incrementos de la función de conducción
#(incrementos de un movimiento browniano de varianza kappa)
d = [R(1/2)*np.sqrt(kappa*Delta_k) for i in range(n)]

#punto inicial
z0 = 0
sle=np.empty(n,dtype=complex)
sle[0]=z0

for k in range(1,n):
    sle[k] = hk(z0,k,Delta_k,d)

#gráfica
plt.plot(sle.real,sle.imag,linewidth=0.5)


