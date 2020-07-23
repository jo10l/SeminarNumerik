# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:22:10 2020

@author: Tom

This file tests if the Runge Kutta Ansatz is on track with
the previous results, namely if it is about the same as the analytical solution.
"""


import numpy as np
import matplotlib.pyplot as plt

from PlotAssistance import plot_error, plot_nicely
from Variables import r0x, r0y, v0x, v0y, m, k, g
from Curve_Calculation import curve_analytical, curve_naive, curve_runge_kutta


#############Runge Simulator Plotten und Vergleichen mit alten Resultaten##################
###########################################################################################
t, p, s = curve_runge_kutta()
x_rk, y_rk = zip(*p)


plt.figure()

x_math, y_math = curve_naive()
plot_nicely(x_math, y_math, 'b', "Ohne Luftwiderstand")

x_real, y_real = curve_analytical()
plot_nicely(x_real, y_real, 'g', "Analytische Lösung")

plot_nicely(x_rk, y_rk, 'r', 'RungeKutta 4. Ordn.')

plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

##################Geschwindigkeit in längerem Bereich anschauen##############################
################################################################################?#############
t, p, s = curve_runge_kutta(np.linspace(0,50))
vx_rk, vy_rk = zip(*s)

plt.figure()
plt.title("Speed from t=0 to t=50")
plt.plot(t, vx_rk, 'g', label='Speed Horizontal (x)')
plt.plot(t, vy_rk, 'b', label='Speed Vertical (y)')
plt.xlabel('t')
plt.ylabel('Speed')
plt.legend()
plt.grid()
plt.show()

"""Man sieht, dass bei -75m/s die g Kraft durch den Luftwiderstand aufgehoben wird.
Ebenfalls wird die GEschwindigkeit in x-Richtung irgendwann komplett ausgebremst und geht gegen 0.
Die Resultate sind also wie erwartet."""

