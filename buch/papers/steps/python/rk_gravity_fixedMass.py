#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:56:15 2020

@author: terminator
"""

import rungeKutta as rk

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)  # https://matplotlib.org/api/ticker_api.html



debug=[]
debugk=[]
callcount=0



def rk_system_nd_ssc_single_test_step(x0, g_vec, x_end, deriv, hmin, hmax, qfactor):     #additional debug features
    '''runge_kutta n-dimensional m'th degreee step_size_control single test step(x0, [np.array([y1(0), y2(0)]),np.array([y1'(0), y2'(0)]), ...], x_end, deriv_function(x, y), min_step, max_step, q_factor)'''     
    h=hmin
    htest=hmax
    size=len(g_vec) #degree of dgl
    dimensions=len(g_vec[0])
    x=[x0]
    y=[np.array(g_vec)]
    matrix=np.zeros((size,size))
    matrix[:-1, 1:]=np.eye(size-1)
    vector_deriv_function=np.zeros(size)
    vector_deriv_function[-1]=1 #[0, 0, ..., 0, 1]
    
    #vector=np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), np.full(dimensions, 1)])
    
    while(x[-1]<x_end):
        
        y_ss=y[-1]  #y_step_start
        x_ss=x[-1]  #x_step_start

        #k1=matrix @ y_ss + np.array([i*deriv(x_ss, y_ss) for i in vector_deriv_function])
        k1=matrix @ y_ss +np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss, y_ss)])
        
        y_test=y_ss+htest*k1
        #ktest=matrix @ y_test+np.array([i*deriv(x_ss+htest, y_test) for i in vector_deriv_function])
        ktest=matrix @ y_test+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+htest, y_test)])
        y_difference=np.max(abs(k1-ktest))
        debug.append([y_ss, y_test])
        debugk.append([k1, ktest])
        h=htest/y_difference/qfactor
        if(h<hmin):
            h=hmin
        elif h>hmax:
            h=hmax
        
        y_k1=y_ss+h/2*k1#y-vector for calculating k2 (calculated with k1)
        
        
        #k2=matrix @ y_k1+np.array([i*deriv(x_ss+h/2, y_k1) for i in vector_deriv_function])
        k2=matrix @ y_k1+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+h/2, y_k1)])
        y_k2=y_ss+h/2*k2#y-vector for calculating k3 (calculated with k2)
         
        #k3=matrix @ y_k2+np.array([i*deriv(x_ss+h/2, y_k2)for i in vector_deriv_function])
        k3=matrix @ y_k2+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+h/2, y_k2)])
        y_k3=y_ss+h*k3#y-vector for calculating k4 (calculated with k3)
            
        #k4=matrix @ y_k3+np.array([i*deriv(x_ss+h, y_k3) for i in vector_deriv_function])
        k4=matrix @ y_k3+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+h, y_k3)])
            
        x.append(x[-1]+h)
        y.append(y_ss+h/6*(k1+2*k2+2*k3+k4))
        #y.append(y_ss+h*k1)    #euler
    return x, y







g_adv=1
pMo0_0=np.array([0, 0]) # pMo0(0)
pFi=np.array([2,1])
vMo0_0=np.array([0.669, 0]) #vMo0_(0)=pMo0'(0)
mFi=1


def a_p(x, y):
    pMo0=y[0, 0:2]
    return (pFi-pMo0)*g_adv*mFi/(np.linalg.norm(pFi-pMo0, axis=-1, keepdims=True)**3) #one moving


#------------------------------------different fixed step size-------------

plt.figure()
plt.plot(pFi[0], pFi[1], 'o', label='Gravitationszentrum')
t, pMo=rk.rk_system_nd(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.001)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '-', label=f'h=0.001s, {len(t)-1} steps')
t, pMo=rk.rk_system_nd(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.01)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '-', label=f'h=0.01s, {len(t)-1} steps')
t, pMo=rk.rk_system_nd(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.1)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '.-', label=f'h=0.1s, {len(t)-1} steps')
t, pMo=rk.rk_system_nd(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.2)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '.-', label=f'h=0.2s, {len(t)-1} steps')
t, pMo=rk.rk_system_nd(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.4)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '.-', label=f'h=0.4s, {len(t)-1} steps')
t, pMo=rk.rk_system_nd(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.8)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '.-', label=f'h=0.8s, {len(t)-1} steps')
plt.legend()
plt.xlim(0, 3)
plt.ylim(0, 2)
plt.tight_layout()
#plt.xlabel('x-Position / m')
plt.xticks([])
#plt.ylabel('y-Position / m')
plt.yticks([])
#plt.title('Bahn eines Teilchens um ein Gravitationszentrum')
plt.plot()
plt.savefig('gravity_different_fixed_stepsize.pdf')

# plt.figure()
# t, pMo=rk_system_nd_ssc(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.01, 0, 0)
# plt.plot(t, [np.linalg.norm(a_p(0, i)) for i in pMo], label='|a|')
# plt.plot(t, [a_p(0, i)[0] for i in pMo], label='a_x')
# plt.plot(t, [a_p(0, i)[1] for i in pMo], label='a_y')
# plt.legend()
# plt.plot()

#-------------------------------end different fixed step size-------------
    
#-------------------------comparison fixed/variable step----------------

plt.figure()
plt.plot(pFi[0], pFi[1], 'o', label='Gravitationszentrum')
t, pMo=rk.rk_system_nd_ssc_single_test_step(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.01, 0.01, 5)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '--', color='#1f77b4', label=f'h=0.01s, ({len(pMo)} Schritte)')
t, pMo=rk.rk_system_nd_ssc_single_test_step(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.05, 0.05, 5)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '--', color='#17becf', label=f'h=0.05s, ({len(pMo)} Schritte)')
t, pMo=rk.rk_system_nd_ssc_single_test_step(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.1, 0.1, 5)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '--', color='#ff7f0e', label=f'h=0.1s, ({len(pMo)} Schritte)')
t, pMo=rk_system_nd_ssc_single_test_step(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.01, 2, 4)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '.-', color='#d62728', label=f'h=0.01s ... 2s, ({len(pMo)} Schritte)')

poi=4   #showing test step
#plt.plot([debug[poi][0][0][0], debug[poi][1][0][0]], [debug[poi][0][0][1] , debug[poi][1][0][1]], '-x') 
X, Y=np.meshgrid(np.linspace(0, 3.5, 15+1), np.linspace(0, 2, 10+1))


def a_xy(pMo0): #generate vectorfield
    return (pFi-pMo0)*g_adv*mFi/(np.linalg.norm(pFi-pMo0, axis=-1, keepdims=True)**3) #one moving
arrows=a_xy(np.stack([X, Y], -1))
for x in range(len(arrows)):
    max_len=7
    for y in range(len(arrows[x])):
        if np.linalg.norm(arrows[x][y])>max_len:
            arrows[x][y]=arrows[x][y]/np.linalg.norm(arrows[x][y])*max_len
plt.quiver(X, Y, arrows[:,:,0], arrows[:, :, 1], scale=100)
plt.legend()

plt.xlim(0, 3.5)
plt.ylim(0, 2)
plt.savefig('variable_sep_size_comparison.pdf')


fig, ax=plt.subplots() #step_size
ax.set_xlim(0, 4.5)
ax.set_ylim(0, 2)
ax.step(t[:-1],[t[i+1]-t[i] for i in range(len(t)-1)], '-', where='post')
ax.set_xlabel('time / s')
ax.set_ylabel('step size / s')
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.grid(which="both")
fig.savefig('step_size_fixed_mass.pdf')

#---------------------end comparison fixed/variable step----------------