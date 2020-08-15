# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:22:10 2020

@author: Tom

Im Ansatz 3 betrachten wir r und v separat.
Zur Berechnung erster Ordnung wird in diesem File lineare Interpolation verwendet.
"""


import numpy as np
import matplotlib.pyplot as plt

from PlotAssistance import plot_error, plot_nicely
from Variables import g
from Curve_Calculation import curve_analytical, curve_naive, curve_runge_kutta, runge_kutta_single_time


###Korrektur Ordnung 1####


class Bodenstation():
    def get_Anfangsbedingungen(self, t):
        '''Satelllite asks at time t for Anfangswerte r0x, r0y, v0x, v0y.
        This method provides these values.'''
        
        #wir erfragen die position für delta_t = 0 und = Intervallhälfte "mid_intervall"
        _, [a, b], [c,d] = runge_kutta_single_time(t)
        return ( a, b, c, d)

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
        
        #t ist z.b. 5 und delta t ist einfach [0, 0.01, ... 0.99, 1.00]
        
        dt = self.intervall_duration
        
        ab_r0x_start,  ab_r0y_start,  ab_v0x_start,  ab_v0y_start = b.get_Anfangsbedingungen(t)
        ab_r0x_end,    ab_r0y_end,    ab_v0x_end,    ab_v0y_end   = b.get_Anfangsbedingungen(t + dt)
        
        #Step 1: v_0_0 ausrechnen:
        v_x0_0 = ab_v0x_start
        v_y0_0 = ab_v0y_start
        
        #Step 2: v_0_1 berechnen:
        v_x0_1 = (ab_v0x_end - v_x0_0       ) / dt
        v_y0_1 = (ab_v0y_end - v_y0_0 + g*dt) / dt
        
        #Step 3: r_0_0:
        r_x0_0 = ab_r0x_start
        r_y0_0 = ab_r0y_start
        
        #Step 4: r_0_1:
        r_x0_1 = ( ab_r0x_end - r_x0_0 - dt*(v_x0_0 + dt*v_x0_1)               ) / dt
        r_y0_1 = ( ab_r0y_end - r_y0_0 - dt*(v_y0_0 + dt*v_y0_1) + 0.5*g*dt**2 ) / dt
        
        
        #Step 5: Der ursprüngliche ansatz ist:
        formel_x = lambda ttt: r_x0_0 + r_x0_1 * ttt   +   ttt*(v_x0_0 + ttt*v_x0_1)
        formel_y = lambda ttt: r_y0_0 + r_y0_1 * ttt   +   ttt*(v_y0_0 + ttt*v_y0_1) - 0.5*g*ttt**2
        
        #Step 6: ERgebnisse sind somit:
        x = formel_x(delta_t)
        y = formel_y(delta_t)
        
        
               
        self.t.extend(t + delta_t)
        self.x.extend(x)
        self.y.extend(y)
    
    def __init__(self, intervall_duration = 1, end_time = 25):
        #Zeiten t, und positionen (x,y), welche der Satellit für sich berechnet.
        self.t = []
        self.x = []
        self.y = []
        '''Schickt den satellit auf Reisen.
        Wir starten bei Zeit 0, und hören bei end_time auf.
        Nach jeweils intervall_duration wird die Bodentation um neue werte gefragt.
        Der Satellit rechnet basierend daraus seine position aus.'''
        
        #we want 1000 measurements in the end, so 1000/#intervals = 1000
        self.intervall_duration = intervall_duration
        
        nof_intervalls = int(end_time // intervall_duration)
        pts_per_intervall = int(1000//nof_intervalls)
        
        delta_t = np.linspace(0 ,intervall_duration, pts_per_intervall, endpoint=False)
        
        for t in np.arange(0, end_time, intervall_duration):
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
plt.title("Störungskorrektur Ordnung 1, linear interpoliert")
plot_nicely(x_rk[::50], y_rk[::50], 'g*', 'Exakt per Runge Kutta berechnet')
plt.plot(sat.x, sat.y, 'r', 'Störungsapproximiert')
#plot_nicely(curve_naive()[0], curve_naive()[1], 'b', 'Ohne Luftwiderstand')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz3_Ordnung1_Linear_Curves.png")
plt.show() ##bereits jetzt ist von auge kein fehler zu erkennen.

#Nur den Fehler plotten:
plt.figure()
plt.title("Fehler Ordnung 1, linear interpoliert, Intervalllänge 1s")
err_x = (x_rk - sat.x)
err_y = (y_rk - sat.y)
err_eukl = np.sqrt(err_x**2 + err_y**2)
#plt.plot(t, err_x, 'g.', label="Fehler in x-Richtung")
#plt.plot(t, err_y, 'b.', label="Fehler in y-Richtung")
plt.plot(t, err_eukl, 'r.', label="Euklidische Fehlerdistanz")
plt.yscale("linear")
plt.xlabel('t')
plt.ylabel('Fehler')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz3_Ordnung1_Linear_Error.png")
plt.savefig("figs/perturbation_fig6.png")    #das ist auch für fig7, wenn man oben dt als stüztstelle durch 2 dividiert.
plt.savefig("figs/perturbation_fig6.eps")
plt.show()  #es ist zu sehen, wie der fehler anwächst im laufe eines intervalls, aber gegen ende wieder runter geht. ebenfalls zu sehen: 4x genauer als 0. ordnung.


###halbes intervall again
sat = Satellit1(intervall_duration=0.5, end_time = 25)
plt.figure()
plt.title("Fehler Ordnung 1, linear interpoliert, Intervalllänge 0.5s")
err_x = (x_rk - sat.x)
err_y = (y_rk - sat.y)
err_eukl = np.sqrt(err_x**2 + err_y**2)
#plt.plot(t, err_x, 'g.', label="Fehler in x-Richtung")
#plt.plot(t, err_y, 'b.', label="Fehler in y-Richtung")
plt.plot(t, err_eukl, 'r.', label="Euklidische Fehlerdistanz")
plt.yscale("linear")
plt.xlabel('t')
plt.ylabel('Fehler')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz3_Ordnung1_Linear_Error_halfintervall.png")
plt.savefig("figs/perturbation_fig8.png")
plt.savefig("figs/perturbation_fig8.eps")
plt.show()  #auch hier wieder 4x besser als vorher.