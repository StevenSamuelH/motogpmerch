from django.urls import path
from .views import index, json, addReviewProduk

urlpatterns = [
    path('', index, name='index'),
    path('json/', json),
    path('add-review/', addReviewProduk, name="add"),
]