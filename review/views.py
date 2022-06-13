from django.shortcuts import render
from django.http.response import HttpResponse
from django.core import serializers
from .models import ReviewProduk
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json as j

def index(request):
    produk = ReviewProduk.objects.all()
    response = {'index': produk}
    return render(request, 'review_produk.html', response)

def json(request):
    produk = ReviewProduk.objects.all()
    data = serializers.serialize('json', produk)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addReviewProduk(request):

    data = j.loads(request.body)
    nama_baru = data['namaProduk']
    gambar_baru = data['gambarProduk']
    review_baru = data['reviewProduk']
    rating_baru = data['ratingProduk']
  
    
    Dataproduk = ReviewProduk(nama=nama_baru,
         gambar=gambar_baru,review=review_baru,rating=rating_baru)
    Dataproduk.save()
    return JsonResponse({'status':200})