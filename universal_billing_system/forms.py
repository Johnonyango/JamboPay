from django import forms
from .models import *
from django.contrib.auth.forms import MerchanLoginForm
from django.contrib.auth.models import Merchant
# sign up forms
class LoginForm(MerchantLoginForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = Merchant
        fields = ('email', 'password1', 'password2')
       