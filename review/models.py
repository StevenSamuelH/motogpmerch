from django.db import models

class ReviewProduk(models.Model):
    nama = models.CharField(max_length=100)
    gambar = models.URLField()
    review = models.TextField()
    rating = models.URLField()
