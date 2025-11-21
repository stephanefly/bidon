from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from pypdf import PdfReader, PdfWriter


def _parse_page_ranges(pages_str: str, total_pages: int) -> list[int]:
    """
    Convertit '2-3,7,10-12' en liste d'index 0-based unique/triée.
    Vérifie bornes [1..total_pages].
    """
    if not pages_str:
        raise ValueError("Veuillez saisir au moins une page.")

    indices = set()
    chunks = [c.strip() for c in pages_str.split(",") if c.strip()]
    for c in chunks:
        if "-" in c:
            a_str, b_str = [x.strip() for x in c.split("-", 1)]
            if not (a_str.isdigit() and b_str.isdigit()):
                raise ValueError(f"Intervalle invalide: '{c}'")
            a, b = int(a_str), int(b_str)
            if a > b:
                a, b = b, a  # tolère ordre inversé
            if a < 1 or b > total_pages:
                raise ValueError(f"Hors bornes: '{c}' (pages 1 à {total_pages})")
            for p in range(a, b + 1):
                indices.add(p - 1)
        else:
            if not c.isdigit():
                raise ValueError(f"Entrée invalide: '{c}'")
            p = int(c)
            if p < 1 or p > total_pages:
                raise ValueError(f"Page hors bornes: {p} (1 à {total_pages})")
            indices.add(p - 1)

    out = sorted(indices)
    if not out:
        raise ValueError("Aucune page valide détectée.")
    return out


@require_http_methods(["GET", "POST"])
def split_pdf(request):
    if request.method == "GET":
        return render(request, "trunks/main/split_pdf.html")

    # POST
    pdf_file = request.FILES.get("pdf_file")
    pages_str = (request.POST.get("pages") or "").strip()

    if not pdf_file:
        messages.error(request, "Aucun fichier PDF fourni.")
        return render(request, "trunks/main/split_pdf.html")

    # Optionnel : contrôle de type (meilleur effort)
    if not (pdf_file.content_type in ("application/pdf",) or pdf_file.name.lower().endswith(".pdf")):
        messages.error(request, "Le fichier doit être un PDF.")
        return render(request, "trunks/main/split_pdf.html")

    try:
        reader = PdfReader(pdf_file)
    except Exception:
        messages.error(request, "Impossible de lire le PDF. Fichier corrompu ?")
        return render(request, "trunks/main/split_pdf.html")

    total_pages = len(reader.pages)
    try:
        page_indices = _parse_page_ranges(pages_str, total_pages)
    except ValueError as e:
        messages.error(request, str(e))
        return render(request, "trunks/main/split_pdf.html")

    writer = PdfWriter()
    for idx in page_indices:
        writer.add_page(reader.pages[idx])

    output = BytesIO()
    try:
        writer.write(output)
    finally:
        writer.close()
    output.seek(0)

    # Nom de fichier résultat
    base = (pdf_file.name.rsplit(".", 1)[0]) or "document"
    out_name = f"{base}_extract.pdf"

    response = HttpResponse(output.read(), content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{out_name}"'
    return response
