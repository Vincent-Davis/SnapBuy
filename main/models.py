from django.db import models

class MoodEntry(models.Model):
    nama = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    produk_terjual = models.IntegerField()
    rating = models.FloatField()