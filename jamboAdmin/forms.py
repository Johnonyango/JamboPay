from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from universal_billing_system.models import Merchant

class SignUpForm(UserCreationForm):
    # Email = forms.EmailField()
    # extra_field = forms.CharField(required=True)
    # Business_name = forms.CharField(max_length=20)
    # Business_owner = forms.CharField()
    # Phone_number = forms.CharField(max_length=60)
    # Physical_address = forms.CharField(max_length=60)
    # Post_code = forms.CharField(max_length=20)
    # Town = forms.CharField(max_length=20)
    # JP_paybill = forms.CharField(max_length=20)
    # Industry = forms.CharField()
    # Revstreams = forms.CharField()


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields.pop('username')
    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields.pop('password1')  
    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields.pop('password2')         



    # class Meta:
    #     model = Merchant
    #     fields = ("Email", "Phone_number")
    #     exclude = ['username']

    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.extra_field = self.cleaned_data["city"]
    #     if commit:
    #         user.save()
    #     return user
        
class merchantUSers(UserCreationForm):
    # email=forms.EmailField()
    class Meta:
        model=User
        fields='__all__'

class AddEmployeeForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
