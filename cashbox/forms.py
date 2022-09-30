from django import forms
from .models import Product



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'version', 'price']