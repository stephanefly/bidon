from src.apps.main.modules.yplus_to_y import compute_wall_cellsize


def test_mise_en_forme_splits_each_line():
    rows = compute_wall_cellsize.mise_en_forme([
        "first;second;third;",
        "1;2;3;",
    ])

    assert rows == [
        ["first", "second", "third", ""],
        ["1", "2", "3", ""],
    ]
