from rest_framework import serializers
from .models import DataPembeli

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPembeli
        fields = ['nama', 'alamat', 'kota', 'kelurahan', 'kodepos', 'bukti_img']