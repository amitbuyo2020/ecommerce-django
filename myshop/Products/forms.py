from django.forms import ModelForm
from .models import Product

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductChangeForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'productImg', 'price', 'ratings', 'description']