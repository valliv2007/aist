from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone_order', 'first_name']
# 'card_paid''last_name', 'email', 'city'
