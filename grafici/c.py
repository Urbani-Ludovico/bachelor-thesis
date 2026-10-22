import matplotlib.pyplot as plt
import numpy as np
import pathlib
import os

def costante(x):
    return np.repeat(0.7, len(x))

def periodico(x):
    return ((- x) % 3) / 2

def variabile(x):
    return np.random.uniform(0, 1, len(x))

x = np.arange(0, 11, 1)

for func in (costante, periodico, variabile):
    plt.plot(
        x, func(x),
        label = "Carico " + func.__name__,
        marker = "o"
    )

    plt.xlim(-1, 11)
    plt.ylim(-0.1, 1.1)
    plt.xlabel(r"$t$")
    plt.ylabel(r"$c_\cdot(t)$")

    plt.title(
        "Funzione di carico " + func.__name__ + r" per $c_f$ e $c_p$"
    )

    plt.grid(True, linestyle = "--", alpha = 0.6)
    plt.legend(loc = "upper left")

    plt.tight_layout()
    
    plt.savefig(
        os.path.join(
            pathlib.Path(__file__).parent.resolve(),
            "../tesi/images/functions/c_" + func.__name__ + ".pdf"
        ), 
        dpi = 300
    )
    
    plt.show()