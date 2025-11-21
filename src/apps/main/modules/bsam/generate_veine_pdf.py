import os
from io import BytesIO

from django.http import HttpResponse
from PIL import Image
from reportlab.pdfgen import canvas


def generate_pdf_trace_veine(image_path, revue_veine):
    # Génération du PDF
    buffer = BytesIO()
    square_size = 600  # Taille du carré en pixels
    pdf = canvas.Canvas(buffer, pagesize=(square_size, square_size))

    # Charger l'image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Adapter l’image au carré (ajuster en conservant le ratio)
    aspect_ratio = img_width / img_height
    if aspect_ratio > 1:
        new_width = square_size
        new_height = square_size / aspect_ratio
    else:
        new_height = square_size
        new_width = square_size * aspect_ratio

    # Centrer l’image dans le carré
    x_position = (square_size - new_width) / 2
    y_position = (square_size - new_height) / 2
    # Dessiner l'image dans le PDF
    pdf.drawInlineImage(
        image_path, x_position, y_position, width=new_width, height=new_height
    )

    # Finaliser le PDF
    pdf.showPage()
    pdf.save()

    image_name = os.path.basename(image_path)
    filename = f"{os.path.splitext(image_name)[0]}.pdf"

    # Préparer la réponse HTTP avec le PDF
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="{filename}"'
    )

    buffer.close()
    return response  # Renvoie le PDF généré
