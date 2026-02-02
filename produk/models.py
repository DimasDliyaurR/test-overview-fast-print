from django.db import models
from kategori.models import Kategori
from status.models import Status

class Produk(models.Model):
    id_produk = models.BigAutoField(primary_key=True)
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(
            max_digits=8,
            decimal_places=2
    )
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE,related_name="kategori")
    status = models.ForeignKey(Status, on_delete=models.CASCADE,related_name="status")
   
    class Meta:
        db_table = "produk"
