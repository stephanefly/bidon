import os
import sys
from types import ModuleType, SimpleNamespace

# Provide a lightweight stub for django.conf.settings so the tools module can be imported
if "django" not in sys.modules:
    django_module = ModuleType("django")
    conf_module = ModuleType("django.conf")
    conf_module.settings = SimpleNamespace()
    django_module.conf = conf_module
    sys.modules["django"] = django_module
    sys.modules["django.conf"] = conf_module

from apps.main.modules.gestion_projets import tools


def test_get_user_path_uses_working_repertory(monkeypatch, tmp_path):
    working_dir = tmp_path / "workspace"
    working_dir.mkdir()
    monkeypatch.setattr(tools, "settings", SimpleNamespace(WORKING_REPERTORY=str(working_dir)))

    dummy_obj = SimpleNamespace(created_by="alice")

    assert tools.get_user_path(dummy_obj) == os.path.join(str(working_dir), "alice")


def test_get_color_name_from_code_supports_languages():
    assert tools.get_color_name_from_code("#FF4136") == "Rouge"
    assert tools.get_color_name_from_code("#FF4136", lang="en") == "Red"


def test_get_color_code_from_name_handles_unknown_name():
    assert tools.get_color_code_from_name("Rouge") == "#FF4136"
    assert tools.get_color_code_from_name("Couleur inconnue") is None


def test_get_color_en_from_fr_name_round_trip():
    assert tools.get_color_en_from_fr_name("Bleu") == "Blue"
    assert tools.get_color_en_from_fr_name("Inconnue") is None


def test_get_symbol_name_from_code_returns_unicode_symbol():
    assert tools.get_symbol_name_from_code("circle") == "●"
    assert tools.get_symbol_name_from_code("missing") is None
