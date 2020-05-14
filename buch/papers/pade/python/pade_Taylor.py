#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:01:33 2020

@author: crenda
"""


import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import pade
import scipy.misc

def fac(x):
    res = 1
    for i in range(1, x+1, 1):
        res = res*i
    return res
    
def f(x):
    #return 10*np.sin(x*5)
    return 10*np.arctan(x-2) + 2.0/x

def tay(x):
    return x/1-x**3/fac(3)+x**5/fac(5)-x**7/fac(7)+x**9/fac(9)-x**11/fac(11)+x**13/fac(13)


def f1(x):
    return np.sqrt((1 +2*x)/(1 + x))


x = np.arange(-10,10,0.002)
# x1 = np.arange(0,100,0.1)
# #plt.plot([0,100],[np.sqrt(2),np.sqrt(2)])
# plt.hlines(np.sqrt(2),0,100)
# plt.plot(x1,f1(x1))
# fixup plot so it doesn't draw an extra line across a discontinuity 
def asymptote_nan(y,x,x0list):
    x0list = np.atleast_1d(x0list)
    for x0 in x0list:
        y[np.argmin(abs(x-x0))] = float('nan')
    return y
y = asymptote_nan(f(x),x,x0list=[0])
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
#ax.plot(x,y)
ax.set_ylim(-4,4)
ax.grid('on')
# ax.plot(x,tay(x),markersize=8)
# ax.plot(x,np.sin(x),markersize=8)

x0 = 1.0#1.0
T10poly = scipy.interpolate.approximate_taylor_polynomial(f,x=x0,degree=10, scale=0.05) 
P5poly,Q5poly = pade(T10poly.coeffs[::-1],5)
T10 = lambda x: T10poly(x-x0)
R5_5 = lambda x: P5poly(x-x0)/Q5poly(x-x0)

print(T10poly)
print("P5 poly {}".format(P5poly))
print(Q5poly)
#fig = plt.figure(figsize=(8,6))
#ax = fig.add_subplot(1,1,1)
ax.plot(x,y,label='f(x)')
ax.plot(x0,f(x0),'.k',markersize=8)
yR5 = R5_5(x)
# use real roots of Q5(x-x0) for finding asymptotes 
yR5 = asymptote_nan(yR5, x, [r+x0 for r in np.roots(Q5poly) if np.abs(np.imag(r)) < 1e-8]) 
ax.plot(x,T10(x),label='T10(x)')
ax.plot(x,yR5, label='R5,5(x)')
ax.set_ylim(-40,40)
ax.legend(loc='lower right',labelspacing=0)
ax.grid('on')