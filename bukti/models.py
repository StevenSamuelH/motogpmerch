from distutils.command.upload import upload
from django.db import models

# Create your models here.
class DataPembeli(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=200)
    bukti_img = models.ImageField(upload_to = 'bukti-pembayaran')