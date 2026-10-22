from core import *
import numpy as np

def f(x, omega, sigma):
    return omega * np.exp(- ((x - 1) ** 2) / (2 * sigma ** 2))

x = np.linspace(0, 1, 1000)

#
# Generic
#
beta, sigma = 0.5, 0.2
y = f(x, beta, sigma)

plt, fig, ax = new_plot()

plot(
    ax,
    x, y,
    label = r'$\nu(x, \beta) = \beta \exp\left(-\frac{{(x - 1)}^2}{2 \sigma_\nu^2}\right)$'
)

ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel(r"$\frac{t}{T}$")
ax.set_ylabel(r"$\nu(x, \beta)$")

set_title(
    ax,
    r"Funzione di abbandono $\nu$" + "\n" + r"$\beta = " + str(beta) + r"$, $\sigma_\nu = " + str(sigma) + r"$"
)

ax.grid(True, linestyle = "--", alpha = 0.6)
ax.legend(loc = "upper left")

show_plot(plt, "functions/nu.pdf")