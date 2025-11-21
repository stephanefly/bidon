import datetime as real_datetime
from pathlib import Path

from types import SimpleNamespace

from src.apps.main.modules.bsam import y_to_yplus_tools as tools


def test_copy_bsam_file_trims_quotes_and_copies(tmp_path):
    src = tmp_path / "source.bsam"
    src.write_text("data", encoding="utf-8")
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    dest_path = tools.copy_bsam_file(f'  "{src}"  ', dest_dir)

    assert dest_path == dest_dir / src.name
    assert dest_path.read_text(encoding="utf-8") == "data"


def test_create_launch_bat_writes_expected_batch_file(tmp_path):
    tools.create_launch_bat(tmp_path)

    launch_file = tmp_path / "launch_cannelle.bat"
    content = launch_file.read_text(encoding="utf-8")

    assert content.startswith("@echo off")
    assert "compute_wallcellsize.py" in content


def test_script_header_injects_values(tmp_path):
    header = tools._script_header(Path("/tmp/file.bsam"), 5)

    assert "file.bsam" in header
    assert "yplus_target = 5" in header


def test_create_python_script_combines_header_and_core(tmp_path):
    dest_bsam = tmp_path / "copied.bsam"
    dest_bsam.write_text("placeholder", encoding="utf-8")

    tools.create_python_script(dest_bsam, tmp_path, 3)

    script_content = (tmp_path / "compute_wallcellsize.py").read_text(encoding="utf-8")
    assert str(dest_bsam) in script_content
    assert "def get_info_from_grid" in script_content


def test_create_repertory_y_yplus_creates_structure(monkeypatch, tmp_path):
    fake_settings = SimpleNamespace(WORKING_REPERTORY=str(tmp_path))
    monkeypatch.setattr(tools, "settings", fake_settings)

    class FixedDatetime(real_datetime.datetime):
        @classmethod
        def now(cls):
            return cls(2024, 1, 2, 3, 4, 5)

    monkeypatch.setattr(tools.datetime, "datetime", FixedDatetime)

    recorded = {}

    def fake_copy(bsam_path, work_dir):
        recorded["copy"] = (bsam_path, work_dir)
        return work_dir / "copied.bsam"

    def fake_bat(work_dir):
        recorded["bat"] = work_dir

    def fake_script(dest_bsam, work_dir, y_value):
        recorded["script"] = (dest_bsam, work_dir, y_value)

    monkeypatch.setattr(tools, "copy_bsam_file", fake_copy)
    monkeypatch.setattr(tools, "create_launch_bat", fake_bat)
    monkeypatch.setattr(tools, "create_python_script", fake_script)

    class DummyFile:
        name = "input.txt"

        def chunks(self):
            yield b"hello"

    result_path, display = tools.create_repertory_y_yplus("/tmp/source.bsam", "alice", 7, DummyFile())

    work_dir = Path(result_path)
    assert work_dir.exists()
    assert recorded["copy"][0] == "/tmp/source.bsam"
    assert recorded["bat"] == work_dir
    assert recorded["script"] == (work_dir / "input.txt", work_dir, 7)

    expected_display = Path("alice") / "y_to_y+" / "20240102_030405"
    assert display == str(expected_display)

    saved_file = work_dir / "input.txt"
    assert saved_file.read_bytes() == b"hello"
