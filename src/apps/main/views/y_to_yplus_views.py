from openpyxl import Workbook
from django.http import HttpResponse
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.main.modules.yplus_to_y.compute_wall_cellsize import compute_wallcellsize, mise_en_forme


@login_required
def utilitaire_y_to_yplus(request):

    rows = []
    bsam_path = ""
    y_value = ""

    if request.method == "POST":

        raw_bsam = request.POST.get("bsam_path", "").replace('"', '').strip()
        bsam_path = Path(raw_bsam)

        raw_y = request.POST.get("y_value", "").strip().replace(",", ".")
        y_value = float(raw_y)

        # --- EXPORT EXCEL ---
        action = request.POST.get("action", "").strip()
        request.session["bsam_name"] = bsam_path.stem
        if action == "export_excel":
            rows = request.session.get("yplus_rows", [])
            bsam_name = request.session.get("bsam_name", "resultat")
            return export_excel(rows, bsam_name)

        # --- CALCUL ---
        result_text = compute_wallcellsize(bsam_path, y_value)
        rows = mise_en_forme(result_text)

        # Sauvegarde en session → utile pour export
        request.session["yplus_rows"] = rows

    return render(request, "trunks/main/yplus_to_y.html", {
        "rows": rows, "bsam_path": bsam_path, "y_value": y_value
    })

def export_excel(rows, bsam_name):
    wb = Workbook()
    ws = wb.active
    ws.title = f"yplus-to-y_{bsam_name}"

    # En-têtes
    headers = [
        "Grille", "y+", "y (µm)", "cf",
        "utau/Uref (%)", "Uref (m/s)", "utau (m/s)",
        "Corde (mm)", "Reynolds"
    ]
    ws.append(headers)

    for row in rows:
        ws.append(row)

    # Nom dynamique
    filename = f"yplus-to-y_{bsam_name}.xlsx"

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    wb.save(response)
    return response
