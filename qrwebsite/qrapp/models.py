from django.db import models

class QRCode(models.Model):
    data = models.TextField()
    overlay_image = models.ImageField(upload_to='overlays/', null=True, blank=True)  # User-uploaded image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR Code for {self.data[:20]}"
