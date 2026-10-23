from matplotlib import pyplot as plt
import numpy as np
import pathlib
import os

def lambda_func(f_f, f_p, d, gamma, omega_f, omega_p, omega_d, b):
    return gamma / (1 + np.exp(-omega_f * f_f - omega_p * f_p - omega_d * d + b))

x = np.linspace(0, 15, 1000)

#
# f_f
#
f_p, d, gamma, omega_f, omega_p, omega_d, b = 0, 0, 1, 1, 1, 1, 5
y = lambda_func(x, f_p, d, gamma, omega_f, omega_p, omega_d, b)

plt.plot(
    x, y,
    label = r'$\lambda(f_f, f_p, d, \gamma) = \gamma \frac{1}{1 + \exp\left(-\omega_f f_f - \omega_p f_p - \omega_d d + b\right)}$'
)

plt.xlim(0, 15)
plt.ylim(-0.1, 1.1)
plt.xlabel(r"$f_f$")
plt.ylabel(r"$\lambda(f_f, f_p, d, \gamma)$")

plt.title(
    r"Funzione di infortunio $\lambda$" + "\n" + r"$f_p = " + str(f_p) + r"$, $d = " + str(d) + r"$, $b = " + str(b) + r"$"
)

plt.grid(True, linestyle = "--", alpha = 0.6)
plt.legend(loc = "lower right")

plt.tight_layout()

plt.savefig(
    os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../tesi/images/functions/lambda_ff.pdf"
    ), 
    dpi = 300
)

plt.show()