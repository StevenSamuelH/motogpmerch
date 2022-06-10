from django.urls import path
from .views import index, json

urlpatterns = [
    path('', index, name='index'),
    path('json/', json)
]