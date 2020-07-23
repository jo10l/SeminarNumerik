# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:28:56 2020

@author: Tom
"""

#Konstanten
g   = 9.81   #Erdanziehung
rho = 1.293  #Dichte des Mediums. Annahme: Standardluft T= 0° und p = 1013hPa konstant
c_w = 0.45   #Einfluss der Geometrie und Material. Experimentell zu bestimmender Wert. Eigentlich wäre der von der GEschwindigkeit abhängig.
A   = 0.045  #Sitrnfläche des Körper
m   = 7.275  # masse vom Körper
k   = 0.5 * rho * c_w * A  # alle Obigen zusammen, es gilt F_Luft = k*v^2


#set global start parameters
r0x = 0
r0y = 0
v0x = 100
v0y = 100