from django import forms
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import MerchantLoginForm

class LoginForm(MerchantLoginForm):
   '''
   User login form.
   '''
   
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

   class Meta:
      model = User
      fields = ['username','password']