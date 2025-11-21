from src.apps.main.modules.graph_perfo_0d import user_case


class DummyLoc:
    def __init__(self, header_values):
        self._header_values = header_values

    def __getitem__(self, key):
        row, col = key
        assert row == 0
        return self._header_values[col]


class DummyFrame:
    def __init__(self, columns, header_values):
        self.columns = columns
        self.loc = DummyLoc(header_values)


def test_base_name_strips_suffix():
    assert user_case._base_name("GLOBAL RDE-OGV.2") == "GLOBAL RDE-OGV"


def test_build_schema_groups_columns_and_generates_fallbacks():
    headers = [
        "Point",
        "GLOBAL RDE-OGV.2",
        "GLOBAL RDE-OGV.3",
        "RDE-RM1-RM2",
    ]
    header_values = {
        headers[1]: "Qcorr_ref",
        headers[2]: "etapol",
        headers[3]: "  ",
    }
    df = DummyFrame(headers, header_values)

    schema = user_case._build_schema(df)

    assert schema["GLOBAL RDE-OGV"] == [
        (headers[1], "Qcorr_ref"),
        (headers[2], "etapol"),
    ]
    assert schema["RDE-RM1-RM2"][0][1] == "var_0"


def test_build_config_row_classifies_each_group():
    data = {
        "GLOBAL RDE-OGV": [],
        "RM1-RM2": [],
        "RD1-RD3": [],
        "RM5": [],
    }

    grouped = user_case.build_config_row(data)

    assert grouped["global"] == ["GLOBAL RDE-OGV"]
    assert "RM1-RM2" in grouped["etage"]
    assert "RD1-RD3" in grouped["pseudo_etage"]
    assert grouped["isole"] == ["RM5"]


def test_build_row_list_deduplicates_and_sorts():
    structure = {
        "global": ["GLOBAL RDE-OGV"],
        "etage": ["RM1-RM2"],
        "pseudo_etage": ["RD1-RD2"],
        "isole": ["RDE"],
    }

    rows = user_case.build_row_list(structure)

    expected = sorted({"GLOBAL RDE", "OGV", "RM1", "RM2", "RD1", "RD2", "RDE"})
    assert rows == expected
