import matplotlib.pyplot as plt
import numpy as np
import pathlib
import os

def r(x, omega, sigma):
    return 2 * omega / (1 + np.exp(sigma * x))

x = np.linspace(0, 15, 1000)

omega, sigma = 1, 0.2

plt.plot(
    x, r(x, omega, sigma),
    label = r"$r(t) = 2 \omega_r \frac{1}{1 + \exp\left(\sigma_r t\right)}$",
)

plt.xlim(0, 15)
plt.ylim(-0.1, 1.1)
plt.xlabel(r"$t$")
plt.ylabel(r"$r(t)$")

plt.title(
    r"Funzione di recupero $r$" + "\n" + r"$\omega_r = " + str(omega) + r"$, $\sigma_r = " + str(sigma) + r"$"
)

plt.grid(True, linestyle = "--", alpha = 0.6)
plt.legend(loc = "upper left")

plt.tight_layout()

plt.savefig(
    os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../tesi/images/functions/r.pdf"
    ), 
    dpi = 300
)

plt.show()