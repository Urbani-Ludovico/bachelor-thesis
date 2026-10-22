import matplotlib.pyplot as plt
import pathlib
import os

def new_plot():
    fig, ax = plt.subplots(
        figsize = (8, 5)
    )

    return (plt, fig, ax)

def show_plot(plt, path = None):
    plt.tight_layout()

    if path is not None:
        plt.savefig(
            os.path.join(
                pathlib.Path(__file__).parent.resolve(),
                "../tesi/images/",
                path
            ), 
            dpi = 300
        )

    plt.show()

def plot(
    ax,
    x, y,
    color: str | None = "blue",
    linewidth = 2,
    label = None
):
    ax.plot(
        x, y,
        color = color,
        linewidth = linewidth,
        label = label
    )

def set_title(
    ax,
    title,
    fontsize = 12
):
    ax.set_title(
        title,
        fontsize = fontsize
    )