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


class GenerateBillForm(forms.Form):

   class Meta:
      model = GenerateBillForm

      field=('__all__')
   #  name = forms.CharField(max_length=30)
   #  email = forms.EmailField(max_length=254)
   #  phone = forms.CharField(max_length=30)
   #  RevenueStreamID = forms.CharField(max_length=30)
   #  narration = forms.CharField(
   #      max_length=2000,
   #      widget=forms.Textarea(),
   #      help_text='Write here your message!'
   #  )
  
   #  amount = forms.CharField(max_length=30)
   #  Quantity = forms.CharField(max_length=30)