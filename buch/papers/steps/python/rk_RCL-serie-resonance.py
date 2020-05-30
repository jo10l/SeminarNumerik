#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:51:50 2020

@author: terminator
"""


import rungeKutta
import numpy as np
import matplotlib.pyplot as plt

w=10    #RCL serie resonance
R=1
C=0.04
L=0.25
U0=5

def y_2nd_is(x, y):
    return -w/L*np.sin(w*x)*U0-y[0]/C/L-y[1]*R/L


x, y=rungeKutta.rk_system(0, [0, U0/L], 5, y_2nd_is, 0.1)

plt.figure()

plt.plot(x, [y[n][0] for n in range(len(x))], 'C3-', label="i(t) / A")
plt.plot([x/200 for x in range(1000)], np.cos([x/200*10 for x in range(1000)])*5, 'C2--', label='U(t) / V')
plt.legend()
plt.grid()
plt.xlabel('t / s')
plt.savefig('RCL-serie-resonance.pdf')