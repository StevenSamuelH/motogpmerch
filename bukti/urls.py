from django.urls import path
from .views import add_data, addDataFlutter

urlpatterns = [
    path('', add_data),
    path('add-produk/data-pembeli', addDataFlutter)
]
