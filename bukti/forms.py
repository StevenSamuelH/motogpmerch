from django import forms
from .models import DataPembeli
from django.utils.translation import ugettext_lazy as _

class DataPembeliForm(forms.ModelForm):
    class Meta:
        model = DataPembeli
        fields = "__all__"
        # Ganti label
        labels = {
            'nama' : _('Nama Pembeli'),
            'alamat' : _('Alamat Pembeli'),
            'bukti_img' : _('Upload Bukti Pembayaran'),
        }