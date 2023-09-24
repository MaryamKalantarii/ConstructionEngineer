from django import forms
from .models import ContactUs,Order



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email','subject', 'message']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email','phone', 'message']