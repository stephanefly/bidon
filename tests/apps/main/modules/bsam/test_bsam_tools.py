
from src.apps.main.modules.bsam import bsam_tools


def test_echelle_plot_updates_global_extrema():
    y_values = [[1.0, 3.0, 2.0], [0.5, 4.5]]

    y_min, y_max = bsam_tools.echelle_plot(y_values, None, None)

    assert y_min == 0.5
    assert y_max == 4.5


def test_echelle_plot_keeps_existing_limits_when_no_values():
    y_min, y_max = bsam_tools.echelle_plot([[], []], 1.0, 5.0)

    assert y_min == 1.0
    assert y_max == 5.0
