"""Test legend with a title."""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from .helpers import assert_equality

mpl.use("Agg")


def plot() -> Figure:
    fig = plt.figure()
    plt.plot([-1, 1], [-1, 1], label="my legend")
    plt.legend(title="my title")
    return fig


def test() -> None:
    assert_equality(plot, __file__[:-3] + "_reference.tex")
