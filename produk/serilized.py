from rest_framework import serializers
from .models import Produk 

class ProdukSerializer(serializers.ModelSerializer):
    harga = serializers.DecimalField(max_digits=8,decimal_places=2)
    nama_produk = serializers.CharField()

    class Meta:
        model = Produk
        fields = "__all__"
