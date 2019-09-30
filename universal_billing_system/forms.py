from django import forms
from .models import *


class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = '__all__'
        widgets = {
            'Revstreams': forms.CheckboxSelectMultiple(),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = NewsLetterRecipients
        fields = '__all__'
