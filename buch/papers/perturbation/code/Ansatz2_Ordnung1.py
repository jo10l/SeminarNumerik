# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:22:10 2020

@author: Tom
Störungstheorie erster Ordnung mit Sattelit und Bodenstation
"""


import numpy as np
import matplotlib.pyplot as plt

from PlotAssistance import plot_error, plot_nicely
from Variables import g
from Curve_Calculation import curve_analytical, curve_naive, curve_runge_kutta, runge_kutta_single_time


###Korrektur Ordnung 1####


class Bodenstation():
    def get_Anfangsbedingungen(self, t, mid_intervall):
        '''Satelllite asks at time t for Anfangswerte r0x, r0y, v0x, v0y.
        This method provides these values.'''
        
        #grundwerte für delta_t = 0 und delkta_t = mid_intervall
        _, [b0_r0x, b0_r0y], [b0_v0x, b0_v0y] = runge_kutta_single_time(t)
        _, [bm_r0x, bm_r0y], [bm_v0x, bm_v0y] = runge_kutta_single_time(t+mid_intervall)
        
        #jetzt müssen wir die unbekannten evaluieren.
        #wir nutrzen die foglenden variablne:
        #x(t) = r0x + v0x * dt  = r0x_0 + t*r0x_1 + dt* ( v0x_0 + t*v0x_1 )
        #y(t) = r0y + v0y * dt  = r0y_0 + t*r0y_1 + dt* ( v0y_0 + t*v0y_1 ) - 0.5*g*dt**2
        
        #Terme 0.ter Ordnung sind einfach:
        r0x_0 = b0_r0x
        r0y_0 = b0_r0y
        
        v0x_0 = b0_v0x
        v0y_0 = b0_v0y
        
        dt = mid_intervall
        
        
        v0x_1 = (bm_v0x - v0x_0) / dt
        r0x_1 = (bm_r0x - r0x_0 - dt*(v0x_0 + v0x_1*dt)) / dt       
        
        v0y_1 = (bm_v0y - v0y_0 + g*dt) / dt
        r0y_1 = (bm_r0y - r0y_0 - dt*(v0y_0 + v0y_1*dt) + 0.5*g*dt**2) / dt  
        
        #der satellit will ja eig nur r0x, r0y, v0x, v0y kennen, die jetzt halt von dt abhäöngen.
        #wir können dazu lambdas returnen.
        
        r0x = lambda dt: r0x_0 + dt*r0x_1
        r0y = lambda dt: r0y_0 + dt*r0y_1
        
        v0x = lambda dt: v0x_0 + dt*v0x_1
        v0y = lambda dt: v0y_0 + dt*v0y_1
        
        return ( r0x, r0y, v0x, v0y )

b = Bodenstation()


class Satellit1():
    #Zeiten t, und positionen (x,y), welche der Satellit für sich berechnet.
    t = []
    x = []
    y = []
    
    intervall_duration = 1
    
    #Satellit hat kontakt zur Bodenstation
    b = Bodenstation();
    
    def calculate_pos_in_near_future(self, t, delta_t):
        '''Der Satellit nutzt diese Methode, um seine Position zu berechnen.
        Er verlangt nach Anfangswerten und rechnet danan die Position für die delta_t aus.
        Die Resultate werden in den Klassenmembern gespeichert.'''
        
        #müssen die mitte des intervalls kennen:
        mid_intervall = self.intervall_duration
        
        b_r0x,  b_r0y,  b_v0x,  b_v0y = b.get_Anfangsbedingungen(t, mid_intervall)

        
        #rechne wie bei 0ter ordnung, aber die r0 und v0 sind jetzt abhängig von delta_t
        
        x = b_r0x(delta_t) + delta_t * b_v0x(delta_t)
        y = b_r0y(delta_t) + delta_t * b_v0y(delta_t) - 0.5*g*delta_t**2
        
        self.t.extend(t + delta_t)
        self.x.extend(x)
        self.y.extend(y)
    
    def __init__(self, intervall_duration = 1, end_time = 25):
        '''Schickt den satellit auf Reisen.
        Wir starten bei Zeit 0, und hören bei end_time auf.
        Nach jeweils intervall_duration wird die Bodentation um neue werte gefragt.
        Der Satellit rechnet basierend daraus seine position aus.'''
        
        #we want 1000 measurements in the end, so 1000/#intervals = 1000
        self.intervall_duration = intervall_duration
        
        nof_intervalls = end_time // intervall_duration
        pts_per_intervall = 1000//nof_intervalls
        
        delta_t = np.linspace(0 ,intervall_duration, pts_per_intervall, endpoint=False)
        
        for t in range(0, end_time, intervall_duration):
            self.calculate_pos_in_near_future(t, delta_t)
        
    
    
        

sat = Satellit1(intervall_duration=1, end_time = 25)
    
####Resultate Plotten####

timespan = np.linspace(0,25,1000, endpoint=False)

#'echte kurve'##
t, p, s = curve_runge_kutta(timespan)
x_rk, y_rk = zip(*p)
x_rk = np.array(x_rk)
y_rk = np.array(y_rk)

plt.figure()
plt.title("Störungskorrektur Ordnung 1")
plot_nicely(x_rk[::50], y_rk[::50], 'g*', 'Exakt per Runge Kutta berechnet')
plot_nicely(sat.x, sat.y, 'r', 'Störungsapproximiert')
plot_nicely(curve_naive()[0], curve_naive()[1], 'b', 'Ohne Luftwiderstand')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz2_Ordnung1_Curves.png")
plt.show() ##bereits jetzt ist von auge kein fehler zu erkennen.


#Nur den Fehler plotten:
plt.figure()
plt.title("Fehler")
err_x = (x_rk - sat.x)
err_y = (y_rk - sat.y)
err_eukl = np.sqrt(err_x**2 + err_y**2)
plt.plot(t, err_x, 'g.', label="Fehler in x-Richtung")
plt.plot(t, err_y, 'b.', label="Fehler in y-Richtung")
plt.plot(t, err_eukl, 'r.', label="Euklidische Distanz")
plt.yscale("linear")
plt.xlabel('t')
plt.ylabel('Fehler')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz2_Ordnung1_Error.png")
plt.show()  #es ist zu sehen, wie der fehler anwächst im laufe eines intervalls, und sich dann wieder resettet.



#Nur den Fehler plotten der erstn 200 damit man es besser sehen kann.
plt.figure()
plot_error(x_rk[:200], y_rk[:200], sat.x[:200], sat.y[:200], 'r.', 'Fehler (eukl. Distanz)', timespan[:200])
plt.xlabel('t')
plt.ylabel('Fehlerdistanz')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz2_Ordnung1_Error_detail.png")
plt.show()  #es ist zu sehen, wie der fehler anwächst im laufe eines intervalls, und sich dann wieder resettet.

