from django.db import models
import uuid  
class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    nama = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    produk_terjual = models.IntegerField()
    rating = models.FloatField()