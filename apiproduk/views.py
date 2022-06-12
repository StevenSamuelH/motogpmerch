from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from http.server import HTTPServer
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
import json as j
from django.core import serializers
from django.http.response import HttpResponse
# Create your views here.

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@csrf_exempt
def daftarDataProdukAPI(request):

    data = j.loads(request.body)
    name_baru = data['namaProduk']
    price_baru = float(data['priceProduk'])
    description_baru= data['DeskripsiProduk']
    image_baru = data['image']
  
    
    Dataproduk = Product(name=name_baru,
         price=price_baru,description=description_baru,image=image_baru)
    Dataproduk.save()
    return JsonResponse({'status':200})




def json(request):
    data = serializers.serialize('json',Product.objects.all())
    return HttpResponse(data, content_type="application/json")

