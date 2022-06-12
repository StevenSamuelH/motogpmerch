from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('add-produk/data-api', views.daftarDataProdukAPI, name='daftar'),
]