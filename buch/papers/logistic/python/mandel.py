import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

left = -2.0
right = 1.0
top = 1.0
bottom = -1.0

x = np.linspace(left, right, 2000)
y = np.linspace(bottom, top, 2000)
c = x[:,newaxis] + 1j*y[newaxis,:]
z = c
for i in range(0, 250):
    z = z**2 + c

print("done")

m = 1 - (abs(z) < 2)

plt.imshow(m.T, extent=[left, right, bottom, top], cmap='gray')
plt.xlim(left, right)
plt.ylim(bottom, top)
plt.tight_layout()
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.savefig("../figures/mandel.png", dpi=300)
