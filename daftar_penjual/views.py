from django.shortcuts import render
from django.http import HttpResponse
from .models import Merchant

# Create your views here.
def index(request):
    response = {'Merchant' : Merchant.objects.all()}
    return render(request, 'daftar_penjual.html', response)
