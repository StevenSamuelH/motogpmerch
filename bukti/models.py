from distutils.command.upload import upload
from django.db import models

# Create your models here.
class DataPembeli(models.Model):
    nama = models.CharField( max_length=50)
    alamat = models.CharField( max_length=200)
    kota = models.CharField( max_length=50)
    kelurahan = models.CharField( max_length=100)
    kodepos = models.CharField( max_length=10)
    bukti_img = models.URLField()