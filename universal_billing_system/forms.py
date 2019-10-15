from django import forms	
from .models import *
from django.contrib.auth.models import User	
from bootstrap_datepicker_plus import DatePickerInput
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
            'due_date': DatePickerInput(
                options={
                    "format": "MM/DD/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),
        }
        exclude = ['status','generated_by','bill_id']
# class MerchantForm(forms.ModelForm):
#     class Meta:
#         model = Merchant
#         fields = '__all__'
       
        # exclude = ['Merchant_id']

class NoteForm(forms.ModelForm):
    class Meta:
        model = NewsLetterRecipients
        fields = '__all__'
        # widgets = {
        #     '__all__': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # }


class AddEmployeeForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']