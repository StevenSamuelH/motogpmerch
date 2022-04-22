from django.urls import path
from . import views;
urlpatterns = [
   
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
  
  

    # TODO Add 'tugas' path using list_tugas Views
]