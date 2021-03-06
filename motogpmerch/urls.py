import daftar_penjual.urls as dp
"""motogpmerch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import profil_produk.urls as profil_produk

from django.conf import settings
from django.conf.urls.static import static
import bukti.urls as bukti
import review.urls as review
from . import settings
import apiproduk.urls as apiproduk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('profilproduk/', include(profil_produk)),
    path('bukti-pembayaran/', include(bukti)),
    path('review-produk/', include(review)),
    path('daftar-penjual/', include(dp)),
    path('apiproduk/', include(apiproduk)),
    path('apipembeli/', include(bukti))
]


  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
