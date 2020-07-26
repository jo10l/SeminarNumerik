#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:33:27 2020

@author: midori
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100,100000)
f = np.sqrt((1+2*x)/(1+x))
ft = 1 + x/2 - 5/8*x**2 +13/16*x**3 - 141/128*x**4 + 399/256*x**5 - 2353/1024*x**6 + 7205/2048*x**7
pad = (1 + 13/4*x + 41/16*x**2)/(1 + 11/4*x + 29/16*x**2)

diff1 = abs(ft-f)
diff2 = abs(pad-f)

plt.figure("Taylor")
plt.ylim(1, 4)
plt.xlim(0, 10)
plt.plot(x, f)
plt.plot(x, ft)
plt.grid(True)
plt.hlines(np.sqrt(2), 0,10)
plt.savefig("bilder/taylorProb{}.pdf".format(1))

plt.figure("Pade")
#plt.ylim(1, 2)
plt.xlim(0, 100)
plt.plot(x, f)
plt.plot(x[::100], pad[::100],"--")
plt.grid(True)
plt.hlines(np.sqrt(2), 0,100)
plt.savefig("bilder/taylorProb{}.pdf".format(2))

plt.figure("Taylor diff")
plt.grid(True)
plt.ylim(0, 10)
plt.xlim(0, 10)
plt.plot(x, diff1)
plt.savefig("bilder/taylorProb{}.pdf".format(3))

plt.figure("Pade diff")
plt.grid(True)
#plt.ylim(0, 0.1)
plt.xlim(0, 100)
plt.plot(x, diff2)
plt.savefig("bilder/taylorProb{}.pdf".format(4))