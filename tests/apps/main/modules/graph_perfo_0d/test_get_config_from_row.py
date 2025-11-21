from pathlib import Path

from src.apps.main.modules.graph_perfo_0d import get_config_from_row as config


def test_set_filepath_returns_expected_structure(tmp_path):
    case_dir = tmp_path / "case_data"
    antares, gradients, bsam, perfos = config.set_filepath(case_dir)

    assert antares == case_dir / "calculation/carte_antares.py"
    assert gradients == case_dir / "post/postAnNA/Gradients_Complets.trac"
    assert bsam == case_dir / "init/bc_BSAM"
    assert perfos == case_dir / "post/postAnNA/Perfos0D_moy_7.xlsx"


def test_extract_numbers_letters_splits_characters():
    letters, numbers = config.extract_numbers_letters("Row12A")

    assert letters == "RowA"
    assert numbers == "12"


def test_get_first_rotor_and_stator_identifies_positions():
    rows = [
        config.Row(flux="total", position=0, omega=0.0, nb_blade=20, bsam_name="S1"),
        config.Row(flux="total", position=1, omega=100.0, nb_blade=20, bsam_name="R1"),
        config.Row(flux="total", position=2, omega=0.0, nb_blade=20, bsam_name="S2"),
    ]

    rotor_index, rotor = config.get_first_rotor(rows)
    stator_index, stator = config.get_first_stator(rows)

    assert rotor_index == 1
    assert rotor.bsam_name == "R1"
    assert stator_index == 0
    assert stator.bsam_name == "S1"


def test_get_flux_alias_converts_between_strings_and_codes():
    assert config.get_flux_alias("total", data_type="bsam") == 1
    assert config.get_flux_alias(2, data_type="cfd") == "secondaire"


def test_get_row_by_flux_filters_matching_rows():
    rows = [
        config.Row(flux="total", position=0, omega=0.0, nb_blade=20, bsam_name="S1"),
        config.Row(flux="primaire", position=1, omega=0.0, nb_blade=20, bsam_name="S2"),
    ]

    primaire_rows = config.get_row_by_flux(rows, flux="primaire")

    assert len(primaire_rows) == 1
    assert primaire_rows[0].bsam_name == "S2"


def test_rename_row_applies_aliases_and_preserves_unknown_names():
    assert config.rename_row("BDE12") == "RDE12"
    assert config.rename_row("S5") == "RD5"
    assert config.rename_row("X99") == "X99"


def test_find_row_by_renamed_bsam_matches_using_alias():
    row_dict = {
        "row_a": {"bsam_name": "BDE12", "flux": "total"},
        "row_b": {"bsam_name": "S5", "flux": "total"},
    }

    found = config.find_row_by_renamed_bsam(row_dict, "RDE12")
    assert found == {"row_a": row_dict["row_a"]}
    assert config.find_row_by_renamed_bsam(row_dict, "RD5") == {"row_b": row_dict["row_b"]}
    assert config.find_row_by_renamed_bsam(row_dict, "missing") is None


def test_define_config_list_generates_groupings_with_aliases():
    def make_row(name, omega, flux="total"):
        return config.Row(
            flux=flux,
            position=0,
            omega=omega,
            nb_blade=10,
            bsam_name=name,
        )

    rows = [
        make_row("S1", omega=0.0),
        make_row("R1", omega=100.0),
        make_row("S2", omega=0.0),
    ]

    config_list = config.define_config_list(rows, rename=True)

    assert "RD1-RD2" in config_list["global"]
    assert "RM1-RD2" in config_list["etage"]
    assert "RD1-RM1" in config_list["pseudo_etage"]
    assert {"RD1", "RM1", "RD2"}.issubset(config_list["isole"])
