from django.shortcuts import render
from .models import ReviewProduk

def index(request):
    produk = ReviewProduk.objects.all()
    response = {'index': produk}
    return render(request, 'review_produk.html', response)