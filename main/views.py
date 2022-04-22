from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from daftar_penjual.models import Merchant
from profil_produk.models import Product
from review.models import ReviewProduk

def home(request):
    return render(request, 'main/home.html')

def produk(request):
    product = Product.objects.all()
    review = ReviewProduk.objects.all()
    response = {'products' : product}
    return render(request, 'main/daftar_produk.html', response)
