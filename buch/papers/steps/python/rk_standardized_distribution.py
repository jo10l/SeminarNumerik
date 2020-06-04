#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:08:53 2020

@author: terminator
"""

import rungeKutta as rk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


debug=[]
debugk=[]
callcount=0

def rk_system_nd_ssc(x0, g_vec, x_end, deriv, hmin, hmax, qfactor):
    '''runge_kutta n-dimensional m'th degreee (x0, [np.array([y1(0), y2(0)]),np.array([y1'(0), y2'(0)]), ...], x_end, deriv_function(x, y), step_size)'''     
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

mu=0
sigma=1


def phi_xy(x, y):
    return np.exp(-((x-mu)/sigma)**2/2)/sigma/np.sqrt(2*np.pi)

# x, y=rungeKutta.rk_fs(mu, 0.5, 7, phi_xy, 0.1, x_start=-7)
# fi, a=plt.subplots()
# a.axes.set_xlim(-6, 6)
# a.axes.set_ylim(-0.05, 1.45)
# a.plot(x, [phi_xy(x, 0) for x in x], '-', color="#000000", label='phi(x)')
# a.plot(x, y, '-', color='C0', label='F(x)')
# a.legend()
# a.grid()
# fi.tight_layout()


fig=plt.figure(figsize=(6, 6))
gs=gridspec.GridSpec(4, 1)
ax=fig.add_subplot(gs[0:3, 0])
a_phi=fig.add_subplot(gs[3, 0], sharex=ax)
fig.tight_layout()
ax.set
ax.axes.set_xlim(-6, 6)
ax.axes.set_ylim(-0.05, 1.45)
a_phi.set_ylim(-0.05, 0.55)
a_phi.grid()
X, Y=np.meshgrid(np.r_[-6: 6+0.75: 0.75],np.r_[0: 1.55+0.1: 0.1])
arrows=np.stack([np.ones_like(X), phi_xy(X, 0)], axis=-1)
arrows/=np.array([(ax.axes.get_xlim()[1]-ax.axes.get_xlim()[0])*0.7, (ax.axes.get_ylim()[1]-ax.axes.get_ylim()[0])])
arrows=arrows/np.linalg.norm(arrows, axis=-1, keepdims=True)



x, y=rk.rk_system_nd(mu-7*sigma, np.array([[0]]), mu+7*sigma, phi_xy, 0.01)  #F-preview
ax.plot(x, [y[0, 0] for y in y], '--', label='F(x)', c='#606060')
#ax.plot(x, [y[0, 0] for y in y], 'o-', label='F(x)')

x, y=rk_system_nd_ssc(mu-7*sigma, np.array([[0]]), mu+7*sigma, phi_xy, 0.01, 2, 20)
ax.legend()
ax.quiver(X, Y, arrows[:, :, 0], arrows[:, :, 1], scale=20, width=0.002, label='phi(x,y)')# poi=4   #showing test step
poi=8
a_phi.plot(np.r_[-7: 7: 0.1], phi_xy(np.r_[-7: 7: 0.1], 0), label='phi(x)')

F, =ax.plot([],[], 'o-', c='C1')
line,= ax.plot([], [], 'rX',)
test_step,=ax.plot([],[], '-k', color='#000000', lw=4)
taken_step,=ax.plot([],[], '-k', color='#FF0000')
phi_step_start,=a_phi.plot([],[], 'x-.', label='phi(start)')
phi_test_step,=a_phi.plot([],[], 'x-.', label='phi(test)')
#phi_step_taken,=a_phi.plot([],[], 'x-.', label='phi(step)')
a_phi.legend(loc='upper right')
fig.savefig(f'simplestep-n{0:02d}.pdf')

for poi in np.r_[1:17]:
    F.set_data([x[i] for i in range(poi+1)], [y[i][0,0] for i in range(poi+1)])   #F(x)
    line.set_data([x[poi], x[poi]+2], [debug[poi][0][0][0] , debug[poi][1][0][0]])  #red crosses
    test_step.set_data([x[poi], x[poi]+2], [-0.04]) #black bar on bottom
    taken_step.set_data([x[poi], x[poi+1]], [-0.04])    #red bar bottom
    
    phi_step_start.set_data([-7, x[poi], 7],np.full(3, phi_xy(x[poi], 0)))
    phi_test_step.set_data([-7, x[poi]+2, 7],np.full(3, phi_xy(x[poi]+2, 0)))
    #phi_step_taken.set_data([-7, x[poi+1], 7],np.full(3, phi_xy(x[poi+1], 0)))
    a_phi.set_title(f'start-test: {abs(phi_xy(x[poi], 0)-phi_xy(x[poi]+2, 0)):5.3f}  =>  step= {x[poi+1]-x[poi]:5.3f}  =>  start-step: {abs(phi_xy(x[poi], 0)-phi_xy(x[poi+1], 0)):5.3f}')
    fig.savefig(f'simplestep-n{poi:02d}.pdf')