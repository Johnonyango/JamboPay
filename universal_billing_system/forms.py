from django import forms
from .models import *
from django.contrib.auth.forms import MerchanLoginForm
from django.contrib.auth.models import Merchant
<<<<<<< HEAD
=======

from authtools.forms import UserCreationForm

>>>>>>> mannu-rest-api-merchants
# sign up forms
class LoginForm(MerchantLoginForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = Merchant
        fields = ('email', 'password1', 'password2')
        # profile forms
<<<<<<< HEAD
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
=======

class UserCreationForm(UserCreationForm):
    """
    A UserCreationForm with optional password inputs.
    """

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(UserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2
>>>>>>> mannu-rest-api-merchants
