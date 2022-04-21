from django.db import models

# Create your models here.

class Merchant(models.Model):
    id_number = models.BigIntegerField(default=100000)
    name = models.TextField(default='example : Anugrah Shop')
    email = models.EmailField(default='example : anugrah_shop123@somemailhosting.com')
    address = models.TextField(default='Write your address here...')

