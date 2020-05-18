# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sympy as sym

import numpy as np
import matplotlib.pyplot as plt
import rungeKutta as rk

def f(x, y):
    return np.e**y

t, y=rk.rk_system_nd_ssc_fehlberg(0, [np.array([0])], 1, f, hmin=1e-6, hmax=2, epsilon=1e-6, hstart=0.2)
# t, y=rk.rk_system_nd(0, [np.array([0])], 2, f, 0.1) # 10 steps

x=np.arange(0, 1, 1e-6)
plt.plot(x, np.log((-1)/(np.array(x)-1)), '--', c='#8F8F8F',label='analytisch')
plt.plot(t, [y[0,0] for y in y], '.-', label='numerisch', c=(0.8, 0.2, 0, .5))
plt.ylim(0, 12)
plt.title("y'=e^y, y(0)=0")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('test3.pdf')


fig, ax=plt.subplots() #step_size
ax.set_xlim(0, len(t)-2)
#ax.set_ylim(1e-6, 1)
ax.semilogy((np.r_[t, t[-1]]-np.r_[0, t])[1:], '-C1', drawstyle='steps-post')#[t[i+1]-t[i] for i in range(len(t)-1)]
ax.plot([t[i+1]-t[i] for i in range(len(t)-1)], '.C1')
ax.set_xlabel('step n')
ax.set_ylabel('step size')
ax.grid(which="both")
fig.tight_layout()
plt.savefig('test3_step.pdf')




