import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1-x)

def plot(r, ax, x0):
    x = np.arange(0, 13, 1)
    y = np.ones_like(x) * x0
    for i in range(1, len(x)):
        y[i] = logistic(r, y[i-1])
    ax.plot(x, y, "-k", label=str("λ = "+str(r)))
    ax.plot(x, y, ".k")
    ax.set_xlim(0, len(x)-1)
    ax.set_ylim(0, 1.0)
    ax.set_xticks(x)
    ax.set_ylabel("Population x")
    ax.legend(loc="upper left")
    ax.grid()

fig, axs = plt.subplots(3)

plot(0.8, axs[0], 0.5)
plot(1.8, axs[1], 0.025)
plot(2.8, axs[2], 0.025)

axs[2].set_xlabel("Jahr n")

plt.tight_layout()
plt.savefig("../figures/pop_logistic.pdf")
plt.show()
