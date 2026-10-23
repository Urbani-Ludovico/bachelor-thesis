import matplotlib.pyplot as plt
import numpy as np
import pathlib
import os

def f(x, omega, sigma):
    return omega * np.exp(- (x ** 2) / (2 * sigma ** 2))

x = np.linspace(0, 1, 1000)

#
# Generic
#
omega, sigma = 10, 0.2
y = f(x, omega, sigma)

plt.plot(
    x, y,
    label = r'$\mu(x) = \omega_\mu \, \exp\left(-\frac{x^2}{2 \sigma_\mu^2}\right)$'
)

plt.xlim(0, 1)
plt.ylim(-1, max(y) + 1)
plt.xlabel(r"$\frac{t}{T}$")
plt.ylabel(r"$\mu(x)$")

plt.title(
    r"Funzione di crescita $\mu$" + "\n" + r"$\omega_\mu = " + str(omega) + r"$, $\sigma_\mu = " + str(sigma) + r"$"
)

plt.grid(True, linestyle = "--", alpha = 0.6)
plt.legend(loc = "upper right")

plt.tight_layout()

plt.savefig(
    os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../tesi/images/functions/mu.pdf"
    ),
    dpi = 300
)

plt.show()

#
# Sigma
#

for sigma in [0.05, 0.1, 0.2, 0.3, 0.5]:
    y = f(x, omega, sigma)
    plt.plot(
        x, y,
        label = r'$\sigma_\mu = ' + str(sigma) + r'$',
        color = None
    )

plt.xlim(0, 1)
plt.ylim(-1, max(y) + 1)
plt.xlabel(r"$\frac{t}{T}$")
plt.ylabel(r"$\mu(x)$")

plt.title(
    r"Funzione di crescita $\mu$" + "\n" + r"$\omega_\mu = " + str(omega) + r"$"
)

plt.grid(True, linestyle = "--", alpha = 0.6)
plt.legend(loc = "upper right")

plt.tight_layout()

plt.savefig(
    os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../tesi/images/functions/mu_sigma.pdf"
    ),
    dpi = 300
)

plt.show()