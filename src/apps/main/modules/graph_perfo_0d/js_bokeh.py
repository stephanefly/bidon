from bokeh.models import CustomJS, Select, TapTool
from config.settings.base import PATH_STYLE
# Store debounce timer outside the callback to avoid overlapping calls
FETCH_DEBOUNCE = "var debounceTimer = null;"

def click_copie(p, source):
    callback_copy = CustomJS(
        args=dict(source=source),
        code="""
        const selected_index = source.selected.indices[0];  
        if (selected_index !== undefined) {
            const file_path = source.data['path'][selected_index];
            const cas_name = source.data['name'][selected_index];  
            navigator.clipboard.writeText(file_path).then(function() {
                alert('Chemin copié dans le presse-papiers : ' + cas_name);  
            }, function(err) {
                console.error('Erreur lors de la copie : ', err);
            });
        }
        """,
    )
    tap_tool = TapTool(callback=callback_copy)
    p.add_tools(tap_tool)
    # Activer le TapTool par défaut
    p.toolbar.active_tap = tap_tool

    return p


def callback_selection(source, scatter, etat_id):
    scatter.selection_glyph = scatter.glyph.clone()
    scatter.selection_glyph.line_width = 8
    scatter.selection_glyph.line_color = "black"

    scatter.nonselection_glyph = scatter.glyph.clone()
    scatter.nonselection_glyph.fill_alpha = 0.4

    # Base URL selon ton déploiement
    if PATH_STYLE == "windows":
        save_url_base = "/save_selection/"
    else:
        save_url_base = "/trunks/save_selection/"

    callback = CustomJS(
        args=dict(source=source, etat_id=etat_id, save_url_base=save_url_base),
        code=FETCH_DEBOUNCE + """
        function getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
            return "";
        }

        console.log("etat_id:", etat_id);

        if (debounceTimer) {
            clearTimeout(debounceTimer);
        }

        debounceTimer = setTimeout(function() {
            var indices = source.selected.indices;
            var data = source.data;
            var selected_cases = [];
            var selected_cases_id = [];

            for (var i = 0; i < indices.length; i++) {
                selected_cases.push(data['cas_name'][indices[i]]);
                selected_cases_id.push(data['cas_id'][indices[i]]);
            }

            console.log("Sélection envoyée:", selected_cases_id);

            var ul = document.getElementById('selected-cases');
            if (ul) {
                ul.innerHTML = "";
                selected_cases.forEach(function(cas) {
                    var li = document.createElement('li');
                    li.textContent = (cas || "").trim();
                    ul.appendChild(li);
                });
            }

            var hidden_ids = document.getElementById('selected-cases-hidden');
            if (hidden_ids) {
                hidden_ids.value = JSON.stringify(selected_cases_id);
            }
            var hidden_names = document.getElementById('selected-cases-names');
            if (hidden_names) {
                hidden_names.value = JSON.stringify(selected_cases);
            }

            const csrfToken = getCookie("csrftoken");
            const url = window.location.origin + save_url_base + etat_id + '/';

            fetch(url, {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    selected_cases: selected_cases,
                    selected_cases_id: selected_cases_id
                })
            }).then(function(response) {
                console.log("HTTP status:", response.status);
                return response.text().then(function(txt) {
                    if (!response.ok) {
                        console.error("Erreur d'enregistrement:", response.status, txt);
                    } else {
                        console.log("Données enregistrées avec succès:", txt);
                    }
                });
            }).catch(function(err) {
                console.error("Erreur réseau :", err);
            });

        }, 200);
        """
    )

    source.selected.js_on_change("indices", callback)


def callback_surbrillance(source_shared):
    callback_sync = CustomJS(
        args=dict(sources=source_shared),
        code="""
        var selected_indices = cb_obj.indices;
        sources.forEach(function(source) {
            source.selected.indices = selected_indices;
            source.change.emit();
        });
        """
    )

    for source in source_shared:
        source.selected.js_on_change("indices", callback_sync)
