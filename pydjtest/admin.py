# -*- coding: utf-8 -*-

from django.contrib import admin
from pydjtest import models

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'weight', 'heigth');
    pass

admin.site.register(models.Products, ProductsAdmin)