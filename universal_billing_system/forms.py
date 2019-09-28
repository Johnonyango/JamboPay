from django import forms
from .models import Bills
from django.contrib.auth.models import User	
from django.contrib.auth.forms import MerchanLoginForm
from django.contrib.auth.forms import MerchantLoginForm	
from django.contrib.auth.models import Merchant

class LoginForm(MerchantLoginForm):	class LoginForm(MerchantLoginForm):
   '''	    email = forms.EmailField(max_length=200, help_text='Required')
   User login form.	    class Meta:
   '''	        model = Merchant


class BillsForm(forms.ModelForm):
   class Meta:
      model = Bills
      fields = '__all__'



