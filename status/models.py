from django.db import models

class Status(models.Model):
    id_status = models.BigAutoField(primary_key=True)
    nama_status = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_status

    class Meta:
        db_table = "status"
