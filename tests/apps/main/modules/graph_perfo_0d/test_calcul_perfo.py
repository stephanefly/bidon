import math

import numpy as np
import pytest

from src.apps.main.modules.graph_perfo_0d import calcul_perfo


def test_calculer_qcorr_scales_with_temperature_and_pressure():
    qcorr = calcul_perfo.calculer_qcorr(100.0, 300.0, 101325.0)
    expected = 100.0 * math.sqrt(300.0 / 288.15)
    assert qcorr == pytest.approx(expected, rel=1e-6)


def test_compute_polynomial_blends_species_coefficients():
    far = 0.1
    war = 0.05
    coeffs = calcul_perfo.compute_polynomial(far, war)
    assert coeffs.shape == (8,)
    cp_air = np.array([1.06843e03, -5.21742e-01, 1.23785e-03, -6.27984e-07,
                       -3.3094e-10, 4.70972e-13, -1.79613e-16, 2.35822e-20])
    cp_kerosene = np.array([1.2850007e03, 2.3021158e00, -5.27394e-04, 0.0,
                            0.0, 0.0, 0.0, 0.0])
    cp_water = np.array([0.188457e04, -0.484304, 0.173478e-02, -0.114179e-05,
                         0.334500e-09, -0.386134e-13, 0.0, 0.0])
    expected = (cp_air + far * cp_kerosene + war * cp_water) / (1 + far + war)
    assert np.allclose(coeffs, expected)


def test_set_perfo_data_format_rounds_values():
    formatted = calcul_perfo.set_perfo_data_format(0.1234, 0.98765, 1.2345, 2.3456, 3.4567, 4.5678, 5.6789)
    assert formatted == {
        "Cd": 12.34,
        "Etapol": 0.9877,
        "Qcorr_ref": 1.2345,
        "Qcorr": 2.3456,
        "Pi": 3.4567,
        "PisQcorr_ref": 4.5678,
        "Tau": 5.6789,
    }


def test_update_perfo_data_zeroes_fields_based_on_mode():
    data = {"Cd": 10, "Etapol": 20}
    calcul_perfo.update_perfo_data(data, stator_only=True)
    assert data["Etapol"] == 0
    data = {"Cd": 10, "Etapol": 20}
    calcul_perfo.update_perfo_data(data, stator_only=False)
    assert data["Cd"] == 0
