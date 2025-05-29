from django import forms
from ..models.product_model import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # ya da sadece kullanmak istediğiniz alanlar listesi
