from django import forms	
from universal_billing_system.models import *
from django.contrib.auth.models import User	


class SignupForm():
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = Merchant
        fields = ('__all__')
        
