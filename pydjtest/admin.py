# -*- coding: utf-8 -*-

from django.contrib import admin
from pydjtest import models, forms

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'weight', 'heigth');
    form = forms.ProductFormAdmin
    class Media:
        css = {
            "all": (
                "/static/css/bootstrap.css",
                "/static/css/colorpicker.css",
                )
        }
        js = (
            "/static/js/jquery-1.8.0.min.js",
            "/static/js/bootstrap.js",
            "/static/js/bootstrap-colorpicker.js",
            )


admin.site.register(models.Products, ProductsAdmin)