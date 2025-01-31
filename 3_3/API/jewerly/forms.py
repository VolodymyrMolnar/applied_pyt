from django import forms
from .models import Client, OrderDetails, Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'total_price', 'status', 'client', 'employee']

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['quantity', 'product', 'order']



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone', 'email', 'address']
