from django import forms

from kategori.models import Kategori
from produk.models import Produk
from status.models import Status


class ProdukForm(forms.ModelForm) :
    class Meta:
        model = Produk
        fields = ["nama_produk","harga","kategori","status"]

        widgets = {
                'nama_produk' : forms.TextInput(attrs={'placeholder' : 'Masukkan nama produk...'}),
                'harga' : forms.NumberInput(attrs={'placeholder' : 'Masukkan harga produk...'}),
        }

        def __init__(self, *args, **kwargs) :
            super().__init__(*args,**kwargs)

            self.fields["kategori"].queryset = Kategori.objects.all()
            self.fields["kategori"].empty_label = "-- Pilih Kategori --"
            
            self.fields["status"].queryset = Status.objects.all()
            self.fields["status"].empty_label = "-- Pilih Status --"
