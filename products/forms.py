from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Productfields = '__all__'


    def __init__(self, *args, **kwargs):
        suprt().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in catgories]

        self.fields['category'].choices = firnedly_names
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'