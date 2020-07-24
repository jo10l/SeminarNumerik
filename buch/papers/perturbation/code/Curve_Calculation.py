# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:52:55 2020

@author: Tom
"""

from Variables import r0x, r0y, v0x, v0y, m, k, g
import numpy as np
import scipy.integrate as sp


############Funktionen zur Berechnun der Flugbahn. 1x Mathematisch, 1x Realistisch##########
############################################################################################

def curve_naive(t  = np.linspace(0,25,26) ):
    '''Calculates a simple curve for all t's
    Returns x and y, both arrays with the calculated coordinates'''
    x = r0x + t*v0x
    y = r0y + t*v0y - 0.5*g*t**2
    return (x,y)

def curve_analytical( t = np.linspace(0,25,26) ):
    '''Uses Matroid Matheplanet Tutorial 2 to calculate a curve with air drag.
    Tutorial 2 provided an alayitcal solution to this but it was meant to calculate
    the dragged curve using numerical integration.
    However, this is nice for comparison.
    Returns x and y, both arrays with the calculated coordinates'''  
    #Gleichung 6
    x = r0x + m/k * np.log(k/m * v0x*t + 1)
    
    #Hilfsvariablen gemäss Tutorial
    voo = np.sqrt(m*g/k)
    p = 2*k/m*voo
    lc = lambda x: np.log(np.cos(x)) #Hilfsfunktion für Übersicht
    
    #Gleichung 7, umkehrzeitpunkt
    t_U= voo/g * np.arctan(v0y/voo)
    t_up = [time for time in t if time <= t_U]
    t_down = [time for time in t if time > t_U]
    
    #y_Position bei Umkehrung
    y_U = voo**2/(2*g) * np.log(1 + v0y**2 / voo**2)

    #Gleichung 8
    y_up = r0y + voo**2/g * ( lc( g*(t_U-t_up)/voo ) - lc(g*t_U/voo) )
    
    #Gleichung 9
    y_down = r0y + y_U - voo*(t_down-t_U) - m/k * np.log(0.5*np.exp(-p*(t_down-t_U)) + 0.5)
    
    y = np.append(y_up, y_down)
    return (x,y)


######Runge Kutta#######

def dgl(t, y):
    '''The differential equation to solve.
    See my paper from "Week 8"
	Original Source: https://matheplanet.com/default3.html?call=article.php?sid=1501'''
    r_x = y[0]
    r_y = y[1]
    v_x = y[2]
    v_y = y[3]
    
    p0 = v_x
    p1 = v_y
    p2 = -k/m * np.sqrt(v_x**2 + v_y**2) * v_x
    p3 = -k/m * np.sqrt(v_x**2 + v_y**2) * v_y - g
    
    return [p0, p1, p2, p3]

def runge_kutta_single_time(t):
    '''Runs RK Ord 4 to find Position and Speed at time t.
    Returns time t at the end (which should equal t you inputted),
    as well as position and speed, which are both an array with 2 values for x and y'''
    rk = sp.solve_ivp(fun=dgl, t_span = (0,t), y0 = [r0x, r0y, v0x, v0y], method='RK45', vectorized = True)
    
    assert rk.status == 0
    
    time_at_end     = rk.t[-1]
    position_at_end = rk.y[0:2, -1]
    speed_at_end    = rk.y[2:4, -1]

    """
    #Debug Printing:
    print("t   = ", time_at_end)
    print("Pos = ", position_at_end)
    print("Spd = ", speed_at_end)
    print()
    """
    
    return (time_at_end, position_at_end, speed_at_end)
    

def curve_runge_kutta(t_span = np.linspace(0,25,26)):
    '''Runs runge kutta for a timespan t_span.
    Returns:
        times = all times runge kutta was caculated for.
        positions: list of all positions for each of the t's.
        speeds: list of all speeds for each of the t's.
    To un-zip posititions and speeds use  x, y = zip(*positions)'''
    times = []
    positions = []
    speeds = []
    for t in t_span:
        [te, p, s] = runge_kutta_single_time(t)
        times.append(te)
        positions.append(p)
        speeds.append(s)
    return (times, positions, speeds)




