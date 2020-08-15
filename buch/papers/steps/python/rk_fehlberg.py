#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:54:02 2020

@author: terminator
"""

import numpy as np
import matplotlib.pyplot as plt
import rungeKutta as rk

debug=[]

repeat=[]

def rk_system_nd_ssc_fehlberg(x0, g_vec, x_end, deriv, hmin, hmax, epsilon=0.01, hstart=None):      #additional debug features
    '''runge_kutta n-dimensional m'th degreee romberg step size control(x0, [np.array([y1(0), y2(0)]),np.array([y1'(0), y2'(0)]), ...], x_end, deriv_function(x, y), step_size_min, step_size max, local_error, hstart)'''
    if hstart:
        h=hstart
    else:
        h=hmin
    size=len(g_vec) #degree of dgl
    dimensions=len(g_vec[0])
    x=[x0]
    y=[np.array(g_vec)]
    matrix=np.zeros((size,size))
    matrix[:-1, 1:]=np.eye(size-1)
    vector_deriv_function=np.full(dimensions, 0)
    while(x[-1]<x_end):
        step_ok=False
        while(not step_ok):
            y_ss=y[-1]  #y_step_start
            x_ss=x[-1]  #x_step_start
    
            k1=matrix @ y_ss +np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss, y_ss)])
            hk1=h*k1#y-vector for calculating k2 (calculated with k1)
            
            y2=y_ss+2/9*hk1        
            k2=matrix @ y2+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+2/9*h, y2)])
            hk2=h*k2#y-vector for calculating k3 (calculated with k2)
            
            y3=y_ss+1/12*hk1+1/4*hk2
            k3=matrix @ y3+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+1/3*h, y3)])
            hk3=h*k3
            
            y4=y_ss+69/128*hk1-243/128*hk2+135/64*hk3
            k4=matrix @ y4+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+3/4*h, y4)])
            hk4=h*k4
            
            y5=y_ss-17/12*hk1+27/4*hk2-27/5*hk3+16/15*hk4
            k5=matrix @ y5+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+h, y5)])
            hk5=h*k5
            
            y6=y_ss+65/432*hk1-5/16*hk2+13/16*hk3+4/27*hk4+5/144*hk5
            k6=matrix @ y6+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+5/6*h, y6)])
            hk6=h*k6
            
            y_4th=y_ss+1/9*hk1+9/20*hk3+16/45*hk4+1/12*hk5
            #y_5th=y_ss+47/450*hk1+12/25*hk3+32/225*hk4+1/30*hk5+6/25*hk6
            T=np.max(abs((-2*hk1+9*hk3-64*hk4-15*hk5+72*hk6)/300))
            
            if(T<epsilon/20):       #very accurate, increase step size
                x.append(x_ss+h)
                y.append(y_4th)
                h=2*h
                print('double step size')
                
                if(h>hmax):
                    h=hmax
                    print('step max!')
                
                step_ok=True
            elif(T>epsilon):    #unaccurate, decrease step size
                if(h==hmin):
                    x.append(x_ss+h)
                    y.append(y_4th)
                    step_ok=True
                else:
                    h=h/2
                    #step_ok=False
                    print('halve step size')
                    repeat.append([])
                    
                    if(h<hmin):
                        print('step min!')
                        h=hmin
                

                    
                
            else:           #accurate enough, keep step size
                x.append(x_ss+h)
                y.append(y_4th)
                step_ok=True
                print('keep step size')
    return x, y


g_adv=1
pMo0_0=np.array([0, 0]) # pMo0(0)
pFi=np.array([2,1])
vMo0_0=np.array([0.669, 0]) #vMo0_(0)=pMo0'(0)
mFi=1


def a_p(x, y):
    pMo0=y[0, 0:2]
    return (pFi-pMo0)*g_adv*mFi/(np.linalg.norm(pFi-pMo0, axis=-1, keepdims=True)**3) #one moving

plt.figure()
plt.plot(pFi[0], pFi[1], 'o', label='Gravitationszentrum')


print('run0:')
t, pMo=rk.rk_system_nd_ssc_fehlberg(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.01, 0.01)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '--', c='#8F8F8F',label=f'h=0.01s => {len(t)-1} steps')

print('run1:')
t, pMo=rk.rk_system_nd_ssc_fehlberg(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.1, 0.1)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '-.', label=f'h=0.1s => {len(t)-1} steps', c='#FF0080')


print('run2:')
t, pMo=rk.rk_system_nd_ssc_fehlberg(0, [pMo0_0, vMo0_0], 4.5, a_p, 0.15, 0.15)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], 'x-', label=f'h=0.15s => {len(t)-1} steps')

print('run3:')
t, pMo=rk_system_nd_ssc_fehlberg(0, [pMo0_0, vMo0_0], 4.5, a_p, hmin=0.01, hmax=5, epsilon=0.001, hstart=1)
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], linestyle=':', marker='.', label=f'h=variabel => {len(t)+len(repeat)-1}={len(t)-1}+{len(repeat)} steps')


plt.legend()

plt.xlim(0, 3)
plt.ylim(0, 2)

plt.tight_layout()
plt.yticks([])
plt.xticks([])

plt.savefig('comparison_fehlberg_ssc.pdf')

fig, ax=plt.subplots() #step_size
ax.set_xlim(0, 4.5)
ax.set_ylim(0.01, 10)
ax.semilogy(t[:],(np.r_[t, t[-1]]-np.r_[0, t])[1:], '-C1', drawstyle='steps-post')#[t[i+1]-t[i] for i in range(len(t)-1)]
ax.plot(t[:-1],[t[i+1]-t[i] for i in range(len(t)-1)], '.C1')
ax.set_xlabel('time / s')
ax.set_ylabel('step size / s')
ax.grid(which="both")
fig.tight_layout()
fig.savefig('step_size_fixed_mass_fehlberg.pdf')