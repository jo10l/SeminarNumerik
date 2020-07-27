# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:28:45 2020

@author: Tom-LT

Turorial:
https://matheplanet.com/matheplanet/nuke/html/article.php?sid=735

Ein anderes Tutorial mit anderem Ansatz
https://matheplanet.com/default3.html?call=article.php?sid=1501



Konvention:
    Wir schauen immer den Zeitbereich von t=0 bis t=25 an mit Schritten von t=1.
    So geht es sauber auf mit den Indexes.
    Diese Werte sind auch als Defaults gsetzt bei den einzelnen Funktionen.
"""


import numpy as np
import matplotlib.pyplot as plt

from PlotAssistance import plot_error, plot_nicely
from Variables import r0x, r0y, v0x, v0y, m, k, g
from Curve_Calculation import curve_analytical, curve_naive



########################Reguläre Bahnen plotten##################
#################################################################


plt.figure()

x_naive, y_naive = curve_naive()
plot_nicely(x_naive, y_naive, 'b', "Ohne Luftwiderstand")

x_analytical, y_analytical = curve_analytical()
plot_nicely(x_analytical, y_analytical, 'r', "Mit Luftwiderstand")

plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()


#########################Lineare Störungskorrektur#####################
#######################################################################


#Initial Values for t=0 - nothing to correct, no correcetion factors
x_lin = [x_naive[0]]
y_lin = [y_naive[0]]


for t in range(1,26):
    #update position for t=1..25
    
    #Calculate ny based on measurement at t-1
    #for t=1, this is div by zero. just set ny to 0 then
    if (t==1):
        ny_x=ny_y=0
    else:
        ny_x = (x_analytical[t-1] - r0x - (t-1)*v0x)/(t-1)**2
        ny_y = (y_analytical[t-1] - r0y - (t-1)*v0y + 0.5*g*(t-1)**2)/(t-1)**2
    
    #Calculate Position at t=t iwth the nov calculated ny
    #Gleichung 3 einsetzen
    x_corr_new = r0x + t*(v0x + ny_x*t)
    y_corr_new = r0y + t*(v0y + ny_y*t) - 0.5*g*t**2
    
    x_lin.append(x_corr_new)
    y_lin.append(y_corr_new)
    


plt.figure()
plt.title("Lineare Korrektur")
plot_nicely(x_naive, y_naive, 'b', "Ohne Luftwiderstand")
plot_nicely(x_analytical, y_analytical, 'r', "Mit Luftwiderstand")
plot_nicely(x_lin, y_lin, 'c', "Linear korrigiert")

plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
#plt.legend(loc = 'upper right')
plt.grid()
plt.show()



#################Quadratische Korrektur###################
##########################################################

x_qd = [x_naive[0],x_naive[1]]
y_qd = [y_naive[0],y_naive[1]]   ##adding first 2 positions here since we cannot correct them.

for t in range(2,26):
    #calculate position predictions for t=2..25
    #we use existing data for t-1 und t-2
    
    #Gleichung 5 auf Seite 3
    A = np.array([[1, t-1], [1,t-2]])
    
    if (t==2):
        ny_x1 = ny_x2 = ny_y1 = ny_y2 = 0
    else:
        b_help = lambda t: (x_analytical[t] - r0x - v0x*t ) / t**2
        b = np.array([b_help(t-1), b_help(t-2)])
        ny_x1, ny_x2 = np.linalg.inv(A) @ b
        
        #Gleichung 6
        b_help = lambda t: (y_analytical[t] - r0y - v0y*t + 0.5*g*t**2 ) / t**2
        b = np.array([b_help(t-1), b_help(t-2)])
        ny_y1, ny_y2 = np.linalg.inv(A) @ b
    

    
    #Predict Position for t=2 and onwars [Gleichung £]
    #note for t=2 this will just resulat in mathematical position ;)
    x_corr_new = r0x + v0x*t + ny_x1*t**2 + ny_x2 * t**3
    y_corr_new = r0x + v0y*t + ny_y1*t**2 + ny_y2 * t**3 - 0.5*g*t**2
    
    x_qd.append(x_corr_new)
    y_qd.append(y_corr_new)



plt.figure()
plt.title("Mit quadratischer Abhängigkeit")
plot_nicely(x_naive, y_naive, 'b', "Ohne Luftwiderstand")
plot_nicely(x_analytical, y_analytical, 'r*', "Mit Luftwiderstand")
plot_nicely(x_qd, y_qd, 'k', "Quadratisch korrigiert")

plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()




##########Fehler Plotten############
####################################


plt.figure()
plt.title("Fehler")

plot_error(x_analytical, y_analytical, x_naive, y_naive, 'b+', 'Ohne Korrektur')
plot_error(x_analytical, y_analytical, x_lin, y_lin, 'b.', 'Lineare Korrektur')
plot_error(x_analytical, y_analytical, x_qd, y_qd, 'b*', 'Quadratische Korrektur')

plt.xlabel('t')
plt.ylabel('Fehler')
plt.legend()
plt.grid()
plt.show()


###Plot all Results as text###

for t in range(26):
    print("===================== t = {} =========================".format(t))
    print("{:>35s}({: 8.2f},{: 8.2f})".format("Position Naive: ", x_naive[t], y_naive[t] ))
    print("{:>35s}({: 8.2f},{: 8.2f})".format("Position Analystical: ", x_analytical[t], y_analytical[t] ))
    print("{:>35s}({: 8.2f},{: 8.2f})".format("Position Linear Corrected: ", x_lin[t], y_lin[t] ))
    print("{:>35s}({: 8.2f},{: 8.2f})".format("Position Quadratic Corrected: ", x_qd[t], y_qd[t] ))
    print()

