"""Test standalone colorbar (fig.colorbar with cax=ax, no main plot).

From matplotlib's colorbar_only tutorial:
https://matplotlib.org/stable/users/explain/colors/colorbar_only.html
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from .helpers import assert_equality

mpl.use("Agg")


def plot() -> Figure:
    # Basic continuous colorbar - figure has only the colorbar axes
    fig, ax = plt.subplots(figsize=(6, 1), layout="constrained")

    cmap = mpl.colormaps["cool"]
    norm = mpl.colors.Normalize(vmin=5, vmax=10)

    fig.colorbar(
        mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
        cax=ax,
        orientation="horizontal",
        label="Some Units",
    )
    return fig


def test() -> None:
    assert_equality(plot, "test_colorbar_only_reference.tex")
