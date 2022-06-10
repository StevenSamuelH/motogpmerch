from django.shortcuts import render
from django.http.response import HttpResponse
from django.core import serializers
from .models import ReviewProduk

def index(request):
    produk = ReviewProduk.objects.all()
    response = {'index': produk}
    return render(request, 'review_produk.html', response)

def json(request):
    produk = ReviewProduk.objects.all()
    data = serializers.serialize('json', produk)
    return HttpResponse(data, content_type="application/json")