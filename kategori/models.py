from django.db import models

class Kategori(models.Model) :
    id_kategori = models.BigAutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.nama_kategori

    class Meta:
        db_table = "kategori"

