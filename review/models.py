from django.db import models

class ReviewProduk(models.Model):
    nama = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='motogpmerch-images')
    review = models.TextField()
    rating = models.ImageField(upload_to='motogpmerch-images')
