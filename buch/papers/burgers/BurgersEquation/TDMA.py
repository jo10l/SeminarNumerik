# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:10:22 2020

@author: m2schmid
"""
import sympy
import numpy as np
import dill
dill.settings['recurse'] = True

#parameters
M = 30
# dx = 0.33
# dt = 0.33
#variables

dt = sympy.symbols('dt')
dx = sympy.symbols('dx')
uj = np.array(list(sympy.symbols('u^{n}_0:'+str(M))))
x = np.array(list(sympy.symbols('u^{n+1}_0:'+str(M))))

d = 2*dx*uj
d[0] = dx*uj[0]
d[-1] = dx*uj[-1]

a = -dt*uj[1:]
c = dt*uj[:-1]

b = np.full(M, 2*dx, dtype=sympy.Symbol)
b[0] = dx - dt*uj[0]
b[-1] = dx + dt*uj[-1]

c[0] = c[0]/b[0]
d[0] = d[0]/b[0]
for i in range(1, M-1):
    c[i] = c[i]/(b[i]-a[i]*c[i-1])
    d[i] = (d[i]-a[i]*d[i-1])/(b[i]-a[i]*c[i-1])

x[-1] = d[-1]

for i in range(M-2, -1, -1):
    x[i] = d[i]-c[i]*x[i+1]

f = []
for i in range(M):
    f.append(sympy.lambdify([dt, dx, uj], x[i]))

dill.dump(f, open("myfile", "wb"))

# for i in range(len(x)):
#     print(sympy.printing.latex(sympy.simplify(x[i])))
#     print('\n')