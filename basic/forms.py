from django import forms

class UserForm(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    