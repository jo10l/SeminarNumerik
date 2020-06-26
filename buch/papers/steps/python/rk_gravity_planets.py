#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:56:15 2020

@author: terminator
"""

import rungeKutta
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g_adv=1
pMo0_0=np.array([0, 0]) # pMo0(0)
pMo1_0=np.array([-7.5, 0])
pMo2_0=np.array([-8.5, 0])
vMo0_0=np.array([0, -0.125]) #vMo0_(0)=pMo0'(0)
vMo1_0=np.array([0, 2])
vMo2_0=np.array([0, 0.5])
mMo0=20
mMo1=1
mMo2=1


def a_p(x, y):
    pMo0=y[0, 0:2]
    pMo1=y[0, 2:4]
    pMo2=y[0, 4:6]
    aMo0=(pMo1-pMo0)*g_adv*mMo1/(np.linalg.norm(pMo1-pMo0)**3) +\
        (pMo2-pMo0)*g_adv*mMo2/(np.linalg.norm(pMo2-pMo0)**3)
    aMo1=(pMo0-pMo1)*g_adv*mMo0/(np.linalg.norm(pMo0-pMo1)**3) +\
        (pMo2-pMo1)*g_adv*mMo2/(np.linalg.norm(pMo2-pMo1)**3)
    aMo2=(pMo0-pMo2)*g_adv*mMo0/(np.linalg.norm(pMo0-pMo2)**3) +\
        (pMo1-pMo2)*g_adv*mMo1/(np.linalg.norm(pMo1-pMo2)**3)
    return np.array([aMo0, aMo1, aMo2]).reshape(6)
#t, pMo=rungeKutta.rk_system_nd(0, [np.array([pMo0_0, pMo1_0, pMo2_0]).reshape(6), np.array([vMo0_0, vMo1_0, vMo2_0]).reshape(6)], 20, a_p, 0.01) #fixed_step
t, pMo=rungeKutta.rk_system_nd_ssc_single_test_step(0, [np.array([pMo0_0, pMo1_0, pMo2_0]).reshape(6), np.array([vMo0_0, vMo1_0, vMo2_0]).reshape(6)], 20, a_p, 0.01, 2, 5) #variable_step
# t, pMo=rungeKutta.rk_system_nd_ssc_romberg(0, [np.array([pMo0_0, pMo1_0, pMo2_0]).reshape(6), np.array([vMo0_0, vMo1_0, vMo2_0]).reshape(6)], 20, a_p, 0.01, 2, 0.001) #variable_step fehlberg

#-----------------------------------static_plot------------------------------------------

plt.figure()    #static planet plot
plt.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '.-', label='Mo0')
plt.plot([i[0][2] for i in pMo], [i[0][3] for i in pMo], '.-', label='Mo1')
plt.plot([i[0][4] for i in pMo], [i[0][5] for i in pMo], '.-', label='Mo2')
plt.legend()

# plt.savefig('deleteme_gravity.pdf')

# plt.figure()  #parameters pos, v, acc
# plt.plot(t, [np.linalg.norm(i[0]) for i in pMo], label='pos')
# plt.plot(t, [np.linalg.norm(i[1]) for i in pMo], label='velocity')
# plt.plot(t, [np.linalg.norm(a_p(0, i)) for i in pMo], label='acc')

# plt.legend()

plt.figure() #step_size
plt.xlim()
plt.step(t[:-1],[t[i+1]-t[i] for i in range(len(t)-1)], where='post')
plt.xlabel('time / s')
plt.ylabel('step size / s')


#---------------------------------end_statc_plot---------------------

#---------------------------------gravity_animated--------------------

t, pMo=rungeKutta.rk_system_nd(0, [np.array([pMo0_0, pMo1_0, pMo2_0]).reshape(6), np.array([vMo0_0, vMo1_0, vMo2_0]).reshape(6)], 20, a_p, 0.01) #fixed_step

pMo_x=[i[0] for i in pMo[::20]]

    
def data_gen():
    for x0, y0, x1, y1, x2, y2  in pMo_x:
        yield x0, y0, x1, y1, x2, y2


def init():
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()

ax.plot([i[0][0] for i in pMo], [i[0][1] for i in pMo], '-.',label='m0=20')
ax.plot([i[0][2] for i in pMo], [i[0][3] for i in pMo], '-.', label='m1=1')
ax.plot([i[0][4] for i in pMo], [i[0][5] for i in pMo], '-.', label='m2=1')
ax.legend()

line,= ax.plot([], [], 'ro', lw=2)
xdata, ydata,= [0,0,0], [0,0,0]


def run(data):
    # update the data
    x0, y0, x1, y1, x2, y2 = data
    xdata[0]=x0
    ydata[0]=y0
    xdata[1]=x1
    ydata[1]=y1
    xdata[2]=x2
    ydata[2]=y2

    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=64,
                              repeat=False, init_func=init)
plt.show()
ani.save('planets.mp4')

#---------------------end_gravity_animated--------------------------------