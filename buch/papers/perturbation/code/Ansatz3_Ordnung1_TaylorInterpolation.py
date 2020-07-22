# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:22:10 2020

@author: Tom

Im Ansatz 3 betrachten wir r und v separat.
Zur Berechnung erster Ordnung wird in diesem File Taylor Approximation verwendet.
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




class Satellit1t():

    
    def calculate_pos_in_near_future(self, t, delta_t):
        '''Der Satellit nutzt diese Methode, um seine Position zu berechnen.
        Er verlangt nach Anfangswerten und rechnet danan die Position für die delta_t aus.
        Die Resultate werden in den Klassenmembern gespeichert.'''
        
        #t ist z.b. 5 und delta t ist einfach [0, 0.01, ... 0.99, 1.00]
        
        eps = 0.001
        
        ab_r0x_start,  ab_r0y_start,  ab_v0x_start,  ab_v0y_start = self.b.get_Anfangsbedingungen(t)
        ab_r0x_end,    ab_r0y_end,    ab_v0x_end,    ab_v0y_end   = self.b.get_Anfangsbedingungen(t + eps)
        
        all_start = np.array( self.b.get_Anfangsbedingungen(t) )
        all_end = np.array( self.b.get_Anfangsbedingungen(t + eps) )
        
        #Step 1: r0 v0 wie üblich
        r_x0_0 = ab_r0x_start
        r_y0_0 = ab_r0y_start
        v_x0_0 = ab_v0x_start
        v_y0_0 = ab_v0y_start
    

        
        #Step 2: Ableitung gemäss Runge Kutta:
        dot_rx0, dot_ry0, dot_vx0, dot_vy0 = (all_end - all_start ) / eps
        r_x0_1 = dot_rx0
        r_y0_1 = dot_ry0
        v_x0_1 = dot_vx0
        v_y0_1 = dot_vy0
                
        """Ich betrachte hier v udn rseparat, ohne deren interaktion, drum geht der fehler eig erst hoch und so etc pp blabla, is mir jetzt aber egal."""
    
        
        #Step 5: Der ursprüngliche ansatz ist:
        formel_x = lambda ttt: r_x0_0 + r_x0_1 * ttt   #+   ttt*(v_x0_0 + ttt*v_x0_1)
        formel_y = lambda ttt: r_y0_0 + r_y0_1 * ttt   #+   ttt*(v_y0_0 + ttt*v_y0_1) - 0.5*g*ttt**2
        
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
        self.b = Bodenstation()
        
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
        
    
    
        

sat = Satellit1t(intervall_duration=1, end_time = 25)
    
####Resultate Plotten####

timespan = np.linspace(0,25,1000, endpoint=False)

#'echte kurve'##
t, p, s = curve_runge_kutta(timespan)
x_rk, y_rk = zip(*p)
x_rk = np.array(x_rk)
y_rk = np.array(y_rk)

plt.figure()
plt.title("Störungskorrektur Ordnung 1, Taylor")
plot_nicely(x_rk[::5], y_rk[::5], 'g*', 'Exakt per Runge Kutta berechnet')
plot_nicely(sat.x, sat.y, 'r', 'Störungsapproximiert')
#plot_nicely(curve_naive()[0], curve_naive()[1], 'b', 'Ohne Luftwiderstand')
#plt.axis('equal')
plt.xlim(200,500)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz3_Ordnung1_Taylor_Curves.png")
plt.show() ##bereits jetzt ist von auge kein fehler zu erkennen.


#Nur den Fehler plotten:
plt.figure()
plt.title("Fehler Ordnung 1, Taylor interpoliert, Intervalllänge 1")
err_x = (x_rk - sat.x)
err_y = (y_rk - sat.y)
err_eukl = np.sqrt(err_x**2 + err_y**2)
plt.plot(t, err_x, 'g.', label="Fehler in x-Richtung")
plt.plot(t, err_y, 'b.', label="Fehler in y-Richtung")
plt.plot(t, err_eukl, 'r.', label="Euklidische Fehlerdistanz")
plt.yscale("linear")
plt.xlabel('t')
plt.ylabel('Fehler')
plt.legend()
plt.grid()
plt.savefig("figs/Ansatz3_Ordnung1_Taylor_Error.png")
plt.show()  #jo das hat uns sozusagen nix gebrahct, da taylor halt am anfang genauer ist, hinten raus aber schlechter.


###halbes intervall again
sat = Satellit1t(intervall_duration=0.5, end_time = 25)
plt.figure()
plt.title("Fehler Ordnung 1, Taylor interpoliert, Intervalllänge 0.5")
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
plt.savefig("figs/Ansatz3_Ordnung1_Taylor_Error_halfintervall.png")
plt.show()  #faktor vier besser