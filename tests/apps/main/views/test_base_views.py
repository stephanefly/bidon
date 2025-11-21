import sys
from types import ModuleType, SimpleNamespace
from apps.main.models import UtilitaireConfiguration

models_module = sys.modules.get("apps.main.models")
if models_module is None:
    models_module = ModuleType("apps.main.models")
    sys.modules["apps.main.models"] = models_module


def _ensure_model(name):
    if not hasattr(models_module, name):
        setattr(models_module, name, type(name, (), {"objects": SimpleNamespace()}))


for _model_name in [
    "Cas",
    "Etat",
    "IsoVitesse",
    "Row",
    "RowPair",
    "Aube",
]:
    _ensure_model(_model_name)

from apps.main.views import base_views

def make_request(get_params=None):
    return SimpleNamespace(GET=get_params or {}, META={}, method="GET")


def test_configuration_renders_expected_template(monkeypatch):
    captured = {}

    def fake_render(request, template_name):
        captured["request"] = request
        captured["template"] = template_name
        return "rendered"

    monkeypatch.setattr(base_views, "render", fake_render)

    request = make_request()
    response = base_views.configuration.__wrapped__(request)

    assert response == "rendered"
    assert captured["template"] == "trunks/main/configuration.html"


def test_recherche_globale_populates_results_from_models(monkeypatch):
    render_context = {}

    def fake_render(request, template_name, context):
        render_context.update(context)
        return context

    class DummyManager:
        def __init__(self, result):
            self.result = result
            self.calls = 0

        def filter(self, *args, **kwargs):
            self.calls += 1
            return self.result

    project_manager = DummyManager(["project"])
    etat_manager = DummyManager(["etat"])
    cas_manager = DummyManager(["cas"])
    iso_manager = DummyManager(["iso"])

    monkeypatch.setattr(base_views, "render", fake_render)
    monkeypatch.setattr(base_views, "Project", SimpleNamespace(objects=project_manager))
    monkeypatch.setattr(base_views, "Etat", SimpleNamespace(objects=etat_manager))
    monkeypatch.setattr(base_views, "Cas", SimpleNamespace(objects=cas_manager))
    monkeypatch.setattr(base_views, "IsoVitesse", SimpleNamespace(objects=iso_manager))

    request = make_request({"q": "fan"})

    response_context = base_views.recherche_globale.__wrapped__(request)

    assert response_context["query"] == "fan"
    assert response_context["results"]["projects"] == ["project"]
    assert response_context["results"]["etats"] == ["etat"]
    assert response_context["results"]["cas"] == ["cas"]
    assert response_context["results"]["iso_vitesse"] == ["iso"]


def test_recherche_globale_skips_queries_when_no_term(monkeypatch):
    def fail(*args, **kwargs):
        raise AssertionError("Queryset should not be used when no query term is provided")

    monkeypatch.setattr(base_views, "render", lambda request, template, context: context)
    monkeypatch.setattr(base_views, "Project", SimpleNamespace(objects=SimpleNamespace(filter=fail)))
    monkeypatch.setattr(base_views, "Etat", SimpleNamespace(objects=SimpleNamespace(filter=fail)))
    monkeypatch.setattr(base_views, "Cas", SimpleNamespace(objects=SimpleNamespace(filter=fail)))
    monkeypatch.setattr(base_views, "IsoVitesse", SimpleNamespace(objects=SimpleNamespace(filter=fail)))

    request = make_request({})

    context = base_views.recherche_globale.__wrapped__(request)

    assert context["query"] == ""
    assert context["results"] == {
        "projects": [],
        "etats": [],
        "cas": [],
        "iso_vitesse": [],
    }
