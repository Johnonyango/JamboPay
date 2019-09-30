from django import forms
from .models import Bills


class BillsForm(forms.ModelForm):
   class Meta:
       model = Bills
       fields = '__all__'