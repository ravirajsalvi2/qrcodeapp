import os
import qrcode
from PIL import Image
from django.shortcuts import render
from .forms import QRCodeForm
from io import BytesIO

def generate_qr_code(data, overlay_image=None):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    if overlay_image:
        overlay = Image.open(overlay_image).convert("RGBA")
        overlay = overlay.resize((qr_img.size[0] // 4, qr_img.size[1] // 4))
        pos = (
            (qr_img.size[0] - overlay.size[0]) // 2,
            (qr_img.size[1] - overlay.size[1]) // 2,
        )
        qr_img.paste(overlay, pos, overlay)

    return qr_img

def qr_code_view(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data['data']
            overlay_image = form.cleaned_data['overlay_image']

            # Generate the QR code
            qr_img = generate_qr_code(data, overlay_image.file if overlay_image else None)

            # Ensure the 'media' directory exists
            media_dir = os.path.join(os.path.dirname(__file__), '..', 'media')
            if not os.path.exists(media_dir):
                os.makedirs(media_dir)

            # Save the generated QR code
            qr_code_path = os.path.join(media_dir, 'generated_qr.png')
            qr_img.save(qr_code_path)

            return render(request, "qrapp/qr_result.html", {"qr_image": "generated_qr.png"})
    else:
        form = QRCodeForm()

    return render(request, "qrapp/qr_form.html", {"form": form})
