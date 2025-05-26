# your_app/forms/product_form.py
from django import forms
from ..models.product_model import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
