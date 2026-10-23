import matplotlib.pyplot as plt
import numpy as np
import pathlib
import os

def f(x, omega, sigma):
    return omega * np.exp(- ((x - 1) ** 2) / (2 * sigma ** 2))

x = np.linspace(0, 1, 1000)

beta, sigma = 0.5, 0.2
y = f(x, beta, sigma)

plt.plot(
    x, y,
    label = r'$\nu(x, \beta) = \beta \exp\left(-\frac{{(x - 1)}^2}{2 \sigma_\nu^2}\right)$'
)

plt.xlim(0, 1)
plt.ylim(-0.1, 1.1)
plt.xlabel(r"$\frac{t}{T}$")
plt.ylabel(r"$\nu(x, \beta)$")

plt.title(
    r"Funzione di abbandono $\nu$" + "\n" + r"$\beta = " + str(beta) + r"$, $\sigma_\nu = " + str(sigma) + r"$"
)

plt.grid(True, linestyle = "--", alpha = 0.6)
plt.legend(loc = "upper left")

plt.tight_layout()

plt.savefig(
    os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../tesi/images/functions/nu.pdf"
    ), 
    dpi = 300
)

plt.show()