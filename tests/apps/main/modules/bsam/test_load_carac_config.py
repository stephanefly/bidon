from types import SimpleNamespace

from src.apps.main.modules.bsam import bsam_tools


def test_load_carac_config_fills_missing_height(tmp_path, monkeypatch):
    filepath = tmp_path / "carac.yaml"
    filepath.write_text("placeholder", encoding="utf-8")

    config_data = {
        "lst_carac": [
            {"carac_name": "alpha", "Nb_hauteur_base": 2},
            {"carac_name": "beta"},
        ]
    }
    monkeypatch.setattr(
        bsam_tools,
        "yaml",
        SimpleNamespace(safe_load=lambda _: config_data),
    )

    items = bsam_tools.load_carac_config(nb_graph=3, filepath=str(filepath))

    assert items[0]["Nb_hauteur_base"] == 2
    assert items[1]["Nb_hauteur_base"] == 3


def test_load_carac_config_returns_empty_when_missing_list(tmp_path, monkeypatch):
    filepath = tmp_path / "empty.yaml"
    filepath.write_text("placeholder", encoding="utf-8")

    monkeypatch.setattr(
        bsam_tools,
        "yaml",
        SimpleNamespace(safe_load=lambda _: {}),
    )

    assert bsam_tools.load_carac_config(nb_graph=1, filepath=str(filepath)) == []
