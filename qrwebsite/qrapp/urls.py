from django.urls import path
from .views import qr_code_view

urlpatterns = [
    path('', qr_code_view, name='qr_code_view'),
]
