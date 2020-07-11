# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:35:22 2020

@author: m2schmid
"""

from sympy.solvers import solve
import sympy
import numpy as np

# ut = sympy.symbols('u^{n+1}_{0:3}')


# dt = sympy.symbols('dt')
# dx = sympy.symbols('dx')

# u1t = sympy.symbols('u^{n}_{0:3}')
# eqns = []

# eqns.append((ut[0]-u1t[0])/dt+u1t[0]*(ut[1]-ut[0])/dx)
# for i in range(1,2,1):
#     eqns.append((ut[i]-u1t[i])/dt+u1t[i]*(ut[i+1]-ut[i-1])/(2*dx))
# eqns.append((ut[-1]-u1t[-1])/dt+u1t[-1]*(ut[-1]-ut[-2])/dx)

# # print(sympy.printing.latex(eqns))
# sols = sympy.simplify(sympy.solve(eqns, ut))
# print(sols)

# nextr = []
# for keys,values in sols.items():
#     print('\n')
#     # nextr.append(float(values))
#     print(str(keys)+'='+sympy.printing.latex(values))

dt = sympy.symbols(r'\Delta{t}\\,')
dx = sympy.symbols(r'\Delta{x}\\,')

u = sympy.symbols(r'u^{n}_{i}\\,')
ut = sympy.symbols(r'u^{n-1}_{i}\\,')
utx = sympy.symbols(r'u^{n-1}_{i-1}\\,')
ut1x = sympy.symbols(r'u^{n-1}_{i+1}\\,')
u1  = sympy.symbols(r'u^{n}_{i-1}\\,')
eqn = (u- ut)/dt + ut*(u-u1)/(dx)
sols = sympy.simplify(sympy.solve(eqn, u))
print(sympy.printing.latex(sols))