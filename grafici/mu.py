from core import *
import numpy as np

def f(x, omega, sigma):
    return omega * np.exp(- (x ** 2) / (2 * sigma ** 2))

x = np.linspace(0, 1, 1000)

#
# Generic
#
omega, sigma = 10, 0.2
y = f(x, omega, sigma)

plt, fig, ax = new_plot()

plot(
    ax,
    x, y,
    label = r'$\mu(x) = \omega_\mu \, \exp\left(-\frac{x^2}{2 \sigma_\mu^2}\right)$'
)

ax.set_xlim(0, 1)
ax.set_ylim(-1, max(y) + 1)
ax.set_xlabel(r"$\frac{t}{T}$")
ax.set_ylabel(r"$\mu(x)$")

set_title(
    ax,
    r"Funzione di crescita $\mu$" + "\n" + r"$\omega_\mu = " + str(omega) + r"$, $\sigma_\mu = " + str(sigma) + r"$"
)

ax.grid(True, linestyle = "--", alpha = 0.6)
ax.legend(loc = "upper right")

show_plot(plt, "functions/mu.pdf")

#
# Sigma
#

plt, fig, ax = new_plot()

for sigma in [0.05, 0.1, 0.2, 0.3, 0.5]:
    y = f(x, omega, sigma)
    plot(
        ax,
        x, y,
        label = r'$\sigma_\mu = ' + str(sigma) + r'$',
        color = None
    )

ax.set_xlim(0, 1)
ax.set_ylim(-1, max(y) + 1)
ax.set_xlabel(r"$\frac{t}{T}$")
ax.set_ylabel(r"$\mu(x)$")

set_title(
    ax,
    r"Funzione di crescita $\mu$" + "\n" + r"$\omega_\mu = " + str(omega) + r"$"
)

ax.grid(True, linestyle = "--", alpha = 0.6)
ax.legend(loc = "upper right")

show_plot(plt, "functions/mu_sigma.pdf")