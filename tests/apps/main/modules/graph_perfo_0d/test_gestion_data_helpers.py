from datetime import datetime

from src.apps.main.modules.graph_perfo_0d import gestion_data


def test_make_json_serializable_handles_numpy_and_datetime(monkeypatch):
    class FakeNumpyInt:
        def __init__(self, value):
            self._value = value

        def item(self):
            return self._value

    class FakeNumpyFloat(FakeNumpyInt):
        pass

    monkeypatch.setattr(gestion_data.np, "integer", FakeNumpyInt, raising=False)
    monkeypatch.setattr(gestion_data.np, "floating", FakeNumpyFloat, raising=False)

    numpy_value = FakeNumpyInt(42)
    float_value = FakeNumpyFloat(3.14)
    dt_value = datetime(2024, 1, 2, 3, 4, 5)

    assert gestion_data.make_json_serializable(numpy_value) == 42
    assert gestion_data.make_json_serializable(float_value) == 3.14
    assert gestion_data.make_json_serializable(dt_value) == dt_value.isoformat()

    class Dummy:
        def __init__(self):
            self.value = 1

    fallback = gestion_data.make_json_serializable(Dummy())
    assert isinstance(fallback, str)


def test_find_key_in_data_walks_nested_structures_and_dataframe(monkeypatch):
    nested = {
        "level1": {
            "target": "from_dict",
            "items": [
                {"other": 1},
                {"deep": {"another": "value"}},
            ],
        }
    }

    assert gestion_data.find_key_in_data(nested, "target") == "from_dict"

    class DummySeries:
        def __init__(self, values):
            self.values = values

    class DummyDataFrame:
        def __init__(self, data):
            self._data = data
            self.columns = list(data.keys())

        def __getitem__(self, key):
            return self._data[key]

    monkeypatch.setattr(gestion_data.pd, "DataFrame", DummyDataFrame, raising=False)

    dataframe = gestion_data.pd.DataFrame({"target": DummySeries(["from_df"])})
    assert gestion_data.find_key_in_data(dataframe, "target") == "from_df"

    assert gestion_data.find_key_in_data([{"missing": 0}], "target") is None
