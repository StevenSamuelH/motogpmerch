from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import DataPembeli
from .forms import DataPembeliForm

# Create your views here.
def add_data(request):
    data_pembeli = DataPembeliForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if data_pembeli.is_valid():
            data_pembeli.save()
            return http.HttpResponseRedirect('')
    response = {'form' : data_pembeli}
    return render(request, 'bukti_pembayaran.html', response)
