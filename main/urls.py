from unicodedata import name
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('daftar-produk', views.produk,  name='produk'),
]
