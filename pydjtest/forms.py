import django.forms as forms
from pydjtest.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products

