# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:32:02 2020

@author: micha
"""
import matplotlib.pyplot as plt
import numpy as np

Q = np.zeros(100)
Q2_plus = np.zeros(100)
Q2_min = np.zeros(100)
t=np.linspace(0,100,100)

Q[0]=1
Q2_plus[0]=1
Q2_min[0]=1
kappa = 1
dt = 0.03

for i in range(100):
    Q[i] = Q[0]*(1-kappa*dt)**i
    Q2_plus[i] = Q2_plus[0]*(-kappa*dt+np.sqrt(kappa**2*dt**2+1))**i
    Q2_min[i] = Q2_min[0]*(-kappa*dt-np.sqrt(kappa**2*dt**2+1))**i


BIGGER_SIZE = 22
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

plt.plot(t, Q2_min,lw=2, label=r"$\xi_-$")
plt.plot(t, Q2_plus,lw=3, label=r"$\xi_+$")
plt.plot(t, Q,"o", lw=3, label="Q, explicit")
plt.title(r"$\Delta t = 0.03$, $\kappa = 1$, $Q(0)=1$")
plt.ylim(-5,5)
plt.xlim(0,100)
plt.legend()
plt.tight_layout()
plt.grid(True)