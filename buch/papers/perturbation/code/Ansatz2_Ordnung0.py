# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:22:10 2020

@author: Tom

Störungstheorie Ordnung 0 mit Sattelit und Bodenstation
"""


import numpy as np
import matplotlib.pyplot as plt

from PlotAssistance import plot_error, plot_nicely
from Variables import g
from Curve_Calculation import curve_analytical, curve_naive, curve_runge_kutta, runge_kutta_single_time


###Korrektur Ordnung 0####
###Paper von Dani Woche 7###

#For easier understandiung, we do it object oriented.

class Bodenstation():
    def get_Anfangsbedingungen(self, t):
        '''Satelllite asks at time t for Anfangswerte r0x, r0y, v0x, v0y.
        This method provides these values.'''
        _, [b_r0x, b_r0y], [b_v0x, b_v0y] = runge_kutta_single_time(t)
        return ( b_r0x, b_r0y, b_v0x, b_v0y )

class Satellit0():   
    #Satellit hat kontakt zur Bodenstation
    b = Bodenstation();
    
    def calculate_pos_in_near_future(self, t, delta_t):
        '''Der Satellit nutzt diese Methode, um seine Position zu berechnen.
        Er verlangt nach Anfangswerten zur Zeit t und rechnet danan die Position für die folgende Zeit delta_t aus.
        Die Resultate werden in den Klassenmembern gespeichert.'''
        b_r0x, b_r0y, b_v0x, b_v0y = self.b.get_Anfangsbedingungen(t)
        
        #daraus positionen berechnen für das intervall delta_t, z.B. für delta_t = [0, 0.25, 0.5, 0.75]
        x = b_r0x + delta_t * b_v0x
        y = b_r0y + delta_t * b_v0y - 0.5*g*delta_t**2
        
        self.t.extend(t + delta_t)
        self.x.extend(x)
        self.y.extend(y)
    
    def __init__(self, intervall_duration = 1, end_time = 25):
        self.t = []
        self.x = []
        self.y = []
        '''Schickt den satellit auf Reisen.
        Wir starten bei Zeit 0, und hören bei end_time auf.
        Man kann die Intervall-Dauer mit geben.
        Daraus ergeben sich die Anzahl Intervalle, also bei end_time25, 1sec intervall wären das 25 intervalle.
        
        Insgesamt wollen wir am ende 1000 Positionswerte (für easy plotting).
        
        Nach jeweils intervall_duration wird die Bodentation um neue werte gefragt.
        Der Satellit rechnet basierend daraus seine position aus.'''
        
        #we want 1000 measurements in the end, so 1000/#intervals = 1000
        nof_intervalls = int(end_time // intervall_duration)
        pts_per_intervall = int(1000//nof_intervalls)
        
        delta_t = np.linspace(0 ,intervall_duration, pts_per_intervall, endpoint=False)
        
        for t in np.arange(0, end_time, intervall_duration):
            self.calculate_pos_in_near_future(t, delta_t)
        
    
    


sat = Satellit0(intervall_duration=1, end_time = 25)
    
####Resultate Plotten####

timespan = np.linspace(0,25,1000, endpoint=False)

##'echte kurve'##
t, p, s = curve_runge_kutta(timespan)
x_rk, y_rk = zip(*p)
x_rk = np.array(x_rk)
y_rk = np.array(y_rk)

plt.figure()
plt.title("Störungskorrektur Ordnung 0")
plot_nicely(x_rk[::50], y_rk[::50], 'g*', 'Exakt per Runge Kutta berechnet')
plot_nicely(sat.x, sat.y, 'r', 'Störungsapproximiert')
plot_nicely(curve_naive()[0], curve_naive()[1], 'b', 'Ohne Luftwiderstand')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz2_Ordnung0_Curves.png")
plt.show() ##bereits jetzt ist von auge kein fehler zu erkennen.


#Nur den Fehler plotten:
plt.figure()
plt.title("Fehler mit Intervalllänge 1s")
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
plt.savefig("figs/Ansatz2_Ordnung0_Errors.png")       ####Figure 3
plt.savefig("figs/perturbation_fig3.png")       ####Figure 3
plt.savefig("figs/perturbation_fig3.eps")       ####Figure 3
plt.show()  #es ist zu sehen, wie der fehler anwächst im laufe eines intervalls, und sich dann wieder resettet.



#############################################
##Halbierung der Intervalllänge
################################################
sat = Satellit0(intervall_duration=0.5, end_time = 25)

timespan = np.linspace(0,25,1000, endpoint=False)

#Nur den Fehler plotten:
plt.figure()
plt.title("Fehler mit Intervalllänge 0.5s")
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
plt.savefig("figs/Ansatz2_Ordnung0_Intervall0.5s_Errors.png")
plt.savefig("figs/perturbation_fig4.png")       ####Figure 4
plt.savefig("figs/perturbation_fig4.eps")       ####Figure 4
plt.show()  #es ist zu sehen, der fehler ist etwa 4x kleiner geworden, also 2 bit GEanugikeitsgewinn.


#####nochmal halbieren:
sat = Satellit0(intervall_duration=0.25, end_time = 25)

timespan = np.linspace(0,25,1000, endpoint=False)

#Nur den Fehler plotten:
plt.figure()
plt.title("Fehler mit Intervalllänge 0.25s")
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
plt.savefig("figs/Ansatz2_Ordnung0_Intervall0.25s_Errors.png")
plt.savefig("figs/perturbation_fig5.png")       ####Figure 4
plt.savefig("figs/perturbation_fig5.eps")       ####Figure 4
plt.show()  #es ist zu sehen, der fehler ist etwa 4x kleiner geworden, also 2 bit Geanugikeitsgewinn.


##für debug: bahn x und bahn y separat geplottet##
"""
plt.figure()
plt.plot(timespan, x_rk, 'r', label='x rk')
plt.plot(timespan, y_rk, 'b', label='y rk')
plt.plot(timespan, sat.x, 'c', label='x sat')
plt.plot(timespan, sat.y, 'g', label='y sat')
plt.legend()
plt.xlabel('t')
plt.ylabel('x und y position')
plt.show()
"""