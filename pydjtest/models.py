import django.db.models as models
import os
from pydjtest.settings import MEDIA_ROOT

class Products(models.Model):
    id         = models.AutoField(primary_key=True)
    name       = models.CharField(max_length=255, verbose_name="Name")
    alias      = models.CharField(max_length=255, verbose_name="Alias")
    weight     = models.FloatField(verbose_name="Weight")
    heigth     = models.FloatField(verbose_name="Heigth")
    short_desc = models.TextField(verbose_name="Short decsription")
    desc       = models.TextField(verbose_name="Full desctiption text")

    color      = models.CharField(max_length=255, verbose_name="Color")
    photo      = models.ImageField(upload_to='photos', verbose_name="Product photo")