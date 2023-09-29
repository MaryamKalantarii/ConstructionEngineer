from django import forms
from .models import ContactUs,Order_Work



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email','subject', 'message']

class  Order_WorkForm(forms.ModelForm):
    class Meta:
        model = Order_Work
        fields = ['name', 'email','phone', 'message']
        