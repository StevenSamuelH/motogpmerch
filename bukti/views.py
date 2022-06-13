from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import DataPembeli
from .forms import DataPembeliForm
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
def add_data(request):
    data_pembeli = DataPembeliForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if data_pembeli.is_valid():
            data_pembeli.save()
            return HttpResponseRedirect('https://motogpmerch.herokuapp.com/')
    response = {'form' : data_pembeli}
    return render(request, 'bukti_pembayaran.html', response)

@csrf_exempt
def addDataFlutter(request):
    data = j.loads(request.body)
    nama = data['nama']
    alamat = data['alamat']
    kota = data['kota']
    kelurahan = data['kecamatan']
    kodepos = data['kodePos']
    bukti_img = data['buktiImg']

    dataProduk = DataPembeli(nama = nama, alamat = alamat, kota = kota, kelurahan = kelurahan, kodepos = kodepos, bukti_img = bukti_img)
    dataProduk.save()
    return JsonResponse({'status' : 200})
