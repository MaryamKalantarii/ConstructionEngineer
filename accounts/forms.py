from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = ['username', 'email', 'password1', 'password2','id_code', 'mobile', 'image']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomeUser
        fields= ['username', 'email','id_code', 'mobile', 'image']