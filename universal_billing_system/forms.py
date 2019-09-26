from django import forms
<<<<<<< HEAD


=======
from .models import *
from django.contrib.auth.forms import MerchanLoginForm
from django.contrib.auth.models import Merchant
# sign up forms
class LoginForm(MerchantLoginForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = Merchant
        fields = ('email', 'password1', 'password2')
        # profile forms
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user','timestamp']

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         exclude = ['user','profile','timestamp']
# # review
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         exclude = ['user','project','average']
>>>>>>> 0a308a8e2f2057c9ab446bf35339a996e1e15f84
