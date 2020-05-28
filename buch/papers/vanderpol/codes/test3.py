import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(y,x):
    dydt = np.exp(y)
    return dydt

# initial condition
y0 = 0

# time points
k_list = [0, 1, 2, 3, 4, 5, 6, 7]
x = []
for k in k_list:
    x.append( 1 - 10**-k)


# solve ODE
y = odeint(model,y0,x)
print(y)

# plot results
