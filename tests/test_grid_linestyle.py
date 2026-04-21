"""Grid linestyle (e.g. ':', '--') is forwarded to PGFPlots grid styles."""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from .helpers import assert_equality

mpl.use("Agg")


def plot() -> Figure:
    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_subplot(111)
    ax.plot([0, 1, 2], [0, 1, 0], color="navy")
    ax.grid(visible=True, linestyle=":", linewidth=0.8)
    ax.set_xlim(-0.1, 2.1)
    ax.set_ylim(-0.1, 1.1)
    return fig


def test() -> None:
    assert_equality(plot, __file__[:-3] + "_reference.tex")
