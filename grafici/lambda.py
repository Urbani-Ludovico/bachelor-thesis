from core import *
import numpy as np

def f(f_f, f_p, d, gamma, omega_f, omega_p, omega_d, b):
    return gamma / (1 + np.exp(-omega_f * f_f - omega_p * f_p - omega_d * d + b))

x = np.linspace(0, 15, 1000)

#
# f_f
#
f_p, d, gamma, omega_f, omega_p, omega_d, b = 0, 0, 1, 1, 1, 1, 5
y = f(x, f_p, d, gamma, omega_f, omega_p, omega_d, b)

plt, fig, ax = new_plot()

plot(
    ax,
    x, y,
    label = r'$\lambda(f_f, f_p, d, \gamma) = \gamma \frac{1}{1 + \exp\left(-\omega_f f_f - \omega_p f_p - \omega_d d + b\right)}$'
)

ax.set_xlim(0, 15)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel(r"$f_f$")
ax.set_ylabel(r"$\lambda(f_f, f_p, d, \gamma)$")

set_title(
    ax,
    r"Funzione di infortunio $\lambda$" + "\n" + r"$f_p = " + str(f_p) + r"$, $d = " + str(d) + r"$, $b = " + str(b) + r"$"
)

ax.grid(True, linestyle = "--", alpha = 0.6)
ax.legend(loc = "upper left")

show_plot(plt, "functions/lambda_ff.pdf")