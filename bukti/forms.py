from django import forms
from .models import DataPembeli

class DataPembeliForm(forms.ModelForm):
    class Meta:
        model = DataPembeli
        fields = "__all__"