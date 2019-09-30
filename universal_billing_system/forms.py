from django import forms	
from .models import *
from django.contrib.auth.models import User	
# from django.contrib.auth.forms import MerchanLoginForm
# from django.contrib.auth.forms import MerchantLoginForm
# from django.contrib.auth.models import Merchant

# sign up forms
class LoginForm():
   	email = forms.EmailField(max_length=200, help_text='Required')
   	class Meta:
   	        model = Merchant
         
# class SignupForm():
#     email = forms.EmailField(max_length=200, help_text='Required')
#     class Meta:
#         model = Merchant
#         fields = ('username', 'email', 'password1', 'password2')
        


class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = '__all__'
        widgets = {
            'Revstreams': forms.CheckboxSelectMultiple(),
        }
