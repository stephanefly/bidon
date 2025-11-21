from types import SimpleNamespace

import pytest

from src.apps.main.modules.genepi import create_file_genepi


@pytest.fixture(autouse=True)
def stub_color_and_symbol(monkeypatch):
    monkeypatch.setattr(create_file_genepi, "get_color_name_from_code", lambda code, lang: f"color-{code}")
    monkeypatch.setattr(create_file_genepi, "get_symbol_name_from_code", lambda code: f"symbol-{code}")


def make_iso(name, color="#123456", marker="triangle"):
    return SimpleNamespace(name=name, color=color, marker=marker)


def make_bsam(name, path, iso_name):
    return SimpleNamespace(name=name, file_path=path, iso_vitesse=make_iso(iso_name))


def test_create_info_cas_lines_numbers_duplicate_isos():
    iso = make_iso("ISO-A")
    cas1 = SimpleNamespace(iso_vitesse=iso, bsam_path="/a", repertory="/r1")
    cas2 = SimpleNamespace(iso_vitesse=iso, bsam_path="/b", repertory="/r2")

    params = {
        "DetectionCasProcheBSAM": True,
        "RecalageKD": False,
        "TrierIso": True,
    }

    lines = create_file_genepi.create_info_cas_lines([cas1, cas2], params)

    titles = [line for line in lines if "TitreCas" in line]
    assert "'ISO-A'" in titles[0]
    assert "ISO-A - 02" in titles[1]


def test_create_info_bsam_lines_formats_each_entry():
    bsam = make_bsam("Case1", "/tmp/path1", "ISO-X")

    lines = create_file_genepi.create_info_bsam_lines([bsam], {})

    assert any("Case1" in line for line in lines)
    assert any("color-#123456" in line for line in lines)
    assert any("symbol-triangle" in line for line in lines)


def test_complete_genepi_file_injects_paths(monkeypatch):
    fake_settings = SimpleNamespace(BASE_DIR="/base")
    monkeypatch.setattr(create_file_genepi, "settings", fake_settings)

    param_genepi = {
        "mise_en_forme": "/configs/template.py",
        "titre": "Essai",
        "ExportPDF": True,
        "ExportExcel": False,
        "ExportPPT": True,
        "dico_aubes": {"Total": ["A1"], "Primaire": [], "Secondaire": []},
    }

    content = create_file_genepi.complete_genepi_file(param_genepi)

    assert "TitrePres = \"Essai\"" in content
    assert "apps/main/modules/genepi/genepi_auto.py" in content
    assert "DicoLabelAube2Trace" in content
