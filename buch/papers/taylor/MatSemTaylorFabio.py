'''
28.4.2020
@Autor: Fabio Marti
Logistische Funktion die anhand von Runge-Kutta und Taylor approximiert wird.
Also korrekte loesung wird die homogene Loesung der Differentialgleichung angezeigt
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline


# homogene Loesung der DGL mit Annahme G=1, f0=0.5 und k=1
def logift(x, k=1, G=1):
    return G/(1+np.e**(-G*k*x)*(G/f0-1))

# Ableitungen der Logistischen Funktion
# y' = k*y*(G-y)
# k = np.log(1/y-1)/x
def logisticft1(x,y):
    return np.log(1/y-1)/x*(y**2-y)

def logisticft2(x,y):
    return -np.log(1/y-1)/x*logisticft1(x,y)*(1-2*y)

def logisticft3(x,y):
    return -np.log(1/y-1)/x*(logisticft2(x,y)-2*(y*logisticft2(x,y)+logisticft1(x,y)**2))

def logisticft4(x,y):
    return -np.log(1/y-1)/x*(logisticft3(x,y)-2*(y*logisticft3(x,y)+3*logisticft1(x,y)*logisticft2(x,y)))

def logisticft5(x,y):
    return -np.log(1/y-1)/x*(logisticft4(x,y)-2*(y*logisticft4(x,y)+4*logisticft1(x,y)*logisticft3(x,y)+3*logisticft2(x,y)**2))


'''
Erarbeiten der Logistischen Funktion anhand von Runge Kutta:
'''

def rungafunction(y0, runga_start, runga_end, runga_nsteps, runga_rank):
    runga_steps = np.linspace(runga_start, runga_end, runga_nsteps+1)
    step = runga_steps[1] - runga_steps[0]
    halfstep = step/2
    yaprox = y0
    rungaft = range(runga_nsteps+1)
    rungaft[0]=yaprox
    derivation = 0

    for n in range(runga_nsteps):
        for r in range(runga_rank):
            if r == 0:
                derivation = logisticft1(runga_steps[n], yaprox)
            else:
                derivation = logisticft1(runga_steps[n]+halfstep, yaprox+derivation*halfstep)
        yaprox = yaprox+derivation*step
        rungaft[n+1]=yaprox
    return rungaft


'''
Erarbeiten der Logistischen Funktion anhand der Taylorgleichung
'''
def taylorfunction(y0, taylor_start, taylor_end, taylor_nsteps, taylor_rank):
    taylor_steps = np.linspace(taylor_start, taylor_end, taylor_nsteps+1)
    step = taylor_steps[1] - taylor_steps[0]
    yaprox = y0
    taylorft = range(taylor_nsteps+1)
    taylorft[0]=yaprox

    for n in range(taylor_nsteps):
        yaprox += logisticft1(taylor_steps[n], yaprox)*step
        if taylor_rank > 1:
            yaprox += logisticft2(taylor_steps[n], yaprox)/2*step**(2)
        if taylor_rank > 2:
            yaprox += logisticft3(taylor_steps[n], yaprox)/6*step**(3)
        if taylor_rank > 3:
            yaprox += logisticft4(taylor_steps[n], yaprox)/24*step**(4)
        if taylor_rank > 4:
            yaprox += logisticft5(taylor_steps[n], yaprox)/120*step**(5)
        taylorft[n+1]=yaprox
    return taylorft


def maxFehlerRunga(runga_nsteps, yr, rungaft):
    maxFehler = 0
    for n in range(runga_nsteps+1):
        if abs(yr[n]-rungaft[n]) > maxFehler:
            maxFehler = abs(yr[n]-rungaft[n])
    return maxFehler

def maxFehlerTaylor(taylor_nsteps, yt, taylorft):
    maxFehler = 0
    for n in range(taylor_nsteps+1):
        if abs(yt[n]-taylorft[n]) > maxFehler:
            maxFehler = abs(yt[n]-taylorft[n])
    return maxFehler

# Allgemeine Werte
size = 10000
start = -5
end = -0.02
x = np.linspace(start, end, size)
G = 1 # Endwert festgelegt, nicht aenderbar
f0 = 0.5  # Anfangswert y(0), nicht aenderbar
k = 1  # Wachstumsrate, aendert nur fuer Gleichung, nicht fuer Taylorapproximation

runga_start = start
runga_end = end
runga_nsteps = 5
runga_rank = 5
runga_steps = np.linspace(runga_start, runga_end, runga_nsteps+1)

taylor_start = start
taylor_end = end
taylor_nsteps = 5
taylor_rank = 5
pos = (taylor_end-taylor_start)/2
taylor_steps = np.linspace(taylor_start, taylor_end, taylor_nsteps+1)

# Zur Darstellung der DGL
ngraphs = 6
endDGL = 2
startDGL = -2
xDGL = np.linspace(start, endDGL, size)

# Berechnung der exakten Kurve
y = logift(x, k)

# Berechnung der Ableitungen in der Mitte
ytest1 = logisticft1(x,y)
ytest2 = logisticft2(x,y)
ytest3 = logisticft3(x,y)
ytest4 = logisticft4(x,y)
ytest5 = logisticft5(x,y)


rungaft1 = rungafunction(logift(start), runga_start, runga_end, runga_nsteps, 1)
taylorft1 = taylorfunction(logift(start), taylor_start, taylor_end, taylor_nsteps, 1)
rungaft2 = rungafunction(logift(start), runga_start, runga_end, runga_nsteps, 2)
taylorft2 = taylorfunction(logift(start), taylor_start, taylor_end, taylor_nsteps, 2)
rungaft3 = rungafunction(logift(start), runga_start, runga_end, runga_nsteps, 3)
taylorft3 = taylorfunction(logift(start), taylor_start, taylor_end, taylor_nsteps, 3)
rungaft4 = rungafunction(logift(start), runga_start, runga_end, runga_nsteps, 4)
taylorft4 = taylorfunction(logift(start), taylor_start, taylor_end, taylor_nsteps, 4)
rungaft5 = rungafunction(logift(start), runga_start, runga_end, runga_nsteps, 5)
taylorft5 = taylorfunction(logift(start), taylor_start, taylor_end, taylor_nsteps, 5)


rungaft = rungafunction(logift(start), runga_start, runga_end, runga_nsteps, runga_rank)
taylorft = taylorfunction(logift(start), taylor_start, taylor_end, taylor_nsteps, taylor_rank)
yr = logift(np.linspace(runga_start, runga_end, runga_nsteps+1))
yt = logift(np.linspace(taylor_start, taylor_end, taylor_nsteps+1))
   


plt.figure()
plt.plot(x, y, linestyle='-', marker='', color="black", label='Logistische Funktion')
plt.plot(runga_steps, rungaft1, linestyle='-', marker='.', color="#6060FF", label='Runge-Kutta/Taylor Approximation, Ordnung = 1')
'''
plt.plot(runga_steps, rungaft1, linestyle='-', marker='.', color="#6060FF", label='Runga Approximation, Ordnung = 1')
plt.plot(taylor_steps, taylorft1, linestyle='-', marker='.', color="#60FF60", label='Taylor Approximation, Ordnung = 1')
plt.plot(runga_steps, rungaft2, linestyle='-', marker='.', color="#2020C0", label='Runga Approximation, Ordnung = 2')
plt.plot(taylor_steps, taylorft2, linestyle='-', marker='.', color="#20C020", label='Taylor Approximation, Ordnung = 2')
plt.plot(runga_steps, rungaft3, linestyle='-', marker='.', color="#0000A0", label='Runga Approximation, Ordnung = 3')
plt.plot(taylor_steps, taylorft3, linestyle='-', marker='.', color="#00A000", label='Taylor Approximation, Ordnung = 3')
plt.plot(runga_steps, rungaft4, linestyle='-', marker='.', color="#000060", label='Runga Approximation, Ordnung = 4')
plt.plot(taylor_steps, taylorft4, linestyle='-', marker='.', color="#006000", label='Taylor Approximation, Ordnung = 4')
'''
plt.plot(runga_steps, rungaft5, linestyle='-', marker='.', color="#000080", label='Runge-Kutta Approximation, Ordnung = 5')
plt.plot(taylor_steps, taylorft5, linestyle='-', marker='.', color="#008000", label='Taylor Approximation, Ordnung = 5')
plt.legend(loc="best")
#plt.ylim(0, 0.5)
plt.xlim(start, end)
#plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
plt.legend(loc="upper left")
plt.grid()
plt.xlabel('x-Achse (Zeit)')
plt.ylabel('y-Achse (Anzahl)')
plt.savefig('LogisticFunction.pdf')


plt.figure()
plt.plot(runga_steps, (yr-rungaft)*1e6, linestyle='-', marker='', color="blue", label='Fehler Runge Approximation, Ordnung = 5')
plt.plot(taylor_steps, (yt-taylorft)*1e6, linestyle='-', marker='', color="green", label='Fehler Taylor Approximation, Ordnung = 5')
plt.legend(loc="best")
# plt.ylim(0, 0.5)
plt.xlim(start, end)
plt.legend()
plt.grid()
plt.xlabel('x-Achse (Zeit)')
plt.ylabel('Fehler in Millionstel')
plt.savefig('FehlerRungaUndTaylor.pdf')


yn=range(ngraphs)

for n in range(ngraphs):
    yn[n] = logift(xDGL,4**(n-3))
    
color=["#A0FFA0","#60FF60","#20C020","#00A000","#006000","#002000","#FF6060","#C02020","#A00000","#600000"]

plt.figure()
for r in range(ngraphs):
    n = ngraphs-r-1
    labelDGL = 'DGL mit k =' + str(4**(n-3))
    plt.plot(xDGL, yn[n], linestyle='-', marker='', color=color[n], label=labelDGL)
    if r == ngraphs/2:
        plt.legend(loc="upper left")
plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
plt.legend(loc="upper left")
# plt.ylim(0, 0.5)
plt.xlim(startDGL, endDGL)
plt.grid()
plt.xlabel('x-Achse (Zeit)')
plt.ylabel('y-Achse (Anzahl)')
plt.savefig('DGLDarstellung.pdf')

