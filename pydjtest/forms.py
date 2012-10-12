import django.forms as forms
from pydjtest.models import Products
from django.utils.safestring import mark_safe

class ProductColorWidget(forms.Widget):
    def __init__(self, attrs=None):
        super(ProductColorWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        out = '''
            <input type="text" id="id_%s" name="%s" value="%s" class="colorpicker" %s />
            <script>$(".colorpicker").colorpicker()</script>''' % (name, name, value, final_attrs);
        return mark_safe(out)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products

class ProductFormAdmin(forms.ModelForm):
    class Meta:
        model = Products
        widgets = {
          'color': ProductColorWidget(),
        }