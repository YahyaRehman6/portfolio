from django import forms
from .models import *


# class Form(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

class Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']